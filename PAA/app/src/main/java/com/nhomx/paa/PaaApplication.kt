package com.nhomx.paa

import android.app.Application
import android.os.StrictMode

class PaaApplication : Application() {

    override fun onCreate() {
        super.onCreate()

        // Bật StrictMode ở bản DEBUG để tự động bắt các vi phạm trên Main Thread (Bonus P9-T2)
        if (BuildConfig.DEBUG) {
            StrictMode.setThreadPolicy(
                StrictMode.ThreadPolicy.Builder()
                    .detectDiskReads()
                    .detectDiskWrites()
                    .detectNetwork()
                    .penaltyLog()
                    .build()
            )

            StrictMode.setVmPolicy(
                StrictMode.VmPolicy.Builder()
                    .detectLeakedSqlLiteObjects()
                    .detectLeakedClosableObjects()
                    .detectActivityLeaks()
                    .penaltyLog()
                    .build()
            )
        }
    }
}
