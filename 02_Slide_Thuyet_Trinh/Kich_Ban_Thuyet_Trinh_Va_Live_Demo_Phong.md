# KỊCH BẢN THUYẾT TRÌNH TOÀN VĂN & HƯỚNG DẪN LIVE DEMO DÀNH CHO BẠN ĐINH THANH PHONG (VÀ HOÀNG THÁI ĐĂNG KHOA)

> **MÔN HỌC:** PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG (MOBILE APPLICATION DEVELOPMENT)  
> **TRƯỜNG:** ĐẠI HỌC TÔN ĐỨC THẮNG (TDTU) – KHOA CÔNG NGHỆ THÔNG TIN  
> **GIẢNG VIÊN HƯỚNG DẪN:** **GV: TRẦN ĐẠI NHÂN**  
> **ĐỀ TÀI:** PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID (PERFORMANCE PROFILING)  
> **SẢN PHẨM:** ỨNG DỤNG THỰC NGHIỆM PAA (PERFORMANCE ANALYSIS APP)  
> **THỜI LƯỢNG DỰ KIẾN:** 8 – 10 PHÚT (Bao gồm Slide + Live Demo)

---

## BẢNG PHÂN CHIA VAI DIỄN & TIẾN TRÌNH THUYẾT TRÌNH

| Phần | Nội dung trình bày | Người nói chính | Thời lượng | Nhiệm vụ cụ thể |
| :---: | :--- | :---: | :---: | :--- |
| **Phần 1** | **Slide 1 $\rightarrow$ Slide 4:** Chào hỏi, Giới thiệu đề tài, Mục lục, Đặt vấn đề & Tiêu chuẩn Android Vitals | **Đăng Khoa** | 2.5 phút | Tạo ấn tượng mở đầu chuyên nghiệp, nêu rõ bối cảnh và các tiêu chuẩn của Google. |
| **Phần 2** | **Slide 5 $\rightarrow$ Slide 6:** Nguyên lý tầng sâu AOSP (Pipeline VSYNC 16.67ms, Looper ANR & ART Heap Leak) | **Thanh Phong** | 2.0 phút | Thể hiện chiều sâu kiến thức hệ điều hành Android, làm cầu nối cho bài thực nghiệm. |
| **Phần 3** | **Slide 7 $\rightarrow$ Slide 10:** Giới thiệu PAA & **LIVE DEMO 3 PHÒNG LAB** trên Máy ảo/Điện thoại | **Thanh Phong** | 3.5 phút | **TRỌNG TÂM CHIẾN LƯỢC:** Cầm máy thao tác bấm trực tiếp, chỉ vào các con số đối chứng BAD vs OPT. |
| **Phần 4** | **Slide 11 $\rightarrow$ Slide 13:** Tổng kết Bảng số liệu đối chứng, 5 Nguyên tắc vàng, Kết luận & Q&A | **Đăng Khoa** | 2.0 phút | Chốt hạ kết quả định lượng khoa học, bài học thực tế và mở lời mời Thầy đặt câu hỏi. |

---

# TOÀN VĂN LỜI THOẠI THUYẾT TRÌNH TỪNG SLIDE

---

## PHẦN 1: MỞ ĐẦU & BỐI CẢNH ĐỀ TÀI (ĐĂNG KHOA TRÌNH BÀY)

### 🎙️ SLIDE 1: TRANG BÌA (00:00 – 00:45)
*(Đăng Khoa đứng thẳng, nét mặt tự tin, mắt nhìn về phía Thầy Trần Đại Nhân)*

