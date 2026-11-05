package com.nhomx.paa.data

import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONArray
import java.io.File

class JsonResultStore(private val context: Context) : ResultStore {

    private val file: File
        get() = File(context.filesDir, "results.json")

    override suspend fun add(result: MeasurementResult) = withContext(Dispatchers.IO) {
        val list = getAllInternal().toMutableList()
        list.add(0, result) // Thêm bản mới nhất lên đầu
        saveInternal(list)
    }

    override suspend fun getAll(): List<MeasurementResult> = withContext(Dispatchers.IO) {
        getAllInternal()
    }

    override suspend fun getByModule(module: String): List<MeasurementResult> = withContext(Dispatchers.IO) {
        getAllInternal().filter { it.module.equals(module, ignoreCase = true) }
    }

    override suspend fun delete(id: Long) = withContext(Dispatchers.IO) {
        val list = getAllInternal().filterNot { it.id == id }
        saveInternal(list)
    }

    override suspend fun clear() = withContext(Dispatchers.IO) {
        if (file.exists()) {
            file.delete()
        }
    }

    private fun getAllInternal(): List<MeasurementResult> {
        if (!file.exists()) return emptyList()
        return try {
            val content = file.readText(Charsets.UTF_8)
            val jsonArray = JSONArray(content)
            val list = mutableListOf<MeasurementResult>()
            for (i in 0 until jsonArray.length()) {
                val obj = jsonArray.getJSONObject(i)
                list.add(MeasurementResult.fromJson(obj))
            }
            list
        } catch (e: Exception) {
            e.printStackTrace()
            emptyList()
        }
    }

    private fun saveInternal(list: List<MeasurementResult>) {
        try {
            val jsonArray = JSONArray()
            for (item in list) {
                jsonArray.put(item.toJson())
            }
            file.writeText(jsonArray.toString(2), Charsets.UTF_8)
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
}
