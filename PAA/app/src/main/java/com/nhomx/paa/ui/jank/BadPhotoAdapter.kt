package com.nhomx.paa.ui.jank

import android.content.Context
import android.graphics.BitmapFactory
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.nhomx.paa.core.Constants
import com.nhomx.paa.data.PhotoItem
import com.nhomx.paa.databinding.ItemPhotoBadBinding

// =========================================================================
// --- [TEST JANK BAD: MÔ PHỎNG GIẬT LAG GIAO DIỆN] ---
// Nguyên nhân gây lag:
// 1. Nạp ảnh Bitmap trực tiếp trên luồng chính (Main Thread) làm đơ UI.
// 2. Chạy vòng lặp cộng chuỗi nặng và tính toán thừa ngay trong onBindViewHolder.
// 3. Gọi notifyDataSetChanged() bắt RecyclerView phải vẽ lại toàn bộ danh sách.
// =========================================================================
class BadPhotoAdapter(
    private val context: Context,
    private var items: List<PhotoItem>
) : RecyclerView.Adapter<BadPhotoAdapter.BadViewHolder>() {

    // --- Cập nhật dữ liệu kiểu cũ: Bắt vẽ lại toàn bộ không qua tính Diff ---
    fun updateData(newItems: List<PhotoItem>) {
        this.items = newItems
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BadViewHolder {
        val binding = ItemPhotoBadBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return BadViewHolder(binding)
    }

    override fun onBindViewHolder(holder: BadViewHolder, position: Int) {
        val item = items[position]

        // --- BƯỚC 1: Gán nội dung văn bản cơ bản ---
        holder.binding.tvTitleBad.text = item.title
        holder.binding.tvIdBad.text = "#${item.id}"

        // --- BƯỚC 2: [LỖI HIỆU NĂNG 1] Tính toán thừa & nối chuỗi liên tục trên Main Thread ---
        var redundantStr = ""
        for (i in 0 until 50) {
            redundantStr += "${item.title.length * i},"
        }
        holder.binding.tvDescBad.text = "${item.description} [hash: ${redundantStr.hashCode()}]"

        // --- BƯỚC 3: [LỖI HIỆU NĂNG 2] Đọc và giải mã ảnh Bitmap thô chặn đứng Main Thread (>16.67ms) ---
        try {
            val assetPath = "${Constants.IMAGES_DIR}/${item.imageName}"
            context.assets.open(assetPath).use { stream ->
                val options = BitmapFactory.Options().apply {
                    inSampleSize = Constants.BAD_DECODE_SAMPLE_SIZE
                }
                val bitmap = BitmapFactory.decodeStream(stream, null, options)
                holder.binding.ivPhotoBad.setImageBitmap(bitmap)
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    override fun getItemCount(): Int = items.size

    class BadViewHolder(val binding: ItemPhotoBadBinding) : RecyclerView.ViewHolder(binding.root)
}