> "Kính chào Thầy Trần Đại Nhân và toàn thể các bạn sinh viên đang có mặt trong buổi báo cáo Giữa kỳ ngày hôm nay.  
> 
> Em tên là **Hoàng Thái Đăng Khoa**, và đồng hành cùng em là bạn **Đinh Thanh Phong**. Hôm nay, nhóm chúng em rất vinh dự được đại diện nhóm báo cáo đề tài Giữa kỳ môn Phát triển Ứng dụng Di động với chủ đề:  
> **'Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (Performance Profiling)'**  
> đi kèm sản phẩm thực nghiệm là bộ công cụ **PAA (Performance Analysis App)** do nhóm tự xây dựng hoàn toàn từ con số không.  
> 
> Sau đây, em xin kính mời Thầy và các bạn cùng bước vào nội dung chi tiết của đề tài."

---

### 🎙️ SLIDE 2: MỤC LỤC & BỐ CỤC BÁO CÁO (00:45 – 01:15)
*(Đăng Khoa chuyển slide, chỉ tay vào 4 khối nội dung)*

> "Dạ thưa Thầy, bài báo cáo của nhóm em được tổ chức chặt chẽ thành **4 trụ cột nội dung chính**:  
> 
> • **Thứ nhất:** Nhóm làm rõ bối cảnh đặt vấn đề và bộ tiêu chuẩn kiểm định **Google Play Android Vitals**.  
> • **Thứ hai:** Đi sâu vào **nguyên lý tầng sâu của hệ điều hành AOSP**, giải mã nhịp xung VSYNC 16.67ms, cơ chế nghẽn Looper và rò rỉ vùng nhớ ART Heap.  
> • **Thứ ba:** Trình diễn sản phẩm thực nghiệm **ứng dụng PAA** với 3 phòng Lab đối chứng: Giật lag giao diện, Nghẽn tính toán CPU, và Rò rỉ bộ nhớ.  
> • **Và thứ tư:** Tổng kết **bảng số liệu đối chứng định lượng** Trước và Sau khi tối ưu, từ đó đúc kết 5 nguyên tắc vàng dành cho lập trình viên Android di động."

---

### 🎙️ SLIDE 3: ĐẶT VẤN ĐỀ & TÁC ĐỘNG HIỆU NĂNG (01:15 – 02:00)

> "Thưa Thầy, trong thực tế phát triển phần mềm, một ứng dụng 'chạy đúng tính năng' là chưa đủ. Một ứng dụng chỉ có thể giữ chân được người dùng nếu nó chạy **thực sự mượt mà và ổn định**.  
> 
> Theo thống kê chính thức từ Google, có tới **48% người dùng** sẽ gỡ cài đặt ứng dụng ngay trong ngày đầu tiên nếu họ gặp phải tình trạng đơ lag hoặc phản hồi chậm chạp. Trong thế giới Android với hàng chục ngàn dòng máy phần cứng phân mảnh, các lập trình viên thường xuyên đối mặt với **3 'căn bệnh' kinh điển**:  
> 1. Giao diện bị khựng giật khi cuộn danh sách (Render Jank).  
> 2. Màn hình bị đóng băng không phản hồi, dẫn đến hộp thoại treo ứng dụng (ANR).  
> 3. Bộ nhớ RAM bị phình to liên tục do rò rỉ bộ nhớ (Memory Leak), khiến hệ thống bị quá tải và sập ứng dụng.  
> 
> Nhận thức được tầm quan trọng sống còn đó, nhóm em đã chọn đề tài này để tìm ra phương pháp chẩn đoán và khắc phục triệt để."

---

### 🎙️ SLIDE 4: TIÊU CHUẨN GOOGLE PLAY ANDROID VITALS (02:00 – 02:30)

