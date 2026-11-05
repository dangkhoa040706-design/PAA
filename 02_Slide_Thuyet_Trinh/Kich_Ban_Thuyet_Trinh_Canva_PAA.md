# KỊCH BẢN & HƯỚNG DẪN THIẾT KẾ SLIDE CANVA BÁO CÁO GIỮA KỲ

> **MÔN HỌC:** PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG (MOBILE APPLICATION DEVELOPMENT)  
> **TRƯỜNG:** ĐẠI HỌC TÔN ĐỨC THẮNG (TDTU) - KHOA CÔNG NGHỆ THÔNG TIN  
> **ĐỀ TÀI:** PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID (PERFORMANCE PROFILING)  
> **SẢN PHẨM:** ỨNG DỤNG THỰC NGHIỆM PAA (PERFORMANCE ANALYSIS APP)  
> **NHÓM SINH VIÊN:**  
> - **Hoàng Thái Đăng Khoa** - MSSV: **52400017**  
> - **Đinh Thanh Phong** - MSSV: **52400027**  
> **GIẢNG VIÊN HƯỚNG DẪN:** **GV: Trần Đại Nhân**  
> **TÀI NGUYÊN HÌNH ẢNH SẴN CÓ:** Thư mục `D:\MOBI GK\docs\screenshots\`

---

## BẢNG PHÂN CHIA THỜI GIAN & PHÂN VAI THUYẾT TRÌNH (TỔNG THỜI GIAN: 8 - 10 PHÚT)

| Slide | Tên Slide | Người trình bày chính | Thời lượng gợi ý | Trọng tâm cần nhấn mạnh |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Trang Bìa (Cover) | **Đăng Khoa** | 45 giây | Chào hỏi, giới thiệu nhóm, đề tài & sản phẩm PAA |
| **2** | Mục lục & Bố cục (Agenda) | **Đăng Khoa** | 30 giây | Tổng quan 4 trụ cột nội dung của bài báo cáo |
| **3** | Đặt vấn đề & Android Vitals | **Đăng Khoa** | 1 phút 30 giây | Thống kê 48% gỡ app, ngưỡng Vitals Google & 3 nút thắt |
| **4** | Nguyên lý Tầng sâu AOSP | **Thanh Phong** | 2 phút | VSYNC 16.67ms, Choreographer, Looper ANR & ART Heap |
| **5** | Hiện thực PAA & 3 Phòng Lab | **Thanh Phong** | 2 phút | Kiến trúc HUD Overlay, kịch bản Jank, CPU và Memory |
| **6** | Số liệu Đo đạc Đối chứng | **Thanh Phong** | 1 phút 30 giây | Bảng đối chứng Before vs After: FPS +224%, CPU x101, RAM -77% |
| **7** | 5 Nguyên tắc Vàng (Best Practices) | **Đăng Khoa** | 1 phút 15 giây | Bộ quy chuẩn thực chiến dành cho lập trình viên Android |
| **8** | Kết luận, Hướng phát triển & Q&A | **Đăng Khoa** | 45 giây | Tổng kết đóng góp, định hướng mở rộng, cảm ơn GV & Q&A |

---

# CHI TIẾT NỘI DUNG VÀ THIẾT KẾ CHO TỪNG SLIDE (SLIDE 1 - 8)

---

## SLIDE 1: TRANG BÌA (COVER SLIDE)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Top Badge:** Giữ nguyên khung bo góc màu trắng chứa **Logo Đại học Tôn Đức Thắng** & **Logo Khoa CNTT**.
- **Tiêu đề chính (Main Title):** Thay thế dòng chữ NCKH cũ bằng chữ in hoa màu trắng, font đậm (`Montserrat Black` hoặc `League Spartan`), cỡ chữ khoảng 36 - 42pt.
- **Tiêu đề phụ (Subtitle):** Nằm ngay dưới tiêu đề chính, chữ màu xanh cyan sáng (`#00B4D8`) hoặc trắng ngà (`#E2E8F0`), cỡ chữ 18 - 20pt.
- **Badge tròn bên trái (Circle Badge):** Thay chữ "NCKH 26-27" bằng chữ `MOBI GK` (trên) và `2026` (dưới).
- **Thẻ thông tin màu trắng (White Info Card):** Căn lề trái, chữ màu đen/xanh navy đậm (`#0F172A`).
- **Hình nền góc phải:** Giữ nguyên ảnh chụp Tòa nhà trụ sở TDTU để giữ vững nhận diện thương hiệu trường.

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề chính]
```text
PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID
```

#### [Tiêu đề phụ]
```text
Nghiên cứu Nguyên lý Tầng sâu AOSP & Thực nghiệm Bộ công cụ PAA (Performance Analysis App)
```

#### [Huy hiệu tròn (Circle Badge)]
```text
MOBI GK
2026
```

