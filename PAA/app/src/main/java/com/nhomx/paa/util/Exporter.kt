package com.nhomx.paa.util

import android.content.Context
import android.content.Intent
import androidx.core.content.FileProvider
import com.nhomx.paa.data.MeasurementResult
import java.io.File
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

object Exporter {

    /**
     * Xuất danh sách kết quả đo ra file CSV khớp chuẩn các cột của sheet NhatKyDo trong So_lieu_do_mau.xlsx.
     */
    fun exportToCsv(context: Context, results: List<MeasurementResult>): File {
        val dateFormat = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault())
        val csvFile = File(context.cacheDir, "PAA_NhatKyDo_${System.currentTimeMillis()}.csv")

        csvFile.bufferedWriter(Charsets.UTF_8).use { writer ->
            // Tiêu đề các cột khớp hoàn toàn với file Excel biểu mẫu
            writer.write("Module,Variant,Lần đo,Ngày giờ,Mã TB,Build,Kịch bản,Jank (%),P95 (ms),FPS TB,CPU TB (%),Thời gian (ms),RAM đỉnh (MB),Số leak,Ghi chú\n")

            for (res in results) {
                val dateStr = dateFormat.format(Date(res.timestamp))
                val jankStr = res.jankPercent?.let { String.format(Locale.US, "%.1f", it) } ?: ""
                val p95Str = res.frameP95Ms?.let { String.format(Locale.US, "%.1f", it) } ?: ""
                val fpsStr = res.avgFps?.let { String.format(Locale.US, "%.1f", it) } ?: ""
                val cpuStr = res.avgCpuPercent?.let { String.format(Locale.US, "%.1f", it) } ?: ""
                val execStr = res.execTimeMs?.toString() ?: ""
                val ramStr = res.peakRamMb?.let { String.format(Locale.US, "%.1f", it) } ?: ""
                val leakStr = res.leakCount?.toString() ?: ""
                val noteClean = (res.note ?: "").replace(",", ";")

                val line = "${res.module},${res.variant},${res.runIndex},\"$dateStr\",\"${res.deviceModel}\",${res.buildType},\"${res.scenarioName}\",$jankStr,$p95Str,$fpsStr,$cpuStr,$execStr,$ramStr,$leakStr,\"$noteClean\"\n"
                writer.write(line)
            }
        }
        return csvFile
    }

    /**
     * Mở hộp thoại chia sẻ file CSV qua Email, Drive, Zalo hoặc lưu vào máy tính.
     */
    fun shareCsv(context: Context, csvFile: File) {
        val uri = FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            csvFile
        )

        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "text/csv"
            putExtra(Intent.EXTRA_STREAM, uri)
            putExtra(Intent.EXTRA_SUBJECT, "Nhật ký số liệu đo hiệu năng PAA")
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }

        context.startActivity(Intent.createChooser(intent, "Xuất kết quả đo PAA qua"))
    }
}