> "Để đánh giá hiệu năng một cách khoa học chứ không phải cảm tính, nhóm em căn cứ trực tiếp vào bộ chỉ số **Android Vitals** – đây là hệ thống radar giám sát chất lượng chính thức được Google Play tích hợp sẵn trên hàng tỷ thiết bị.  
> 
> Google đã đặt ra 3 'ngưỡng đỏ' cực kỳ khắt khe:  
> • **Tỷ lệ khung hình chậm (Slow rendering):** Không được vượt quá **25%** số khung hình mất nhiều hơn 16.67ms.  
> • **Tỷ lệ khung hình đóng băng (Frozen frames):** Không được quá **0.1%** số khung hình bị đơ trên 700ms.  
> • **Và tỷ lệ treo ANR:** Tuyệt đối không được vượt quá **0.47%** số phiên sử dụng.  
> Nếu một ứng dụng vượt qua các ngưỡng này, Google Play sẽ lập tức hạ bậc đề xuất tìm kiếm và hiển thị cảnh báo đỏ tới người dùng.  
> 
> Để hiểu rõ vì sao lại có các ngưỡng số liệu này, sau đây em xin nhường lại phần trình bày cho bạn **Đinh Thanh Phong** sẽ đi sâu vào nguyên lý tầng sâu của hệ thống."

---

## PHẦN 2: NGUYÊN LÝ TẦNG SÂU AOSP (THANH PHONG TRÌNH BÀY)

### 🎙️ SLIDE 5: RENDERING PIPELINE & VSYNC 16.67MS (02:30 – 03:30)
*(Thanh Phong bước lên, cúi đầu chào Thầy, giọng nói dõng dạc, rành mạch)*

> "Dạ em xin cảm ơn bạn Đăng Khoa. Kính thưa Thầy Trần Đại Nhân, em tên là **Đinh Thanh Phong**. Em xin phép được tiếp tục bài báo cáo bằng việc giải mã cơ chế hoạt động bên dưới của hệ thống đồ họa Android.  
> 
> Như trong **Slide số 5 bài 8 (AsyncTask & Thread)** Thầy đã từng giảng dạy: Đa số màn hình điện thoại hoạt động ở tần số quét 60Hz. Điều đó có nghĩa là phần cứng làm tươi màn hình mỗi 16.67 mili-giây thông qua một nhịp xung phần cứng gọi là **VSYNC**.  
> 
> Nhìn vào sơ đồ chuỗi dựng hình trên slide:  
> • Khi xung VSYNC phát ra, thành phần `Choreographer` sẽ đánh thức luồng chính Main Thread để bắt đầu chuỗi 3 pha: **`measure()`** (đo kích thước View) $\rightarrow$ **`layout()`** (xác định tọa độ) $\rightarrow$ **`draw()`** (ghi các lệnh vẽ vào DisplayList).  
> • Sau đó, các lệnh vẽ được chuyển sang `RenderThread` độc lập để biên dịch thành lệnh OpenGL/Vulkan và gửi xuống phần cứng GPU.  
> 
> ⚠️ **Nút thắt cổ chai nằm ở đâu?**  
> Nếu chúng ta thiết kế giao diện lồng sâu quá nhiều tầng LinearLayout và RelativeLayout, thuật toán `measure()` sẽ phải duyệt đệ quy cấp số nhân, cộng thêm việc giải mã ảnh Bitmap nặng trên Main Thread sẽ làm tiêu tốn quá 16.67ms. Khi VSYNC tiếp theo tới mà khung hình chưa vẽ xong, hệ thống buộc phải hiển thị lại khung hình cũ, và người dùng sẽ thấy ngay một cú khựng giật (Jank)!"

---

### 🎙️ SLIDE 6: LOOPER ANR & VÙNG NHỚ ART HEAP (03:30 – 04:30)