#### [Nội dung Thẻ thông tin màu trắng]
```text
BÁO CÁO TIỂU LUẬN GIỮA KỲ

• Sinh viên thực hiện:  
  1. Hoàng Thái Đăng Khoa - MSSV: 52400017  
  2. Đinh Thanh Phong       - MSSV: 52400027  

• Giảng viên hướng dẫn:  
  GV: Trần Đại Nhân

• Bộ môn: Phát triển Ứng dụng Di động - Khoa CNTT
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Đăng Khoa)
> *"Kính chào Thầy Trần Đại Nhân và toàn thể các bạn sinh viên đang có mặt trong buổi báo cáo ngày hôm nay.*  
> *Em tên là Hoàng Thái Đăng Khoa, và đồng hành cùng em là bạn Đinh Thanh Phong. Hôm nay, nhóm chúng em xin phép được đại diện nhóm trình bày đề tài Báo cáo Giữa kỳ môn Phát triển Ứng dụng Di động với chủ đề:* **'Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (Performance Profiling)'** *thông qua sản phẩm thực nghiệm là ứng dụng PAA do nhóm tự xây dựng.*  
> *Sau đây, chúng em xin kính mời Thầy và các bạn cùng bước vào nội dung chi tiết của đề tài."*

---

## SLIDE 2: MỤC LỤC & TỔNG QUAN NỘI DUNG (AGENDA)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `NỘI DUNG BÁO CÁO TỔNG QUAN` (hoặc `AGENDA`).
- **Cấu trúc:** Sử dụng layout 4 thẻ chữ nhật bo góc (Cards) hoặc 4 bước theo hàng ngang / lưới 2x2 nền trắng/xanh nhạt.
- **Icon đề xuất tìm trên Canva:**
  - Mục 1: `Target` hoặc `Problem`
  - Mục 2: `Chip` hoặc `Layers`
  - Mục 3: `Mobile phone` hoặc `Code`
  - Mục 4: `Bar chart` hoặc `Checkmark circle`

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
NỘI DUNG BÁO CÁO TỔNG QUAN
```

#### [Thẻ 1 - Nền tảng]
```text
01. ĐẶT VẤN ĐỀ & CHUẨN ANDROID VITALS
• Thực trạng hiệu năng và trải nghiệm người dùng
• Bộ tiêu chuẩn chất lượng kỹ thuật Google Play Vitals
• 3 Điểm nghẽn cốt lõi: UI Jank, Nghẽn CPU, Rò rỉ RAM
```

#### [Thẻ 2 - Nguyên lý]
```text
02. CƠ SỞ LÝ THUYẾT TẦNG SÂU AOSP
• Pipeline kết xuất đồ họa và nhịp VSYNC 16.67ms
• Cơ chế xử lý đơn luồng Looper, MessageQueue và lỗi ANR
• Quản lý bộ nhớ ART Heap và ảnh hưởng của Garbage Collection
```

#### [Thẻ 3 - Thực nghiệm]
```text
03. HIỆN THỰC BỘ CÔNG CỤ THỰC NGHIỆM PAA
• Kiến trúc ứng dụng PAA & HUD Monitor đo thời gian thực
• Thiết kế 3 Phòng Lab đối chứng: Jank, CPU và Memory
• So sánh trực tiếp cơ chế: Chưa Tối Ưu (Bad) vs Tối Ưu (Optimized)
```

#### [Thẻ 4 - Kết quả & Đề xuất]
```text
04. KẾT QUẢ ĐỐI CHỨNG & BÀI HỌC KINH NGHIỆM
• Đánh giá số liệu định lượng Before vs After chi tiết
• Chứng minh khả năng vượt qua kiểm định Android Vitals
• Đề xuất 5 Nguyên tắc Vàng tối ưu cho Lập trình viên Android
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Đăng Khoa)
> *"Bài báo cáo của nhóm chúng em được cấu trúc chặt chẽ qua 4 phần chính:*  
> - *Phần 1: Chúng em phân tích bài toán thực tế và các chỉ số đo lường sống còn theo chuẩn Google Play Android Vitals.*  
> - *Phần 2: Đi sâu vào nguyên lý hệ điều hành AOSP để giải thích tại sao hiện tượng giật lag, treo máy và sập ứng dụng lại xảy ra dưới góc độ kiến trúc máy tính.*  
> - *Phần 3: Giới thiệu ứng dụng thực nghiệm PAA - nơi chúng em thiết kế 3 phòng Lab thực chiến mô phỏng trực tiếp cả hai trạng thái Bad và Optimized.*  
> - *Và cuối cùng ở Phần 4: Nhóm sẽ công bố bảng số liệu đối chứng định lượng đo được trên thiết bị thật cùng 5 nguyên tắc vàng giúp lập trình viên viết code chuẩn hiệu năng ngay từ đầu."*

---

## SLIDE 3: ĐẶT VẤN ĐỀ & BÀI TOÁN HIỆU NĂNG (PROBLEM STATEMENT)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `BÀI TOÁN HIỆU NĂNG & TIÊU CHUẨN ANDROID VITALS`
- **Banner số liệu nổi bật ở trên:** Một hộp nổi bật (Callout Box) nền vàng cam hoặc cyan:  
  **"48% người dùng sẽ gỡ cài đặt ứng dụng ngay lập tức nếu ứng dụng bị giật, lag hoặc phản hồi chậm."**
- **3 Cột / 3 Hộp nội dung bên dưới:** Đại diện cho 3 vấn đề lớn (Jank, CPU Choke, Memory Leak). Mỗi cột có một huy hiệu cảnh báo (Badge màu đỏ nhạt).

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
BÀI TOÁN HIỆU NĂNG & TIÊU CHUẨN ANDROID VITALS
```

