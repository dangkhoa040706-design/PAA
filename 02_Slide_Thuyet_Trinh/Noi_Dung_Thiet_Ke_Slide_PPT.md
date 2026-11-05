# TÀI LIỆU NỘI DUNG VÀ HƯỚNG DẪN THIẾT KẾ SLIDE POWERPOINT / CANVA (13 SLIDES)

> **MÔN HỌC:** PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG (MOBILE APPLICATION DEVELOPMENT)  
> **TRƯỜNG:** ĐẠI HỌC TÔN ĐỨC THẮNG (TDTU) – KHOA CÔNG NGHỆ THÔNG TIN  
> **GIẢNG VIÊN HƯỚNG DẪN:** **GV: TRẦN ĐẠI NHÂN**  
> **NHÓM THỰC HIỆN:**  
> 1. **Hoàng Thái Đăng Khoa** – MSSV: **52400017**  
> 2. **Đinh Thanh Phong** – MSSV: **52400027**  
> **SẢN PHẨM:** ỨNG DỤNG THỰC NGHIỆM PAA (PERFORMANCE ANALYSIS APP)  
> **TỶ LỆ MÀN HÌNH:** 16:9 Widescreen (13.333 x 7.5 inches)  
> **BỘ MÀU CHỦ ĐẠO:** TDTU Blue (`#0A4D9E`), PAA Scarlet (`#BC0024`), Dark Slate (`#0F172A`), Cyan (`#00B4D8`), Light Gray (`#F1F5F9`), White (`#FFFFFF`).

---

## BẢNG TỔNG HỢP CÁC FILE ẢNH & SƠ ĐỒ CẦN CHÈN VÀO TỪNG SLIDE

Tất cả các file ảnh dưới đây đều đã có sẵn trong thư mục: **`D:\MOBI GK\04_Hinh_Anh_Va_So_Do\`**

| Slide | Tên Slide | Tên file ảnh cần chèn | Vị trí đặt trên Slide |
| :---: | :--- | :--- | :--- |
| **1** | Trang bìa | `01_home.png` + `PAA_1_logo_trong_suot.png` | Góc phải (Mockup điện thoại) & Top banner |
| **2** | Mục lục báo cáo | `PAA_2_logo_ten_trong_suot.png` | Góc dưới bên phải |
| **3** | Đặt vấn đề & Nút thắt | *Icon cảnh báo, biểu đồ tụt hạng app* | Cột minh họa bên phải |
| **4** | Tiêu chuẩn Android Vitals | *Bảng ngưỡng Vitals của Google Play* | Khung so sánh chính giữa |
| **5** | Pipeline Đồ họa & VSYNC 16.67ms | `08_diagram_rendering_pipeline.png` | **Chính giữa Slide (Chiếm toàn bộ nửa phải)** |
| **6** | Looper ANR & ART Heap Leak | `09_diagram_memory_leak_art.png`<br>`10_diagram_cpu_threading.png` | Đặt 2 sơ đồ song song ở nửa dưới slide |
| **7** | Ứng dụng PAA & HUD Monitor | `01_home.png` | Nửa bên phải (Ảnh chụp màn hình thật) |
| **8** | Lab 1: Render Jank (Lag UI) | `02_jank_bad.png`<br>`03_jank_opt.png` | **Đặt cạnh nhau: Bên trái BAD, bên phải OPT** |
| **9** | Lab 2: Nghẽn CPU & ANR | `04_cpu_lab.png`<br>`07_cpu_result_panel.png` | Đặt bên phải (Màn hình đo + Bảng xác minh) |
| **10** | Lab 3: Rò rỉ RAM (Memory Leak) | `05_memory_lab.png` | Nửa bên phải (Màn hình 20 instance leak) |
| **11** | Bảng Số liệu Đối chứng | `11_chart_performance_benchmarks.png`<br>`06_results.png` | **Bên trái: Biểu đồ cột / Bên phải: Ảnh Results** |
| **12** | 5 Nguyên tắc vàng lập trình | `palette.png` | Nửa dưới slide |
| **13** | Kết luận & Lời cảm ơn | `PAA_3_logo_nen_pearl.png` | Chính giữa trang kết thúc |

---

# CHI TIẾT NỘI DUNG TỪNG SLIDE (SLIDE 1 ĐẾN SLIDE 13)

---

### SLIDE 1: TRANG BÌA (COVER SLIDE)

* **Loại bố cục:** Nền xanh Navy đậm (`#0A4D9E`), thanh banner trắng phía trên, chia 2 cột.
* **Top Banner:** Khung trắng bo góc chứa dòng chữ: **`TRƯỜNG ĐẠI HỌC TÔN ĐỨC THẮNG - KHOA CÔNG NGHỆ THÔNG TIN`** (Chữ màu xanh Navy đậm `#0A4D9E`).
* **Tiêu đề chính (Title - Chữ trắng, font to đậm 32pt):**  
  `PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID`
