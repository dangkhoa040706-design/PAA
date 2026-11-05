package com.nhomx.paa.ui.jank

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.nhomx.paa.MainActivity
import com.nhomx.paa.R
import com.nhomx.paa.core.Variant
import com.nhomx.paa.data.MeasurementResult
import com.nhomx.paa.databinding.FragmentJankBinding
import com.nhomx.paa.metrics.MetricsCollector
import com.nhomx.paa.scenario.JankScenario
import com.nhomx.paa.scenario.ScenarioState
import com.nhomx.paa.ui.overlay.MetricsOverlayView
import kotlinx.coroutines.Job
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch

// =========================================================================
// --- [MÀN HÌNH GIAO DIỆN: PHÒNG LAB 1 - JANK LAB] ---
// Chức năng:
// 1. Cho phép chuyển đổi nhanh giữa hai chế độ: BAD (Layout lồng 6 tầng) vs OPTIMIZED (ConstraintLayout).
// 2. Tích hợp nút chạy kiểm thử tự động cuộn danh sách (JankScenario).
// 3. Hiển thị bảng kết quả định lượng: FPS, Jank %, P95, Peak RAM, Avg CPU.
// =========================================================================
class JankFragment : Fragment() {

    private var _binding: FragmentJankBinding? = null
    private val binding get() = _binding!!

    private val viewModel: JankViewModel by viewModels()
    private val collector = MetricsCollector()
    private var scenario: JankScenario? = null
    private var scenarioJob: Job? = null

    private var badAdapter: BadPhotoAdapter? = null
    private var goodAdapter: GoodPhotoAdapter? = null
    private var overlayView: MetricsOverlayView? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentJankBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // --- KHỞI TẠO CÁC THÀNH PHẦN GIAO DIỆN & OVERLAY ---
        setupUI()
        setupOverlay()
        observeData()
    }

    private fun setupUI() {
        val mainActivity = activity as? MainActivity

        // --- 1. Tiêu đề và nút quay lại ---
        binding.headerControls.tvModuleTitle.text = "1. Jank Lab"
        binding.headerControls.btnBack.setOnClickListener {
            scenario?.cancelScenario()
            collector.stop()
            parentFragmentManager.popBackStack()
        }

        // --- 2. Cấu hình danh sách cuộn RecyclerView ---
        binding.rvPhotos.layoutManager = LinearLayoutManager(requireContext())
        binding.rvPhotos.setHasFixedSize(true)

        // --- 3. [CÔNG TẮC CHUYỂN ĐỔI]: BAD (Chưa tối ưu) <---> OPTIMIZED (Đã tối ưu) ---
        binding.headerControls.swVariant.setOnCheckedChangeListener { _, isChecked ->
            cancelMeasurement()
            val newVariant = if (isChecked) Variant.OPTIMIZED else Variant.BAD
            viewModel.setVariant(newVariant)
            updateVariantUI(newVariant)
            applyAdapter(newVariant)
        }

        // --- 4. Nút bấm Chạy kịch bản đo đạc tự động ---
        binding.headerControls.btnRun.setOnClickListener {
            runMeasurement()
        }

        // --- 5. Nút Hủy đo ---
        binding.headerControls.btnCancel.setOnClickListener {
            cancelMeasurement()
        }

        // --- 6. Nút Lưu kết quả vào cơ sở dữ liệu JSON ---
        binding.headerControls.btnSave.setOnClickListener {
            viewModel.saveResult {
                Toast.makeText(requireContext(), "Đã lưu kết quả đo thành công!", Toast.LENGTH_SHORT).show()
                binding.headerControls.btnSave.isEnabled = false
            }
        }
    }

    private fun setupOverlay() {
        // Gắn thanh HUD Monitor nổi lên trên cùng màn hình
        val activity = activity as? MainActivity ?: return
        val overlayContainer = activity.findViewById<ViewGroup>(R.id.overlayContainer)
        if (overlayContainer != null && overlayView == null) {
            val overlay = MetricsOverlayView(requireContext())
            overlayContainer.removeAllViews()
            overlayContainer.addView(overlay)
            overlayView = overlay
        }

        // Cập nhật số liệu FPS, RAM, CPU lên HUD theo thời gian thực
        viewLifecycleOwner.lifecycleScope.launch {
            collector.snapshot.collectLatest { snapshot ->
                overlayView?.updateMetrics(snapshot)
            }
        }
    }

    private fun observeData() {
        // Lắng nghe dữ liệu danh sách ảnh từ ViewModel
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.items.collectLatest { items ->
                if (items.isNotEmpty()) {
                    badAdapter = BadPhotoAdapter(requireContext(), items)
                    goodAdapter = GoodPhotoAdapter().apply { submitList(items) }
                    applyAdapter(viewModel.variant.value)
                }
            }
        }

        // Lắng nghe trạng thái BAD / OPTIMIZED
        viewLifecycleOwner.lifecycleScope.launch {
            viewModel.variant.collectLatest { variant ->
                updateVariantUI(variant)
            }
        }
    }

    // --- Áp dụng Adapter tương ứng với chế độ đang chọn ---
    private fun applyAdapter(variant: Variant) {
        if (variant == Variant.BAD) {
            binding.rvPhotos.adapter = badAdapter
        } else {
            binding.rvPhotos.adapter = goodAdapter
        }
    }

    // --- Cập nhật giao diện Huy hiệu (Badge) đỏ/xanh tương ứng ---
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

    // --- [TIẾN HÀNH ĐO ĐẠC]: Khởi chạy kịch bản cuộn danh sách tự động ---
    private fun runMeasurement() {
        val window = requireActivity().window
        val currentScenario = JankScenario(requireContext(), window, binding.rvPhotos, collector)
        scenario = currentScenario

        binding.headerControls.btnRun.isEnabled = false
        binding.headerControls.btnCancel.isEnabled = true
        binding.headerControls.btnSave.isEnabled = false
        binding.headerControls.progressRunning.visibility = View.VISIBLE
        binding.resultPanel.cardResultPanel.visibility = View.GONE

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

    // --- HIỂN THỊ BẢNG KẾT QUẢ ĐỐI CHỨNG ĐỊNH LƯỢNG ---
    private fun displayResult(res: MeasurementResult) {
        binding.resultPanel.cardResultPanel.visibility = View.VISIBLE
        binding.resultPanel.tvResultHeader.text = "KẾT QUẢ: JANK LAB - ${res.variant}"

        binding.resultPanel.tvResFps.text = res.avgFps?.let { String.format("%.1f", it) } ?: "--"
        binding.resultPanel.tvResJank.text = res.jankPercent?.let { String.format("%.1f%%", it) } ?: "--"
        binding.resultPanel.tvResP95.text = res.frameP95Ms?.let { String.format("%.1f ms", it) } ?: "--"
        binding.resultPanel.tvResRam.text = res.peakRamMb?.let { "${it.toInt()} MB" } ?: "--"
        binding.resultPanel.tvResCpu.text = res.avgCpuPercent?.let { "${it.toInt()}%" } ?: "--"

        // Ẩn hàng thời gian tính toán vì thuộc về CPU Lab
        binding.resultPanel.rowExecTime.visibility = View.GONE
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
