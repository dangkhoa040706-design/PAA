package com.nhomx.paa

import com.nhomx.paa.metrics.Stats
import org.junit.Assert.assertEquals
import org.junit.Test

class StatsTest {

    @Test
    fun testMean() {
        val numbers = listOf(10f, 20f, 30f, 40f, 50f)
        assertEquals(30f, Stats.mean(numbers), 0.001f)
    }

    @Test
    fun testPercentileP50() {
        val numbers = listOf(10f, 20f, 30f, 40f, 50f)
        assertEquals(30f, Stats.percentile(numbers, 50.0), 0.001f)
    }

    @Test
    fun testPercentileP90() {
        val numbers = listOf(1f, 2f, 3f, 4f, 5f, 6f, 7f, 8f, 9f, 10f)
        // Với n=10, rank = 0.9 * 9 = 8.1 -> numbers[8] = 9, numbers[9] = 10 -> 9.1
        assertEquals(9.1f, Stats.percentile(numbers, 90.0), 0.05f)
    }

    @Test
    fun testImprovementPercentLowerIsBetter() {
        // Jank % từ 25% giảm xuống 2.5% -> Cải thiện 90%
        val bad = 25f
        val opt = 2.5f
        assertEquals(90f, Stats.improvementPercent(bad, opt, lowerIsBetter = true), 0.001f)
    }

    @Test
    fun testImprovementPercentHigherIsBetter() {
        // FPS từ 40 tăng lên 58 -> Cải thiện 45%
        val bad = 40f
        val opt = 58f
        assertEquals(45f, Stats.improvementPercent(bad, opt, lowerIsBetter = false), 0.001f)
    }
}