* **Tiêu đề phụ (Subtitle - Chữ màu Cyan `#00B4D8`, 16pt):**  
  `Nghiên cứu Nguyên lý Tầng sâu AOSP & Thực nghiệm Bộ công cụ PAA (Performance Analysis App)`
* **Thẻ thông tin sinh viên & GVHD (Nền trắng bo góc, chữ đen):**
  * **Học phần:** Phát triển Ứng dụng Di động
  * **Giảng viên hướng dẫn:** **GV: Trần Đại Nhân**
  * **Sinh viên thực hiện:**  
    1. **Hoàng Thái Đăng Khoa** – MSSV: **52400017**  
    2. **Đinh Thanh Phong** – MSSV: **52400027**
* **Huy hiệu phụ:** Hình tròn màu Cyan `#00B4D8` bên góc chứa chữ: `MOBI GK` / `2026`.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\01_home.png`
  * Vị trí: Đặt ở góc phải màn hình, tạo hiệu ứng mockup điện thoại nghiêng 3D hoặc lồng trong khung viền smartphone.

---

### SLIDE 2: MỤC LỤC & TỔNG QUAN NỘI DUNG BÁO CÁO (AGENDA)

* **Tiêu đề Slide:** `MỤC LỤC & BỐ CỤC BÁO CÁO`
* **Tagline:** `4 Trụ cột nội dung nghiên cứu và thực nghiệm`
* **Bố cục:** 4 thẻ card hình chữ nhật bo góc nền trắng, xếp theo dạng lưới 2x2 hoặc 4 cột ngang:
  * **Thẻ 1 (Số 01 - Màu Navy): ĐẶT VẤN ĐỀ & TIÊU CHUẨN GOOGLE PLAY**
    * Thách thức phân mảnh phần cứng Android.
    * Ngưỡng đào thải người dùng & Chỉ số Google Play Android Vitals.
  * **Thẻ 2 (Số 02 - Màu Cyan): NGUYÊN LÝ TẦNG SÂU HỆ ĐIỀU HÀNH AOSP**
    * Nhịp xung VSYNC 16.67ms và Rendering Pipeline.
    * Cơ chế nghẽn Looper ANR & Cây tham chiếu GC Root rò rỉ RAM.
  * **Thẻ 3 (Số 03 - Màu Scarlet): BỘ CÔNG CỤ THỰC NGHIỆM PAA & 3 PHÒNG LAB**
    * Kiến trúc HUD Monitor đo đạc thời gian thực.
    * Thực nghiệm đối chứng 3 Lab: UI Jank, Nghẽn CPU, Rò rỉ Bộ nhớ.
  * **Thẻ 4 (Số 04 - Màu Xanh lá): SỐ LIỆU ĐỐI CHỨNG & BỘ QUY CHUẨN THỰC CHIẾN**
    * Bảng đo định lượng Before vs After (FPS, CPU ms, RAM PSS).
    * 5 Nguyên tắc vàng dành cho lập trình viên Android di động.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\PAA_2_logo_ten_trong_suot.png`
  * Vị trí: Đặt trang trí ở góc dưới cùng bên phải slide.

