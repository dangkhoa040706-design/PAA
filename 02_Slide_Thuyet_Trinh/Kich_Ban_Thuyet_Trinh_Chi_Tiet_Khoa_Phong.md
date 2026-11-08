# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO GIỮA KỲ TOÀN VĂN (17 SLIDES)
## ĐỀ TÀI: PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID (PAA)

> **Môn học:** Phát triển Ứng dụng Di động (Mobile Application Development)  
> **Trường:** Đại học Tôn Đức Thắng (TDTU) – Khoa Công nghệ Thông tin  
> **Giảng viên hướng dẫn:** **GV: Trần Đại Nhân**  
> **Nhóm sinh viên thực hiện:**  
> 1. **Hoàng Thái Đăng Khoa** – MSSV: **52400017**  
> 2. **Đinh Thanh Phong** – MSSV: **52400027**  
> **Sản phẩm thực nghiệm:** Ứng dụng PAA (Performance Analysis App)  
> **Tổng thời lượng thuyết trình:** **16 – 18 phút** (Dự phòng 2 phút cho Q&A trong tổng 20 phút)  

---

## 📌 BẢNG PHÂN VAI & MỐC THỜI GIAN THEO DÕI

| STT | Tên Slide | Mốc thời gian | Người nói | Thao tác / Media trình chiếu |
| :---: | :--- | :---: | :---: | :--- |
| **01** | Trang bìa đề tài | 00:00 – 00:40 | **Đăng Khoa** | Mở đầu, chào Thầy & các bạn. |
| **02** | Phân công nhiệm vụ nhóm | 00:40 – 01:20 | **Đăng Khoa** | Giới thiệu vai trò của Khoa và Phong. |
| **03** | Đặt vấn đề & Áp lực hiệu năng | 01:20 – 02:10 | **Đăng Khoa** | 3 Căn bệnh kinh điển & Tác động 48% gỡ app. |
| **04** | Tiêu chuẩn Google Play Vitals | 02:10 – 02:50 | **Đăng Khoa** | Thước đo radar giám sát chất lượng quốc tế. |
| **05** | 3 Ngưỡng cảnh báo đỏ của Google | 02:50 – 03:30 | **Đăng Khoa** | 25% chậm, 0.1% đóng băng, 0.47% ANR. |
| **06** | Giới thiệu PAA & Hệ thống HUD | 03:30 – 04:15 | **Đăng Khoa** | Cầu nối sản phẩm PAA & HUD đo phần cứng. |
| **07** | Cấu trúc 3 Phòng Lab của PAA | 04:15 – 04:50 | **Đăng Khoa** | 3 Nút chức năng: Jank, CPU, Memory. |
| **08** | Lab 1: Render Jank (Bản BAD) | 04:50 – 05:45 | **Đăng Khoa** | **Phát Video Demo BAD**: Lag giật, HUD đỏ 7.8 FPS. |
| **09** | Lab 1: Render Jank (Bản OPT) | 05:45 – 06:45 | **Đăng Khoa** | **Phát Video Demo OPT**: Mượt mà 55 FPS (+605%). |
| 🔄 | *Chuyển lời từ Khoa sang Phong* | 06:45 – 07:00 | **Khoa $\rightarrow$ Phong** | Chuyển giao phần kỹ thuật CPU & RAM. |
| **10** | Lab 2: Nghẽn CPU & ANR (Bản BAD) | 07:00 – 08:15 | **Thanh Phong** | **Phát Video Demo BAD CPU**: Đơ cứng 1,582 ms. |
| **11** | Lab 2: Tối ưu CPU Coroutines (OPT) | 08:15 – 09:30 | **Thanh Phong** | **Phát Video Demo OPT CPU**: Xử lý 128 ms / 0 ms Cache. |
| **12** | Lab 3: Rò rỉ RAM (Kịch bản & BAD) | 09:30 – 10:45 | **Thanh Phong** | **Phát Video Demo BAD RAM**: Kẹt GC Root, 20 leak. |
| **13** | Lab 3: Triệt tiêu rò rỉ RAM (OPT) | 10:45 – 12:00 | **Thanh Phong** | **Phát Video Demo OPT RAM**: WeakReference, 0 leak. |
| **14** | Bảng Tổng hợp Số liệu Định lượng | 12:00 – 13:30 | **Thanh Phong** | Phân tích bảng đối chứng 5 chỉ số then chốt. |
| **15** | Hình ảnh Biểu đồ Thực nghiệm | 13:30 – 14:45 | **Thanh Phong** | Biểu đồ cột trực quan trên Pixel 7. |
| 🔄 | *Chuyển lời từ Phong sang Khoa* | 14:45 – 15:00 | **Phong $\rightarrow$ Khoa** | Chuyển giao phần đúc kết và kết luận. |
| **16** | 5 Nguyên tắc vàng Android Dev | 15:00 – 16:30 | **Đăng Khoa** | Đúc kết 5 trụ cột kiến trúc chuẩn công nghiệp. |
| **17** | Kết luận & Lời cảm ơn (Q&A) | 16:30 – 17:30 | **Đăng Khoa** | Cảm ơn Thầy Trần Đại Nhân & Mời đặt câu hỏi. |

