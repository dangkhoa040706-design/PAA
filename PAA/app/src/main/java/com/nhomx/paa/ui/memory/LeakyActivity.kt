package com.nhomx.paa.ui.memory

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity
import com.nhomx.paa.core.Constants
import com.nhomx.paa.core.Variant
import com.nhomx.paa.databinding.ActivityLeakyBinding
import java.lang.ref.WeakReference

// =========================================================================
// --- [MÀN HÌNH THỰC NGHIỆM: LEAKY ACTIVITY] ---
// Màn hình được mở và tự đóng lặp đi lặp lại 10 lần (Constants.MEM_LOOPS)
// Mỗi màn hình cố tình ngậm 5MB RAM (dummyPayload) để tạo tải bộ nhớ rõ rệt:
// - Ở bản BAD: 10 instance = 50MB RAM bị rò rỉ vĩnh viễn trên ART Heap.
// - Ở bản OPTIMIZED: 10 instance được giải phóng ngay lập tức sau mỗi lần đóng.
// =========================================================================
class LeakyActivity : AppCompatActivity(), CustomMemoryListener {

    private lateinit var binding: ActivityLeakyBinding

    // Handler mô phỏng công việc ngầm bị delay
    private val handler = Handler(Looper.getMainLooper())
    private var delayedRunnable: Runnable? = null

    // Cố tình cấp phát mảng byte 5MB để quan sát rõ rỉ bộ nhớ trên đồ thị Profiler
    private var dummyPayload: ByteArray? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLeakyBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val variantName = intent.getStringExtra(EXTRA_VARIANT) ?: Variant.BAD.name
        val isOpt = variantName == Variant.OPTIMIZED.name
        val iteration = intent.getIntExtra(EXTRA_ITERATION, 1)

        binding.tvIteration.text = "Lần mở: #$iteration / ${Constants.MEM_LOOPS}"
        binding.tvMode.text = "Chế độ: $variantName"

        // --- BƯỚC 1: Cấp phát 5MB RAM cho màn hình này ---
        dummyPayload = ByteArray(5 * 1024 * 1024)

        if (!isOpt) {
            // =====================================================================
            // --- [TEST MEMORY BAD: 3 KIỂU RÒ RỈ KINH ĐIỂN TRONG ANDROID] ---
            // =====================================================================

            // Kiểu 1: Singleton / biến tĩnh giữ chặt tham chiếu mạnh tới Activity
            LeakHolder.leakyActivities.add(this)

            // Kiểu 2: Handler postDelayed chạy ngầm (10 phút) giữ ngầm tham chiếu tới Activity Context
            delayedRunnable = Runnable {
                println("Delayed task executed for: ${dummyPayload?.size}")
            }
            handler.postDelayed(delayedRunnable!!, 600_000L)

            // Kiểu 3: Đăng ký listener vào danh sách toàn cục nhưng không bao giờ unregister
            LeakHolder.leakyListeners.add(this)
        } else {
            // =====================================================================
            // --- [TEST MEMORY OPTIMIZED: GIẢI PHÁP CHỐNG RÒ RỈ HOÀN TOÀN] ---
            // =====================================================================

            // Giải pháp: Sử dụng WeakReference để Garbage Collector có thể tự do dọn dẹp
            LeakHolder.safeActivities.add(WeakReference(this))
        }

        // Tự động đóng màn hình sau 350ms để mô phỏng chu trình người dùng đóng mở app liên tục
        handler.postDelayed({
            finish()
        }, 350L)
    }

    override fun onDestroy() {
        super.onDestroy()
        val isOpt = intent.getStringExtra(EXTRA_VARIANT) == Variant.OPTIMIZED.name
        if (isOpt) {
            // =====================================================================
            // --- [GIẢI PHÁP OPTIMIZED: DỌN DẸP THEO VÒNG ĐỜI LIFECYCLE] ---
            // =====================================================================

            // 1. Hủy bỏ tác vụ chạy ngầm của Handler để không giữ Context
            delayedRunnable?.let { handler.removeCallbacks(it) }

            // 2. Giải phóng mảng byte 5MB về null
            dummyPayload = null
        }
    }

    override fun onDataChanged() {
        // Callback của CustomMemoryListener
    }

    companion object {
        const val EXTRA_VARIANT = "extra_variant"
        const val EXTRA_ITERATION = "extra_iteration"
    }
}