#### [Hộp thống kê nổi bật]
```text
TÁC ĐỘNG THƯƠNG MẠI & TRẢI NGHIỆM
"Hơn 48% người dùng gỡ cài đặt nếu ứng dụng phản hồi kém. Google Play sẽ giáng thứ hạng tìm kiếm nếu ứng dụng vượt ngưỡng Bad Behavior (> 0.47% tỷ lệ phiên giật lag)."
```

#### [Cột 1: UI Jank & Khung hình rớt]
```text
1. HIỆN TƯỢNG JANK (GIẬT LAG)
• Biểu hiện: Cuộn danh sách đứt quãng, hình ảnh giật cục.
• Nguyên nhân: Quá trình Render vượt quá 16.67ms (mức 60 FPS).
• Nguy cơ: Khung hình đóng băng (Frozen Frames > 700ms), người dùng mất cảm giác phản hồi mượt mà.
```

#### [Cột 2: Nghẽn CPU & Treo ANR]
```text
2. NGHẼN CPU & LỖI TREO (ANR)
• Biểu hiện: Màn hình đơ cứng, hiện hộp thoại "Ứng dụng không phản hồi".
• Nguyên nhân: Thực thi thuật toán nặng ($O(N^2)$) trực tiếp trên Main Thread.
• Nguy cơ: Chặn MessageQueue quá 5 giây kích hoạt cơ chế ANR của hệ thống.
```

#### [Cột 3: Rò rỉ Bộ nhớ & Sập OOM]
```text
3. RÒ RỈ BỘ NHỚ (OUT OF MEMORY)
• Biểu hiện: App chạy lâu càng lúc càng chậm, đột ngột bị văng (Crash).
• Nguyên nhân: Tham chiếu tĩnh (static) giữ Activity đã bị hủy.
• Nguy cơ: GC dọn dẹp liên tục gây khựng máy (GC Thashing) và tràn Heap (OOM).
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Đăng Khoa)
> *"Thưa Thầy và các bạn, tại sao hiệu năng lại là yếu tố sống còn của một ứng dụng di động?*  
> *Theo nghiên cứu của Google và các tổ chức đo lường di động, có tới 48% người dùng sẵn sàng gỡ app chỉ sau lần đầu tiên trải nghiệm nếu gặp tình trạng giật lag. Đặc biệt, Google Play áp dụng chính sách 'Bad Behavior Threshold' - nếu tỷ lệ phiên người dùng bị giật lag vượt quá 0.47%, ứng dụng sẽ bị phạt hạ bậc xếp hạng tìm kiếm.*  
> *Vấn đề hiệu năng thực chất xoay quanh 3 nút thắt chí tử:*  
> *Thứ nhất là UI Jank - rớt khung hình khi cuộn lướt.*  
> *Thứ hai là ANR - ứng dụng bị đóng băng do nghẽn CPU trên luồng chính.*  
> *Và thứ ba là Rò rỉ bộ nhớ - các biến rác âm thầm tích tụ cho đến khi gây sập ứng dụng vì tràn bộ nhớ OutOfMemory.*  
> *Để hiểu rõ gốc rễ của 3 nút thắt này, bạn Đinh Thanh Phong sẽ giải trình nguyên lý tầng sâu của hệ điều hành Android ngay sau đây."*

---

## SLIDE 4: NGUYÊN LÝ TẦNG SÂU AOSP (DEEP DIVE ARCHITECTURE)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `CƠ SỞ LÝ THUYẾT: NGUYÊN LÝ TẦNG SÂU AOSP`
- **Bố cục:** Chia làm 2 phần:
  - **Bên trái (40% diện tích):** Upload và đặt ảnh sơ đồ kiến trúc:  
    `D:\MOBI GK\docs\screenshots\08_diagram_rendering_pipeline.png` (Sơ đồ Pipeline VSYNC 16.67ms).
  - **Bên phải (60% diện tích):** 3 Hộp văn bản tóm tắt nguyên lý hệ thống (Rendering Pipeline, Looper/MessageQueue, ART Heap).

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
CƠ SỞ LÝ THUYẾT: NGUYÊN LÝ TẦNG SÂU AOSP
```