---

# TOÀN VĂN LỜI THOẠI THUYẾT TRÌNH TỪNG SLIDE

---

## 🎙️ PHẦN 1: TỔNG QUAN, BỐI CẢNH & LAB 1 (ĐĂNG KHOA TRÌNH BÀY)

### 📌 SLIDE 1: TRANG BÌA ĐỀ TÀI (00:00 – 00:40)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Đứng thẳng, phong thái tự tin, hướng mắt về phía Thầy Trần Đại Nhân và cả lớp.
* **Lời thoại:**
> *"Kính chào Thầy Trần Đại Nhân và các bạn sinh viên đang có mặt trong buổi báo cáo Giữa kỳ ngày hôm nay.*  
>  
> *Em tên là **Hoàng Thái Đăng Khoa**, và đồng hành cùng em là bạn **Đinh Thanh Phong**. Hôm nay, nhóm chúng em rất vinh dự được đại diện nhóm báo cáo đề tài Giữa kỳ môn Phát triển Ứng dụng Di động với chủ đề:*  
> **'Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (Performance Profiling)'**  
> *đi kèm sản phẩm thực nghiệm là ứng dụng **PAA (Performance Analysis App)** do nhóm tự xây dựng hoàn toàn bằng ngôn ngữ Kotlin trên Android Studio.*  
>  
> *Sau đây, em xin phép được bắt đầu bài báo cáo."*  
*(Bấm chuyển sang Slide 2)*

---

### 📌 SLIDE 2: PHÂN CÔNG NHIỆM VỤ THỰC HIỆN ĐỀ TÀI (00:40 – 01:20)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Tay mở hướng nhẹ về phía bạn Phong đang đứng bên cạnh.
* **Lời thoại:**
> *"Để hoàn thành đề tài một cách khoa học và bám sát thực tiễn công nghiệp, nhóm chúng em đã phân chia nhiệm vụ rất rõ ràng theo hai mảng chuyên môn:*  
>  
> *Về phần em – **Hoàng Thái Đăng Khoa**: Em đảm nhiệm việc nghiên cứu tiêu chuẩn kỹ thuật Google Play Android Vitals, thiết kế các kịch bản kiểm thử đối chứng, phân tích tối ưu giao diện ở Lab 1 và tổng hợp toàn bộ tài liệu báo cáo học thuật.*  
>  
> *Đồng hành cùng em là bạn **Đinh Thanh Phong**: Bạn Phong phụ trách hiện thực hóa mã nguồn Kotlin cho ứng dụng PAA, trực tiếp lập trình hệ thống giám sát HUD thời gian thực, xây dựng các thuật toán xử lý đa luồng ở Lab 2, quản lý bộ nhớ ở Lab 3 và phụ trách phần Video Demo thực nghiệm.*  
>  
> *Sự phối hợp chặt chẽ này giúp nhóm vừa đảm bảo tính đúng đắn về mặt lý thuyết, vừa kiểm chứng được bằng sản phẩm chạy thật."*  
*(Bấm chuyển sang Slide 3)*

---

### 📌 SLIDE 3: ĐẶT VẤN ĐỀ VÀ ÁP LỰC HIỆU NĂNG (01:20 – 02:10)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Nhấn giọng ở cụm từ "Thực trạng khắc nghiệt", chỉ tay vào khối 3 căn bệnh và tác động kinh doanh.
* **Lời thoại:**
> *"Thưa Thầy và các bạn, trong lập trình di động, một ứng dụng 'chạy đúng tính năng' mới chỉ là điều kiện cần. Điều kiện đủ để giữ chân người dùng chính là **trải nghiệm mượt mà và ổn định**.*  
>  
> *Hiện nay, hệ sinh thái Android có hơn **24.000 mẫu phần cứng phân mảnh** từ máy siêu rẻ vài trăm nghìn đến flagship hàng chục triệu. Trong khi tài nguyên CPU và RAM trên máy di động luôn bị giới hạn, các lập trình viên thường xuyên đối mặt với **3 'căn bệnh' kinh điển**:*  
> *Thứ nhất là **Khựng giật giao diện (UI Jank)** khi lướt danh sách.*  
> *Thứ hai là **Đóng băng màn hình gây lỗi treo app (ANR - Application Not Responding)**.*  
> *Và thứ ba là **Rò rỉ bộ nhớ (Memory Leak)** khiến app càng chạy càng nặng rồi sập bất thình lình.*  
>  
> *Hậu quả thương mại là vô cùng khốc liệt: Thống kê cho thấy **hơn 48% người dùng sẽ gỡ cài đặt app ngay trong 24 giờ đầu** nếu gặp hiện tượng giật lag, và điểm đánh giá sao trên Play Store sẽ tụt dốc không phanh xuống dưới 3.0 sao."*  
*(Bấm chuyển sang Slide 4)*