---

### SLIDE 3: ĐẶT VẤN ĐỀ & TÁC ĐỘNG SỐNG CÒN CỦA HIỆU NĂNG

* **Tiêu đề Slide:** `ĐẶT VẤN ĐỀ: VÌ SAO HIỆU NĂNG LÀ SỐNG CÒN?`
* **Tagline:** `Thách thức phân mảnh thiết bị & Ngưỡng chịu đựng của người dùng`
* **Bố cục:** 2 Cột (Trái: 3 Nút thắt hiệu năng / Phải: Thống kê định lượng).
* **Nội dung Cột Trái (3 Nút thắt hiệu năng kinh điển):**
  * ❌ **UI Khựng giật (Jank):** Cuộn danh sách đơ lag do giải mã ảnh nặng và layout lồng sâu.
  * ❌ **Treo ứng dụng (ANR):** Thuật toán tính toán nặng O(N²) khóa cứng Main UI Thread.
  * ❌ **Rò rỉ bộ nhớ (Memory Leak):** Đối tượng chết nhưng bị biến tĩnh giữ chặt, gây phình RAM và văng app (OOM).
* **Nội dung Cột Phải (Hậu quả kinh doanh - Thống kê của Google):**
  * 🔴 **48% người dùng** gỡ cài đặt ứng dụng ngay trong ngày đầu nếu phát hiện app bị giật lag hoặc chạy chậm.
  * 🔴 **Tụt hạng Google Play:** Điểm đánh giá (Rating) bị kéo tụt xuống dưới 3.0 sao do người dùng phàn nàn về hiệu năng.
  * 🔴 **Tốn pin & Nóng máy:** CPU chạy luẩn quẩn và Garbage Collector dọn dẹp liên tục gây hao tổn phần cứng.

---

### SLIDE 4: TIÊU CHUẨN GOOGLE PLAY ANDROID VITALS

* **Tiêu đề Slide:** `TIÊU CHUẨN ĐÁNH GIÁ: GOOGLE PLAY ANDROID VITALS`
* **Tagline:** `Các ngưỡng đỏ (Bad Behavior Thresholds) hệ thống dùng để đánh giá chất lượng`
* **Bố cục:** 3 Khối Card nổi bật đặt ngang hàng nhau:
  * **Khối 1: TỶ LỆ KHUNG HÌNH CHẬM (SLOW RENDERING)**
    * Ngưỡng xấu: **> 25% số khung hình** mất nhiều hơn **16.67 mili-giây** để hiển thị (tương đương màn hình < 60 FPS).
    * Hậu quả: App bị đánh cờ vàng, giảm khả năng đề xuất trên Google Play Store.
  * **Khối 2: TỶ LỆ KHUNG HÌNH ĐÓNG BĂNG (FROZEN FRAMES)**
    * Ngưỡng xấu: **> 0.1% số khung hình** mất nhiều hơn **700 mili-giây** (gần 1 giây đơ hoàn toàn).
    * Hậu quả: Người dùng tưởng app bị treo, thoát app cưỡng bức.
  * **Khối 3: TỶ LỆ PHÁT SINH LỖI ANR (ANR RATE)**
    * Ngưỡng xấu: **> 0.47% số phiên sử dụng** xuất hiện hộp thoại "Ứng dụng không phản hồi".
    * Hậu quả: Google Play cảnh báo người dùng trước khi bấm nút Cài đặt app.

---

### SLIDE 5: NGUYÊN LÝ TẦNG SÂU: RENDERING PIPELINE & VSYNC 16.67MS