> "Tiếp theo, ở tầng xử lý logic và quản lý bộ nhớ:  
> 
> 🧵 **Về cơ chế điều phối luồng (Thread Dispatching):**  
> Toàn bộ giao diện Android vận hành trên một vòng lặp vô tận là `Looper.loop()`, liên tục rút các thông điệp từ `MessageQueue` ra xử lý. Khi lập trình viên chạy một thuật toán nặng độ phức tạp $O(N^2)$ trực tiếp trên Main Thread, MessageQueue bị khóa cứng. Các thao tác chạm của người dùng bị dồn ứ lại quá 5 giây và hệ điều hành sẽ ngay lập tức kích hoạt hộp thoại **ANR (Application Not Responding)** theo đúng cảnh báo ở **Slide 6 bài 8**.  
> 
> 🧠 **Về cơ chế rò rỉ vùng nhớ ART Heap:**  
> Máy ảo Android Runtime (ART) thu gom rác bằng thuật toán duyệt cây từ các gốc **GC Root**. Khi người dùng đóng một Activity (chu trình `onDestroy()` ở **Slide 24 bài 2.2**), toàn bộ tài nguyên màn hình đó phải được giải phóng. Nhưng nếu trong code tồn tại một biến `static` hoặc một `Handler` chạy ngầm vẫn đang giữ chặt tham chiếu mạnh (Strong Reference) tới Activity đó, máy ảo ART sẽ xem đây là đối tượng còn sống. Kết quả là hàng chục Megabyte RAM bị giam giữ vĩnh viễn trên Heap, dẫn tới lỗi cạn kiệt bộ nhớ OutOfMemory!  
> 
> Để kiểm chứng chính xác các nguyên lý này bằng thực nghiệm, nhóm em đã thiết kế nên bộ công cụ PAA."

---

## PHẦN 3: HIỆN THỰC PAA & KỊCH BẢN LIVE DEMO (THANH PHONG)

### 🎙️ SLIDE 7: BỘ CÔNG CỤ PAA & HUD MONITOR (04:30 – 05:00)

> "Thưa Thầy, ứng dụng PAA được nhóm em xây dựng theo mô hình một 'Phòng thí nghiệm hiệu năng di động' với các đặc điểm kỹ thuật nổi bật:  
> • **Tích hợp thanh HUD Monitor nổi trên đỉnh:** Sử dụng `FrameMetrics API` đo lường trực tiếp từ phần cứng để hiển thị thời gian thực 4 chỉ số: **FPS**, **Jank %**, **RAM PSS** và **CPU %**.  
> • **Công tắc gạt tức thời (BAD <---> OPTIMIZED):** Cho phép đối chứng trực tiếp giữa bản có lỗi cố ý và bản đã khắc phục tối ưu trên cùng một thiết bị.  
> 
> Ngay sau đây, em xin phép được **kết nối màn hình máy ảo và thực hiện LIVE DEMO trực tiếp 3 phòng Lab** để Thầy cùng theo dõi!"

---

# 🔴 KỊCH BẢN LIVE DEMO TỪNG BƯỚC CHO THANH PHONG (RẤT QUAN TRỌNG)

*(Lúc này Thanh Phong cầm điện thoại hoặc đưa con chuột máy tính lên màn hình máy ảo đang chạy PAA)*

---

### 🎬 BƯỚC 1: DEMO MÀN HÌNH CHÍNH (HOME DASHBOARD)
* **Thao tác:** Mở app PAA lên màn hình Home.
* **Lời nói của Phong:**
  > *"Kính thưa Thầy, đây là màn hình chính của ứng dụng PAA. Ở trên cùng, Thầy có thể thấy thanh HUD Monitor đang hiển thị thông số thời gian thực. Bên dưới, hệ thống tự động nhận diện thiết bị đang chạy: Máy ảo Android 14, RAM 4GB, màn hình tần số quét 60Hz. App cung cấp 3 phòng Lab tương ứng với 3 vấn đề lớn. Em xin phép vào phòng Lab đầu tiên: **1. Jank Lab**."*

---

### 🎬 BƯỚC 2: DEMO PHÒNG LAB 1 – UI JANK (GIẬT LAG KHUNG HÌNH)
* **Thao tác 2.1 (Bản BAD):**
  1. Bấm vào thẻ **"1. Jank Lab"**.
  2. Để nguyên công tắc ở màu đỏ **BAD**.
  3. Bấm nút **"Chạy đo"**.
  4. Màn hình tự động cuộn danh sách 500 item qua lại 3 lượt (cuộn rất giật, khựng từng nhịp rõ rệt).
