package com.nhomx.paa.metrics

import android.view.Window
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

class MetricsCollector {

    val frameTracker = FrameMetricsTracker()
    private val cpuSampler = CpuSampler()

    private val _snapshot = MutableStateFlow(MetricsSnapshot())
    val snapshot: StateFlow<MetricsSnapshot> = _snapshot.asStateFlow()

    private var samplingJob: Job? = null
    private val scope = CoroutineScope(Dispatchers.Default)

    private val ramSamples = mutableListOf<Float>()
    private val cpuSamples = mutableListOf<Float>()
    private var isRunning = false

    fun start(window: Window, refreshRate: Int = 60) {
        if (isRunning) stop()
        isRunning = true

        ramSamples.clear()
        cpuSamples.clear()

        frameTracker.start(window, refreshRate)
        cpuSampler.reset()

        samplingJob = scope.launch {
            while (isActive && isRunning) {
                delay(500L)
                val currentRam = MemorySampler.samplePssMb()
                val currentCpu = cpuSampler.sampleCpuPercent()
                val currentFps = frameTracker.getSnapshotFps()
                val currentJank = frameTracker.getSnapshotJankPercent()

                synchronized(this@MetricsCollector) {
                    if (currentRam > 0) ramSamples.add(currentRam)
                    if (currentCpu >= 0) cpuSamples.add(currentCpu)
                }

                _snapshot.value = MetricsSnapshot(
                    fps = currentFps,
                    jankPercent = currentJank,
                    ramMb = currentRam,
                    cpuPercent = currentCpu
                )
            }
        }
    }

    fun stop() {
        isRunning = false
        samplingJob?.cancel()
        samplingJob = null
        frameTracker.stop()
    }

    fun reset() {
        stop()
        frameTracker.reset()
        cpuSampler.reset()
        ramSamples.clear()
        cpuSamples.clear()
        _snapshot.value = MetricsSnapshot()
    }

    @Synchronized
    fun getPeakRamMb(): Float = ramSamples.maxOrNull() ?: MemorySampler.samplePssMb()

    @Synchronized
    fun getAvgCpuPercent(): Float = Stats.round1(Stats.mean(cpuSamples))

    @Synchronized
    fun getRamSamples(): List<Float> = ArrayList(ramSamples)
}