---

### 📌 SLIDE 4: TIÊU CHUẨN GOOGLE PLAY VITALS (02:10 – 02:50)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Nhấn mạnh chữ "Android Vitals" và "Radar giám sát chất lượng".
* **Lời thoại:**
> *"Để bảo vệ người dùng, Google không để các lập trình viên muốn làm gì thì làm. Họ đã triển khai hệ thống **Google Play Android Vitals**.*  
>  
> *Bản chất của Android Vitals là một hệ thống radar giám sát chất lượng kỹ thuật tự động, tích hợp sẵn trên mọi thiết bị chạy Google Play Services. Hệ thống này âm thầm theo dõi từng phiên sử dụng của người dùng.*  
>  
> *Nếu một ứng dụng có hiệu năng tồi vi phạm vào các 'ngưỡng đỏ' của Google, thuật toán Play Store sẽ lập tức **giáng hạng tìm kiếm**, gỡ khỏi mục đề xuất, và nghiêm trọng nhất là **hiển thị một thông báo màu đỏ cảnh báo ngay trang tải app**: 'Ứng dụng này có thể hoạt động không ổn định trên thiết bị của bạn'. Đây coi như là 'bản án tử' cho bất kỳ sản phẩm phần mềm nào."*  
*(Bấm chuyển sang Slide 5)*

---

### 📌 SLIDE 5: 3 NGƯỠNG CẢNH BÁO ĐỎ CỦA GOOGLE (02:50 – 03:30)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Chỉ lần lượt vào 3 cột chỉ số: 25%, 0.1% và 0.47%.
* **Lời thoại:**
> *"Cụ thể, Google kiểm soát chặt chẽ 3 lằn ranh đỏ sau:*  
> *Một là **Tỷ lệ khung hình chậm (Slow rendering)**: Một phiên bị tính là chậm nếu có trên 25% số frame mất nhiều hơn 16.67ms để vẽ. Ngưỡng tối đa Google cho phép chỉ là **25%**.*  
> *Hai là **Tỷ lệ khung hình đóng băng (Frozen Frames)**: Tức là khung hình bị đứng hình chết cứng trên 700ms. Ngưỡng tối đa cực kỳ khắt khe: **không được vượt quá 0.1%**.*  
> *Và ba là **Tỷ lệ treo ứng dụng (User-perceived ANR)**: Tức là người dùng gặp phải hộp thoại 'Ứng dụng không phản hồi'. Ngưỡng đỏ tối đa là **0.47%**.*  
>  
> *Và đây chính là bộ thước đo quốc tế mà nhóm chúng em lấy làm chuẩn mực để đánh giá toàn bộ dự án."*  
*(Bấm chuyển sang Slide 6)*

---

### 📌 SLIDE 6: BỘ CÔNG CỤ PAA & HỆ THỐNG HUD (03:30 – 04:15)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Chỉ vào mockup màn hình điện thoại bên trái và thanh HUD trên đỉnh.
* **Lời thoại:**
> *(Cầu nối dẫn dắt)*: *"Vậy làm thế nào một lập trình viên có thể đo lường và biết ứng dụng của mình có vi phạm chuẩn Google hay không?*  
>  
> *Đó chính là lý do nhóm chúng em đã tự tay xây dựng bộ công cụ thực nghiệm mang tên **PAA (Performance Analysis App)**.*  
>  
> *Điểm đặc biệt nhất của PAA là thanh **HUD Monitor nổi thời gian thực** trên cùng màn hình. Thay vì phải cắm dây vào máy tính bật Profiler phức tạp, PAA đọc trực tiếp từ `FrameMetrics API` phần cứng và bộ nhớ `Debug.MemoryInfo` của Android, liên tục cập nhật 4 thông số: **FPS**, **Tỷ lệ Jank (%)**, **RAM PSS** và **CPU (%)** theo nhịp 500ms.*  
>  
> *Đồng thời, app tích hợp công tắc đối chứng kép: **BAD (chưa tối ưu)** và **OPTIMIZED (đã tối ưu)** trên cùng một thiết bị để so sánh trực quan."*  
*(Bấm chuyển sang Slide 7)*

---

### 📌 SLIDE 7: CẤU TRÚC 3 PHÒNG LAB CỦA PAA (04:15 – 04:50)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Chỉ vào 3 mũi tên nối từ menu app sang 3 phòng Lab.
* **Lời thoại:**
> *"Trên màn hình chính của PAA, chúng em phân bổ thành 3 phòng Lab thực nghiệm chuyên sâu tương ứng với 3 căn bệnh kinh điển mà nhóm đã nêu:*  
> *👉 **Lab 1:** Nghiên cứu về Đồ họa & Cấu trúc View để giải quyết bài toán Render Jank.*  
> *👉 **Lab 2:** Nghiên cứu về Xử lý đa luồng và tải tính toán CPU để triệt tiêu lỗi treo ANR.*  
> *👉 **Lab 3:** Nghiên cứu về Quản lý vòng đời Activity và rò rỉ vùng nhớ trên máy ảo ART.*  
>  
> *Và sau đây, em xin kính mời Thầy cùng bước vào phòng Lab đầu tiên: **Lab 1: Khắc phục Render Jank**."*  
*(Bấm chuyển sang Slide 8)*