* **Lời nói của Phong:**
  > *"Thưa Thầy, ở bản BAD, nhóm em lồng 6 tầng layout và decode ảnh Bitmap 3000x2000 thô trực tiếp trong hàm onBindViewHolder trên Main Thread.  
  > Khi kịch bản tự động cuộn 3 lượt, Thầy có thể thấy màn hình giật rất mạnh. Nhìn lên thanh HUD Monitor: **FPS tụt xuống chỉ còn 23.5**, và **tỷ lệ Jank vọt lên mức đỏ nguy hiểm: 72.3%**! Thời gian vẽ P95 mất tới 35.8ms, vượt xa ngân sách 16.67ms.  
  > Em bấm nút **'Lưu'** để ghi nhận kết quả bản BAD."*

* **Thao tác 2.2 (Bản OPTIMIZED):**
  1. Bấm gạt công tắc sang **OPTIMIZED** (chuyển sang màu xanh lá).
  2. Bấm nút **"Chạy đo"**.
  3. Danh sách lại tự động cuộn 3 lượt (lần này cuộn cực kỳ mượt mà, trơn tru như nhung).
* **Lời nói của Phong:**
  > *"Bây giờ, em gạt sang chế độ OPTIMIZED: Nhóm đã thay thế bằng layout phẳng 1 tầng ConstraintLayout theo Slide 37 bài 1.3, dùng ListAdapter + DiffUtil theo bài 5.3, và nạp ảnh qua thư viện Coil ngoài luồng nền.  
  > Thầy thấy màn hình cuộn mượt mà hoàn toàn: **FPS đã đạt chuẩn 58.2**, **tỷ lệ Jank giảm ngoạn mục xuống chỉ còn 2.1%**, và **P95 đạt 14.2ms**, nằm an toàn trong ngân sách 16.67ms VSYNC!  
  > Em bấm **'Lưu'** kết quả bản OPTIMIZED."*

---

### 🎬 BƯỚC 3: DEMO PHÒNG LAB 2 – CPU LAB (NGHẼN LUỒNG & ANR)
* **Thao tác 3.1 (Bản BAD):**
  1. Bấm nút Mũi tên quay lại $\rightarrow$ Bấm vào thẻ **"2. CPU Lab"**.
  2. Chọn mục **30.000 phần tử**.
  3. Để nguyên công tắc ở **BAD**.
  4. Bấm nút **"Chạy đo"**.
  5. Màn hình lập tức đơ cứng, vòng quay đứng yên trong khoảng 2.5 giây.
* **Lời nói của Phong:**
  > *"Sang phòng Lab 2: Bài toán tìm số trùng trên tập dữ liệu 30.000 số nguyên. Ở bản BAD, nhóm chạy thuật toán 2 vòng lặp O(N²) trực tiếp trên Main Thread.  
  > Khi em bấm nút Chạy đo, Thầy thấy toàn bộ giao diện bị đơ cứng, em chạm vào màn hình hoàn toàn không phản hồi trong suốt **2.520 mili-giây** (hơn 2.5 giây). Nếu kéo dài quá 5 giây, hệ điều hành sẽ lập tức bật lỗi ANR theo đúng cảnh báo ở Slide 6 bài 8!  
  > Em bấm **'Lưu'** bản BAD."*

* **Thao tác 3.2 (Bản OPTIMIZED):**
  1. Gạt công tắc sang **OPTIMIZED** (xanh lá).
  2. Bấm nút **"Chạy đo"**.
  3. Kết quả hiện ra **tức thì ngay trong chớp mắt (0 giây)**!
* **Lời nói của Phong:**
  > *"Bây giờ ở bản OPTIMIZED: Nhóm nâng cấp thuật toán sang dùng HashMap O(N) và đẩy sang Worker Thread qua Coroutines Dispatchers.Default theo Slide 8 bài 8.  
  > Em vừa bấm nút thì kết quả hiện ra ngay lập tức: Thời gian tính toán chỉ mất vỏn vẹn **3 mili-giây**! Tức là nhanh hơn bản BAD tới **840 lần**, và luồng UI luôn luôn thông thoáng 100%.  
  > Đặc biệt ở bên dưới, ô Xác minh đáp số chứng minh: Cả 2 bản đều tìm ra chính xác cùng một số lượng phần tử trùng lặp và cùng một tổng giá trị, đảm bảo tính đúng đắn tuyệt đối của thuật toán. Em bấm **'Lưu'**."*

