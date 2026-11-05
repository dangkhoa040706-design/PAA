package com.nhomx.paa.ui.results

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.nhomx.paa.core.Module
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.JsonResultStore
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.metrics.Stats
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

data class ComparisonRow(
    val metricName: String,
    val badValue: String,
    val optValue: String,
    val improvement: String,
    val isPositive: Boolean
)

class ResultsViewModel(application: Application) : AndroidViewModel(application) {

    private val resultStore = JsonResultStore(application)

    private val _allResults = MutableStateFlow<List<MeasurementResult>>(emptyList())
    val allResults: StateFlow<List<MeasurementResult>> = _allResults.asStateFlow()

    private val _selectedModule = MutableStateFlow(Module.JANK.name)
    val selectedModule: StateFlow<String> = _selectedModule.asStateFlow()

    private val _comparisonRows = MutableStateFlow<List<ComparisonRow>>(emptyList())
    val comparisonRows: StateFlow<List<ComparisonRow>> = _comparisonRows.asStateFlow()

    private val _comparisonNote = MutableStateFlow<String?>(null)
    val comparisonNote: StateFlow<String?> = _comparisonNote.asStateFlow()

    init {
        loadResults()
    }

    fun selectModule(moduleName: String) {
        _selectedModule.value = moduleName
        computeComparison(_allResults.value, moduleName)
    }

    fun loadResults() {
        viewModelScope.launch {
            val list = resultStore.getAll()
            _allResults.value = list
            computeComparison(list, _selectedModule.value)
        }
    }

    fun deleteResult(id: Long) {
        viewModelScope.launch {
            resultStore.delete(id)
            loadResults()
        }
    }

    fun clearHistory() {
        viewModelScope.launch {
            resultStore.clear()
            loadResults()
        }
    }

    private fun computeComparison(list: List<MeasurementResult>, module: String) {
        val moduleResults = list.filter { it.module.equals(module, ignoreCase = true) }
        val badList = moduleResults.filter { it.variant.equals(Variant.BAD.name, ignoreCase = true) }
        val optList = moduleResults.filter { it.variant.equals(Variant.OPTIMIZED.name, ignoreCase = true) }

        if (badList.isEmpty() || optList.isEmpty()) {
            _comparisonRows.value = emptyList()
            _comparisonNote.value = "Chưa có đủ dữ liệu đối đầu (cần ít nhất 1 lần đo bản BAD và 1 lần đo bản OPTIMIZED)."
            return
        }

        _comparisonNote.value = null
        val rows = mutableListOf<ComparisonRow>()

        when (module.uppercase()) {
            "JANK" -> {
                // 1. % Frame Jank (Càng thấp càng tốt)
                val badJank = Stats.mean(badList.mapNotNull { it.jankPercent })
                val optJank = Stats.mean(optList.mapNotNull { it.jankPercent })
                val jankImp = Stats.improvementPercent(badJank, optJank, lowerIsBetter = true)
                rows.add(
                    ComparisonRow(
                        metricName = "% Frame Jank",
                        badValue = String.format("%.1f%%", badJank),
                        optValue = String.format("%.1f%%", optJank),
                        improvement = String.format("%+.1f%%", jankImp),
                        isPositive = jankImp >= 0
                    )
                )

                // 2. Frame Time P95 (Càng thấp càng tốt)
                val badP95 = Stats.mean(badList.mapNotNull { it.frameP95Ms })
                val optP95 = Stats.mean(optList.mapNotNull { it.frameP95Ms })
                val p95Imp = Stats.improvementPercent(badP95, optP95, lowerIsBetter = true)
                rows.add(
                    ComparisonRow(
                        metricName = "P95 Frame Time",
                        badValue = String.format("%.1f ms", badP95),
                        optValue = String.format("%.1f ms", optP95),
                        improvement = String.format("%+.1f%%", p95Imp),
                        isPositive = p95Imp >= 0
                    )
                )

                // 3. FPS Trung bình (Càng cao càng tốt)
                val badFps = Stats.mean(badList.mapNotNull { it.avgFps })
                val optFps = Stats.mean(optList.mapNotNull { it.avgFps })
                val fpsImp = Stats.improvementPercent(badFps, optFps, lowerIsBetter = false)
                rows.add(
                    ComparisonRow(
                        metricName = "FPS Trung bình",
                        badValue = String.format("%.1f", badFps),
                        optValue = String.format("%.1f", optFps),
                        improvement = String.format("%+.1f%%", fpsImp),
                        isPositive = fpsImp >= 0
                    )
                )
            }
            "CPU" -> {
                // Thời gian thực thi (Càng thấp càng tốt)
                val badExec = Stats.mean(badList.mapNotNull { it.execTimeMs?.toFloat() })
                val optExec = Stats.mean(optList.mapNotNull { it.execTimeMs?.toFloat() })
                val execImp = Stats.improvementPercent(badExec, optExec, lowerIsBetter = true)
                rows.add(
                    ComparisonRow(
                        metricName = "Thời gian xử lý",
                        badValue = String.format("%.0f ms", badExec),
                        optValue = String.format("%.0f ms", optExec),
                        improvement = String.format("%+.1f%%", execImp),
                        isPositive = execImp >= 0
                    )
                )

                // Tải CPU TB (Càng thấp càng tốt)
                val badCpu = Stats.mean(badList.mapNotNull { it.avgCpuPercent })
                val optCpu = Stats.mean(optList.mapNotNull { it.avgCpuPercent })
                val cpuImp = Stats.improvementPercent(badCpu, optCpu, lowerIsBetter = true)
                rows.add(
                    ComparisonRow(
                        metricName = "CPU Trung bình",
                        badValue = String.format("%.0f%%", badCpu),
                        optValue = String.format("%.0f%%", optCpu),
                        improvement = String.format("%+.1f%%", cpuImp),
                        isPositive = cpuImp >= 0
                    )
                )
            }
            "MEMORY" -> {
                // RAM Đỉnh PSS (Càng thấp càng tốt)
                val badRam = Stats.mean(badList.mapNotNull { it.peakRamMb })
                val optRam = Stats.mean(optList.mapNotNull { it.peakRamMb })
                val ramImp = Stats.improvementPercent(badRam, optRam, lowerIsBetter = true)
                rows.add(
                    ComparisonRow(
                        metricName = "RAM PSS đỉnh",
                        badValue = String.format("%.0f MB", badRam),
                        optValue = String.format("%.0f MB", optRam),
                        improvement = String.format("%+.1f%%", ramImp),
                        isPositive = ramImp >= 0
                    )
                )

                // Số Activity Instance bị leak (Càng thấp càng tốt)
                val badLeaks = Stats.mean(badList.mapNotNull { it.leakCount?.toFloat() })
                val optLeaks = Stats.mean(optList.mapNotNull { it.leakCount?.toFloat() })
                rows.add(
                    ComparisonRow(
                        metricName = "Instance bị rò rỉ",
                        badValue = String.format("%.0f", badLeaks),
                        optValue = String.format("%.0f", optLeaks),
                        improvement = if (badLeaks > 0 && optLeaks == 0f) "Đã triệt tiêu" else "--",
                        isPositive = optLeaks < badLeaks
                    )
                )
            }
        }

        _comparisonRows.value = rows
    }
}
