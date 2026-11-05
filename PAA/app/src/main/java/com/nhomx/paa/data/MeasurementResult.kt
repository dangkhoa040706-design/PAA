package com.nhomx.paa.data

import org.json.JSONObject

data class MeasurementResult(
    val id: Long = System.currentTimeMillis(),
    val module: String,             // JANK, CPU, MEMORY
    val variant: String,            // BAD, OPTIMIZED
    val runIndex: Int = 1,
    val timestamp: Long = System.currentTimeMillis(),
    val deviceModel: String,
    val androidVersion: String,
    val totalRamMb: Int,
    val buildType: String,
    val scenarioName: String,
    val durationMs: Long,
    val avgFps: Float? = null,
    val jankPercent: Float? = null,
    val frameP50Ms: Float? = null,
    val frameP90Ms: Float? = null,
    val frameP95Ms: Float? = null,
    val frameP99Ms: Float? = null,
    val avgCpuPercent: Float? = null,
    val execTimeMs: Long? = null,
    val peakRamMb: Float? = null,
    val ramSamples: String? = null, // JSON array string
    val leakCount: Int? = null,
    val note: String? = null
) {
    fun toJson(): JSONObject {
        return JSONObject().apply {
            put("id", id)
            put("module", module)
            put("variant", variant)
            put("runIndex", runIndex)
            put("timestamp", timestamp)
            put("deviceModel", deviceModel)
            put("androidVersion", androidVersion)
            put("totalRamMb", totalRamMb)
            put("buildType", buildType)
            put("scenarioName", scenarioName)
            put("durationMs", durationMs)
            avgFps?.let { put("avgFps", it.toDouble()) }
            jankPercent?.let { put("jankPercent", it.toDouble()) }
            frameP50Ms?.let { put("frameP50Ms", it.toDouble()) }
            frameP90Ms?.let { put("frameP90Ms", it.toDouble()) }
            frameP95Ms?.let { put("frameP95Ms", it.toDouble()) }
            frameP99Ms?.let { put("frameP99Ms", it.toDouble()) }
            avgCpuPercent?.let { put("avgCpuPercent", it.toDouble()) }
            execTimeMs?.let { put("execTimeMs", it) }
            peakRamMb?.let { put("peakRamMb", it.toDouble()) }
            ramSamples?.let { put("ramSamples", it) }
            leakCount?.let { put("leakCount", it) }
            note?.let { put("note", it) }
        }
    }

    companion object {
        fun fromJson(json: JSONObject): MeasurementResult {
            return MeasurementResult(
                id = json.optLong("id", System.currentTimeMillis()),
                module = json.getString("module"),
                variant = json.getString("variant"),
                runIndex = json.optInt("runIndex", 1),
                timestamp = json.optLong("timestamp", 0L),
                deviceModel = json.optString("deviceModel", ""),
                androidVersion = json.optString("androidVersion", ""),
                totalRamMb = json.optInt("totalRamMb", 0),
                buildType = json.optString("buildType", "release"),
                scenarioName = json.optString("scenarioName", ""),
                durationMs = json.optLong("durationMs", 0L),
                avgFps = if (json.has("avgFps")) json.getDouble("avgFps").toFloat() else null,
                jankPercent = if (json.has("jankPercent")) json.getDouble("jankPercent").toFloat() else null,
                frameP50Ms = if (json.has("frameP50Ms")) json.getDouble("frameP50Ms").toFloat() else null,
                frameP90Ms = if (json.has("frameP90Ms")) json.getDouble("frameP90Ms").toFloat() else null,
                frameP95Ms = if (json.has("frameP95Ms")) json.getDouble("frameP95Ms").toFloat() else null,
                frameP99Ms = if (json.has("frameP99Ms")) json.getDouble("frameP99Ms").toFloat() else null,
                avgCpuPercent = if (json.has("avgCpuPercent")) json.getDouble("avgCpuPercent").toFloat() else null,
                execTimeMs = if (json.has("execTimeMs")) json.getLong("execTimeMs") else null,
                peakRamMb = if (json.has("peakRamMb")) json.getDouble("peakRamMb").toFloat() else null,
                ramSamples = if (json.has("ramSamples")) json.getString("ramSamples") else null,
                leakCount = if (json.has("leakCount")) json.getInt("leakCount") else null,
                note = if (json.has("note")) json.getString("note") else null
            )
        }
    }
}