---

### 🎬 BƯỚC 4: DEMO PHÒNG LAB 3 – MEMORY LAB (RÒ RỈ BỘ NHỚ RAM)
* **Thao tác 4.1 (Bản BAD):**
  1. Bấm quay lại $\rightarrow$ Bấm vào thẻ **"3. Memory Lab"**.
  2. Để công tắc ở **BAD**.
  3. Bấm nút **"Chạy đo"**.
  4. Màn hình tự động chớp tắt mở/đóng 20 Activity con liên tục (mỗi lần ngậm 5MB).
  5. Sau khi chạy xong, chỉ tay vào dòng chữ `RAM PSS: 128 MB` và `Số instance Activity còn sống: 20`.
  6. **BẤM NÚT "Kích hoạt GC thủ công"** $\rightarrow$ Toast hiện ra $\rightarrow$ RAM vẫn kẹt cứng ở `128 MB`.
* **Lời nói của Phong:**
  > *"Đây là phòng Lab 3: Kiểm thử rò rỉ bộ nhớ. Kịch bản vừa tự động mở và đóng 20 Activity, mỗi màn hình cố tình ngậm 5MB RAM. Ở bản BAD, do biến tĩnh Singleton giữ chặt tham chiếu, 20 Activity này không thể giải phóng.  
  > Thầy thấy RAM đã tăng vọt lên **128 MB**.  
  > Bây giờ, em chủ động bấm nút **'Kích hoạt GC thủ công'** để ép máy ảo ART chạy dọn rác. Thầy thấy đấy: Dù em đã ép dọn rác, **RAM vẫn kẹt cứng ở mức 128 MB và hệ thống báo 20 Activity vẫn còn sống nguyên**! Đây chính là bằng chứng xác thực của lỗi Memory Leak: GC hoàn toàn bó tay khi còn dính GC Root.  
  > Em bấm **'Lưu'** bản BAD."*

* **Thao tác 4.2 (Bản OPTIMIZED):**
  1. Gạt công tắc sang **OPTIMIZED**.
  2. Bấm nút **"Chạy đo"**.
  3. Màn hình lại tự động chớp tắt mở/đóng 20 lần.
  4. Sau khi chạy xong, bấm nút **"Kích hoạt GC thủ công"**.
  5. Chỉ tay vào màn hình: RAM tụt về mức nền **`106 MB`** và dòng chữ báo: **`Số instance Activity còn sống: 0`**.
* **Lời nói của Phong:**
  > *"Sang bản OPTIMIZED: Nhóm em thay thế bằng `WeakReference` và hủy đăng ký callback trong `onDestroy()` theo Slide 25 bài 2.2.  
  > Sau 20 lần mở đóng, khi bấm nút dọn rác, máy ảo ART đã thu hồi sạch sẽ toàn bộ: **RAM lập tức tụt về mức nền cơ bản 106 MB**, và **số Activity rò rỉ là 0 instance**! Toàn bộ rác đã được giải phóng 100%. Em bấm **'Lưu'**."*

---