* **Tiêu đề Slide:** `NGUYÊN LÝ TẦNG SÂU: CHUỖI DỰNG HÌNH & NHỊP XUNG VSYNC`
* **Tagline:** `Quy tắc ngân sách 16.67ms (Slide 5 Bài 8 & Slide 37 Bài 1.3)`
* **Bố cục:** 2 Cột (Trái: Giải thích 4 giai đoạn / Phải: Sơ đồ kỹ thuật).
* **Nội dung Cột Trái:**
  * ⏱️ **Ngân sách 16.67ms (60Hz):** Mỗi 16.67ms, tín hiệu phần cứng VSYNC kích hoạt `Choreographer.doFrame()`.
  * 🔄 **Main Thread Traversal:** Thực hiện tuần tự 3 pha: `measure()` (đo đạc) $\rightarrow$ `layout()` (sắp xếp vị trí) $\rightarrow$ `draw()` (ghi lệnh vẽ DisplayList).
  * ⚠️ **Nguyên nhân gây Jank:** Layout lồng sâu nhiều tầng (LinearLayout lồng RelativeLayout) khiến pha đo đạc bị nhân bội đệ quy; cộng thêm việc đọc I/O ảnh đè lên Main Thread làm thời gian vượt ngưỡng 16.67ms.
  * 🚀 **Giải pháp:** Chuyển sang `ConstraintLayout` phẳng 1 tầng để tối ưu thời gian `measure()` thành $O(1)$.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\08_diagram_rendering_pipeline.png`
  * Vị trí: Đặt toàn bộ nửa bên phải Slide, phóng to để thấy rõ luồng từ VSYNC $\rightarrow$ Main Thread $\rightarrow$ RenderThread $\rightarrow$ SurfaceFlinger.

---

### SLIDE 6: NGUYÊN LÝ TẦNG SÂU: LOOPER ANR & ART HEAP LEAK

* **Tiêu đề Slide:** `NGUYÊN LÝ TẦNG SÂU: ĐIỀU PHỐI LUỒNG & BỘ NHỚ ART HEAP`
* **Tagline:** `Cơ chế nghẽn MessageQueue và Cây tham chiếu GC Root (Slide 4, 8 Bài 8 & Slide 24 Bài 2.2)`
* **Bố cục:** 2 Phần (Phần trên: Phân tích 2 nguy cơ / Phần dưới: 2 sơ đồ kiến trúc).
* **Nội dung:**
  * 🧵 **Nghẽn Looper gây ANR (CPU Block):**
    * Main Thread chạy trên một vòng lặp vô tận `Looper.loop()` lấy sự kiện từ `MessageQueue`.
    * Khi một thuật toán nặng $O(N^2)$ chạy trên Main Thread, MessageQueue bị tắc nghẽn, các thao tác chạm và vẽ bị chặn lại $> 5$ giây $\rightarrow$ Bật hộp thoại ANR.
  * 🧠 **Rò rỉ vùng nhớ ART Heap (Memory Leak):**
    * Máy ảo ART thu gom rác dựa trên cây tham chiếu GC Root.
    * Khi Activity đã bị đóng (`onDestroy`), nhưng một biến `static` hoặc `Handler` chạy ngầm vẫn giữ tham chiếu mạnh (Strong Reference), GC xem đối tượng này vẫn còn sống và không thể giải phóng khỏi Heap.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File 1: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\10_diagram_cpu_threading.png` (Đặt bên trái phía dưới).
  * File 2: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\09_diagram_memory_leak_art.png` (Đặt bên phải phía dưới).

---

### SLIDE 7: BỘ CÔNG CỤ THỰC NGHIỆM PAA & THANH HUD MONITOR

* **Tiêu đề Slide:** `HIỆN THỰC SẢN PHẨM: BỘ CÔNG CỤ THỰC NGHIỆM PAA`
* **Tagline:** `Ứng dụng giám sát hiệu năng thời gian thực với thanh HUD Monitor độc lập`
* **Bố cục:** 2 Cột (Trái: 4 Tính năng nổi bật / Phải: Ảnh chụp màn hình thật).
* **Nội dung Cột Trái:**
  * 🎛️ **Công tắc gạt chuyển đổi tức thì (BAD vs OPTIMIZED):** Cho phép đối chứng trực tiếp trên cùng một màn hình mà không cần cài lại app.
  * 📊 **Thanh HUD Monitor nổi trên đỉnh:** Giám sát liên tục 4 chỉ số: **FPS**, **Jank %**, **RAM PSS (MB)**, và **CPU %**.
  * 🚥 **Hệ thống cảnh báo màu sắc:**
    * 🟢 Xanh lá: Hiệu năng tối ưu (FPS $\ge 55$, Jank $\le 5\%$, CPU $< 40\%$).
    * 🟡 Vàng: Cảnh báo quá tải nhẹ.
    * 🔴 Đỏ: Nguy hiểm, giật lag nặng (FPS $< 40$, Jank $> 15\%$, CPU $\ge 75\%$).
  * ⚙️ **Tự động nhận diện phần cứng:** Đọc Model máy, phiên bản Android OS, dung lượng RAM và tần số quét màn hình (Hz).
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\01_home.png`
  * Vị trí: Đặt bên phải, có mũi tên chỉ vào thanh HUD Monitor trên cùng.

