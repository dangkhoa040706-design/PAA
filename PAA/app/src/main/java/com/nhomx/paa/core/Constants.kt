package com.nhomx.paa.core

object Constants {
    // Jank Lab
    const val JANK_ITEM_COUNT = 200
    const val JANK_SCROLL_STEP_PX = 25
    const val BAD_DECODE_SAMPLE_SIZE = 1 // Chỉnh nếu máy yếu để cân bằng: giật rõ nhưng không OOM

    // CPU Lab
    const val CPU_N = 50_000
    const val CPU_DATA_FILE = "cpu_data.csv"

    // Memory Lab
    const val MEM_LOOPS = 20
    const val MEM_SCREEN_DELAY_MS = 350L

    // Test Data Assets
    const val ITEMS_JSON_FILE = "items.json"
    const val IMAGES_DIR = "images"
}