---

### 📌 SLIDE 8: LAB 1: KHẮC PHỤC RENDER JANK – BẢN BAD (04:50 – 05:45)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Bấm phát **Video Demo BAD** trên khung điện thoại, chỉ tay vào thanh HUD màu đỏ và bảng kết quả đo.
* **Lời thoại:**
> *"Ở bản Chưa tối ưu (BAD), nhóm đã cố tình cài cắm hai lỗi kiến trúc giao diện phổ biến nhất:*  
> *Thứ nhất: Tạo bố cục item lồng ghép tới 6 tầng `LinearLayout` và `RelativeLayout`, bắt hệ điều hành phải chạy thuật toán đo đạc `Measure/Layout` đệ quy cực kỳ nặng.*  
> *Thứ hai: Đọc và giải mã trực tiếp ảnh kích thước lớn từ Assets ngay trong hàm `onBindViewHolder` trên Main Thread.*  
>  
> *(Hướng mắt vào Video Demo)*: *Như Thầy và các bạn đang thấy trên video demo, khi thực hiện cuộn danh sách 500 phần tử, giao diện bị giật cục dữ dội.*  
> *Thanh HUD trên đầu lập tức đổi sang màu đỏ cảnh báo:*  
> *Tốc độ khung hình sụt giảm thảm hại xuống chỉ còn **7.8 FPS**, và tỷ lệ rớt khung hình (Jank) lên tới **99.8%**, thời gian trễ P95 lên đến **577.2 ms**. Bản BAD đã hoàn toàn phá vỡ trải nghiệm người dùng."*  
*(Bấm chuyển sang Slide 9)*

---

### 📌 SLIDE 9: LAB 1: KHẮC PHỤC RENDER JANK – BẢN OPTIMIZED (05:45 – 06:45)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Bấm phát **Video Demo OPT**, chỉ tay vào thanh HUD màu xanh lá cây và con số cải thiện.
* **Lời thoại:**
> *"Để khắc phục triệt để, ở bản OPTIMIZED, nhóm chúng em đã áp dụng 3 giải pháp kỹ thuật chuẩn công nghiệp:*  
> *Thứ nhất: Làm phẳng bố cục về đúng 1 tầng duy nhất bằng `ConstraintLayout`.*  
> *Thứ hai: Nâng cấp `RecyclerView.Adapter` sang `ListAdapter` kết hợp `DiffUtil` để chỉ vẽ lại item thực sự thay đổi.*  
> *Thứ ba: Sử dụng thư viện **Coil** để nạp ảnh bất đồng bộ ngoài luồng phụ, tự động thu nhỏ mẫu điểm ảnh (downsampling) và lưu đệm 2 tầng vào RAM.*  
>  
> *(Hướng mắt vào Video Demo)*: *Khi gạt công tắc sang OPTIMIZED và cuộn lại danh sách, sự khác biệt xuất hiện ngay lập tức: Thanh HUD chuyển sang màu xanh lá mượt mà, tốc độ khung hình đạt **55.0 FPS**, tỷ lệ Jank được kéo giảm tuyệt đối về **0.0%**.*  
>  
> *Mức độ cải thiện đạt **+605%**, loại bỏ 100% hiện tượng rớt frame, giúp app vượt qua chuẩn khắt khe của Android Vitals một cách xuất sắc."*  
*(Chuyển sang bước giao quyền)*

---

### 🔄 CHUYỂN LỜI TỪ KHOA SANG PHONG (06:45 – 07:00)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Nghiêng đầu mỉm cười, giơ tay mời bạn Đinh Thanh Phong bước lên.
* **Lời thoại:**
> *"Vừa rồi là phần thực nghiệm về giao diện đồ họa. Tiếp theo, để đi sâu vào các bài toán kỹ thuật phức tạp hơn về điều phối đa luồng CPU và quản lý bộ nhớ RAM trên máy ảo ART, em xin trân trọng nhường lại phần trình bày cho bạn **Đinh Thanh Phong**."*  
*(Phong gật đầu cảm ơn Khoa, bước lên bục, bấm chuyển sang Slide 10)*

---

## 🎙️ PHẦN 2: LAB 2 CPU, LAB 3 MEMORY & SỐ LIỆU ĐỐI CHỨNG (THANH PHONG TRÌNH BÀY)

