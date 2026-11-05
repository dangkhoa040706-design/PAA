package com.nhomx.paa

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import com.nhomx.paa.databinding.ActivityMainBinding
import com.nhomx.paa.ui.home.HomeFragment

// =========================================================================
// --- [ACTIVITY TRUNG TÂM: MAIN ACTIVITY] ---
// Đóng vai trò là Host Activity chứa:
// 1. fragmentContainer: Điều hướng giữa Màn hình chính (Home) và 3 phòng Lab.
// 2. overlayContainer: Chứa thanh HUD Monitor nổi trên cùng hiển thị FPS, RAM, CPU thời gian thực.
// =========================================================================
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Khởi động màn hình chính (HomeFragment) khi mở app
        if (savedInstanceState == null) {
            openFragment(HomeFragment(), addToBackStack = false)
        }
    }

    /**
     * Hàm điều hướng chuyển đổi giữa các Fragment phòng Lab
     */
    fun openFragment(fragment: Fragment, addToBackStack: Boolean = true) {
        val transaction = supportFragmentManager.beginTransaction()
            .replace(R.id.fragmentContainer, fragment)
        if (addToBackStack) {
            transaction.addToBackStack(null)
        }
        transaction.commit()
    }
}
