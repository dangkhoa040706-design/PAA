package com.nhomx.paa.ui.results

import android.os.Bundle
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.nhomx.paa.R
import com.nhomx.paa.core.Module
import com.nhomx.paa.databinding.FragmentResultsBinding
import com.nhomx.paa.util.Exporter
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

class ResultsFragment : Fragment() {

    private var _binding: FragmentResultsBinding? = null
    private val binding get() = _binding!!

    private val viewModel: ResultsViewModel by viewModels()
    private var adapter: ResultAdapter? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentResultsBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        setupUI()
        observeData()
    }

    private fun setupUI() {
        binding.btnBack.setOnClickListener {
            parentFragmentManager.popBackStack()
        }

        // 1. RecyclerView lịch sử
        adapter = ResultAdapter(emptyList()) { result ->
            // Xác nhận xóa từng item
            AlertDialog.Builder(requireContext())
                .setTitle("Xác nhận xóa")
                .setMessage("Bạn có chắc chắn muốn xóa bản ghi đo #${result.runIndex} (${result.module} - ${result.variant})?")
                .setPositiveButton("Xóa") { _, _ ->
                    viewModel.deleteResult(result.id)
                }
                .setNegativeButton("Hủy", null)
                .show()
        }
        binding.rvHistory.layoutManager = LinearLayoutManager(requireContext())
        binding.rvHistory.adapter = adapter

        // 2. ChipGroup chọn module
        binding.chipGroupModules.setOnCheckedStateChangeListener { _, checkedIds ->
            if (checkedIds.isEmpty()) return@setOnCheckedStateChangeListener
            val selectedModule = when (checkedIds.first()) {
                R.id.chipJank -> Module.JANK.name
                R.id.chipCpu -> Module.CPU.name
                R.id.chipMemory -> Module.MEMORY.name
                else -> Module.JANK.name
            }
            viewModel.selectModule(selectedModule)
        }

        // 3. Nút Xuất CSV
        binding.btnExportCsv.setOnClickListener {
            val list = viewModel.allResults.value
            if (list.isEmpty()) {
                Toast.makeText(requireContext(), "Chưa có dữ liệu nào để xuất!", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            try {
                val csvFile = Exporter.exportToCsv(requireContext(), list)
                Exporter.shareCsv(requireContext(), csvFile)
            } catch (e: Exception) {
                Toast.makeText(requireContext(), "Lỗi khi xuất file: ${e.message}", Toast.LENGTH_SHORT).show()
            }
        }

        // 4. Nút Xóa toàn bộ lịch sử
        binding.btnClearAll.setOnClickListener {
            AlertDialog.Builder(requireContext())
                .setTitle("Xóa toàn bộ lịch sử")
                .setMessage("Hành động này sẽ xóa toàn bộ các lần đo đã lưu trong máy. Bạn có chắc không?")
                .setPositiveButton("Xóa tất cả") { _, _ ->
                    viewModel.clearHistory()
                    Toast.makeText(requireContext(), "Đã làm sạch toàn bộ lịch sử đo!", Toast.LENGTH_SHORT).show()
                }
                .setNegativeButton("Hủy", null)
                .show()
        }
    }

    private fun observeData() {
        // Lịch sử toàn bộ
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.allResults.collectLatest { list ->
                adapter?.updateList(list)
            }
        }

        // Ghi chú khi thiếu dữ liệu đối chiếu
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.comparisonNote.collectLatest { note ->
                if (note != null) {
                    binding.tvCompareNote.visibility = View.VISIBLE
                    binding.tvCompareNote.text = note
                    binding.llComparisonRows.visibility = View.GONE
                } else {
                    binding.tvCompareNote.visibility = View.GONE
                    binding.llComparisonRows.visibility = View.VISIBLE
                }
            }
        }

        // Các hàng so sánh
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.comparisonRows.collectLatest { rows ->
                renderComparisonRows(rows)
            }
        }
    }

    private fun renderComparisonRows(rows: List<ComparisonRow>) {
        binding.llComparisonRows.removeAllViews()
        val context = requireContext()

        val colorInk = ContextCompat.getColor(context, R.color.paa_ink)
        val colorOpt = ContextCompat.getColor(context, R.color.paa_opt)
        val colorBad = ContextCompat.getColor(context, R.color.paa_bad)
        val colorOutline = ContextCompat.getColor(context, R.color.paa_outline)

        for (row in rows) {
            val rowLayout = LinearLayout(context).apply {
                orientation = LinearLayout.HORIZONTAL
                setPadding(8, 12, 8, 12)
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT
                )
            }

            // Tên chỉ số
            val tvMetric = TextView(context).apply {
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1.4f)
                text = row.metricName
                setTextColor(colorInk)
                textSize = 12f
            }

            // Giá trị BAD
            val tvBad = TextView(context).apply {
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f)
                text = row.badValue
                setTextColor(colorBad)
                gravity = Gravity.CENTER
                textSize = 12f
            }

            // Giá trị OPT
            val tvOpt = TextView(context).apply {
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f)
                text = row.optValue
                setTextColor(colorOpt)
                gravity = Gravity.CENTER
                textSize = 12f
            }

            // % Cải thiện
            val tvImprovement = TextView(context).apply {
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1.2f)
                text = row.improvement
                setTextColor(if (row.isPositive) colorOpt else colorBad)
                gravity = Gravity.END
                textSize = 12f
            }

            rowLayout.addView(tvMetric)
            rowLayout.addView(tvBad)
            rowLayout.addView(tvOpt)
            rowLayout.addView(tvImprovement)

            binding.llComparisonRows.addView(rowLayout)

            // Divider nhỏ giữa các dòng
            val divider = View(context).apply {
                layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, 1)
                setBackgroundColor(colorOutline)
            }
            binding.llComparisonRows.addView(divider)
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