---

### SLIDE 8: PHÒNG LAB 1: THỰC NGHIỆM RENDER JANK (UI LAG)

* **Tiêu đề Slide:** `PHÒNG LAB 1: THỰC NGHIỆM ĐỐI CHỨNG RENDER JANK`
* **Tagline:** `Kịch bản tự động cuộn 500 item x 3 lượt đo đạc FrameMetrics`
* **Bố cục:** So sánh đối đầu 2 cột (Bên trái: BAD / Bên phải: OPTIMIZED).
* **Nội dung:**
  * 🔴 **BẢN BAD (CHƯA TỐI ƯU):**
    * Cây giao diện lồng **6 tầng** LinearLayout/RelativeLayout (`item_photo_bad.xml`).
    * Giải mã ảnh Bitmap thô 3000x2000 trực tiếp trên Main Thread trong `onBindViewHolder()`.
    * Gọi `notifyDataSetChanged()` ép vẽ lại toàn bộ danh sách.
    * 👉 **Kết quả: FPS tụt còn 23.5 | Jank vọt lên 72.3% | P95 chạm 35.8 ms.**
  * 🟢 **BẢN OPTIMIZED (ĐÃ TỐI ƯU):**
    * Cấu trúc phẳng **1 tầng** duy nhất bằng `ConstraintLayout` (`item_photo_good.xml`).
    * Nạp ảnh bất đồng bộ và tự động Downsample bằng thư viện **Coil**.
    * Dùng `ListAdapter` + `DiffUtil` chỉ cập nhật phần tử thay đổi.
    * 👉 **Kết quả: FPS đạt chuẩn 58.2 | Jank giảm còn 2.1% | P95 chỉ 14.2 ms.**
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File 1: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\02_jank_bad.png` (Đặt bên cột BAD).
  * File 2: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\03_jank_opt.png` (Đặt bên cột OPTIMIZED).

---

### SLIDE 9: PHÒNG LAB 2: THỰC NGHIỆM NGHẼN CPU & ANR

* **Tiêu đề Slide:** `PHÒNG LAB 2: THỰC NGHIỆM NGHẼN CPU & NGUY CƠ ANR`
* **Tagline:** `Bài toán tìm phần tử trùng lặp trên tập dữ liệu 30.000 số nguyên`
* **Bố cục:** So sánh 2 phương pháp thuật toán và kiến trúc điều phối luồng.
* **Nội dung:**
  * 🔴 **BẢN BAD: Thuật toán $O(N^2)$ trên Main Thread**
    * 2 vòng lặp lồng nhau quét toàn bộ mảng, chiếm dụng 100% tài nguyên Main Thread.
    * Khóa chặt MessageQueue trong **2.520 mili-giây** (màn hình đơ hoàn toàn).
    * Người dùng bấm vào màn hình không phản hồi $\rightarrow$ Nguy cơ văng hộp thoại ANR.
  * 🟢 **BẢN OPTIMIZED: Thuật toán $O(N)$ trên Coroutines + Cache**
    * Nâng cấp sang bảng băm `HashMap` đếm tần suất chỉ với 1 vòng lặp duy nhất $O(N)$.
    * Đẩy sang Worker Thread qua `withContext(Dispatchers.Default)`.
    * Tích hợp In-memory Cache trả kết quả tức thì trong 0ms khi gọi lại.
    * 👉 **Kết quả: Thời gian xử lý từ 2.520 ms giảm xuống chỉ còn 3 ms (Tăng tốc 840 lần)!**
    * ✅ **Xác minh đáp số:** Cả 2 bản đều tìm ra đúng số lượng phần tử trùng khớp 100%.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File 1: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\04_cpu_lab.png` (Màn hình điều khiển).
  * File 2: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\07_cpu_result_panel.png` (Bảng kết quả & Xác minh).

