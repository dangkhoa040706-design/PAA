package com.nhomx.paa.ui.jank

import androidx.recyclerview.widget.DiffUtil
import com.nhomx.paa.data.PhotoItem

class PhotoDiffCallback : DiffUtil.ItemCallback<PhotoItem>() {

    override fun areItemsTheSame(oldItem: PhotoItem, newItem: PhotoItem): Boolean {
        return oldItem.id == newItem.id
    }

    override fun areContentsTheSame(oldItem: PhotoItem, newItem: PhotoItem): Boolean {
        return oldItem == newItem
    }
}
