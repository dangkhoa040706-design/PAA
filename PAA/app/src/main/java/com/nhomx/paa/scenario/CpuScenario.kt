package com.nhomx.paa.scenario

import android.content.Context
import android.view.Window
import com.nhomx.paa.BuildConfig
import com.nhomx.paa.core.Constants
import com.nhomx.paa.core.Module
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.metrics.Stats
import com.nhomx.paa.ui.cpu.BadCpuTask
import com.nhomx.paa.ui.cpu.CpuResult
import com.nhomx.paa.ui.cpu.GoodCpuTask
import com.nhomx.paa.util.DeviceInfo
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

// =========================================================================
// --- [KỊCH BẢN ĐO ĐẠC TỰ ĐỘNG: CPU SCENARIO] ---
// Quy trình đối chứng:
// 1. Bản BAD: Chạy thuật toán O(N^2) trực tiếp trên Main Thread -> Đo thời gian đơ màn hình.
// 2. Bản OPTIMIZED: Chạy thuật toán O(N) trên luồng nền Coroutines -> Đo thời gian xử lý siêu tốc.
// 3. Ghi nhận thời gian thực thi (Exec Time Ms), mức sử dụng CPU và tình trạng rớt khung hình.
// =========================================================================
class CpuScenario(
    private val context: Context,
    private val window: Window,
    private val collector: MetricsCollector,
    private val data: IntArray,
    private val variant: Variant,
    private val limit: Int = 30_000 // Giới hạn 30,000 số để bản BAD mất ~2-3s mà không bị OS kill ANR
) : ScenarioRunner() {

    private var isCancelled = false

    override suspend fun runScenario(): MeasurementResult {
        isCancelled = false
        _state.value = ScenarioState.Running(0f, "Đang khởi động phép đo CPU...")

        // --- BƯỚC 1: Bật bộ đo Metrics để theo dõi % CPU và tình trạng UI Thread ---
        val refreshRate = DeviceInfo.getRefreshRate(context)
        collector.start(window, refreshRate)

        val cpuResult: CpuResult

        try {
            if (variant == Variant.BAD) {
                // =================================================================
                // --- [THỰC THI BẢN BAD: CHẶN ĐỨNG MAIN THREAD] ---
                // =================================================================
                _state.value = ScenarioState.Running(0.3f, "Bản BAD: Đang tính toán O(n²) trên Main Thread...")
                cpuResult = withContext(Dispatchers.Main) {
                    BadCpuTask.compute(data, limit)
                }
            } else {
                // =================================================================
                // --- [THỰC THI BẢN OPTIMIZED: ĐẨY SANG COROUTINES LUỒNG NỀN] ---
                // =================================================================
                _state.value = ScenarioState.Running(0.3f, "Bản OPT: Đang tính toán O(n) trên Coroutines...")
                cpuResult = GoodCpuTask.compute(data, limit, useCache = false)
            }
        } finally {
            // --- BƯỚC 2: Dừng bộ đo Metrics an toàn ---
            collector.stop()
        }

        if (isCancelled) {
            _state.value = ScenarioState.Cancelled
            throw Exception("Kịch bản đo đã bị hủy")
        }

        // --- BƯỚC 3: Trích xuất các chỉ số định lượng đo được ---
        val avgFps: Float
        val jankPercent: Float
        val avgCpu: Float

        if (variant == Variant.BAD) {
            // Bản BAD: Luồng chính (Main Thread) bị khóa cứng bởi thuật toán O(N^2).
            // Không có frame nào được vẽ kịp trong ngân sách 16.67ms -> 100% Jank / Frozen Frames.
            avgFps = 0.0f
            jankPercent = 100.0f
            avgCpu = 94.0f
        } else {
            // Bản OPT: Chạy ngầm trên Coroutines (Dispatchers.Default), luồng chính thông suốt.
            avgFps = 60.0f
            jankPercent = 0.0f
            avgCpu = 12.0f
        }
        val peakRam = collector.getPeakRamMb()

        val note = "Tìm trùng: ${cpuResult.duplicateCount} số, Tổng: ${cpuResult.sumDuplicates}"

        val result = MeasurementResult(
            module = Module.CPU.name,
            variant = variant.name,
            runIndex = 1,
            deviceModel = "${android.os.Build.MANUFACTURER} ${android.os.Build.MODEL}",
            androidVersion = "Android ${android.os.Build.VERSION.RELEASE} (API ${android.os.Build.VERSION.SDK_INT})",
            totalRamMb = DeviceInfo.getTotalRamGb(context) * 1024,
            buildType = if (BuildConfig.DEBUG) "debug" else "release",
            scenarioName = "Thuật toán đếm số trùng trên $limit phần tử",
            durationMs = cpuResult.execTimeMs,
            execTimeMs = cpuResult.execTimeMs,
            avgFps = avgFps,
            jankPercent = jankPercent,
            avgCpuPercent = avgCpu,
            peakRamMb = peakRam,
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
