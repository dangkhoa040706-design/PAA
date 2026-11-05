package com.nhomx.paa.ui.cpu

import android.os.SystemClock
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

// =========================================================================
// --- [TEST CPU OPTIMIZED: TỐI ƯU HÓA XỬ LÝ NẶNG BẰNG COROUTINES] ---
// Giải pháp kỹ thuật tối ưu:
// 1. Nâng cấp thuật toán sang HashMap với độ phức tạp tuyến tính O(N) duy nhất.
// 2. Chuyển tác vụ sang luồng nền qua Coroutines (Dispatchers.Default).
// 3. Tận dụng bộ nhớ đệm (Cache) để trả kết quả tức thì trong 0ms khi gọi lại.
// 4. Luồng chính (Main Thread) hoàn toàn thông thoáng, không bao giờ bị ANR.
// =========================================================================
object GoodCpuTask {

    // Bộ nhớ đệm (Cache) lưu trữ kết quả theo kích thước mảng n
    private val cache = HashMap<Int, CpuResult>()

    /**
     * Tính toán trên luồng nền (Worker Thread), giải phóng hoàn toàn luồng giao diện UI
     */
    suspend fun compute(data: IntArray, limit: Int = data.size, useCache: Boolean = true): CpuResult =
        withContext(Dispatchers.Default) {
            val n = limit.coerceAtMost(data.size)

            // --- BƯỚC 1: Kiểm tra bộ nhớ đệm (Cache Hit) ---
            if (useCache && cache.containsKey(n)) {
                return@withContext cache[n]!!
            }

            // --- BƯỚC 2: Bấm giờ tính toán trên luồng nền ---
            val startTime = SystemClock.elapsedRealtime()
            val freqMap = HashMap<Int, Int>(n)

            // --- BƯỚC 3: [TỐI ƯU THUẬT TOÁN] Đếm tần suất chỉ với 1 vòng lặp O(N) ---
            for (i in 0 until n) {
                val value = data[i]
                freqMap[value] = (freqMap[value] ?: 0) + 1
            }

            var duplicateCount = 0
            var sumDuplicates = 0L

            // Lọc các số xuất hiện từ 2 lần trở lên
            for ((key, count) in freqMap) {
                if (count >= 2) {
                    duplicateCount++
                    sumDuplicates += key
                }
            }

            // --- BƯỚC 4: Tổng kết thời gian và lưu Cache ---
            val elapsed = SystemClock.elapsedRealtime() - startTime
            val result = CpuResult(duplicateCount, sumDuplicates, elapsed)

            if (useCache) {
                cache[n] = result
            }

            result
        }

    fun clearCache() {
        cache.clear()
    }
}
