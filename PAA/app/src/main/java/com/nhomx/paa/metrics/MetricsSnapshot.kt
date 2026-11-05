package com.nhomx.paa.metrics

data class MetricsSnapshot(
    val fps: Float = 0f,
    val jankPercent: Float = 0f,
    val ramMb: Float = 0f,
    val cpuPercent: Float = 0f
)