### 📌 SLIDE 10: LAB 2: TỐI ƯU CPU & TRIỆT TIÊU ANR – BẢN BAD (07:00 – 08:15)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Phong cúi chào Thầy, bấm phát **Video Demo BAD CPU**, chỉ vào màn hình bị đơ cứng.
* **Lời thoại:**
> *"Em xin cảm ơn bạn Đăng Khoa. Kính thưa Thầy và các bạn, em tên là **Đinh Thanh Phong**, sau đây em xin phép được tiếp tục với **Phòng Lab 2: Tối ưu CPU và Triệt tiêu nguy cơ treo máy ANR**.*  
>  
> *Ở Lab 2, nhóm đặt ra bài toán xử lý dữ liệu: Tìm kiếm và tính tổng các phần tử trùng lặp trên một tập dữ liệu gồm **30.000 số nguyên**.*  
>  
> *Ở bản Chưa tối ưu (BAD), chúng em cài cắm lỗi lập trình rất hay gặp ở các bạn mới học: Sử dụng thuật toán ngây thơ 2 vòng lặp lồng nhau có độ phức tạp thời gian lên tới **$O(N^2)$**, và nguy hiểm nhất là **chạy trực tiếp trên luồng giao diện Main Thread**.*  
>  
> *(Hướng mắt vào Video Demo)*: *Khi em bấm nút 'Chạy đo', toàn bộ hàng đợi `MessageQueue` của Main Thread bị khóa chặt. Giao diện bị đóng băng hoàn toàn trong suốt **1,582 ms** (tương đương gần 1.6 giây), người dùng không thể chạm hay vuốt bất kỳ nút nào. Nếu tác vụ này kéo dài thêm vài giây nữa, hệ điều hành Android sẽ lập tức ném ra hộp thoại sập ANR."*  
*(Bấm chuyển sang Slide 11)*

---

### 📌 SLIDE 11: LAB 2: TỐI ƯU CPU – BẢN OPTIMIZED (08:15 – 09:30)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Bấm phát **Video Demo OPT CPU**, chỉ vào kết quả trả về tức thì.
* **Lời thoại:**
> *"Để giải cứu luồng chính Main Thread, ở bản OPTIMIZED, nhóm chúng em thực hiện hai cải tiến then chốt:*  
> *Thứ nhất về thuật toán: Chuyển từ thuật toán duyệt mảng $O(N^2)$ sang sử dụng cấu trúc bảng băm **`HashMap`** để đếm tần suất chỉ với 1 vòng lặp duy nhất, đưa độ phức tạp về mức tuyến tính **$O(N)$**.*  
> *Thứ hai về phân luồng: Sử dụng **Kotlin Coroutines** với ngữ cảnh `Dispatchers.Default` để đẩy toàn bộ tác vụ tính toán sang các luồng công nhân (Worker Thread) chạy ngầm, tận dụng tối đa sức mạnh đa nhân CPU phần cứng.*  
>  
> *(Hướng mắt vào Video Demo)*: *Khi bấm nút chạy trên bản OPT, thời gian xử lý lần đầu giảm từ 1,582 ms xuống chỉ còn **128 ms** (nhanh hơn gấp 12 lần, mức cải thiện đạt **+91.9%**). Đặc biệt, khi tận dụng bộ nhớ đệm Cache, các lần gọi lại trả về kết quả ngay lập tức trong **0 đến 3 ms**.*  
>  
> *Quan trọng nhất là trong suốt quá trình tính toán, thanh HUD của luồng chính hoàn toàn thông suốt, không rớt một khung hình nào, và hai bản cho ra đáp số trùng khớp chính xác 100% là 8.439 số trùng."*  
*(Bấm chuyển sang Slide 12)*

---

### 📌 SLIDE 12: LAB 3: KIỂM SOÁT RÒ RỈ RAM & XÁC THỰC VỚI GC – BẢN BAD (09:30 – 10:45)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Bấm phát **Video Demo BAD RAM**, chỉ vào nút "Kích hoạt GC thủ công" và con số RAM kẹt lại.
* **Lời thoại:**
> *"Tiếp theo, em xin kính mời Thầy bước sang phòng Lab phức tạp nhất: **Lab 3: Kiểm soát Rò rỉ RAM và Xác thực cùng bộ dọn rác Garbage Collector**.*  
>  
> *Để mô phỏng hiện tượng Memory Leak, nhóm thiết kế kịch bản: Tự động mở và đóng liên tục một `LeakyActivity` con **20 lần**. Mỗi màn hình khi sinh ra cố tình cấp phát một mảng bộ nhớ **5 MB**.*  
>  
> *Ở bản BAD, chúng em cài cắm 3 lỗi rò rỉ kinh điển:*  
> *1. Lưu tham chiếu Activity vào biến tĩnh `static` Singleton toàn cục.*  
> *2. Dùng `Handler.postDelayed` chạy ngầm 10 phút ngầm giữ Context.*  
> *3. Đăng ký Listener toàn cục nhưng không bao giờ hủy.*  
>  
> *(Hướng mắt vào Video Demo)*: *Sau khi đóng mở 20 màn hình, chúng em bấm nút **'Kích hoạt GC thủ công'** để ép máy ảo ART dọn rác. Nhưng kết quả hiển thị trên bảng đo cho thấy: Bộ thu gom rác ART hoàn toàn bất lực vì các Activity đã vướng vào cây tham chiếu **GC Root**. Bộ nhớ **RAM PSS bị kẹt cứng ở mức 133 MB** và toàn bộ **20 Activity instance vẫn còn sống nguyên trong Heap**, đe dọa trực tiếp gây ra lỗi sập app tràn bộ nhớ OutOfMemory."*  
*(Bấm chuyển sang Slide 13)*

