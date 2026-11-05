package com.nhomx.paa.scenario

import com.nhomx.paa.data.MeasurementResult
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

sealed class ScenarioState {
    object Idle : ScenarioState()
    data class Running(val progress: Float, val message: String = "") : ScenarioState()
    data class Finished(val result: MeasurementResult) : ScenarioState()
    object Cancelled : ScenarioState()
    data class Failed(val error: String) : ScenarioState()
}

abstract class ScenarioRunner {

    protected val _state = MutableStateFlow<ScenarioState>(ScenarioState.Idle)
    val state: StateFlow<ScenarioState> = _state.asStateFlow()

    abstract suspend fun runScenario(): MeasurementResult
    abstract fun cancelScenario()
}
