package com.nhomx.paa.data

import android.content.Context
import com.nhomx.paa.core.Constants
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONArray
import java.io.BufferedReader
import java.io.InputStreamReader

object AssetLoader {

    suspend fun loadPhotoItems(context: Context): List<PhotoItem> = withContext(Dispatchers.IO) {
        val jsonString = context.assets.open(Constants.ITEMS_JSON_FILE).bufferedReader().use { it.readText() }
        val jsonArray = JSONArray(jsonString)
        val list = mutableListOf<PhotoItem>()
        for (i in 0 until jsonArray.length()) {
            val obj = jsonArray.getJSONObject(i)
            list.add(
                PhotoItem(
                    id = obj.getInt("id"),
                    title = obj.getString("title"),
                    description = obj.getString("description"),
                    imageName = obj.getString("imageName")
                )
            )
        }
        list
    }

    suspend fun loadCpuData(context: Context, limit: Int = Constants.CPU_N): IntArray = withContext(Dispatchers.IO) {
        val values = IntArray(limit)
        var count = 0
        context.assets.open(Constants.CPU_DATA_FILE).use { inputStream ->
            BufferedReader(InputStreamReader(inputStream)).use { reader ->
                var line = reader.readLine() // Bỏ dòng tiêu đề (index,value)
                while (count < limit) {
                    line = reader.readLine() ?: break
                    val commaIndex = line.indexOf(',')
                    if (commaIndex != -1) {
                        values[count++] = line.substring(commaIndex + 1).trim().toInt()
                    }
                }
            }
        }
        if (count < limit) values.copyOf(count) else values
    }
}