---

### 📌 SLIDE 13: LAB 3: TRIỆT TIÊU RÒ RỈ RAM – BẢN OPTIMIZED (10:45 – 12:00)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Bấm phát **Video Demo OPT RAM**, chỉ vào con số RAM tụt sâu và Leak về 0.
* **Lời thoại:**
> *"Để xử lý dứt điểm bài toán rò rỉ bộ nhớ, ở bản OPTIMIZED, nhóm áp dụng giải pháp quản lý vòng đời chặt chẽ:*  
> *Thứ nhất: Thay thế toàn bộ tham chiếu mạnh bằng tham chiếu yếu **`WeakReference<Activity>`**, cho phép Garbage Collector tự do thu hồi vùng nhớ ngay khi Activity bị đóng.*  
> *Thứ hai: Trong hàm vòng đời `onDestroy()`, chủ động gọi `handler.removeCallbacks()` để hủy bỏ mọi công việc trễ và giải phóng bộ đệm payload về `null`.*  
>  
> *(Hướng mắt vào Video Demo)*: *Khi lặp lại đúng kịch bản mở đóng 20 màn hình trên bản OPT và bấm nút ép dọn rác GC: Máy ảo ART lập tức quét sạch toàn bộ các đối tượng mồ côi. Dung lượng RAM PSS hạ sâu từ 133 MB về mức sàn an toàn là **114 MB** (thu hồi thành công **19 MB RAM rác**), và số lượng Activity rò rỉ được triệt tiêu hoàn toàn về **0 Instance**.*  
>  
> *Đây là bằng chứng xác thực rõ ràng nhất chứng minh cơ chế quản lý vòng đời của nhóm hoạt động hoàn hảo."*  
*(Bấm chuyển sang Slide 14)*

---

### 📌 SLIDE 14: BẢNG TỔNG HỢP SỐ LIỆU ĐỐI CHỨNG ĐỊNH LƯỢNG (12:00 – 13:30)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Đứng nghiêng người, tay chỉ lần lượt từng hàng trong Bảng tổng hợp so sánh 5 tiêu chí.
* **Lời thoại:**
> *"Thưa Thầy và các bạn, trên Slide 14 là **Bảng tổng hợp số liệu đối chứng định lượng** được nhóm trích xuất trực tiếp từ các lần đo thực nghiệm trên ứng dụng PAA:*  
>  
> *1. Về **Tốc độ khung hình**: Bản BAD đạt 23.1 FPS $\rightarrow$ Bản OPT vọt lên **58.4 FPS**, mức cải thiện đạt **+152.8%**.*  
> *2. Về **Tỷ lệ giật khung hình Jank**: Bản BAD rớt tới 72.3% $\rightarrow$ Bản OPT kéo giảm triệt để về **0.0% (Triệt tiêu)**.*  
> *3. Về **Thời gian khóa Main Thread (CPU)**: Bản BAD làm đơ máy 2,520 ms $\rightarrow$ Bản OPT xử lý xong trong **3 ms** (nhanh gấp **840 lần**).*  
> *4. Về **Dung lượng RAM sau dọn rác**: Giảm từ 128 MB xuống 106 MB $\rightarrow$ Tiết kiệm thành công **22 MB RAM**.*  
> *5. Về **Rò rỉ đối tượng (Memory Leak)**: Triệt tiêu sạch **100%** từ 20 instance rò rỉ về **0 Instance**.*  
>  
> *Các con số định lượng này chứng minh rằng: Chỉ cần thay đổi đúng tư duy kiến trúc mã nguồn, hiệu năng ứng dụng đã được nâng cấp ngoạn mục mà không cần nâng cấp phần cứng."*  
*(Bấm chuyển sang Slide 15)*

---

