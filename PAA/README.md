# PAA - Performance Analysis App
> **Ứng dụng Phòng Thí Nghiệm Phân Tích & Tối Ưu Hiệu Năng Android**  
> Đề tài 1: *Android Application Performance Analysis and Optimization* (Giữa kỳ)

---

## 1. Giới thiệu dự án
**PAA** là ứng dụng Android được thiết kế theo triết lý thực nghiệm: *"Tạo bệnh (BAD) $\rightarrow$ Chẩn đoán bệnh (Profiler/ADB/LeakCanary) $\rightarrow$ Chữa bệnh (OPTIMIZED) $\rightarrow$ Đo lường & So sánh số liệu Trước/Sau"*.

Ứng dụng cung cấp 3 module thực nghiệm chuyên sâu:
1. **Jank Lab (Lag/Giật giao diện):**
   - **BAD:** Decode Bitmap lớn từ Assets trực tiếp trên Main Thread trong `onBindViewHolder`, Layout lồng 5–6 tầng lồng nhau gây overdraw nặng, gọi `notifyDataSetChanged()`.
   - **OPTIMIZED:** Tải ảnh bất đồng bộ + resize với Coil (`file:///android_asset/images/`), `ListAdapter` + `DiffUtil.ItemCallback`, Layout phẳng 1 tầng `ConstraintLayout`.
2. **CPU Lab (Tải tính toán nặng):**
   - **BAD:** Thuật toán $O(n^2)$ duyệt cặp tìm phần tử trùng và tính tổng trên 50.000 số nguyên (`cpu_data.csv`) chạy trực tiếp trên Main Thread, làm đơ UI.
   - **OPTIMIZED:** Thuật toán $O(n)$ với `HashMap` chạy trên `Dispatchers.Default` (Coroutines), cache kết quả, UI mượt mà, phản hồi tiến trình. Hai bản cho **cùng một đáp số**.
3. **Memory Lab (Rò rỉ bộ nhớ):**
   - **BAD:** 3 kiểu leak phổ biến (Singleton `LeakHolder` giữ tham chiếu mạnh Activity, `Handler` inner class `postDelayed` 10 phút, Listener toàn cục không hủy).
   - **OPTIMIZED:** Dùng `WeakReference`, `removeCallbacksAndMessages(null)` trong `onDestroy`, gỡ listener đối xứng.
4. **Lõi đo lường & Kết quả:**
   - **Metrics Overlay thời gian thực:** Hiển thị trực tiếp FPS, % Jank, RAM PSS, % CPU trên màn hình (nền bán trong suốt `#CC2A1A1D`, chữ ngọc trai `#F0EAD6`, font 15sp rõ nét cho video demo 1080p).
   - **Lưu trữ & So sánh:** Lưu kết quả vào `results.json`, tự động tính trung bình và % cải thiện, xuất file CSV tương thích 100% cột Excel `So_lieu_do_mau.xlsx`.

---

## 2. Yêu cầu môi trường & Cài đặt
* **Android Studio:** Hedgehog / Iguana / Koala / Ladybug hoặc mới hơn.
* **Hệ điều hành thiết bị:** Android 7.0 (API 24) trở lên (khuyến nghị Android 10+ / API 29+ để dùng thẻ `<profileable>`).
* **minSdk:** 24 | **targetSdk / compileSdk:** 34.
* **Ngôn ngữ & UI:** Kotlin, XML + RecyclerView + ViewBinding.

---

## 3. Cách build & chạy ứng dụng
1. Mở thư mục `PAA` trong Android Studio.
2. Đồng bộ dự án (Gradle Sync).
3. **Chọn Build Variant:**
   - `debug`: Dùng khi phát triển, bắt lỗi bằng **LeakCanary** và **StrictMode** (`applicationId = com.nhomx.paa.debug`).
   - `release`: Dùng khi đo hiệu năng chính thức (benchmark) để có số liệu tốc độ khách quan (`applicationId = com.nhomx.paa`).
4. Nhấn **Run (Shift + F10)** lên máy thật đã bật USB Debugging.

---

## 4. Hướng dẫn sử dụng & Quay Video Demo
1. **Tại màn hình Dashboard (Home):**
   - Xem thông tin thiết bị (Model, phiên bản Android, dung lượng RAM, tần số quét màn hình Hz).
   - Chạm vào một trong 3 Card để mở module tương ứng.
2. **Trong từng Module:**
   - **Gạt công tắc:** Chuyển đổi linh hoạt giữa chế độ **BAD** (màu đỏ) và **OPTIMIZED** (màu xanh lá).
   - **Chạy đo:** Nhấn nút **"Chạy đo"** để kích hoạt kịch bản tự động lặp lại (cuộn 3 lượt danh sách, tính toán $N$ số, mở đóng 20 lần màn hình con).
   - **Quan sát số liệu:** Theo dõi Metrics Overlay nhảy số thời gian thực và xem bảng tổng kết ở cuối kịch bản.
   - **Lưu kết quả:** Nhấn **"Lưu"** để ghi lại lần đo vào lịch sử.
3. **Màn hình Results:**
   - Chọn Tab module để xem bảng đối chiếu Trước/Sau với tỷ lệ phần trăm cải thiện.
   - Nhấn **"Xuất CSV"** để chia sẻ dữ liệu hoặc sao chép vào sheet `NhatKyDo` của file báo cáo.

---

## 5. Lệnh ADB hữu ích khi đo đạc
```bash
# Kiểm tra kết nối máy thật
adb devices

# Đặt lại thống kê frame trước khi chạy đo
adb shell dumpsys gfxinfo com.nhomx.paa reset

# Xuất thống kê frame (sau khi cuộn xong Jank Lab)
adb shell dumpsys gfxinfo com.nhomx.paa

# Kiểm tra bộ nhớ PSS của tiến trình
adb shell dumpsys meminfo com.nhomx.paa

# Buộc dừng ứng dụng để đo lại từ đầu
adb shell am force-stop com.nhomx.paa
```
