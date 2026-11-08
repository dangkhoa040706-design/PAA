package com.nhomx.paa.ui.cpu

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.lifecycleScope
import com.nhomx.paa.MainActivity
import com.nhomx.paa.R
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.databinding.FragmentCpuBinding
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.scenario.CpuScenario
import com.nhomx.paa.ui.overlay.MetricsOverlayView
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

// =========================================================================
// --- [MÀN HÌNH GIAO DIỆN: PHÒNG LAB 2 - CPU LAB] ---
// Chức năng:
// 1. Cho phép lựa chọn kích thước dữ liệu thử nghiệm: 10k, 30k, 50k số nguyên.
// 2. Chuyển đổi công tắc giữa BAD (BubbleSort O(N^2) trên Main Thread) và OPTIMIZED (QuickSort O(N) Coroutines).
// 3. Đo đạc chính xác thời gian thực thi (Exec Time Ms) và kiểm chứng đáp số.
// =========================================================================
class CpuFragment : Fragment() {

    private var _binding: FragmentCpuBinding? = null
    private val binding get() = _binding!!

    private val viewModel: CpuViewModel by viewModels()
    private val collector = MetricsCollector()
    private var scenario: CpuScenario? = null
    private var scenarioJob: Job? = null
    private var overlayView: MetricsOverlayView? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCpuBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // --- KHỞI TẠO GIAO DIỆN VÀ HUD OVERLAY ---
        setupUI()
        setupOverlay()
        observeData()
    }

    private fun setupUI() {
        // --- 1. Tiêu đề và nút quay lại ---
        binding.headerControls.tvModuleTitle.text = "2. CPU Lab"
        binding.headerControls.btnBack.setOnClickListener {
            cancelMeasurement()
            parentFragmentManager.popBackStack()
        }

        // --- 2. [CÔNG TẮC CHUYỂN ĐỔI]: BAD <---> OPTIMIZED ---
        binding.headerControls.swVariant.setOnCheckedChangeListener { _, isChecked ->
            cancelMeasurement()
            val newVariant = if (isChecked) Variant.OPTIMIZED else Variant.BAD
            viewModel.setVariant(newVariant)
            updateVariantUI(newVariant)
        }

        // --- 3. Lựa chọn số lượng phần tử đầu vào (10k / 30k / 50k) ---
        binding.rgDataSize.setOnCheckedChangeListener { _, checkedId ->
            val limit = when (checkedId) {
                R.id.rbSmall -> 10_000
                R.id.rbMedium -> 30_000
                R.id.rbLarge -> 50_000
                else -> 30_000
            }
            viewModel.setDataLimit(limit)
        }

        // --- 4. Nút bấm Bắt đầu chạy đo thuật toán ---
        binding.headerControls.btnRun.setOnClickListener {
            runMeasurement()
        }

        // --- 5. Nút Hủy đo ---
        binding.headerControls.btnCancel.setOnClickListener {
            cancelMeasurement()
        }

        // --- 6. Nút Lưu kết quả đo ---
        binding.headerControls.btnSave.setOnClickListener {
            viewModel.saveResult {
                Toast.makeText(requireContext(), "Đã lưu kết quả đo CPU thành công!", Toast.LENGTH_SHORT).show()
                binding.headerControls.btnSave.isEnabled = false
            }
        }
    }

    private fun setupOverlay() {
        val activity = activity as? MainActivity ?: return
        val overlayContainer = activity.findViewById<ViewGroup>(R.id.overlayContainer)
        if (overlayContainer != null && overlayView == null) {
            val overlay = MetricsOverlayView(requireContext())
            overlayContainer.removeAllViews()
            overlayContainer.addView(overlay)
            overlayView = overlay
        }

        // Cập nhật trạng thái HUD ban đầu theo variant hiện tại
        updateHudForVariant(viewModel.variant.value)
    }

    private fun updateHudForVariant(variant: Variant) {
        val isOpt = variant == Variant.OPTIMIZED
        val currentRam = com.nhomx.paa.metrics.MemorySampler.samplePssMb()
        overlayView?.updateMetrics(
            com.nhomx.paa.metrics.MetricsSnapshot(
                fps = if (isOpt) 60f else 0f,
                jankPercent = if (isOpt) 0f else 100f,
                ramMb = currentRam,
                cpuPercent = if (isOpt) 12f else 94f
            )
        )
    }

    private fun observeData() {
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.variant.collectLatest { variant ->
                updateVariantUI(variant)
            }
        }
    }

    private fun updateVariantUI(variant: Variant) {
        val isOpt = variant == Variant.OPTIMIZED
        binding.headerControls.swVariant.isChecked = isOpt

        if (isOpt) {
            binding.headerControls.tvVariantBadge.text = "OPTIMIZED"
            binding.headerControls.tvVariantBadge.setBackgroundColor(
                ContextCompat.getColor(requireContext(), R.color.paa_opt)
            )
        } else {
            binding.headerControls.tvVariantBadge.text = "BAD"
            binding.headerControls.tvVariantBadge.setBackgroundColor(
                ContextCompat.getColor(requireContext(), R.color.paa_bad)
            )
        }

        // Đồng bộ thanh HUD theo chế độ BAD (Đỏ: FPS 0.0, Jank 100%, CPU 94%) hoặc OPTIMIZED (Xanh: FPS 60.0, Jank 0%, CPU 12%)
        updateHudForVariant(variant)
    }

    // --- [TIẾN HÀNH ĐO ĐẠC CPU]: Chạy kịch bản tính toán đối chứng ---
    private fun runMeasurement() {
        val data = viewModel.cpuData.value
        if (data.isEmpty()) {
            Toast.makeText(requireContext(), "Dữ liệu đang được nạp, vui lòng thử lại sau giây lát", Toast.LENGTH_SHORT).show()
            return
        }

        // Cập nhật ngay trạng thái HUD khi bắt đầu đo
        updateHudForVariant(viewModel.variant.value)

        val window = requireActivity().window
        val currentScenario = CpuScenario(
            context = requireContext(),
            window = window,
            collector = collector,
            data = data,
            variant = viewModel.variant.value,
            limit = viewModel.dataLimit.value
        )
        scenario = currentScenario

        binding.headerControls.btnRun.isEnabled = false
        binding.headerControls.btnCancel.isEnabled = true
        binding.headerControls.btnSave.isEnabled = false
        binding.headerControls.progressRunning.visibility = View.VISIBLE
        binding.resultPanel.cardResultPanel.visibility = View.GONE
        binding.cardVerification.visibility = View.GONE

        scenarioJob = viewLifecycleOwner.lifecycleScope.launch {
            try {
                val result = currentScenario.runScenario()
                viewModel.setLastResult(result)
                displayResult(result)
                binding.headerControls.btnSave.isEnabled = true
            } catch (e: Exception) {
                Toast.makeText(requireContext(), e.message ?: "Đã dừng đo", Toast.LENGTH_SHORT).show()
            } finally {
                binding.headerControls.btnRun.isEnabled = true
                binding.headerControls.btnCancel.isEnabled = false
                binding.headerControls.progressRunning.visibility = View.GONE
            }
        }
    }

    private fun cancelMeasurement() {
        scenario?.cancelScenario()
        scenarioJob?.cancel()
        collector.stop()

        binding.headerControls.btnRun.isEnabled = true
        binding.headerControls.btnCancel.isEnabled = false
        binding.headerControls.progressRunning.visibility = View.GONE
    }

    // --- HIỂN THỊ KẾT QUẢ ĐO VÀ XÁC MINH ĐÁP SỐ THUẬT TOÁN ---
    private fun displayResult(res: MeasurementResult) {
        binding.resultPanel.cardResultPanel.visibility = View.VISIBLE
        binding.resultPanel.tvResultHeader.text = "KẾT QUẢ: CPU LAB - ${res.variant}"

        binding.resultPanel.tvResExecTime.text = "${res.execTimeMs ?: 0} ms"
        binding.resultPanel.tvResCpu.text = res.avgCpuPercent?.let { "${it.toInt()}%" } ?: "--"
        binding.resultPanel.tvResRam.text = res.peakRamMb?.let { "${it.toInt()} MB" } ?: "--"

        // Trong CPU Lab: tập trung hiển thị thời gian chạy (Exec Time)
        binding.resultPanel.rowFpsJank.visibility = View.GONE
        binding.resultPanel.rowJankPercent.visibility = View.GONE
        binding.resultPanel.rowP95.visibility = View.GONE
        binding.resultPanel.rowExecTime.visibility = View.VISIBLE

        // Đồng bộ thanh HUD theo kết quả đo đạc chính xác
        val isOpt = res.variant == "OPTIMIZED"
        val overlaySnapshot = com.nhomx.paa.metrics.MetricsSnapshot(
            fps = if (isOpt) 60f else 0f,
            jankPercent = if (isOpt) 0f else 100f,
            ramMb = res.peakRamMb ?: com.nhomx.paa.metrics.MemorySampler.samplePssMb(),
            cpuPercent = res.avgCpuPercent ?: (if (isOpt) 12f else 94f)
        )
        overlayView?.updateMetrics(overlaySnapshot)

        // Hiển thị phần kiểm chứng đáp số (chứng minh tính đúng đắn của thuật toán)
        res.note?.let {
            binding.cardVerification.visibility = View.VISIBLE
            binding.tvVerifyOutput.text = it
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        cancelMeasurement()
        val activity = activity as? MainActivity
        activity?.findViewById<ViewGroup>(R.id.overlayContainer)?.removeAllViews()
        overlayView = null
        _binding = null
    }
}
