package com.nhomx.paa.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.nhomx.paa.MainActivity
import com.nhomx.paa.databinding.FragmentHomeBinding
import com.nhomx.paa.ui.cpu.CpuFragment
import com.nhomx.paa.ui.jank.JankFragment
import com.nhomx.paa.ui.memory.MemoryFragment
import com.nhomx.paa.ui.results.ResultsFragment
import com.nhomx.paa.util.DeviceInfo

// =========================================================================
// --- [MÀN HÌNH CHÍNH: HOME FRAGMENT (DASHBOARD)] ---
// Chức năng:
// 1. Tự động nhận diện và hiển thị thông tin phần cứng thiết bị (Model máy, phiên bản Android, RAM).
// 2. Cung cấp 3 thẻ chọn dẫn tới 3 phòng Lab thực nghiệm (Jank Lab, CPU Lab, Memory Lab).
// 3. Nút truy cập bảng tổng hợp kết quả đối chứng định lượng (ResultsFragment).
// =========================================================================
class HomeFragment : Fragment() {

    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // --- 1. Hiển thị thông số phần cứng thiết bị đang đo đạc ---
        binding.tvDeviceInfo.text = DeviceInfo.getDeviceSummary(requireContext())

        val mainActivity = activity as? MainActivity

        // --- 2. Điều hướng tới Phòng Lab 1: UI Jank ---
        binding.cardJank.setOnClickListener {
            mainActivity?.openFragment(JankFragment())
        }

        // --- 3. Điều hướng tới Phòng Lab 2: Nghẽn CPU ---
        binding.cardCpu.setOnClickListener {
            mainActivity?.openFragment(CpuFragment())
        }

        // --- 4. Điều hướng tới Phòng Lab 3: Rò rỉ RAM (Memory Leak) ---
        binding.cardMemory.setOnClickListener {
            mainActivity?.openFragment(MemoryFragment())
        }

        // --- 5. Điều hướng tới Bảng tổng hợp kết quả (Results) ---
        binding.btnResults.setOnClickListener {
            mainActivity?.openFragment(ResultsFragment())
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        // Giải phóng view binding theo chuẩn Android Lifecycle để tránh rò rỉ RAM
        _binding = null
    }
}
