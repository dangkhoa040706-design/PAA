package com.nhomx.paa.metrics

import android.os.Process
import android.os.SystemClock

// =========================================================================
// --- [BỘ ĐO CPU SAMPLER: ĐO TỶ LỆ CHIẾM DỤNG CPU TIẾN TRÌNH] ---
// Cơ chế đo lường:
// 1. Sử dụng Process.getElapsedCpuTime() để đọc thời gian CPU cấp cho tiến trình.
// 2. Tính toán hiệu số (delta CPU) so với thời gian thực tế trôi qua (delta Realtime).
// 3. Chuẩn hóa theo số nhân CPU phần cứng (Runtime.availableProcessors) để ra % từ 0% đến 100%.
// =========================================================================
class CpuSampler {

    private var lastCpuTimeMs = 0L
    private var lastRealTimeMs = 0L
    private val numCores = Runtime.getRuntime().availableProcessors().coerceAtLeast(1)

    fun reset() {
        lastCpuTimeMs = Process.getElapsedCpuTime()
        lastRealTimeMs = SystemClock.elapsedRealtime()
    }

    /**
     * Đo và tính toán tỷ lệ % CPU sử dụng trong chu kỳ lấy mẫu
     */
    fun sampleCpuPercent(): Float {
        // --- BƯỚC 1: Lấy thời gian CPU hiện tại và đồng hồ hệ thống ---
        val currentCpuTimeMs = Process.getElapsedCpuTime()
        val currentRealTimeMs = SystemClock.elapsedRealtime()

        if (lastRealTimeMs == 0L) {
            lastCpuTimeMs = currentCpuTimeMs
            lastRealTimeMs = currentRealTimeMs
            return 0f
        }

        // --- BƯỚC 2: Tính lượng tài nguyên CPU tiêu thụ trong chu kỳ ---
        val deltaCpu = currentCpuTimeMs - lastCpuTimeMs
        val deltaReal = currentRealTimeMs - lastRealTimeMs

        lastCpuTimeMs = currentCpuTimeMs
        lastRealTimeMs = currentRealTimeMs

        if (deltaReal <= 0) return 0f

        // --- BƯỚC 3: Quy đổi ra phần trăm (%) trên toàn bộ các nhân CPU ---
        val percent = (deltaCpu.toFloat() / (deltaReal.toFloat() * numCores)) * 100f
        return Stats.round1(percent.coerceIn(0f, 100f))
    }
}
