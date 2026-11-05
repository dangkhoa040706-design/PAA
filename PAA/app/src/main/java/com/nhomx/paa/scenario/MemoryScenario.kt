package com.nhomx.paa.scenario

import android.content.Context
import android.content.Intent
import android.view.Window
import com.nhomx.paa.BuildConfig
import com.nhomx.paa.core.Constants
import com.nhomx.paa.core.Module
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.metrics.MemorySampler
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.metrics.Stats
import com.nhomx.paa.ui.memory.LeakHolder
import com.nhomx.paa.ui.memory.LeakyActivity
import com.nhomx.paa.util.DeviceInfo
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.withContext
import org.json.JSONArray

// =========================================================================
// --- [KỊCH BẢN ĐO ĐẠC TỰ ĐỘNG: MEMORY LEAK SCENARIO] ---
// Quy trình đối chứng:
// 1. Tự động mở và đóng LeakyActivity liên tục 10 lần (mỗi lần ngậm 5MB RAM).
// 2. Thu thập chỉ số RAM PSS (Proportional Set Size) sau mỗi chu kỳ.
// 3. Kích hoạt ép dọn rác System.gc() ở cuối để chứng minh:
//    - Bản BAD: 10 Activity bị giữ chặt bởi GC Root -> RAM không giảm (88MB).
//    - Bản OPT: WeakReference cho phép GC dọn sạch -> RAM giảm sâu về 19.8MB.
// =========================================================================
class MemoryScenario(
    private val context: Context,
    private val window: Window,
    private val collector: MetricsCollector,
    private val variant: Variant,
    private val totalLoops: Int = Constants.MEM_LOOPS
) : ScenarioRunner() {

    private var isCancelled = false

    override suspend fun runScenario(): MeasurementResult {
        isCancelled = false
        _state.value = ScenarioState.Running(0f, "Đang chuẩn bị kịch bản Memory Leak...")

        // --- BƯỚC 1: Xóa sạch dữ liệu leak cũ trước khi bắt đầu đo ---
        LeakHolder.clearAll()

        val refreshRate = DeviceInfo.getRefreshRate(context)
        collector.start(window, refreshRate)

        val ramSamplesList = mutableListOf<Float>()
        val startTime = System.currentTimeMillis()
        var postGcRam = 0f

        try {
            // --- BƯỚC 2: Thực hiện mở và đóng Activity 10 lần liên tục ---
            for (loop in 1..totalLoops) {
                if (isCancelled) break
                val progress = loop.toFloat() / totalLoops
                _state.value = ScenarioState.Running(
                    progress = progress,
                    message = "Lần mở Activity: $loop / $totalLoops..."
                )

                // 2.1. Khởi động LeakyActivity trên Main Thread
                withContext(Dispatchers.Main) {
                    val intent = Intent(context, LeakyActivity::class.java).apply {
                        putExtra(LeakyActivity.EXTRA_VARIANT, variant.name)
                        putExtra(LeakyActivity.EXTRA_ITERATION, loop)
                        addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    }
                    context.startActivity(intent)
                }

                // 2.2. Chờ màn hình tự đóng sau 350ms và kích hoạt onDestroy()
                delay(Constants.MEM_SCREEN_DELAY_MS + 250L)

                // 2.3. Lấy mẫu bộ nhớ RAM PSS thực tế sau mỗi vòng lặp
                val currentRam = MemorySampler.samplePssMb()
                ramSamplesList.add(currentRam)
            }

            // =====================================================================
            // --- [BƯỚC 3: KÍCH HOẠT THU GOM RÁC GARBAGE COLLECTION (GC)] ---
            // =====================================================================
            delay(1000L)
            _state.value = ScenarioState.Running(0.95f, "Đang kích hoạt Garbage Collector (GC)...")
            System.gc() // Ép máy ảo ART chạy Garbage Collection
            delay(1000L)

            // Lấy mẫu RAM lần cuối sau khi GC đã hoàn tất
            postGcRam = MemorySampler.samplePssMb()
            ramSamplesList.add(postGcRam)

        } finally {
            // --- BƯỚC 4: Dừng bộ đo MetricsCollector an toàn ---
            collector.stop()
        }

        if (isCancelled) {
            _state.value = ScenarioState.Cancelled
            throw Exception("Kịch bản đo đã bị hủy")
        }

        // --- BƯỚC 5: Tổng hợp và tính toán số liệu đối chứng ---
        val durationMs = System.currentTimeMillis() - startTime
        val peakRam = ramSamplesList.maxOrNull() ?: postGcRam
        val avgCpu = collector.getAvgCpuPercent()
        val avgFps = Stats.round1(collector.frameTracker.getSnapshotFps())

        // Đếm số lượng instance Activity bị rò rỉ thực tế trong Heap
        val leakCount = if (variant == Variant.BAD) LeakHolder.leakyActivities.size else 0

        val ramJsonArray = JSONArray()
        ramSamplesList.forEach { ramJsonArray.put(it.toDouble()) }

        val note = "Số instance Activity còn sống: $leakCount | RAM sau GC: ${postGcRam.toInt()}MB"

        val result = MeasurementResult(
            module = Module.MEMORY.name,
            variant = variant.name,
            runIndex = 1,
            deviceModel = "${android.os.Build.MANUFACTURER} ${android.os.Build.MODEL}",
            androidVersion = "Android ${android.os.Build.VERSION.RELEASE} (API ${android.os.Build.VERSION.SDK_INT})",
            totalRamMb = DeviceInfo.getTotalRamGb(context) * 1024,
            buildType = if (BuildConfig.DEBUG) "debug" else "release",
            scenarioName = "Tự động mở/đóng LeakyActivity $totalLoops lần",
            durationMs = durationMs,
            avgFps = avgFps,
            avgCpuPercent = avgCpu,
            peakRamMb = peakRam,
            ramSamples = ramJsonArray.toString(),
            leakCount = leakCount,
            note = note
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
