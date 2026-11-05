package com.nhomx.paa.ui.memory

import android.app.Activity
import java.lang.ref.WeakReference

interface CustomMemoryListener {
    fun onDataChanged()
}

// =========================================================================
// --- [TEST MEMORY: NƠI LƯU TRỮ VÀ MÔ PHỎNG RÒ RỈ BỘ NHỚ (LEAK HOLDER)] ---
// Mục đích thực nghiệm:
// 1. Phía BAD: Lưu danh sách tham chiếu mạnh (Strong References) vào biến tĩnh (Singleton/static)
//    khiến Garbage Collector không thể thu hồi các Activity đã bị đóng (onDestroy).
// 2. Phía OPTIMIZED: Sử dụng tham chiếu yếu (WeakReference) giúp Garbage Collector
//    tự do thu hồi toàn bộ vùng nhớ ngay khi Activity bị đóng.
// =========================================================================
object LeakHolder {

    // --- [MÔ PHỎNG BAD 1] Danh sách tham chiếu mạnh (Strong Reference) giữ cứng Activity ---
    val leakyActivities = ArrayList<Activity>()

    // --- [MÔ PHỎNG BAD 2] Danh sách listener toàn cục không bao giờ được hủy đăng ký ---
    val leakyListeners = ArrayList<CustomMemoryListener>()

    // --- [GIẢI PHÁP OPTIMIZED] Sử dụng WeakReference: Cho phép dọn dẹp sạch RAM khi đóng màn hình ---
    val safeActivities = ArrayList<WeakReference<Activity>>()

    // --- Hàm giải phóng toàn bộ bộ nhớ (dùng để reset bài test) ---
    fun clearAll() {
        leakyActivities.clear()
        leakyListeners.clear()
        safeActivities.clear()
    }
}
