package com.nhomx.paa.ui.cpu

import android.os.SystemClock

// =========================================================================
// --- [TEST CPU BAD: MÔ PHỎNG NGHẼN CPU & NGUY CƠ LỖI TREO ANR] ---
// Nguyên nhân gây lỗi:
// 1. Thuật toán hai vòng lặp lồng nhau có độ phức tạp O(N^2) cực nặng.
// 2. Chạy TRỰC TIẾP trên luồng chính (Main Thread Block).
// 3. Khóa cứng MessageQueue trong hơn 2 giây -> Giao diện bị đơ cứng (Frozen Frames).
// =========================================================================
object BadCpuTask {

    /**
     * Thực thi tính toán phần tử trùng lặp theo giải thuật ngây thơ O(N^2)
     */
    fun compute(data: IntArray, limit: Int = data.size): CpuResult {
        // --- BƯỚC 1: Bắt đầu bấm giờ đo đạc mili-giây ---
        val startTime = SystemClock.elapsedRealtime()
        val n = limit.coerceAtMost(data.size)

        var duplicateCount = 0
        var sumDuplicates = 0L
        val visited = BooleanArray(n)

        // --- BƯỚC 2: [LỖI NGHẼN CPU] Thuật toán 2 vòng lặp O(N^2) quét toàn bộ mảng ---
        // Vòng lặp này chiếm trọn 100% thời gian xử lý của Main UI Thread
        for (i in 0 until n) {
            if (visited[i]) continue
            var isDuplicate = false
            for (j in i + 1 until n) {
                if (data[i] == data[j]) {
                    isDuplicate = true
                    visited[j] = true
                }
            }
            if (isDuplicate) {
                duplicateCount++
                sumDuplicates += data[i]
            }
        }

        // --- BƯỚC 3: Tính tổng thời gian chiếm dụng Main Thread ---
        val elapsed = SystemClock.elapsedRealtime() - startTime
        return CpuResult(duplicateCount, sumDuplicates, elapsed)
    }
}