### 📌 SLIDE 15: HÌNH ẢNH BIỂU ĐỒ SỐ LIỆU THỰC NGHIỆM (13:30 – 14:45)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Chỉ vào 3 cụm biểu đồ cột màu Đỏ (Trước) vs Xanh (Sau).
* **Lời thoại:**
> *"Để mang lại cái nhìn trực quan nhất, hình ảnh trên Slide 15 là biểu đồ tổng hợp số liệu đo đạc thực nghiệm được trích xuất trên thiết bị kiểm chuẩn Google Pixel 7 chạy Android 14:*  
>  
> *Cột thứ nhất thể hiện Tốc độ khung hình (cột xanh vọt cao gấp 7 lần cột đỏ).*  
> *Cột thứ hai thể hiện Thời gian tải CPU (cột xanh giảm sâu gần chạm đáy).*  
> *Cột thứ ba thể hiện Mức tiêu thụ RAM sau GC (cột xanh thu gọn rõ rệt và giải phóng sạch rác).*  
>  
> *Toàn bộ dữ liệu đo đạc này nhóm cũng đã tích hợp tính năng xuất ra file CSV và JSON trực tiếp từ app PAA để phục vụ công tác kiểm chứng độc lập."*  
*(Chuyển sang bước trả quyền phát biểu)*

---

### 🔄 CHUYỂN LỜI TỪ PHONG TRẢ LẠI CHO KHOA (14:45 – 15:00)
* **Người nói:** **Đinh Thanh Phong**
* **Hành động:** Phong quay sang bạn Khoa, mỉm cười và nhường lại micro.
* **Lời thoại:**
> *"Từ những kết quả thực nghiệm và số liệu đối chứng khoa học vừa rồi, bạn **Hoàng Thái Đăng Khoa** sẽ tiếp tục đúc kết lại 5 nguyên tắc vàng cho lập trình viên và kết luận bài báo cáo."*  
*(Khoa bước lên nhận lại lượt nói, bấm chuyển sang Slide 16)*

---

## 🎙️ PHẦN 3: NGUYÊN TẮC VÀNG, KẾT LUẬN & Q&A (ĐĂNG KHOA TRÌNH BÀY)

### 📌 SLIDE 16: 5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID (15:00 – 16:30)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Giọng nói đanh thép, đúc kết từng nguyên tắc tương ứng với 5 đám mây trên slide.
* **Lời thoại:**
> *"Em xin cảm ơn bạn Phong. Kính thưa Thầy, từ toàn bộ quá trình nghiên cứu lý thuyết tầng sâu AOSP và xây dựng ứng dụng PAA, nhóm chúng em đúc kết ra **5 Nguyên tắc vàng** có giá trị thực chiến cao cho bất kỳ lập trình viên Android nào:*  
>  
> *1. **Tối ưu Giao diện (Rendering):** Luôn ưu tiên dùng `ConstraintLayout` phẳng 1 tầng; tuyệt đối không nạp trực tiếp ảnh độ phân giải cao vào View mà phải dùng thư viện nạp ảnh có downsampling.*  
> *2. **Giải phóng Luồng chính (Threading):** Main Thread chỉ dành riêng cho tương tác UI. Mọi bài toán tính toán nặng, đọc ghi file, Database hay Mạng bắt buộc phải đẩy vào Kotlin Coroutines (`Dispatchers.Default` hoặc `Dispatchers.IO`).*  
> *3. **Quản lý Vòng đời (Lifecycle):** Không bao giờ lưu tham chiếu Context/Activity vào các biến tĩnh `static`; luôn sử dụng `WeakReference` và chủ động hủy đăng ký Listener trong `onDestroy()`.*  
> *4. **Tái sử dụng Tài nguyên (View Recycling):** Khai thác triệt để View-Holder Pattern trong `RecyclerView`; sử dụng `ListAdapter` kết hợp `DiffUtil` để hệ thống chỉ render lại đúng các item có dữ liệu biến động.*  
> *5. **Đo lường Thực nghiệm (Profiling):** Đừng bao giờ tối ưu hóa theo cảm tính hay đoán mò. Hãy luôn dùng công cụ đo lường thực tế (Profiler, Perfetto, FrameMetrics) để bắt đúng 'bệnh' trước khi bốc thuốc."*  
*(Bấm chuyển sang Slide 17)*

---

### 📌 SLIDE 17: KẾT LUẬN & PHẦN HỎI ĐÁP Q&A (16:30 – 17:30)
* **Người nói:** **Hoàng Thái Đăng Khoa**
* **Hành động:** Cả hai bạn Khoa và Phong cùng đứng ngang hàng, nét mặt tươi tắn, hướng về phía Thầy.
* **Lời thoại:**
> *"Kính thưa Thầy Trần Đại Nhân và các bạn sinh viên,*  
>  
> *Thông qua đề tài báo cáo Giữa kỳ hôm nay, nhóm chúng em đã hoàn thành 3 mục tiêu cốt lõi:*  
> *Thứ nhất: Làm sáng tỏ bản chất nguyên lý tầng sâu của hệ điều hành Android (từ nhịp VSYNC 16.67ms, hàng đợi Looper đến bộ thu gom rác ART Heap).*  
> *Thứ hai: Xây dựng thành công ứng dụng thực nghiệm PAA kèm thanh HUD giám sát thời gian thực, chứng minh được các giải pháp tối ưu bằng số liệu định lượng minh bạch.*  
> *Và thứ ba: Đúc kết được bộ quy chuẩn kỹ thuật thực tế cho bản thân và các bạn sinh viên.*  
>  
> *Nhóm chúng em xin gửi lời cảm ơn chân thành và sâu sắc nhất tới **Thầy Trần Đại Nhân** đã tận tình giảng dạy và hướng dẫn chúng em trong suốt học phần Phát triển Ứng dụng Di động.*  
>  
> *Sau đây, nhóm chúng em rất mong nhận được những lời nhận xét, góp ý và câu hỏi phản biện từ Thầy để bài nghiên cứu của chúng em được hoàn thiện hơn nữa.*  
>  
> *Chúng em xin trân trọng cảm ơn Thầy!"*  
*(Cả hai bạn cùng cúi đầu chào Thầy kết thúc bài báo cáo)*