### 🎬 BƯỚC 5: XEM BẢNG TỔNG KẾT & XUẤT CSV
* **Thao tác 5.1:** Bấm quay lại màn hình Home $\rightarrow$ Bấm nút **"BẢNG KẾT QUẢ ĐỐI CHỨNG (RESULTS)"**.
* **Thao tác 5.2:** Bấm chuyển qua các Chip: **Jank**, **CPU**, **Memory**.
* **Lời nói của Phong:**
  > *"Cuối cùng, em mở màn hình Results. Đây là bảng tổng hợp đối đầu định lượng:  
  > • Ở tab Jank: Thầy thấy rõ FPS tăng từ 23 lên 58 (+147%), Jank giảm từ 72% xuống 2%.  
  > • Ở tab CPU: Thời gian giảm từ 2520ms xuống 3ms.  
  > • Ở tab Memory: Bản BAD leak 20 Activity, bản OPTIMIZED đã triệt tiêu hoàn toàn về 0.  
  > Em bấm nút **'Xuất CSV'** để xuất toàn bộ nhật ký số liệu này ra file CSV đồng bộ với biểu mẫu Excel của trường.  
  > 
  > Em xin kết thúc phần Live Demo và nhường lại phần tổng kết cho bạn Đăng Khoa."*

---

## PHẦN 4: TỔNG KẾT & 5 NGUYÊN TẮC VÀNG (ĐĂNG KHOA TRÌNH BÀY)

### 🎙️ SLIDE 11: BẢNG SỐ LIỆU ĐỐI CHỨNG ĐỊNH LƯỢNG (08:00 – 08:45)
*(Đăng Khoa tiếp quản, giọng nói tự tin, đĩnh đạc)*

> "Dạ em xin cảm ơn bạn Thanh Phong. Kính thưa Thầy, trên màn hình Slide 11 là bảng tổng kết số liệu đo đạc thực tế vừa được thực hiện trên ứng dụng PAA.  
> 
> Toàn bộ các chỉ số đều thể hiện sự cải thiện mang tính đột phá:  
> • Độ mượt mà khung hình đạt chuẩn tuyệt đối 58 FPS, triệt tiêu 97% hiện tượng rớt frame.  
> • Thời gian xử lý thuật toán tăng tốc hơn 840 lần, loại bỏ hoàn toàn nguy cơ đóng băng ANR.  
> • Giải phóng toàn bộ 20 instance rò rỉ, giúp ứng dụng duy trì ổn định ở mức RAM nền 106MB mà không bao giờ bị tràn bộ nhớ.  
> Những con số này chính là minh chứng khoa học đanh thép nhất cho các giải pháp tối ưu hóa mà nhóm đã nghiên cứu."

---

### 🎙️ SLIDE 12: 5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN (08:45 – 09:30)

> "Từ những bài học thực nghiệm rút ra trong suốt quá trình xây dựng đề tài, nhóm em đã đúc kết nên **5 Nguyên tắc Vàng** có giá trị ứng dụng cao cho bất kỳ lập trình viên Android nào:  
> 
> 1. **Thứ nhất - Tôn trọng tuyệt đối ngân sách 16.67ms của Main Thread:** Không bao giờ đọc ghi file, giải mã ảnh hay chạy thuật toán nặng trên UI Thread.  
> 2. **Thứ hai - Giữ cây giao diện luôn phẳng (Flat View Hierarchy):** Hạn chế tối đa việc lồng nhiều tầng LinearLayout; ưu tiên sử dụng `ConstraintLayout` theo Slide 37 bài 1.3 để giảm chi phí `measure()`.  
> 3. **Thứ ba - Tối ưu danh sách cuộn với ListAdapter và DiffUtil:** Không sử dụng `notifyDataSetChanged()` bừa bãi; hãy để DiffUtil tính toán độ lệch ngầm trên Background Thread.  
> 4. **Thứ tư - Quản lý chặt chẽ vòng đời Activity:** Luôn hủy bỏ Handler Runnable và unregister Listener trong `onDestroy()`. Khi cần giữ Context, hãy ưu tiên dùng Application Context hoặc `WeakReference`.  
> 5. **Và thứ năm - Đo lường định lượng sớm:** Bật `StrictMode` ngay từ giai đoạn phát triển và kiểm tra thường xuyên bằng Android Studio Profiler trước khi đưa ứng dụng lên môi trường production."

---

### 🎙️ SLIDE 13: KẾT LUẬN & PHẦN HỎI ĐÁP Q&A (09:30 – 10:00)

