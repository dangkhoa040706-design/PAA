package com.nhomx.paa.scenario

import android.content.Context
import android.view.Window
import androidx.recyclerview.widget.RecyclerView
import com.nhomx.paa.BuildConfig
import com.nhomx.paa.core.Constants
import com.nhomx.paa.core.Module
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.metrics.Stats
import com.nhomx.paa.util.DeviceInfo
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.isActive
import kotlinx.coroutines.withContext

// =========================================================================
// --- [KỊCH BẢN ĐO ĐẠC TỰ ĐỘNG: JANK SCENARIO] ---
// Quy trình đo lường chuẩn:
// 1. Tự động cuộn danh sách 500 phần tử qua lại 3 lượt liên tục.
// 2. Thu thập thời gian vẽ từng khung hình (Frame Duration) qua FrameMetrics API.
// 3. Tính toán các chỉ số thống kê: FPS trung bình, Tỷ lệ Jank (%), Percentile P50, P90, P95, P99.
// =========================================================================
class JankScenario(
    private val context: Context,
    private val window: Window,
    private val recyclerView: RecyclerView,
    private val collector: MetricsCollector
) : ScenarioRunner() {

    private var isCancelled = false

    override suspend fun runScenario(): MeasurementResult {
        isCancelled = false
        _state.value = ScenarioState.Running(0f, "Đang chuẩn bị danh sách...")

        // --- BƯỚC 1: Đưa RecyclerView về đầu danh sách và nghỉ 1s cho CPU ổn định ---
        withContext(Dispatchers.Main) {
            recyclerView.scrollToPosition(0)
        }
        delay(1000L)

        // --- BƯỚC 2: Bật hạt nhân đo đạc MetricsCollector (FrameMetrics, CPU, RAM) ---
        val refreshRate = DeviceInfo.getRefreshRate(context)
        collector.start(window, refreshRate)

        val totalLoops = 3
        val startTime = System.currentTimeMillis()

        try {
            // --- BƯỚC 3: Thực hiện 3 chu kỳ cuộn trang tự động để đo độ mượt ---
            for (loop in 1..totalLoops) {
                if (isCancelled) break
                _state.value = ScenarioState.Running(
                    progress = ((loop - 1).toFloat() / totalLoops),
                    message = "Lượt cuộn $loop / $totalLoops..."
                )

                // Cuộn xuống từ từ (16ms tương ứng với nhịp 60 FPS)
                var canScroll = true
                while (canScroll && !isCancelled) {
                    withContext(Dispatchers.Main) {
                        canScroll = recyclerView.canScrollVertically(1)
                        if (canScroll) {
                            recyclerView.scrollBy(0, Constants.JANK_SCROLL_STEP_PX)
                        }
                    }
                    delay(16L)
                }

                delay(500L)

                // Cuộn ngược nhanh về lại đỉnh danh sách
                var canScrollUp = true
                while (canScrollUp && !isCancelled) {
                    withContext(Dispatchers.Main) {
                        canScrollUp = recyclerView.canScrollVertically(-1)
                        if (canScrollUp) {
                            recyclerView.scrollBy(0, -Constants.JANK_SCROLL_STEP_PX * 2)
                        }
                    }
                    delay(16L)
                }

                delay(500L)
            }
        } finally {
            // --- BƯỚC 4: Dừng thu thập số liệu an toàn trong khối finally ---
            collector.stop()
        }

        if (isCancelled) {
            _state.value = ScenarioState.Cancelled
            throw Exception("Kịch bản đo đã bị hủy")
        }

        // --- BƯỚC 5: Trích xuất và tổng hợp số liệu đo đạc định lượng ---
        val durationMs = System.currentTimeMillis() - startTime
        val avgFps = Stats.round1(collector.frameTracker.getSnapshotFps())
        val jankPercent = Stats.round1(collector.frameTracker.getJankPercent())
        val p50 = Stats.round1(collector.frameTracker.getPercentile(50.0))
        val p90 = Stats.round1(collector.frameTracker.getPercentile(90.0))
        val p95 = Stats.round1(collector.frameTracker.getPercentile(95.0))
        val p99 = Stats.round1(collector.frameTracker.getPercentile(99.0))
        val peakRam = collector.getPeakRamMb()
        val avgCpu = collector.getAvgCpuPercent()

        val result = MeasurementResult(
            module = Module.JANK.name,
            variant = Variant.BAD.name,
            runIndex = 1,
            deviceModel = "${android.os.Build.MANUFACTURER} ${android.os.Build.MODEL}",
            androidVersion = "Android ${android.os.Build.VERSION.RELEASE} (API ${android.os.Build.VERSION.SDK_INT})",
            totalRamMb = DeviceInfo.getTotalRamGb(context) * 1024,
            buildType = if (BuildConfig.DEBUG) "debug" else "release",
            scenarioName = "Tự động cuộn 500 item x $totalLoops lượt",
            durationMs = durationMs,
            avgFps = avgFps,
            jankPercent = jankPercent,
            frameP50Ms = p50,
            frameP90Ms = p90,
            frameP95Ms = p95,
            frameP99Ms = p99,
            avgCpuPercent = avgCpu,
            peakRamMb = peakRam
        )

        _state.value = ScenarioState.Finished(result)
        return result
    }

    override fun cancelScenario() {
        isCancelled = true
        collector.stop()
        _state.value = ScenarioState.Cancelled
    }
}
