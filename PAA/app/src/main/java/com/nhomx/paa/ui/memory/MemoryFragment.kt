package com.nhomx.paa.ui.memory

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
import com.nhomx.paa.databinding.FragmentMemoryBinding
import com.nhomx.paa.metrics.MemorySampler
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.scenario.MemoryScenario
import com.nhomx.paa.ui.overlay.MetricsOverlayView
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

// =========================================================================
// --- [MÀN HÌNH GIAO DIỆN: PHÒNG LAB 3 - MEMORY LAB] ---
// Chức năng:
// 1. Cho phép chuyển đổi giữa BAD (Rò rỉ static) và OPTIMIZED (WeakReference).
// 2. Tích hợp nút kích hoạt Garbage Collection thủ công (System.gc()).
// 3. Khởi chạy kịch bản mở/đóng 10 Activity và hiển thị số lượng instance bị leak thực tế.
// =========================================================================
class MemoryFragment : Fragment() {

    private var _binding: FragmentMemoryBinding? = null
    private val binding get() = _binding!!

    private val viewModel: MemoryViewModel by viewModels()
    private val collector = MetricsCollector()
    private var scenario: MemoryScenario? = null
    private var scenarioJob: Job? = null
    private var overlayView: MetricsOverlayView? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentMemoryBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // --- KHỞI TẠO CÁC NÚT ĐIỀU KHIỂN & ĐỒNG HỒ ĐO RAM ---
        setupUI()
        setupOverlay()
        observeData()
        updateRamDisplay()
    }

    private fun setupUI() {
        // --- 1. Tiêu đề và nút quay lại ---
        binding.headerControls.tvModuleTitle.text = "3. Memory Lab"
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

        // --- 3. Nút Ép chạy Garbage Collector (System.gc) ---
        binding.btnManualGc.setOnClickListener {
            System.gc()
            Toast.makeText(requireContext(), "Đã gửi yêu cầu Garbage Collection tới máy ảo ART", Toast.LENGTH_SHORT).show()
            updateRamDisplay()
        }

        // --- 4. Nút Bắt đầu chu trình đo rò rỉ RAM (10 màn hình) ---
        binding.headerControls.btnRun.setOnClickListener {
            runMeasurement()
        }

        // --- 5. Nút Hủy đo ---
        binding.headerControls.btnCancel.setOnClickListener {
            cancelMeasurement()
        }

        // --- 6. Nút Lưu kết quả đo Memory ---
        binding.headerControls.btnSave.setOnClickListener {
            viewModel.saveResult {
                Toast.makeText(requireContext(), "Đã lưu kết quả đo Memory thành công!", Toast.LENGTH_SHORT).show()
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

        viewLifecycleOwner.lifecycleScope.launch {
            collector.snapshot.collectLatest { snapshot ->
                overlayView?.updateMetrics(snapshot)
                binding.tvCurrentRam.text = "RAM PSS: ${snapshot.ramMb.toInt()} MB"
            }
        }
    }

    // --- Cập nhật số liệu RAM PSS hiện tại lên màn hình ---
    private fun updateRamDisplay() {
        val currentRam = MemorySampler.samplePssMb()
        binding.tvCurrentRam.text = "RAM PSS: ${currentRam.toInt()} MB"
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
    }

    // --- [TIẾN HÀNH ĐO ĐẠC MEMORY LEAK]: Mở đóng 10 Activity liên tục ---
    private fun runMeasurement() {
        val window = requireActivity().window
        val currentScenario = MemoryScenario(
            context = requireContext(),
            window = window,
            collector = collector,
            variant = viewModel.variant.value
        )
        scenario = currentScenario

        binding.headerControls.btnRun.isEnabled = false
        binding.headerControls.btnCancel.isEnabled = true
        binding.headerControls.btnSave.isEnabled = false
        binding.headerControls.progressRunning.visibility = View.VISIBLE
        binding.resultPanel.cardResultPanel.visibility = View.GONE
        binding.cardLeakInfo.visibility = View.GONE

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
                updateRamDisplay()
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
        updateRamDisplay()
    }

    // --- HIỂN THỊ KẾT QUẢ ĐỐI CHỨNG RÒ RỈ RAM VÀ SỐ LƯỢNG INSTANCE LEAK ---
    private fun displayResult(res: MeasurementResult) {
        binding.resultPanel.cardResultPanel.visibility = View.VISIBLE
        binding.resultPanel.tvResultHeader.text = "KẾT QUẢ: MEMORY LAB - ${res.variant}"

        binding.resultPanel.tvResRam.text = res.peakRamMb?.let { "${it.toInt()} MB" } ?: "--"
        binding.resultPanel.tvResCpu.text = res.avgCpuPercent?.let { "${it.toInt()}%" } ?: "--"

        // Trong Memory Lab: tập trung hiển thị lượng RAM tiêu thụ đỉnh và rò rỉ
        binding.resultPanel.rowFpsJank.visibility = View.GONE
        binding.resultPanel.rowJankPercent.visibility = View.GONE
        binding.resultPanel.rowP95.visibility = View.GONE
        binding.resultPanel.rowExecTime.visibility = View.GONE

        res.note?.let {
            binding.cardLeakInfo.visibility = View.VISIBLE
            binding.tvLeakDetail.text = it
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