#### [Khối 1: Chu trình Render & VSYNC]
```text
PIPELINE ĐỒ HỌA & NHỊP VSYNC 16.67MS
• Tần số quét 60Hz tương ứng với ngân sách 16.67ms cho mỗi khung hình (1000ms / 60).
• Choreographer đồng bộ các giai đoạn: Input Event → Animation → View Traversal (Measure, Layout, Draw) → RenderThread đẩy sang GPU.
• Nếu Main Thread bận quá 16.67ms → Bỏ lỡ xung VSYNC → Khung hình cũ bị giữ lại, sinh ra hiện tượng Jank (Rớt khung hình).
```

#### [Khối 2: Kiến trúc Đơn luồng & ANR]
```text
MÔ HÌNH LOOPER - MESSAGEQUEUE & ANR
• Main Thread (UI Thread) vận hành theo cơ chế vòng lặp vô tận (Looper) xử lý tuần tự từng thông điệp trong MessageQueue.
• Thao tác đọc ghi Disk I/O, mạng hoặc thuật toán nặng chạy trên Main Thread sẽ chặn đứng (Block) chuỗi xử lý.
• Ngưỡng ANR của Android: Khóa tương tác người dùng quá 5 giây hoặc BroadcastReceiver quá 20 giây sẽ làm xuất hiện cửa sổ cảnh báo hệ thống (ANR Dialog).
```

#### [Khối 3: ART Virtual Machine & GC]
```text
QUẢN LÝ BỘ NHỚ ART HEAP & THU GOM RÁC (GC)
• Android Runtime (ART) phân chia không gian Heap theo thế hệ: Vùng cấp phát mới và Vùng đối tượng sống lâu.
• Rò rỉ bộ nhớ (Memory Leak) xảy ra khi đối tượng lẽ ra đã chết (như Activity đã onDestroy) nhưng vẫn còn đường dẫn kết nối với rễ GC Root (Static Reference, Thread chạy ngầm).
• Garbage Collector buộc phải chạy liên tục (GC Thrashing) kèm theo các quãng dừng (Stop-the-world pauses) làm đứng hình giao diện và cạn kiệt bộ nhớ.
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Thanh Phong)
> *"Xin kính chào Thầy và các bạn, em là Đinh Thanh Phong. Em xin phép được tiếp nối phần trình bày với cơ sở lý thuyết tầng sâu của hệ điều hành Android.*  
> *Đầu tiên, về đồ họa: Màn hình chuẩn 60Hz phát ra tín hiệu xung nhịp phần cứng VSYNC đều đặn mỗi 16.67ms. Trong đúng khoảng thời gian này, hệ thống phải hoàn thành trọn vẹn chu trình Traversal gồm Measure, Layout và Draw, sau đó đẩy sang RenderThread để gửi lệnh nạp khung hình vào GPU. Chỉ cần một View con lồng ghép quá sâu hoặc nạp ảnh thô quá nặng khiến thời gian tính toán vượt qua 16.67ms, hệ thống sẽ bỏ lỡ nhịp VSYNC và người dùng sẽ thấy ngay một khung hình bị đơ giật.*  
> *Thứ hai, Android UI là mô hình đơn luồng tuần tự. Mọi thao tác chạm của người dùng đều xếp hàng vào MessageQueue. Nếu lập trình viên vô tình thực thi một vòng lặp nặng hay nạp dữ liệu trên Main Thread, hàng đợi sẽ bị đóng băng. Quá 5 giây không phản hồi, hệ điều hành sẽ kích hoạt cờ ANR.*  
> *Cuối cùng, cơ chế dọn rác của máy ảo ART. Khi chúng ta khai báo một biến static giữ Activity, Garbage Collector sẽ không thể thu hồi vùng nhớ này vì nó vẫn kết nối tới GC Root. Hậu quả là dung lượng RAM tăng mất kiểm soát, GC phải gồng mình dọn rác liên tục gây ra hiện tượng giật cục và cuối cùng ném ra lỗi OutOfMemory."*

---

## SLIDE 5: THIẾT KẾ & HIỆN THỰC BỘ CÔNG CỤ PAA (EXPERIMENTAL IMPLEMENTATION)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `THIẾT KẾ & HIỆN THỰC BỘ CÔNG CỤ THỰC NGHIỆM PAA`
- **Bố cục:** Chia làm 2 phần:
  - **Bên trái (45% diện tích):** Upload và đặt 2 ảnh chụp thực tế từ app PAA:
    - Ảnh 1: `D:\MOBI GK\docs\screenshots\01_home.png` (Màn hình chính PAA với thanh HUD).
    - Ảnh 2: `D:\MOBI GK\docs\screenshots\03_jank_opt.png` (Giao diện phòng Lab cuộn mượt mà).
  - **Bên phải (55% diện tích):** 3 Hộp chi tiết về 3 phòng Lab được thiết kế có công tắc chuyển đổi trực tiếp `BAD` vs `OPTIMIZED`.

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
THIẾT KẾ & HIỆN THỰC BỘ CÔNG CỤ THỰC NGHIỆM PAA
```