> "Kính thưa Thầy Trần Đại Nhân và các bạn, đề tài của nhóm em không chỉ dừng lại ở lý thuyết sách vở mà đã hiện thực hóa thành công sản phẩm PAA với đầy đủ công cụ đo đạc thực tế. Trong tương lai, nhóm định hướng mở rộng thêm phòng Lab về tiêu hao Pin và tối ưu hóa băng thông Mạng (Battery & Network Profiling) cũng như áp dụng Baseline Profiles để tăng tốc mở app.  
> 
> Chúng em xin gửi lời cảm ơn chân thành nhất tới Thầy Trần Đại Nhân đã tận tình hướng dẫn và trang bị cho chúng em những kiến thức nền tảng vô cùng quý báu trong suốt học kỳ vừa qua.  
> 
> Sau đây, nhóm chúng em xin trân trọng kính mời Thầy đặt câu hỏi và đóng góp ý kiến để đề tài của chúng em được hoàn thiện hơn nữa. Nhóm chúng em xin chân thành cảm ơn Thầy!"

---

# 🛡️ PHAO PHẢN XẠ NHANH: KHI THẦY NGẮT LỜI HỎI ĐỘT XUẤT LÚC PHONG DEMO

Nếu trong lúc bạn Phong đang thao tác máy ảo mà Thầy bất ngờ hỏi dồn, Phong hãy giữ bình tĩnh và trả lời ngay bằng các câu "tủ" sau:

### ⚡ 1. Thầy hỏi: *"Sao RAM sau khi dọn rác ở bản OPT lại là 106MB chứ không phải 19MB?"*
* **Phong trả lời ngay:** *"Dạ thưa Thầy, con số 19.8MB trong tài liệu cũ là đo lượng Java Heap trên máy thật Android 9 đời cũ. Còn máy ảo này đang chạy Android 14 (API 34), mức RAM PSS nền cơ bản của hệ điều hành ban đầu đã là ~105MB rồi ạ. Bản BAD đã làm phình RAM lên 128MB (+22MB leak), và bản OPTIMIZED đã dọn sạch rác, đưa RAM tụt về đúng mức nền tối thiểu 106MB ạ!"*

### ⚡ 2. Thầy hỏi: *"Sao trên thanh HUD ở Lab 3 chữ Jank lại đỏ lòm 100% thế kia?"*
* **Phong trả lời ngay:** *"Dạ thưa Thầy, Lab 3 là bài kiểm thử rò rỉ RAM (Memory Leak), không phải đo độ mượt UI. Kịch bản đang liên tục mở và đóng 20 Activity dồn dập trong vài giây. Việc hệ thống liên tục khởi tạo và hủy Activity khiến nhịp vẽ bị gián đoạn, đây là hiện tượng hoàn toàn bình thường khi đo tải bộ nhớ dồn dập ạ!"*

### ⚡ 3. Thầy hỏi: *"Nút Kích hoạt GC thủ công để làm gì?"*
* **Phong trả lời ngay:** *"Dạ thưa Thầy, nút này gọi `System.gc()` để ép máy ảo ART dọn rác ngay lập tức. Mục đích là để chứng minh: Ở bản BAD, dù em có chủ động ép dọn rác, RAM vẫn kẹt cứng ở 128MB và 20 Activity vẫn còn sống do bị biến tĩnh giữ chặt GC Root, chứng minh lỗi rò rỉ là có thật ạ!"*

### ⚡ 4. Thầy hỏi: *"Hai thuật toán CPU chạy có ra cùng một đáp số không hay tối ưu xong làm sai logic?"*
* **Phong chỉ tay vào màn hình:** *"Dạ thưa Thầy, ô Xác minh đáp số ở bên dưới chứng minh cả bản BAD và bản OPTIMIZED đều tìm ra chính xác cùng số lượng phần tử trùng lặp và cùng tổng giá trị, đảm bảo tính đúng đắn tuyệt đối của bài toán ạ!"*

