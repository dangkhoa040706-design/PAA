package com.nhomx.paa.ui.memory

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.JsonResultStore
import com.nhomx.paa.data.MeasurementResult
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class MemoryViewModel(application: Application) : AndroidViewModel(application) {

    private val resultStore = JsonResultStore(application)

    private val _variant = MutableStateFlow(Variant.BAD)
    val variant: StateFlow<Variant> = _variant.asStateFlow()

    private val _lastResult = MutableStateFlow<MeasurementResult?>(null)
    val lastResult: StateFlow<MeasurementResult?> = _lastResult.asStateFlow()

    fun setVariant(newVariant: Variant) {
        _variant.value = newVariant
    }

    fun setLastResult(result: MeasurementResult) {
        _lastResult.value = result.copy(variant = _variant.value.name)
    }

    fun saveResult(onSuccess: () -> Unit) {
        val result = _lastResult.value ?: return
        viewModelScope.launch {
            resultStore.add(result)
            onSuccess()
        }
    }
}