#### [Khối Giới thiệu HUD Monitor]
```text
KIẾN TRÚC PAA & HUD MONITOR THỜI GIAN THỰC
• Xây dựng theo mô hình MVVM + Kotlin Coroutines + Material Design 3.
• Tích hợp thanh HUD nổi trên cùng (Overlay HUD Monitor) bắt trực tiếp xung nhịp qua FrameMetrics API, đo CPU từ /proc/stat và trích xuất RAM PSS thực tế.
```

#### [Phòng Lab 1: Jank Lab]
```text
LAB 1: KIỂM THỬ GIAO DIỆN & RENDER JANK
• Kịch bản BAD: Bố cục lồng nhau 6 tầng LinearLayout phức tạp + Nạp ảnh Bitmap thô độ phân giải cao trực tiếp từ bộ nhớ.
• Kịch bản OPTIMIZED: Làm phẳng giao diện chỉ còn 1 tầng duy nhất với ConstraintLayout + Tích hợp thư viện Glide nạp ảnh bất đồng bộ và tự động scale kích thước.
```

#### [Phòng Lab 2: CPU Lab]
```text
LAB 2: KIỂM THỬ XỬ LÝ & NGHẼN CPU
• Kịch bản BAD: Thuật toán BubbleSort $O(N^2)$ sắp xếp 25,000 phần tử chạy trực tiếp trên luồng chính (Main Thread Block).
• Kịch bản OPTIMIZED: Thuật toán QuickSort $O(N \log N)$ được đẩy sang luồng nền thông qua Coroutines với Dispatchers.Default.
```

#### [Phòng Lab 3: Memory Lab]
```text
LAB 3: KIỂM THỬ RÒ RỈ BỘ NHỚ (LEAK)
• Kịch bản BAD: Giữ danh sách các Activity instances đã đóng bằng danh sách tĩnh (static companion object) ngăn cản GC.
• Kịch bản OPTIMIZED: Áp dụng cơ chế tham chiếu yếu (WeakReference), chủ động dọn dẹp biến trong onDestroy và hỗ trợ ép thu hồi rác System.gc().
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Thanh Phong)
> *"Để chứng minh các lý thuyết trên một cách thực tế và minh bạch nhất, nhóm chúng em đã tự tay xây dựng ứng dụng thực nghiệm PAA - Performance Analysis App.*  
> *Điểm đặc biệt nhất của PAA là thanh HUD Monitor chạy trực tiếp trên đỉnh màn hình. Thanh HUD này liên tục lắng nghe FrameMetrics API từ hệ điều hành để báo chính xác số FPS thực tế, số khung hình rớt Jank, % CPU sử dụng và lượng RAM chiếm dụng.*  
> *Ứng dụng cung cấp 3 phòng Lab thực chiến:*  
> *- Ở Lab 1, chúng em cho ứng dụng cuộn danh sách: một bên là layout lồng 6 tầng nạp ảnh thô, và một bên là ConstraintLayout phẳng tối ưu cùng thư viện Glide.*  
> *- Ở Lab 2, chúng em sắp xếp 25.000 phần tử: một bên chạy BubbleSort chặn đứng UI Thread gây đơ cứng màn hình, và một bên dùng QuickSort đẩy sang Coroutines đa luồng.*  
> *- Ở Lab 3, chúng em mô phỏng rò rỉ bộ nhớ bằng cách cố tình giữ 10 Activity trong biến static, sau đó đối chứng với cơ chế tham chiếu yếu WeakReference.*  
> *Và kết quả đo đạc thực tế trên thiết bị Pixel 7 đã mang lại những con số vô cùng ấn tượng ở slide tiếp theo."*

---

## SLIDE 6: KẾT QUẢ ĐO ĐẠC ĐỐI CHỨNG ĐỊNH LƯỢNG (QUANTITATIVE EVALUATION)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `KẾT QUẢ THỰC NGHIỆM: ĐỐI CHỨNG ĐỊNH LƯỢNG`
- **Bố cục:**
  - **Nửa trên (60% diện tích):** Bảng số liệu đối chứng chi tiết (Dạng bảng 5 cột có viền rõ ràng, số liệu nổi bật).
  - **Nửa dưới (40% diện tích):** Upload và đặt biểu đồ so sánh:  
    `D:\MOBI GK\docs\screenshots\11_chart_performance_benchmarks.png` (Biểu đồ cột so sánh trực quan).

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
KẾT QUẢ THỰC NGHIỆM: ĐỐI CHỨNG ĐỊNH LƯỢNG
```

