package com.nhomx.paa.ui.overlay

import android.content.Context
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.FrameLayout
import androidx.core.content.ContextCompat
import com.nhomx.paa.R
import com.nhomx.paa.databinding.ViewOverlayBinding
import com.nhomx.paa.metrics.MetricsSnapshot

// =========================================================================
// --- [THANH HUD OVERLAY GIÁM SÁT HIỆU NĂNG THỜI GIAN THỰC] ---
// Chức năng:
// 1. Luôn nổi trên đỉnh màn hình trong suốt quá trình người dùng thao tác.
// 2. Hiển thị 4 thông số: FPS, Jank %, RAM (MB) và CPU (%).
// 3. Tự động đổi màu chỉ thị: Xanh lá (Tốt) -> Vàng (Cảnh báo) -> Đỏ (Nguy hiểm).
// 4. Có nút thu nhỏ/mở rộng để không che khuất nội dung bên dưới.
// =========================================================================
class MetricsOverlayView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : FrameLayout(context, attrs, defStyleAttr) {

    private val binding: ViewOverlayBinding =
        ViewOverlayBinding.inflate(LayoutInflater.from(context), this, true)

    private val colorGood = ContextCompat.getColor(context, R.color.paa_overlay_good)
    private val colorWarn = ContextCompat.getColor(context, R.color.paa_overlay_warn)
    private val colorBad = ContextCompat.getColor(context, R.color.paa_overlay_bad)

    init {
        // --- Nút thu nhỏ / phóng to thanh HUD ---
        binding.ivToggleVisibility.setOnClickListener {
            val isValuesVisible = binding.tvFpsValue.visibility == VISIBLE
            val newVisibility = if (isValuesVisible) GONE else VISIBLE

            binding.tvFpsLabel.visibility = newVisibility
            binding.tvFpsValue.visibility = newVisibility
            binding.tvJankLabel.visibility = newVisibility
            binding.tvJankValue.visibility = newVisibility
            binding.tvRamLabel.visibility = newVisibility
            binding.tvRamValue.visibility = newVisibility
            binding.tvCpuLabel.visibility = newVisibility
            binding.tvCpuValue.visibility = newVisibility

            binding.ivToggleVisibility.setImageResource(
                if (isValuesVisible) android.R.drawable.ic_menu_info_details
                else android.R.drawable.ic_menu_close_clear_cancel
            )
        }
    }

    /**
     * Cập nhật các chỉ số hiệu năng lên thanh HUD và tự động đổi màu cảnh báo
     */
    fun updateMetrics(snapshot: MetricsSnapshot) {
        // --- 1. CẬP NHẬT TỐC ĐỘ KHUNG HÌNH (FPS) ---
        // >= 55 FPS: Xanh lá (Mượt mà) | 40 - 54 FPS: Vàng (Khựng nhẹ) | < 40 FPS: Đỏ (Lag nặng / Đơ)
        binding.tvFpsValue.text = if (snapshot.fps > 0) String.format("%.1f", snapshot.fps) else if (snapshot.jankPercent >= 50f) "0.0" else "--"
        binding.tvFpsValue.setTextColor(
            when {
                snapshot.fps >= 55f -> colorGood
                snapshot.fps >= 40f -> colorWarn
                else -> colorBad
            }
        )

        // --- 2. CẬP NHẬT TỶ LỆ RỚT KHUNG HÌNH (JANK %) ---
        // <= 5%: Xanh lá | 5% - 15%: Vàng | > 15%: Đỏ (Rất nghiêm trọng)
        binding.tvJankValue.text = String.format("%.1f%%", snapshot.jankPercent)
        binding.tvJankValue.setTextColor(
            when {
                snapshot.jankPercent <= 5f -> colorGood
                snapshot.jankPercent <= 15f -> colorWarn
                else -> colorBad
            }
        )

        // --- 3. CẬP NHẬT BỘ NHỚ RAM PSS (MEGABYTE) ---
        binding.tvRamValue.text = "${snapshot.ramMb.toInt()}MB"

        // --- 4. CẬP NHẬT MỨC SỬ DỤNG CPU TỔNG THỂ (%) ---
        // < 40%: Xanh lá | 40% - 75%: Vàng | >= 75%: Đỏ (Quá tải CPU)
        binding.tvCpuValue.text = "${snapshot.cpuPercent.toInt()}%"
        binding.tvCpuValue.setTextColor(
            when {
                snapshot.cpuPercent < 40f -> colorGood
                snapshot.cpuPercent < 75f -> colorWarn
                else -> colorBad
            }
        )
    }
}
