package com.nhomx.paa.ui.results

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import com.nhomx.paa.R
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.databinding.ItemResultBinding
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class ResultAdapter(
    private var results: List<MeasurementResult>,
    private val onDeleteClick: (MeasurementResult) -> Unit
) : RecyclerView.Adapter<ResultAdapter.ResultViewHolder>() {

    private val dateFormat = SimpleDateFormat("dd/MM HH:mm", Locale.getDefault())

    fun updateList(newList: List<MeasurementResult>) {
        this.results = newList
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ResultViewHolder {
        val binding = ItemResultBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ResultViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ResultViewHolder, position: Int) {
        val item = results[position]
        val context = holder.itemView.context

        holder.binding.tvItemModule.text = item.module
        holder.binding.tvItemVariant.text = item.variant
        holder.binding.tvItemTime.text = dateFormat.format(Date(item.timestamp))
        holder.binding.tvItemScenario.text = "Kịch bản: ${item.scenarioName}"

        // Đổi màu badge theo BAD (đỏ) hoặc OPTIMIZED (xanh lá)
        val isOpt = item.variant.equals(Variant.OPTIMIZED.name, ignoreCase = true)
        val badgeColor = if (isOpt) {
            ContextCompat.getColor(context, R.color.paa_opt)
        } else {
            ContextCompat.getColor(context, R.color.paa_bad)
        }
        holder.binding.tvItemVariant.setBackgroundColor(badgeColor)

        // Tổng hợp chuỗi chỉ số theo module
        val metricsSummary = buildString {
            when (item.module.uppercase(Locale.US)) {
                "JANK" -> {
                    append("FPS: ${item.avgFps ?: "--"} | ")
                    append("Jank: ${item.jankPercent ?: "--"}% | ")
                    append("P95: ${item.frameP95Ms?.toInt() ?: "--"}ms | ")
                    append("RAM: ${item.peakRamMb?.toInt() ?: "--"}MB")
                }
                "CPU" -> {
                    append("Thời gian: ${item.execTimeMs ?: "--"}ms | ")
                    append("CPU: ${item.avgCpuPercent?.toInt() ?: "--"}% | ")
                    append("RAM: ${item.peakRamMb?.toInt() ?: "--"}MB")
                }
                "MEMORY" -> {
                    append("RAM đỉnh: ${item.peakRamMb?.toInt() ?: "--"}MB | ")
                    append("Số leak: ${item.leakCount ?: 0} instance")
                }
                else -> {
                    append("RAM: ${item.peakRamMb?.toInt() ?: "--"}MB | ")
                    append("CPU: ${item.avgCpuPercent?.toInt() ?: "--"}%")
                }
            }
        }
        holder.binding.tvItemMetrics.text = metricsSummary

        holder.binding.btnDeleteItem.setOnClickListener {
            onDeleteClick(item)
        }
    }

    override fun getItemCount(): Int = results.size

    class ResultViewHolder(val binding: ItemResultBinding) : RecyclerView.ViewHolder(binding.root)
}