---

# 🎯 BỘ CÂU HỎI VẤN ĐÁP DỰ PHÒNG CỦA THẦY TRẦN ĐẠI NHÂN

Dưới đây là 3 câu hỏi Thầy Trần Đại Nhân rất dễ hỏi xoáy, cùng câu trả lời "chuẩn chuyên gia" đã chuẩn bị sẵn cho hai bạn:

### ❓ Câu 1: Thầy hỏi về thanh HUD ở Lab 2
> **Thầy hỏi:** *"Ủa Khoa với Phong, sao Thầy nhìn ở Slide 10 và 11 của Lab 2 CPU, Thầy thấy FPS với Jank trên đỉnh đầu của bản BAD và OPT đều bằng nhau là 31.7 FPS với 100% vậy em?"*
* **Người trả lời:** **Đinh Thanh Phong** (hoặc Khoa)
* **Câu trả lời chuẩn:**  
> *"Dạ thưa Thầy, thanh HUD trên cùng phản ánh tốc độ vẽ đồ họa (FrameMetrics). Ở Lab 2 là bài toán thuần tính toán thuật toán mảng số nguyên trên giao diện tĩnh (không có cuộn danh sách), nên chỉ số quyết định của Lab 2 không nằm ở FPS mà nằm ở **Thời gian thực thi (Execution Time)** tại Bảng kết quả bên dưới:*  
> *Bản BAD dùng 2 vòng lặp $O(N^2)$ chạy trên Main Thread mất tới **1,582 ms** làm đơ màn hình; còn bản OPT chuyển sang dùng HashMap $O(N)$ và đưa vào Coroutines luồng nền nên chỉ mất **128 ms**, giải phóng hoàn toàn luồng chính ạ!"*

---

### ❓ Câu 2: Thầy hỏi về cơ chế Garbage Collection ở Lab 3
> **Thầy hỏi:** *"Tại sao ở bản BAD của Lab 3, em đã bấm nút 'Kích hoạt GC thủ công' rồi mà hệ thống vẫn không thể giải phóng được 20 Activity đó?"*
* **Người trả lời:** **Đinh Thanh Phong**
* **Câu trả lời chuẩn:**  
> *"Dạ thưa Thầy, cơ chế dọn rác của máy ảo Android ART hoạt động dựa trên giải thuật **Khả năng tiếp cận từ gốc (GC Root Reachability)**. Dù hàm `onDestroy()` của Activity đã kết thúc, nhưng do chúng em lưu biến tĩnh Singleton `static leakyActivities.add(this)`, biến static này nằm trong vùng nhớ tĩnh và đóng vai trò là một **GC Root**.*  
> *Bộ dọn rác GC quét từ GC Root thấy vẫn còn đường dẫn tham chiếu mạnh (Strong Reference) dẫn tới Activity nên nó bắt buộc phải giữ lại, không được phép thu hồi. Chỉ khi chuyển sang `WeakReference` ở bản OPT, mối liên kết mạnh mới bị cắt đứt, cho phép GC dọn sạch bộ nhớ ạ!"*

---

### ❓ Câu 3: Thầy hỏi về Coroutines Dispatchers
> **Thầy hỏi:** *"Trong app PAA, nhóm dùng các Dispatchers nào của Coroutines và phân biệt chúng ra sao?"*
* **Người trả lời:** **Hoàng Thái Đăng Khoa** (hoặc Phong)
* **Câu trả lời chuẩn:**  
> *"Dạ thưa Thầy, nhóm sử dụng 3 Dispatchers chính phù hợp với từng bản chất tác vụ:*  
> *1. **Dispatchers.Main:** Dùng để cập nhật giao diện UI và nhận tương tác người dùng.*  
> *2. **Dispatchers.Default:** Được cấu hình tối ưu cho các tác vụ **ngốn CPU (CPU-intensive)** như thuật toán đếm số trùng lặp trong Lab 2, số luồng được cấp bằng với số nhân CPU phần cứng.*  
> *3. **Dispatchers.IO:** Được cấu hình tối ưu cho các tác vụ **đọc ghi vào ra (I/O-blocking)** như đọc file JSON, nạp ảnh từ thư mục assets và lưu kết quả đo đạc xuống bộ nhớ trong ạ!"*