---

### SLIDE 10: PHÒNG LAB 3: THỰC NGHIỆM RÒ RỈ BỘ NHỚ (MEMORY LEAK)

* **Tiêu đề Slide:** `PHÒNG LAB 3: THỰC NGHIỆM RÒ RỈ BỘ NHỚ (MEMORY LEAK)`
* **Tagline:** `Kịch bản tự động mở và đóng 20 Activity kiểm chứng khả năng thu gom rác ART`
* **Bố cục:** 2 Cột so sánh cơ chế giữ tham chiếu và kết quả dọn rác.
* **Nội dung:**
  * 🔴 **BẢN BAD: Rò rỉ qua biến tĩnh (Static GC Root)**
    * Lưu Activity vào danh sách tĩnh trong Singleton `LeakHolder`.
    * Handler `postDelayed` 10 phút ngầm giữ tham chiếu Context.
    * Cấp phát 5MB RAM cho mỗi Activity. Sau 20 lần mở/đóng:
    * 👉 **Bấm nút ép dọn rác System.gc(): RAM kẹt cứng ở 128 MB, vẫn còn sống nguyên 20 Activity!**
  * 🟢 **BẢN OPTIMIZED: Giải phóng theo vòng đời & WeakReference**
    * Thay thế bằng tham chiếu yếu `WeakReference<Activity>`.
    * Hủy bỏ toàn bộ callback trong `onDestroy()`.
    * 👉 **Bấm nút dọn rác: Garbage Collector dọn sạch toàn bộ, RAM tụt về mức nền 106 MB, số leak về 0!**
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\05_memory_lab.png`
  * Vị trí: Đặt bên phải (Ảnh màn hình báo 20 instance leak kèm Toast dọn rác).

---

### SLIDE 11: BẢNG SỐ LIỆU ĐỐI CHỨNG ĐỊNH LƯỢNG (BENCHMARKS)

* **Tiêu đề Slide:** `TỔNG KẾT ĐỊNH LƯỢNG: SỐ LIỆU TRƯỚC VÀ SAU TỐI ƯU`
* **Tagline:** `Minh chứng khoa học cho hiệu quả tối ưu hóa trên toàn bộ 3 phòng Lab`
* **Bố cục:** Bảng số liệu ở trên hoặc bên trái, biểu đồ cột so sánh ở bên phải:
* **Bảng số liệu đối chứng:**

| Tiêu chí đo lường | Bản BAD (Chưa tối ưu) | Bản OPTIMIZED (Đã tối ưu) | Mức độ Cải thiện |
| :--- | :---: | :---: | :---: |
| **FPS Trung bình** (Lab 1) | 23.5 FPS | **58.2 FPS** | **+ 147.6% (Mượt mà)** |
| **Tỷ lệ Khung hình Jank** (Lab 1) | 72.3% | **2.1%** | **Giảm 97.1% (Triệt tiêu lag)** |
| **P95 Frame Time** (Lab 1) | 35.8 ms | **14.2 ms** | **Đạt chuẩn VSYNC < 16.67ms** |
| **Thời gian tính toán CPU** (Lab 2) | 2.520 ms | **3 ms** | **Nhanh hơn 840 lần** |
| **RAM PSS Đỉnh** (Lab 3) | 128 MB | **106 MB** | **Tiết kiệm 22 MB RAM** |
| **Số Activity Instance bị Leak** | 20 instance | **0 instance** | **Triệt tiêu 100% rò rỉ RAM** |

* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File 1: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\11_chart_performance_benchmarks.png` (Biểu đồ cột so sánh).
  * File 2: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\06_results.png` (Ảnh chụp màn hình Results).

---

### SLIDE 12: 5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID

* **Tiêu đề Slide:** `BỘ QUY CHUẨN THỰC CHIẾN: 5 NGUYÊN TẮC VÀNG`
* **Tagline:** `Kinh nghiệm rút ra từ đề tài dành cho phát triển ứng dụng di động thực tế`
* **Bố cục:** 5 Thẻ ngang hoặc 5 hộp card biểu tượng:
  * 🥇 **Nguyên tắc 1: Tôn trọng Ngân sách 16.67ms của Main Thread**  
    Tuyệt đối không giải mã ảnh Bitmap thô, không đọc/ghi File/Database và không chạy vòng lặp nặng trên UI Thread.
  * 🥈 **Nguyên tắc 2: Giữ Cây Giao diện luôn Phẳng (Flat View Hierarchy)**  
    Ưu tiên sử dụng `ConstraintLayout`, hạn chế lồng quá 3 tầng ViewGroup để giảm thiểu chu kỳ đệ quy Measure/Layout.
  * 🥉 **Nguyên tắc 3: Tối ưu hóa Danh sách cuộn với ListAdapter & DiffUtil**  
    Tránh xa `notifyDataSetChanged()`. Hãy để `DiffUtil` tự động tính toán độ lệch ngầm trên Background Thread.
  * 🏅 **Nguyên tắc 4: Tuân thủ Vòng đời Activity & Dọn dẹp Callback**  
    Hủy đăng ký Listener, gỡ bỏ Handler Runnable trong `onDestroy()`. Dùng `WeakReference` khi cần giữ Context.
  * 🎖️ **Nguyên tắc 5: Đo đạc Định lượng sớm bằng Công cụ Chuyên dụng**  
    Bật `StrictMode` ngay từ bản Debug, phân tích bằng Android Studio Profiler để phát hiện nút thắt cổ chai trước khi phát hành.

---

### SLIDE 13: KẾT LUẬN & PHẦN HỎI ĐÁP (Q&A)

* **Tiêu đề Slide:** `KẾT LUẬN & HƯỚNG PHÁT TRIỂN TIẾP THEO`
* **Tagline:** `Cảm ơn Thầy Trần Đại Nhân và Hội đồng đã lắng nghe bài báo cáo!`
* **Nội dung chính:**
  * ✅ **Đóng góp của Đề tài:**
    * Làm sáng tỏ nguyên lý tầng sâu AOSP (VSYNC, Looper, MessageQueue, ART Heap).
    * Xây dựng thành công ứng dụng thực nghiệm PAA với khả năng đo đạc tự động chuẩn xác.
    * Đưa ra bộ số liệu đối chứng định lượng và giải pháp tối ưu hóa toàn diện.
  * 🔮 **Hướng phát triển mở rộng:**
    * Mở rộng thêm Lab 4 đo lường mức độ tiêu hao Pin & Tối ưu hóa Băng thông Mạng (Battery & Network Profiling).
    * Áp dụng thư viện Jetpack Macrobenchmark và tối ưu tốc độ mở app bằng Baseline Profiles.
  * 💬 **Phần hỏi đáp:** Nhóm sẵn sàng lắng nghe nhận xét và trả lời các câu hỏi vấn đáp từ Thầy.
* 🖼️ **HÌNH ẢNH CẦN CHÈN:**
  * File: `D:\MOBI GK\04_Hinh_Anh_Va_So_Do\PAA_3_logo_nen_pearl.png`
  * Vị trí: Đặt trang nhã ở chính giữa bên dưới dòng chữ Q&A.