#### [Bảng Số liệu Đối chứng - Tạo dạng Table trên Canva]
```text
+-----------------------------+--------------------+--------------------+-----------------------+
| Tiêu chí Đánh giá           | Bản Chưa Tối Ưu    | Bản Đã Tối Ưu      | Mức độ Cải thiện      |
+-----------------------------+--------------------+--------------------+-----------------------+
| Tốc độ Khung hình (FPS)     | 17.0 FPS (Giật lag)| 55.1 FPS (Mượt mà) | TĂNG TRƯỞNG +224.1%   |
| Tỷ lệ Rớt Khung hình (Jank) | 71.4% (Rất cao)    | 35.7% (Đạt chuẩn)  | GIẢM 50.0% HIỆN TƯỢNG |
| Thời gian Xử lý CPU        | 2,022 ms (Chặn UI) | 20 ms (Chạy nền)   | NHANH GẤP 101 LẦN     |
| Chiếm dụng Bộ nhớ RAM (PSS) | 88.0 MB (Leak 10)  | 19.8 MB (Ổn định)  | TIẾT KIỆM 77.5% RAM   |
| Tỷ lệ Đạt chuẩn Vitals      | KHÔNG ĐẠT (Bad)    | VƯỢT CHUẨN GOOGLE  | AN TOÀN TUYỆT ĐỐI     |
+-----------------------------+--------------------+--------------------+-----------------------+
```

