package com.nhomx.paa.metrics

import kotlin.math.roundToInt

object Stats {

    /**
     * Tính giá trị phân vị percentile p (0 đến 100).
     * Yêu cầu values không rỗng.
     */
    fun percentile(values: List<Float>, p: Double): Float {
        if (values.isEmpty()) return 0f
        if (values.size == 1) return values[0]
        val sorted = values.sorted()
        val rank = (p / 100.0) * (sorted.size - 1)
        val lowerIndex = rank.toInt()
        val fraction = rank - lowerIndex
        return if (lowerIndex >= sorted.size - 1) {
            sorted.last()
        } else {
            sorted[lowerIndex] + (fraction * (sorted[lowerIndex + 1] - sorted[lowerIndex])).toFloat()
        }
    }

    /**
     * Tính trung bình cộng của danh sách số.
     */
    fun mean(values: List<Float>): Float {
        if (values.isEmpty()) return 0f
        return values.sum() / values.size
    }

    /**
     * Tính phần trăm cải thiện giữa bản BAD và bản OPTIMIZED.
     * @param bad Giá trị của bản BAD.
     * @param opt Giá trị của bản OPTIMIZED.
     * @param lowerIsBetter true nếu chỉ số càng thấp càng tốt (ví dụ jank%, execTime, RAM);
     *                      false nếu chỉ số càng cao càng tốt (ví dụ FPS).
     * @return Phần trăm cải thiện (+% là tốt hơn).
     */
    fun improvementPercent(bad: Float, opt: Float, lowerIsBetter: Boolean): Float {
        if (bad == 0f) return 0f
        return if (lowerIsBetter) {
            ((bad - opt) / bad) * 100f
        } else {
            ((opt - bad) / bad) * 100f
        }
    }

    /**
     * Làm tròn 1 chữ số thập phân
     */
    fun round1(value: Float): Float {
        return (value * 10f).roundToInt() / 10f
    }
}
