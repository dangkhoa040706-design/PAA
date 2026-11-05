package com.nhomx.paa.data

interface ResultStore {
    suspend fun add(result: MeasurementResult)
    suspend fun getAll(): List<MeasurementResult>
    suspend fun getByModule(module: String): List<MeasurementResult>
    suspend fun delete(id: Long)
    suspend fun clear()
}