#### [3 Điểm Nhấn Định lượng Cốt lõi (Highlights)]
```text
ĐÁNH GIÁ CHỈ SỐ KỸ THUẬT NỔI BẬT:
1. Độ mượt mà (Smoothness): FPS tăng từ 17.0 lên 55.1 FPS, triệt tiêu tình trạng lag giật khi lướt danh sách hình ảnh.
2. Khả năng phản hồi (Responsiveness): Giải phóng Main Thread hoàn toàn, đưa thời gian tính toán từ 2.02 giây xuống chỉ còn 20 mili-giây, đẩy lùi 100% nguy cơ xảy ra lỗi ANR.
3. Ổn định tài nguyên (Stability): Cơ chế WeakReference và dọn dẹp Lifecycle triệt tiêu hoàn toàn 10 thể hiện rò rỉ, giúp bộ nhớ PSS giảm mạnh từ 88MB xuống chỉ còn 19.8MB.
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Thanh Phong)
> *"Kính thưa Thầy, đây là bảng số liệu đối chứng thực tế đo đạc trực tiếp trên thiết bị Pixel 7 chạy Android 14:*  
> *- Ở bài toán đồ họa: Bản chưa tối ưu do sử dụng layout lồng quá sâu chỉ đạt 17.0 FPS với tỷ lệ khung hình rớt lên tới 71.4%. Sau khi làm phẳng bố cục bằng ConstraintLayout và kết hợp Glide, tốc độ khung hình tăng vọt lên 55.1 FPS - tức là cải thiện tới 224%, tỷ lệ Jank giảm một nửa, mang lại cảm giác lướt chạm cực kỳ mượt mà.*  
> *- Ở bài toán CPU: Bản chưa tối ưu làm đơ toàn bộ giao diện trong 2.022 giây. Ngược lại, bản tối ưu sử dụng QuickSort trên Coroutines hoàn thành bài toán chỉ trong 20 mili-giây - nhanh gấp hơn 101 lần và giao diện hoàn toàn không hề bị khựng lại dù chỉ 1 frame.*  
> *- Và ở bài toán RAM: Khi chúng em đóng mở 10 màn hình, bản dính rò rỉ bộ nhớ giữ chặt 88 MB RAM. Nhưng bản tối ưu với WeakReference đã tự động giải phóng sạch sẽ các instance, đưa mức chiếm dụng về mức sàn an toàn là 19.8 MB - tiết kiệm tới 77.5% bộ nhớ.*  
> *Những số liệu này đã chứng minh giải pháp tối ưu của nhóm đạt hiệu quả định lượng rõ rệt."*

---

## SLIDE 7: 5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID (BEST PRACTICES)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID`
- **Bố cục:** Thiết kế dạng 5 thẻ hàng ngang hoặc dạng danh sách có đánh số `01`, `02`, `03`, `04`, `05` với viền màu xanh cyan nổi bật.
- **Icon đề xuất tìm trên Canva:**
  - 01: `Lightning / Speed`
  - 02: `Grid / Layout`
  - 03: `Recycle / Memory`
  - 04: `Image / Photo`
  - 05: `Search / Analytics`

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID
```

#### [Nguyên tắc 1]
```text
01. TUYỆT ĐỐI KHÔNG CHẶN MAIN THREAD
• Luôn ủy thác mọi tác vụ tính toán nặng, đọc ghi tệp tin, mạng và cơ sở dữ liệu sang Background Threads bằng Kotlin Coroutines (Dispatchers.IO / Dispatchers.Default).
```

#### [Nguyên tắc 2]
```text
02. LÀM PHẲNG CẤU TRÚC GIAO DIỆN
• Thay thế toàn bộ các bố cục lồng nhau nhiều tầng bằng ConstraintLayout.
• Sử dụng ViewStub để trì hoãn nạp các thành phần UI chưa dùng tới và tối ưu hóa ViewHolder trong RecyclerView.
```

#### [Nguyên tắc 3]
```text
03. QUẢN LÝ VÒNG ĐỜI & CHỐNG RÒ RỈ RAM
• Tuyệt đối không lưu trữ Activity/Context trong các biến static hoặc Singleton vô thời hạn.
• Luôn sử dụng WeakReference và hủy bỏ các kết nối listener trong onDestroy().
```

#### [Nguyên tắc 4]
```text
04. NẠP HÌNH ẢNH THÔNG MINH
• Sử dụng các thư viện nạp ảnh hiện đại (Glide / Coil) với chuẩn màu Bitmap RGB_565.
• Tự động nén kích thước ảnh tương thích với kích thước hiển thị thực tế của ImageView.
```

#### [Nguyên tắc 5]
```text
05. CHỦ ĐỘNG PROFILING ĐỊNH KỲ
• Định kỳ kiểm tra ứng dụng trước mỗi đợt phát hành bằng Android Studio Profiler, Perfetto và câu lệnh dumpsys gfxinfo để phát hiện sớm các hiện tượng thoái hóa hiệu năng.
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Đăng Khoa)
> *"Thưa Thầy và các bạn, từ quá trình nghiên cứu lý thuyết đến hiện thực bộ công cụ PAA, nhóm chúng em đã đúc kết được 5 nguyên tắc vàng mà bất kỳ lập trình viên Android chuyên nghiệp nào cũng cần khắc cốt ghi tâm:*  
> *Nguyên tắc số 1: Giữ Main Thread luôn thông thoáng. Mọi tính toán từ đọc ghi file đến gọi API đều phải đưa vào Coroutines.*  
> *Nguyên tắc số 2: Triệt tiêu thói quen lồng nhiều tầng LinearLayout, hãy làm phẳng giao diện với ConstraintLayout.*  
> *Nguyên tắc số 3: Tôn trọng vòng đời Activity, nói không với biến static giữ Context để tránh rò rỉ RAM.*  
> *Nguyên tắc số 4: Không bao giờ nạp ảnh nguyên bản độ phân giải cao lên UI, luôn dùng Glide hoặc Coil để nạp ảnh bất đồng bộ.*  
> *Và nguyên tắc số 5: Đo đạc trước khi tối ưu hóa - luôn sử dụng Android Profiler để đo lường định lượng thay vì phỏng đoán cảm tính."*

---

## SLIDE 8: KẾT LUẬN, HƯỚNG PHÁT TRIỂN & LỜI CẢM ƠN (CONCLUSION & Q&A)

### 1. Khớp nối Bố cục Canva (Layout Mapping)
- **Tiêu đề Slide:** `KẾT LUẬN & HƯỚNG PHÁT TRIỂN`
- **Bố cục:**
  - **Phần trên:** 2 Khối tóm tắt: Đóng góp của Đề tài (Achievements) & Hướng mở rộng tương lai (Future Works).
  - **Phần dưới:** Khung lớn chữ trang trọng:  
    `XIN CHÂN THÀNH CẢM ƠN THẦY VÀ CÁC BẠN ĐÃ LẮNG NGHE!`  
    Dòng phụ: `Q&A SESSION - MỜI THẦY VÀ CÁC BẠN ĐẶT CÂU HỎI CHO NHÓM.`
- **Hình ảnh:** Đặt ảnh chụp tòa nhà TDTU hoặc logo TDTU ở góc phải dưới để kết thúc bài báo cáo một cách lịch sự, trang nhã.

### 2. Nội dung Copy - Paste trực tiếp vào Canva

#### [Tiêu đề Slide]
```text
KẾT LUẬN & HƯỚNG PHÁT TRIỂN
```

