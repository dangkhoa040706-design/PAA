package com.nhomx.paa.metrics

import android.os.Handler
import android.os.HandlerThread
import android.view.FrameMetrics
import android.view.Window
import java.lang.ref.WeakReference

// =========================================================================
// --- [HẠT NHÂN ĐO FRAMEMETRICS: BẮT XUNG NHỊP KHUNG HÌNH HỆ THỐNG] ---
// Cơ chế vận hành:
// 1. Đăng ký Window.OnFrameMetricsAvailableListener trên HandlerThread chạy ngầm.
// 2. Nhận chính xác thời gian vẽ từng frame (TOTAL_DURATION tính bằng nano-giây).
// 3. So sánh với ngân sách VSYNC (16.67ms cho 60Hz): Nếu > 16.67ms -> Tính là 1 Jank Frame.
// 4. Tính toán FPS tức thời và tỷ lệ khung hình giật lag theo thời gian thực.
// =========================================================================
class FrameMetricsTracker {

    private var handlerThread: HandlerThread? = null
    private var backgroundHandler: Handler? = null
    private var windowRef: WeakReference<Window>? = null
    private var frameMetricsListener: Window.OnFrameMetricsAvailableListener? = null

    private var frameBudgetMs: Float = 16.67f
    private val frameDurationsMs = ArrayList<Float>(5000)
    private var jankCount = 0
    private var totalFrames = 0
    private var startTimeMs = 0L

    /**
     * Bắt đầu theo dõi và thu thập số liệu từng khung hình từ Window
     */
    @Synchronized
    fun start(window: Window, refreshRate: Int = 60) {
        stop() // Đảm bảo dừng phiên trước nếu có

        windowRef = WeakReference(window)
        // Ngân sách thời gian cho 1 khung hình (1000ms / 60 = 16.67ms)
        frameBudgetMs = if (refreshRate > 0) 1000f / refreshRate else 16.67f

        reset()
        startTimeMs = System.currentTimeMillis()

        // Tạo luồng nền riêng để xử lý callback FrameMetrics mà không làm nặng UI Thread
        val thread = HandlerThread("PAA_FrameMetrics_Thread")
        thread.start()
        handlerThread = thread
        val handler = Handler(thread.looper)
        backgroundHandler = handler

        // --- LẮNG NGHE SỰ KIỆN TỪNG KHUNG HÌNH (FRAMEMETRICS API) ---
        val listener = Window.OnFrameMetricsAvailableListener { _, frameMetrics, _ ->
            // Bỏ frame vẽ đầu tiên do hệ thống thường trễ khởi tạo layout
            val isFirstDraw = frameMetrics.getMetric(FrameMetrics.FIRST_DRAW_FRAME) == 1L
            if (isFirstDraw) return@OnFrameMetricsAvailableListener

            // Trích xuất tổng thời gian vẽ (Total Duration: Measure + Layout + Draw + Sync + GPU)
            val totalDurationNs = frameMetrics.getMetric(FrameMetrics.TOTAL_DURATION)
            val durationMs = totalDurationNs / 1_000_000f

            synchronized(this) {
                frameDurationsMs.add(durationMs)
                totalFrames++
                // Nếu vượt quá ngân sách 16.67ms -> Ghi nhận là 1 khung hình bị Jank
                if (durationMs > frameBudgetMs) {
                    jankCount++
                }
            }
        }

        frameMetricsListener = listener
        window.addOnFrameMetricsAvailableListener(listener, handler)
    }

    /**
     * Dừng theo dõi và giải phóng HandlerThread an toàn
     */
    @Synchronized
    fun stop() {
        val window = windowRef?.get()
        frameMetricsListener?.let { listener ->
            window?.removeOnFrameMetricsAvailableListener(listener)
        }
        frameMetricsListener = null
        windowRef = null

        handlerThread?.quitSafely()
        handlerThread = null
        backgroundHandler = null
    }

    @Synchronized
    fun reset() {
        frameDurationsMs.clear()
        jankCount = 0
        totalFrames = 0
        startTimeMs = System.currentTimeMillis()
    }

    // --- TÍNH TOÁN FPS TỨC THỜI (FRAMES PER SECOND) ---
    @Synchronized
    fun getSnapshotFps(): Float {
        val elapsedSec = (System.currentTimeMillis() - startTimeMs) / 1000f
        return if (elapsedSec > 0.3f && totalFrames > 0) {
            Stats.round1(totalFrames / elapsedSec)
        } else {
            0f
        }
    }

    // --- TÍNH TOÁN TỶ LỆ JANK (% KHUNG HÌNH RỚT) ---
    @Synchronized
    fun getSnapshotJankPercent(): Float {
        val elapsedSec = (System.currentTimeMillis() - startTimeMs) / 1000f
        return if (totalFrames > 0) {
            Stats.round1((jankCount.toFloat() / totalFrames) * 100f)
        } else if (elapsedSec >= 0.5f) {
            // Luồng chính bị khóa cứng (Frozen Frame / UI Block) -> 100% Jank
            100f
        } else {
            0f
        }
    }

    @Synchronized
    fun getTotalFrames(): Int = totalFrames

    @Synchronized
    fun getJankCount(): Int = jankCount

    @Synchronized
    fun getJankPercent(): Float = if (totalFrames > 0) (jankCount.toFloat() / totalFrames) * 100f else 0f

    @Synchronized
    fun getDurationsList(): List<Float> = ArrayList(frameDurationsMs)

    @Synchronized
    fun getPercentile(p: Double): Float = Stats.percentile(frameDurationsMs, p)
}
