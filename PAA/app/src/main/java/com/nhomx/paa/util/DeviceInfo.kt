package com.nhomx.paa.util

import android.app.ActivityManager
import android.content.Context
import android.os.Build
import android.view.WindowManager

object DeviceInfo {

    fun getDeviceSummary(context: Context): String {
        val model = "${Build.MANUFACTURER} ${Build.MODEL}"
        val androidVer = "Android ${Build.VERSION.RELEASE} (API ${Build.VERSION.SDK_INT})"
        val ramGb = getTotalRamGb(context)
        val refreshRate = getRefreshRate(context)
        return "Thiết bị: $model | $androidVer | RAM: ${ramGb}GB | ${refreshRate}Hz"
    }

    fun getTotalRamGb(context: Context): Int {
        val actManager = context.getSystemService(Context.ACTIVITY_SERVICE) as ActivityManager
        val memInfo = ActivityManager.MemoryInfo()
        actManager.getMemoryInfo(memInfo)
        return (memInfo.totalMem / (1024 * 1024 * 1024)).toInt()
    }

    fun getRefreshRate(context: Context): Int {
        val windowManager = context.getSystemService(Context.WINDOW_SERVICE) as WindowManager
        val display = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            context.display
        } else {
            @Suppress("DEPRECATION")
            windowManager.defaultDisplay
        }
        return display?.refreshRate?.toInt() ?: 60
    }
}