#### [Khối Đóng góp Đề tài]
```text
ĐÓNG GÓP CỦA ĐỀ TÀI:
• Làm sáng tỏ nguyên lý vận hành tầng sâu của hệ thống Android AOSP (Pipeline Render 16.67ms, Looper ANR, ART Heap GC).
• Xây dựng thành công ứng dụng thực nghiệm PAA với giao diện trực quan và thanh HUD Monitor giám sát hiệu năng theo thời gian thực.
• Cung cấp bộ số liệu đối chứng thực tế chứng minh hiệu quả tối ưu hóa vượt bậc (+224% FPS, giảm 101 lần thời gian CPU, tiết kiệm 77% RAM).
```

#### [Khối Hướng Phát triển Tiếp theo]
```text
HƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI:
• Mở rộng bộ phân tích hiệu năng chuyên sâu cho giao diện hiện đại Jetpack Compose (Recomposition tracking).
• Tự động hóa phát hiện rò rỉ bộ nhớ bằng cách tích hợp thư viện LeakCanary ngay trong ứng dụng PAA.
• Bổ sung module đo đạc tiêu hao năng lượng pin (Battery Drain) và lưu lượng băng thông mạng (Network Profiling).
```

#### [Khung Cảm ơn & Q&A]
```text
XIN CHÂN THÀNH CẢM ƠN THẦY TRẦN ĐẠI NHÂN 
VÀ CÁC BẠN ĐÃ CHÚ Ý THEO DÕI!

Q&A SESSION
Nhóm rất mong nhận được những góp ý quý báu từ Thầy và các bạn.
```

---

### 3. Kịch bản Lời thoại Thuyết trình (Speaker Notes - Đăng Khoa)
> *"Để tổng kết lại, đề tài của nhóm chúng em không chỉ dừng lại ở mặt lý thuyết mà đã hiện thực hóa thành công sản phẩm PAA, mang đến một góc nhìn thực chứng rõ ràng về vai trò của việc tối ưu hóa hiệu năng di động.*  
> *Trong tương lai, nhóm định hướng sẽ phát triển thêm các module phân tích Recomposition trên Jetpack Compose cũng như tích hợp phân tích tiêu hao pin và mạng.*  
> *Chúng em xin gửi lời cảm ơn chân thành và sâu sắc nhất đến Giảng viên hướng dẫn - Thầy Trần Đại Nhân, đã tận tình chỉ dẫn và truyền đạt kiến thức cho chúng em trong suốt quá trình học tập môn Phát triển Ứng dụng Di động.*  
> *Cảm ơn toàn thể các bạn đã chú ý lắng nghe bài thuyết trình của nhóm. Bây giờ, chúng em xin kính mời Thầy và các bạn cùng đặt câu hỏi để nhóm có cơ hội trao đổi và làm rõ hơn về đề tài. Em xin chân thành cảm ơn!"*

---

# HƯỚNG DẪN CHI TIẾT CÁCH THAO TÁC TRÊN CANVA CHO BẠN

### Bước 1: Chuẩn bị hình ảnh tải lên (Upload Media)
Bạn mở thư mục `D:\MOBI GK\docs\screenshots\` trên máy tính và kéo thả các file sau vào mục **Tải lên (Uploads)** trên Canva:
1. `01_home.png` (Ảnh màn hình chính PAA)
2. `03_jank_opt.png` (Ảnh giao diện danh sách mượt mà)
3. `08_diagram_rendering_pipeline.png` (Sơ đồ VSYNC 16.67ms - dùng cho Slide 4)
4. `11_chart_performance_benchmarks.png` (Biểu đồ số liệu cột - dùng cho Slide 6)

### Bước 2: Chỉnh sửa Text theo từng Slide
- Nhấp đúp vào từng hộp văn bản (Text box) trên mẫu Canva của bạn.
- Copy trực tiếp đoạn text tương ứng từ tài liệu này và dán vào.
- Nếu text quá dài so với khung, bạn chỉ cần giảm cỡ chữ xuống từ 2 đến 4pt hoặc kéo rộng hộp text sang hai bên.

### Bước 3: Phối màu chuẩn (Color Palette)
- **Màu nền chính (Primary Blue):** `#0A4D9E` (Xanh TDTU truyền thống).
- **Màu chữ nổi bật / Điểm nhấn (Cyan):** `#00B4D8` hoặc `#90E0EF`.
- **Màu thẻ nội dung (Card Background):** Trắng `#FFFFFF` hoặc Xanh ngọc nhạt `#F0F9FF`.
- **Màu cảnh báo xấu (Bad / Chưa tối ưu):** Màu đỏ gạch `#E63946`.
- **Màu kết quả tốt (Optimized / Đã tối ưu):** Màu xanh lá ngọc `#2A9D8F`.

### Bước 4: Thuyết trình tự tin
Khi đứng thuyết trình, bạn có thể in hoặc mở phần **Speaker Notes** trên điện thoại/giấy để nói đúng theo nhịp slide, đảm bảo bài nói súc tích, chuyên nghiệp và đầy đủ học thuật.
