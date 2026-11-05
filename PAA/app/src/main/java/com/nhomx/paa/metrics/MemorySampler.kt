package com.nhomx.paa.metrics

import android.os.Debug

// =========================================================================
// --- [BỘ ĐO BỘ NHỚ MEMORY SAMPLER: ĐO RAM PSS VÀ ART HEAP] ---
// Thước đo tiêu chuẩn Android:
// 1. PSS (Proportional Set Size): Chuẩn đo lường thực tế của hệ điều hành Android
//    tính cả phần RAM riêng và phần chia sẻ tương ứng với các tiến trình khác.
// 2. Java Heap: Dung lượng bộ nhớ đối tượng đang cấp phát trong máy ảo ART.
// =========================================================================
object MemorySampler {

    /**
     * Đo dung lượng RAM thực tế PSS (Proportional Set Size) tính theo Megabyte (MB)
     */
    fun samplePssMb(): Float {
        return try {
            val memInfo = Debug.MemoryInfo()
            Debug.getMemoryInfo(memInfo)
            // Trích xuất totalPss tính bằng Kilobytes rồi chia cho 1024 để ra MB
            val pssKb = memInfo.totalPss
            Stats.round1(pssKb / 1024f)
        } catch (e: Exception) {
            0f
        }
    }

    /**
     * Đo dung lượng vùng nhớ đối tượng ART Heap đang sử dụng tính theo Megabyte (MB)
     */
    fun sampleHeapMb(): Float {
        val runtime = Runtime.getRuntime()
        val usedBytes = runtime.totalMemory() - runtime.freeMemory()
        return Stats.round1(usedBytes / (1024f * 1024f))
    }
}
