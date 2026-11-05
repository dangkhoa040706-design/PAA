# KẾ HOẠCH THỰC HIỆN ĐỀ TÀI 1
## Android Application Performance Analysis and Optimization (Performance Profiling)

**Môn:** Phát triển ứng dụng di động | **Hình thức:** Tiểu luận (Giữa kỳ)

---

## MỤC LỤC

1. Phân tích đề bài và barem
2. Mục tiêu điểm số và chiến lược
3. Giới thiệu tổng quan ứng dụng demo (PAA)
4. Chi tiết 3 module demo
5. Kiến trúc, công nghệ và thư viện cần dùng
6. Yếu tố cộng điểm (bonus)
7. Danh sách tài liệu cần nộp
8. Cấu trúc báo cáo chi tiết
9. Slide thuyết trình
10. Mind map
11. Kịch bản video demo
12. Tiến độ thực hiện và phân công
13. Những điều cần tránh (điểm trừ)
14. Câu hỏi giảng viên có thể hỏi
15. Checklist cuối trước khi nộp

---

## 1. PHÂN TÍCH ĐỀ BÀI VÀ BAREM

### 1.1. Đề bài

> Xây dựng một ứng dụng chạy mượt là bước đầu, nhưng ứng dụng chạy trơn tru mới giữ chân được người dùng. Đề tài tập trung vào kỹ năng phân tích, xác định và sửa các vấn đề hiệu năng, gồm **lag, sử dụng CPU và memory leak**.

Như vậy đề tài có **3 trụ cột bắt buộc**:

1. **Lag/Jank (giật UI)**
2. **CPU (tải xử lý)**
3. **Memory leak (rò rỉ bộ nhớ)**

Và một quy trình xuyên suốt: **Phân tích (đo) → Xác định nguyên nhân → Khắc phục → Đo lại để chứng minh**.

### 1.2. Barem chấm điểm (thang 10)

| Nhóm | Điểm | Tiêu chí con | Điểm |
|---|---|---|---|
| **1. Hình thức** | 2.0 | Bố cục | 0.75 |
| | | Hình ảnh | 0.5 |
| | | Lỗi chính tả | 0.75 |
| **2. Nội dung** | 2.0 | Tính đúng đắn | 1.0 |
| | | Diễn đạt | 1.0 |
| **3. Demo** | 6.0 | Chất lượng sản phẩm demo | 4.0 |
| | | Video | 2.0 |
| **4. Điểm trừ** | | Tiêu chí 1, 2 (báo cáo) | -4.0 |
| | | Tiêu chí 3 (demo) | -6.0 |

### 1.3. Tiêu chí đạt mức cao nhất (mức 3, 75% đến 100%)

| Tiêu chí | Để đạt mức cao nhất cần |
|---|---|
| Bố cục | Hợp lý, rõ ràng, dễ theo dõi |
| Hình ảnh | Nhìn rõ, có ghi nguồn |
| Chính tả | Không lỗi hoặc tối đa 3 lỗi |
| Tính đúng đắn | Trình bày đầy đủ nội dung đề tài được phân công, có trọng tâm, điểm nhấn |
| Diễn đạt | Văn phong trôi chảy, mạch lạc, ngắn gọn súc tích, dễ hiểu |
| Chất lượng demo | Hoàn chỉnh, không còn lỗi nghiêm trọng |
| Video | Chuẩn bị tốt, demo sinh động, cuốn hút, người xem quan sát rõ ràng, dễ hiểu |

### 1.4. Ghi chú quan trọng từ đề bài

- Có **kiểm tra đạo văn**: copy từ internet hoặc từ bạn khác thì **0 điểm**.
- Source code demo phải **tự viết**, không lấy từ internet.
- Mỗi video demo **không quá 2 phút**.
- **Deadline đang bị trống trong ảnh**: cần hỏi lại giảng viên.

---

## 2. MỤC TIÊU ĐIỂM SỐ VÀ CHIẾN LƯỢC

**Demo chiếm 6/10 điểm (60%)**, nên phân bổ công sức đề xuất:

| Hạng mục | Tỷ trọng công sức đề xuất |
|---|---|
| Code và demo app | 45% |
| Video | 15% |
| Báo cáo | 20% |
| Slide + mind map | 10% |
| Kiểm tra chéo, đóng gói | 10% |

**Nguyên tắc vàng:**

1. **Mọi thứ phải có số liệu Trước/Sau.** Đây là điểm nhấn thuyết phục nhất của đề tài profiling.
2. **Mỗi thành viên hiểu và giải thích được code mình viết.** Tránh bị trừ 6 điểm.
3. **Không dùng AI/dịch máy để viết hộ báo cáo.** Có thể dùng để tra khái niệm nhưng phải tự diễn đạt lại.
4. **Nộp sớm 1 đến 2 ngày** để có thời gian sửa lỗi.

---

## 3. GIỚI THIỆU TỔNG QUAN ỨNG DỤNG DEMO: "PAA"

### 3.1. Ứng dụng này về cái gì?

**PAA (Performance Analysis App)** là một ứng dụng Android "phòng thí nghiệm hiệu năng". Ứng dụng **cố ý chứa các lỗi hiệu năng phổ biến** và cho phép **chuyển đổi qua lại giữa phiên bản "Bad" (có lỗi) và "Optimized" (đã tối ưu)** ngay trong app. Nhờ vậy người xem video thấy được sự khác biệt trực quan và có số liệu chứng minh.

**Ý tưởng cốt lõi:** *"Tạo bệnh, chẩn đoán bệnh, chữa bệnh, kiểm tra lại."*

### 3.2. Vì sao chọn mô hình này?

- Bám sát đề bài (phân tích, xác định, sửa lỗi).
- Một app duy nhất dễ quản lý, dễ quay video, dễ giải thích.
- Có nút chuyển Bad/Optimized giúp **so sánh trực tiếp** trên cùng một màn hình.
- Tránh nguy cơ bị nghi ngờ đạo văn vì app tự thiết kế theo ý tưởng riêng.

### 3.3. Ứng dụng cần có những gì?

**Các màn hình:**

| # | Màn hình | Mô tả |
|---|---|---|
| 1 | **Home / Dashboard** | Danh sách 3 module demo + nút mở panel đo hiệu năng |
| 2 | **Module 1: Jank Lab** | Danh sách cuộn nặng (ảnh, text) có công tắc Bad/Optimized |
| 3 | **Module 2: CPU Lab** | Bài toán tính toán nặng (ví dụ lọc/sắp xếp/tìm kiếm dữ liệu lớn) có công tắc Bad/Optimized |
| 4 | **Module 3: Memory Lab** | Mở/đóng màn hình nhiều lần để gây leak, hiển thị RAM theo thời gian |
| 5 | **Metrics Overlay** | Lớp phủ nổi hiển thị FPS, % frame jank, RAM, CPU theo thời gian thực |
| 6 | **Results / History** | Bảng lưu kết quả Trước/Sau của mỗi lần chạy, có thể xuất ra file |

**Chức năng chính:**

- Công tắc **Bad ↔ Optimized** cho từng module.
- **Metrics Overlay** hiển thị số liệu real-time (rất có lợi cho video).
- **Lưu kết quả đo** (Room hoặc file JSON) để đưa vào báo cáo.
- **Nút chạy kịch bản tự động** (ví dụ tự cuộn, tự mở 20 lần màn hình) để đo công bằng, lặp lại được.

### 3.4. Sơ đồ tổng quan

```
PAA
├── Home (Dashboard)
├── Module 1: Jank Lab        [Bad | Optimized]
├── Module 2: CPU Lab         [Bad | Optimized]
├── Module 3: Memory Lab      [Bad | Optimized]
├── Metrics Overlay (FPS, Jank%, RAM, CPU)
└── Results (bảng so sánh Trước/Sau)
```

---

## 4. CHI TIẾT 3 MODULE DEMO

### 4.1. Module 1: Jank Lab (Lag/giật UI)

**Kiến thức nền:** Màn hình 60Hz cần mỗi frame trong khoảng **16.67 ms** (90Hz là 11.1 ms, 120Hz là 8.3 ms). Vượt ngưỡng thì mất frame và người dùng thấy giật.

| | Phiên bản BAD | Phiên bản OPTIMIZED |
|---|---|---|
| Xử lý ảnh | Decode Bitmap kích thước lớn ngay trên Main Thread | Tải ảnh bất đồng bộ, resize đúng kích thước hiển thị (Coil/Glide) |
| Danh sách | `notifyDataSetChanged()` toàn bộ, không tái sử dụng tốt | `ListAdapter` + `DiffUtil`, ViewHolder chuẩn |
| Layout | Lồng nhiều tầng LinearLayout/RelativeLayout | `ConstraintLayout` phẳng hơn, giảm số tầng View |
| Xử lý trong `onBindViewHolder` | Tính toán nặng, format chuỗi, `Thread.sleep` mô phỏng | Chuyển tính toán ra ngoài, cache kết quả |
| Overdraw | Nhiều lớp background chồng nhau | Bỏ background thừa |

**Công cụ phát hiện:** Profile GPU Rendering, Layout Inspector, Debug GPU Overdraw, Android Studio Profiler, Perfetto/System Trace, `adb shell dumpsys gfxinfo <package>`.

**Chỉ số chứng minh:** % frame jank, thời gian frame trung bình và percentile 90/95/99 (ms), số frame vượt 16 ms.

### 4.2. Module 2: CPU Lab (Tải CPU)

| | Phiên bản BAD | Phiên bản OPTIMIZED |
|---|---|---|
| Thuật toán | Thuật toán kém hiệu quả (ví dụ O(n²) khi tìm trùng lặp, lọc lặp lại) | Thuật toán tốt hơn (HashMap/HashSet, O(n)), tính một lần |
| Tính lặp | Tính lại cùng một kết quả nhiều lần | Cache/memoization |
| Thread | Chạy trên Main Thread gây đơ UI, có thể gây ANR | `Coroutines` + `Dispatchers.Default` |
| Polling | Vòng lặp/Handler kiểm tra liên tục mỗi vài ms | Dùng sự kiện (Flow/callback) hoặc `WorkManager` |
| Log/Chuỗi | Nối chuỗi trong vòng lặp, log liên tục | `StringBuilder`, bỏ log thừa |

**Công cụ phát hiện:** Android Studio CPU Profiler (Sample Java/Kotlin Methods, Trace), Flame Chart, Top Down/Bottom Up, Perfetto, Simpleperf (nâng cao).

**Chỉ số chứng minh:** % CPU, thời gian thực thi method (ms), số lần gọi, thời gian chờ Main Thread.

### 4.3. Module 3: Memory Lab (Rò rỉ bộ nhớ)

**Kiến thức nền:** Memory leak xảy ra khi object không còn dùng nhưng vẫn bị tham chiếu nên Garbage Collector không thu hồi được. Hậu quả: RAM tăng dần, GC chạy nhiều gây giật, cuối cùng là `OutOfMemoryError`.

| Kịch bản leak (BAD) | Cách sửa (OPTIMIZED) |
|---|---|
| Singleton/static giữ tham chiếu tới `Activity`/`Context` | Dùng `applicationContext`, hoặc `WeakReference` |
| `Handler`/`Runnable` (inner class) còn chạy sau khi Activity hủy | Hủy callback trong `onDestroy`, dùng `lifecycleScope` |
| Listener/Callback/Receiver đăng ký nhưng không hủy | Hủy đăng ký ở đúng lifecycle |
| Bitmap lớn giữ trong static/cache vô hạn | Dùng `LruCache`, giải phóng, resize ảnh |
| Fragment giữ tham chiếu `binding` sau `onDestroyView` | Gán `_binding = null` trong `onDestroyView` |
| Coroutine/Thread chạy vô hạn gắn với Activity | Dùng `viewModelScope`/`lifecycleScope` |

**Công cụ phát hiện:** Memory Profiler (Heap Dump, Allocation Tracking), **LeakCanary**, StrictMode (phát hiện leak đối tượng đóng).

**Chỉ số chứng minh:** Biểu đồ RAM theo thời gian (răng cưa tăng dần so với ổn định), số instance Activity còn tồn tại trong heap dump, báo cáo LeakCanary (leak trace).

---

## 5. KIẾN TRÚC, CÔNG NGHỆ VÀ THƯ VIỆN

### 5.1. Công nghệ

| Hạng mục | Đề xuất |
|---|---|
| Ngôn ngữ | Kotlin |
| UI | **ĐÃ CHỐT: XML + RecyclerView + ViewBinding** (dễ minh họa lỗi hiệu năng cổ điển, công cụ Layout Inspector/GPU Rendering hỗ trợ tốt). Không dùng Compose |
| Kiến trúc | MVVM đơn giản (ViewModel + StateFlow) |
| Bất đồng bộ | Kotlin Coroutines |
| Lưu kết quả | Room hoặc JSON file |
| minSdk | 24 trở lên |
| Build | Gradle (Kotlin DSL) |

### 5.2. Thư viện gợi ý

| Mục đích | Thư viện |
|---|---|
| Phát hiện leak | `LeakCanary` (chỉ `debugImplementation`) |
| Tải ảnh | Coil hoặc Glide (chỉ dùng ở bản Optimized) |
| Đo jank trong app | `androidx.metrics:metrics-performance` (JankStats) |
| Đo benchmark | `androidx.benchmark:benchmark-macro-junit4` (Macrobenchmark) |
| Tối ưu khởi động | Baseline Profile |
| Tracing | `androidx.tracing:tracing-ktx` (tạo trace section tùy chỉnh) |

### 5.3. Công cụ phân tích

- Android Studio Profiler (CPU, Memory, Energy/Network)
- Layout Inspector
- Perfetto / System Trace
- LeakCanary
- StrictMode
- ADB: `dumpsys gfxinfo`, `dumpsys meminfo`, `top`
- Developer Options: Profile GPU Rendering, Show layout bounds, Debug GPU overdraw

### 5.4. Lưu ý khi đo (để số liệu đáng tin)

1. **Đo trên thiết bị thật** (ưu tiên) vì máy ảo cho số liệu sai lệch.
2. Đo bản **release** hoặc build có `debuggable false` khi benchmark (bản debug chậm hơn nhiều).
3. **Đo cùng một kịch bản**, cùng thiết bị, cùng điều kiện (sạc, nhiệt độ, tắt ứng dụng nền).
4. **Đo nhiều lần** (ví dụ 5 lần), lấy trung bình hoặc median.
5. Ghi lại thông số thiết bị (model, Android version, RAM) trong báo cáo.

### 5.5. Cấu trúc thư mục đề xuất

```
PAA/
├── app/src/main/java/.../
│   ├── ui/
│   │   ├── home/
│   │   ├── jank/        (JankFragment, adapter bad/optimized)
│   │   ├── cpu/         (CpuFragment, workers bad/optimized)
│   │   ├── memory/      (MemoryFragment, leak scenarios)
│   │   ├── results/
│   │   └── overlay/     (Metrics overlay)
│   ├── metrics/         (FPS, jank, memory, cpu collector)
│   ├── data/            (Room/JSON, repository)
│   └── util/
├── benchmark/           (Macrobenchmark module)
└── README.md
```

### 5.6. Chi tiết triển khai với XML + RecyclerView (đã chốt)

**Kiến trúc UI:** Single Activity + nhiều Fragment, điều hướng bằng Navigation Component hoặc `FragmentManager` đơn giản. Dùng **ViewBinding** (không dùng `findViewById` hay Kotlin synthetic).

| Module | Cách dựng bản BAD bằng XML/RecyclerView | Cách dựng bản OPTIMIZED |
|---|---|---|
| **Jank** | `RecyclerView.Adapter` thường, `onBindViewHolder` decode Bitmap bằng `BitmapFactory` trên Main Thread, item layout lồng 5 đến 6 tầng `LinearLayout`/`RelativeLayout` có nhiều background chồng nhau, cập nhật dữ liệu bằng `notifyDataSetChanged()` | `ListAdapter` + `DiffUtil.ItemCallback`, tải ảnh bằng Coil/Glide có resize, item layout phẳng bằng `ConstraintLayout`, bỏ background thừa, bật `setHasFixedSize(true)` và `RecycledViewPool` nếu cần |
| **CPU** | Nút bấm chạy tính toán nặng ngay trong `onClick` (Main Thread), thuật toán O(n²), `Handler.postDelayed` lặp liên tục mô phỏng polling | Chạy trong `lifecycleScope.launch(Dispatchers.Default)`, dùng `HashSet`/`HashMap`, cache kết quả, hiển thị `ProgressBar`, bỏ polling |
| **Memory** | `object`/`companion object` giữ `Activity` hoặc `View`, `Handler` inner class còn `postDelayed` sau `onDestroy`, `Fragment` không gán `_binding = null` trong `onDestroyView`, danh sách `Bitmap` giữ trong static | Dùng `applicationContext`/`WeakReference`, `removeCallbacksAndMessages(null)` trong `onDestroy`, `_binding = null`, `LruCache` cho Bitmap |

**Mẹo để demo Jank thể hiện rõ và đo công bằng:**
- Dùng **bộ dữ liệu giả cố định** (ví dụ 500 item, ảnh nằm sẵn trong `res/drawable` hoặc `assets` kích thước lớn) để mỗi lần đo giống nhau.
- Viết **kịch bản cuộn tự động** bằng `recyclerView.smoothScrollBy(...)` hoặc dùng Macrobenchmark `scrollDown()` để cuộn đều mỗi lần đo.
- Đo bằng `adb shell dumpsys gfxinfo <package> reset` trước khi cuộn, rồi `dumpsys gfxinfo <package>` sau khi cuộn để lấy số frame jank.
- Bật **Profile GPU Rendering (On screen as bars)** khi quay video: thanh vượt đường 16 ms màu xanh lá là frame bị trễ, rất trực quan.

**Mẹo cho Memory Lab (XML):**
- Tạo màn hình con mở bằng nút, mỗi lần mở/đóng lại sinh thêm một Activity/Fragment bị leak. Lặp 10 đến 20 lần rồi chụp **Heap Dump** và lọc theo tên class để thấy nhiều instance còn sống.
- Bật LeakCanary ở bản debug để có thông báo leak trace ngay khi demo.

**Gradle (tóm tắt, bạn tự viết và hiểu):**
- Bật `viewBinding { enabled = true }` trong `buildFeatures`.
- Thêm `leakcanary` bằng `debugImplementation`.
- Thêm thư viện Coil/Glide (chỉ dùng trong luồng Optimized), `lifecycle-runtime-ktx`, `kotlinx-coroutines-android`.
- Tạo module `benchmark` riêng cho Macrobenchmark.

---

## 6. YẾU TỐ CỘNG ĐIỂM (BONUS)

Barem không có điểm cộng chính thức, nhưng các yếu tố sau giúp **chắc chắn đạt mức 3 (75% đến 100%)** ở mọi tiêu chí và tạo ấn tượng mạnh với giảng viên.

### 6.1. Cộng điểm về Demo (6 điểm)

| Yếu tố | Lý do cộng điểm |
|---|---|
| **Công tắc Bad/Optimized ngay trong app** | So sánh trực tiếp, dễ quay video |
| **Metrics Overlay real-time** (FPS, RAM, CPU) | Người xem thấy ngay hiệu quả, video "sinh động, cuốn hút" |
| **Kịch bản đo tự động, lặp lại được** | Số liệu công bằng, thể hiện tính chuyên nghiệp |
| **Macrobenchmark** đo startup và scroll | Dùng công cụ chuẩn công nghiệp |
| **Baseline Profile** giảm thời gian khởi động | Kỹ thuật tối ưu hiện đại, đúng chủ đề |
| **JankStats** thu thập jank thật trong app | Số liệu định lượng chính xác |
| **StrictMode** bật ở bản debug | Phát hiện vi phạm Main Thread/leak tự động |
| **LeakCanary** hiển thị leak trace thật | Bằng chứng trực quan cho memory leak |
| **Custom trace** (`Trace.beginSection`) | Đọc Perfetto dễ hơn, thể hiện hiểu biết sâu |
| **Test đa thiết bị** (máy thật, máy yếu, máy ảo) | Chứng minh tối ưu có hiệu quả thực tế |
| **Xử lý ANR** (mô phỏng và khắc phục) | Mở rộng đúng chủ đề hiệu năng |
| **Tối ưu thêm: Energy/Battery, Network, APK size, R8/ProGuard** | Mở rộng kiến thức nhưng chỉ nên làm nếu còn thời gian |
| **Giao diện app gọn đẹp, không crash** | Tiêu chí "hoàn chỉnh, không lỗi nghiêm trọng" |
| **Git có lịch sử commit rõ ràng, từng thành viên đều commit** | Chứng minh tự làm, phòng nghi vấn đạo văn |
| **README rõ ràng** (cách build, chạy, kịch bản demo) | Giảng viên dễ chạy lại |

### 6.2. Cộng điểm về Báo cáo (4 điểm)

| Yếu tố | Lý do |
|---|---|
| Mục lục tự động, đánh số heading nhất quán | Bố cục rõ ràng |
| Danh mục hình, danh mục bảng | Chuyên nghiệp |
| Mọi hình đều có chú thích và nguồn | Đạt tiêu chí hình ảnh |
| Bảng so sánh Trước/Sau có số liệu | Có điểm nhấn |
| Sơ đồ tự vẽ (kiến trúc, quy trình, vòng đời) | Thể hiện hiểu biết, tránh đạo văn |
| Trích dẫn tài liệu chính thống (developer.android.com) | Tính đúng đắn |
| Đọc soát chéo 2 lượt, dùng công cụ kiểm tra chính tả | Dưới 3 lỗi |
| Văn phong ngắn gọn, mỗi đoạn một ý | Tiêu chí diễn đạt |
| Phần "Bài học rút ra" và "Hạn chế" | Thể hiện tư duy phản biện |

### 6.3. Cộng điểm về Video (2 điểm)

- Có kịch bản từng giây, tập trước.
- Có thuyết minh rõ, hoặc phụ đề đầy đủ.
- Phóng to/zoom vào phần số liệu Profiler.
- Chia màn hình **trái Bad, phải Optimized** để so sánh.
- Có nhạc nền nhẹ, không lấn át tiếng.
- Đúng giới hạn thời gian (dưới 2 phút).
- Chất lượng hình rõ nét (1080p).

---

## 7. DANH SÁCH TÀI LIỆU CẦN NỘP

### 7.1. Tài liệu bắt buộc (theo đề bài)

| # | Tài liệu | Định dạng đề xuất | Nội dung |
|---|---|---|---|
| 1 | **Báo cáo** | `.docx` và/hoặc `.pdf` | Trình bày kết quả nghiên cứu và cách thực hiện demo |
| 2 | **Slide thuyết trình** | `.pptx` | Nội dung nghiên cứu |
| 3 | **Mind map** | `.png`/`.pdf` (kèm file gốc nếu được) | Tóm tắt toàn bộ kiến thức thu được |
| 4 | **Source code demo** | Thư mục dự án hoặc `.zip`/link Git | Tự viết, không lấy từ internet |
| 5 | **Video demo** | `.mp4` | Mỗi video tối đa 2 phút |

### 7.2. Tài liệu bổ sung nên có (tăng độ chắc chắn)

| Tài liệu | Mục đích |
|---|---|
| **README.md** trong source code | Hướng dẫn cài, chạy, kịch bản demo |
| **File APK** (bản debug/release) | Giảng viên cài thử nhanh |
| **Bảng số liệu đo** (`.xlsx`/`.csv`) | Bằng chứng số liệu Trước/Sau |
| **Ảnh chụp Profiler gốc** (thư mục `evidence/`) | Chứng minh tự làm |
| **Bảng phân công và đóng góp** từng thành viên | Chứng minh công bằng và tự làm |
| **Danh mục tài liệu tham khảo** | Minh bạch nguồn |
| **Link Git repository** (nếu cho phép) | Lịch sử commit chứng minh tự làm |

### 7.3. Cấu trúc thư mục nộp đề xuất

```
NhomX_DeTai1_AndroidPerformance/
├── 1_BaoCao/
│   └── BaoCao_NhomX.pdf (và .docx)
├── 2_Slide/
│   └── Slide_NhomX.pptx
├── 3_MindMap/
│   └── MindMap_NhomX.png
├── 4_SourceCode/
│   ├── PAA/                (project, đã xóa thư mục build)
│   ├── PAA-debug.apk
│   └── README.md
├── 5_Video/
│   ├── Demo1_Jank.mp4
│   ├── Demo2_CPU.mp4
│   └── Demo3_Memory.mp4
└── 6_BangChung/
    ├── SoLieuDo.xlsx
    ├── AnhProfiler/
    └── PhanCongDongGop.md
```

---

## 8. CẤU TRÚC BÁO CÁO CHI TIẾT

**Độ dài đề xuất:** khoảng 25 đến 40 trang (ưu tiên chất lượng, súc tích hơn là dài dòng).

### Trang bìa, mục lục, danh mục hình/bảng, danh mục viết tắt

### Chương 1. Giới thiệu
- 1.1. Lý do chọn đề tài (hiệu năng ảnh hưởng trải nghiệm, giữ chân người dùng, đánh giá cửa hàng ứng dụng)
- 1.2. Mục tiêu
- 1.3. Phạm vi và đối tượng
- 1.4. Phương pháp thực hiện
- 1.5. Bố cục báo cáo

### Chương 2. Cơ sở lý thuyết
- 2.1. Cơ chế vẽ giao diện của Android: Main Thread, RenderThread, VSync, Choreographer, giới hạn 16.67 ms, hardware acceleration
- 2.2. Jank, frame drop, ANR: khái niệm và nguyên nhân
- 2.3. Hoạt động của CPU với ứng dụng Android: thread, scheduling, Coroutines
- 2.4. Quản lý bộ nhớ: Heap, ART, Garbage Collector, tham chiếu mạnh/yếu
- 2.5. Memory leak: định nghĩa, nguyên nhân phổ biến, hậu quả (OOM)
- 2.6. Vòng đời Activity/Fragment và liên hệ với leak

### Chương 3. Công cụ phân tích hiệu năng
- 3.1. Android Studio Profiler (CPU, Memory, Energy)
- 3.2. Layout Inspector và công cụ Developer Options
- 3.3. Perfetto / System Trace
- 3.4. LeakCanary
- 3.5. StrictMode
- 3.6. Macrobenchmark, JankStats, Baseline Profile
- 3.7. Bảng so sánh công cụ (dùng khi nào, đo cái gì)

### Chương 4. Quy trình phân tích và tối ưu
- 4.1. Quy trình 5 bước: Đặt mục tiêu → Đo baseline → Xác định nguyên nhân → Sửa → Đo lại
- 4.2. Nguyên tắc đo công bằng, môi trường thử nghiệm (thông số thiết bị)

### Chương 5. Triển khai ứng dụng PAA
- 5.1. Tổng quan ứng dụng, kiến trúc, màn hình
- 5.2. Module 1: Jank (mô tả lỗi → phát hiện → nguyên nhân → sửa → kết quả)
- 5.3. Module 2: CPU (cùng cấu trúc)
- 5.4. Module 3: Memory leak (cùng cấu trúc)
- 5.5. Các kỹ thuật bổ sung (Baseline Profile, StrictMode, ...)

### Chương 6. Kết quả và đánh giá
- 6.1. Bảng tổng hợp số liệu Trước/Sau
- 6.2. Biểu đồ so sánh
- 6.3. Phân tích, nhận xét
- 6.4. Hạn chế

### Chương 7. Kết luận và hướng phát triển
- Bài học rút ra, checklist tối ưu hiệu năng (best practices)

### Tài liệu tham khảo, Phụ lục (ảnh chụp bổ sung, bảng đo chi tiết, phân công)

### Bảng mẫu trình bày kết quả (dùng cho mỗi demo)

| Chỉ số | Trước (Bad) | Sau (Optimized) | Cải thiện |
|---|---|---|---|
| % frame jank | ... | ... | ... |
| Frame time P95 (ms) | ... | ... | ... |
| CPU trung bình (%) | ... | ... | ... |
| Thời gian method X (ms) | ... | ... | ... |
| RAM sau 20 lần mở màn hình (MB) | ... | ... | ... |
| Số Activity leak | ... | ... | ... |

### Quy tắc hình ảnh
- Mỗi hình có số thứ tự và chú thích: *Hình 5.2: CPU Profiler của bản Bad. Nguồn: nhóm tự thực hiện.*
- Hình lấy từ tài liệu: ghi rõ nguồn và link (ví dụ: Nguồn: developer.android.com).
- Độ phân giải đủ rõ để đọc chữ, cắt gọn phần thừa, khoanh đỏ vùng quan trọng.

---

## 9. SLIDE THUYẾT TRÌNH

**Gợi ý 15 đến 20 slide (nội dung nghiên cứu, không chép nguyên văn báo cáo):**

| # | Slide |
|---|---|
| 1 | Trang bìa, thành viên |
| 2 | Vì sao hiệu năng quan trọng (số liệu/ví dụ thực tế) |
| 3 | Mục tiêu và phạm vi đề tài |
| 4 | Cơ chế render: 16.67 ms/frame, VSync |
| 5 | Jank và ANR là gì, nguyên nhân |
| 6 | Quản lý bộ nhớ và memory leak |
| 7 | Bộ công cụ profiling |
| 8 | Quy trình 5 bước phân tích tối ưu |
| 9 | Giới thiệu app PAA |
| 10 | Demo 1: Jank (bệnh, công cụ, cách chữa, kết quả) |
| 11 | Demo 2: CPU |
| 12 | Demo 3: Memory leak |
| 13 | Bảng tổng hợp Trước/Sau |
| 14 | Kỹ thuật bổ sung (Baseline Profile, StrictMode, ...) |
| 15 | Best practices / checklist tối ưu |
| 16 | Hạn chế và hướng phát triển |
| 17 | Kết luận |
| 18 | Tài liệu tham khảo |
| 19 | Q&A |

**Nguyên tắc:** ít chữ, nhiều hình/sơ đồ, mỗi slide một thông điệp, cỡ chữ đủ lớn, nhất quán phông và màu.

---

## 10. MIND MAP

**Nhánh trung tâm:** Android Performance

```
Android Performance
├── 1. Nền tảng
│   ├── Render pipeline (VSync, Choreographer, 16.67ms)
│   ├── Main Thread / Worker Thread
│   └── Memory (Heap, GC, ART)
├── 2. Jank / UI Lag
│   ├── Nguyên nhân: Main thread nặng, layout sâu, overdraw, ảnh lớn
│   ├── Công cụ: GPU Rendering, Layout Inspector, Perfetto
│   └── Khắc phục: Coroutines, DiffUtil, ConstraintLayout, Coil
├── 3. CPU
│   ├── Nguyên nhân: Thuật toán kém, tính lặp, polling
│   ├── Công cụ: CPU Profiler, Flame Chart, Simpleperf
│   └── Khắc phục: Cache, thuật toán, WorkManager, Dispatchers
├── 4. Memory Leak
│   ├── Nguyên nhân: Static/Context, Handler, Listener, Bitmap
│   ├── Công cụ: Memory Profiler, Heap Dump, LeakCanary
│   └── Khắc phục: WeakReference, lifecycle, LruCache
├── 5. Quy trình
│   └── Đo → Xác định → Sửa → Đo lại
├── 6. Công cụ nâng cao
│   └── Macrobenchmark, Baseline Profile, JankStats, StrictMode
└── 7. Best Practices
```

Vẽ bằng XMind, Miro, draw.io hoặc Whimsical. Dùng màu khác nhau cho mỗi nhánh, xuất ảnh độ phân giải cao.

---

## 11. KỊCH BẢN VIDEO DEMO (mỗi video dưới 2 phút)

**Nên làm 3 video (mỗi module một video), mỗi video khoảng 1:45 để có biên an toàn.**

### Khung kịch bản mỗi video

| Thời gian | Nội dung | Hình ảnh |
|---|---|---|
| 0:00 đến 0:10 | Giới thiệu vấn đề (ví dụ: "Danh sách này bị giật, hãy xem vì sao") | Tiêu đề + màn hình app |
| 0:10 đến 0:50 | Chạy bản **Bad**: cho thấy hiện tượng + số liệu Profiler/Overlay | Chia đôi màn hình: máy thật + Profiler |
| 0:50 đến 1:00 | Chỉ ra nguyên nhân trong code (vài dòng chính) | Zoom vào code |
| 1:00 đến 1:35 | Chạy bản **Optimized**: cho thấy mượt hơn + số liệu | Giống đoạn Bad để so sánh |
| 1:35 đến 1:45 | Bảng so sánh Trước/Sau và kết luận | Bảng số liệu lớn, rõ |

### Checklist quay video
- [ ] Viết kịch bản lời thoại, tập đọc trước
- [ ] Máy sạc đầy, tắt thông báo, bật chế độ không làm phiền
- [ ] Ghi màn hình (scrcpy hoặc ghi màn hình hệ thống) độ phân giải cao
- [ ] Ghi âm giọng trong môi trường yên tĩnh, hoặc dùng phụ đề
- [ ] Zoom vào số liệu Profiler cho người xem đọc được
- [ ] Cắt ghép chặt, không có đoạn chờ thừa
- [ ] Kiểm tra tổng thời lượng dưới 2:00
- [ ] Xem lại toàn bộ trước khi nộp (hình, tiếng, số liệu đúng)

---

## 12. TIẾN ĐỘ THỰC HIỆN VÀ PHÂN CÔNG

> Giả sử có khoảng 5 tuần. **Hãy điều chỉnh theo deadline thật**: lấy ngày deadline lùi lại để chia tuần.

| Tuần | Công việc | Sản phẩm đầu ra |
|---|---|---|
| **1. Chuẩn bị** | Họp nhóm, phân công. Đọc tài liệu chính thức (developer.android.com/topic/performance). Cài công cụ, làm quen Profiler. Chốt ý tưởng PAA. Tạo Git repo | Kế hoạch, dàn ý báo cáo, danh sách tài liệu tham khảo |
| **2. Xây dựng bản Bad** | Dựng khung app, 3 module bản lỗi. Gắn Metrics Overlay. Đo baseline, chụp ảnh | App bản Bad chạy ổn định, số liệu gốc |
| **3. Tối ưu** | Sửa từng module, đo lại. Thêm bonus (LeakCanary, StrictMode, Macrobenchmark). Test thiết bị thật | App bản Optimized, bảng Trước/Sau |
| **4. Tài liệu** | Viết báo cáo, làm slide, vẽ mind map. Viết kịch bản và quay video | Bản nháp báo cáo, slide, mind map, video thô |
| **5. Hoàn thiện** | Soát chính tả chéo 2 lượt. Kiểm tra ảnh/nguồn. Dựng lại video, kiểm tra thời lượng. Đóng gói. Tập thuyết trình | Bộ hồ sơ hoàn chỉnh, nộp sớm 1 đến 2 ngày |

### Gợi ý phân công (nhóm 4 người, điều chỉnh theo nhóm của bạn)

| Thành viên | Phụ trách chính | Phụ trách phụ |
|---|---|---|
| A (Trưởng nhóm) | Module 1 Jank + kiến trúc app | Tổng hợp báo cáo, quản lý tiến độ |
| B | Module 2 CPU | Slide, Macrobenchmark |
| C | Module 3 Memory + LeakCanary | Mind map, kiểm tra chính tả |
| D | Metrics Overlay, Results, README | Quay và dựng video |

**Lưu ý:** Mỗi người phải hiểu **toàn bộ** app ở mức cơ bản, và hiểu sâu phần mình viết. Mỗi người nên tự viết phần báo cáo cho module mình phụ trách để đảm bảo văn phong là của chính mình.

### Mốc kiểm soát (milestone)

| Mốc | Tiêu chí hoàn thành |
|---|---|
| Hết tuần 1 | Có dàn ý + repo + app khung chạy được |
| Hết tuần 2 | 3 module Bad chạy, đã có số liệu baseline |
| Hết tuần 3 | 3 module Optimized, bảng so sánh hoàn chỉnh |
| Hết tuần 4 | Có bản nháp đầy đủ mọi tài liệu |
| Hết tuần 5 | Đã soát lỗi, đóng gói, nộp |

---

## 13. NHỮNG ĐIỀU CẦN TRÁNH (ĐIỂM TRỪ)

| Rủi ro | Hậu quả | Cách phòng tránh |
|---|---|---|
| Hơn 10 lỗi chính tả | **0 điểm** tiêu chí 1 và 2 (mất 4 điểm) | Đọc chéo, dùng công cụ kiểm tra |
| Viết bằng Google Dịch/ChatGPT, nhờ người khác viết | Trừ tối đa 4 điểm | Tự viết bằng lời mình |
| Báo cáo chỉ toàn ảnh chụp, ít nội dung | Trừ điểm | Mỗi hình đi kèm phân tích |
| Copy từ mạng, từ bạn khác | **0 điểm** | Tự viết, tự code, ghi nguồn tham khảo |
| Code lấy từ mạng, không hiểu code | Trừ 6 điểm | Tự viết, hiểu từng dòng, có lịch sử Git |
| Demo crash/lỗi nghiêm trọng | Mất điểm chất lượng demo | Test nhiều lần, nhiều thiết bị |
| Video quá 2 phút | Có nguy cơ mất điểm video | Kiểm tra thời lượng |
| Hình mờ, không ghi nguồn | Mất điểm hình ảnh | Chụp độ phân giải cao, ghi nguồn |
| Nộp trễ | Mất điểm | Nộp sớm 1 đến 2 ngày |

---

## 14. CÂU HỎI GIẢNG VIÊN CÓ THỂ HỎI (CHUẨN BỊ TRƯỚC)

1. Vì sao ngưỡng là 16.67 ms? Nếu màn hình 120Hz thì sao?
2. Jank khác ANR như thế nào? ANR xảy ra khi nào (ngưỡng thời gian)?
3. Vì sao bạn chọn chuyển xử lý sang `Dispatchers.IO` (hoặc `Default`)? Khác nhau chỗ nào?
4. Giải thích `DiffUtil` hoạt động ra sao, vì sao tốt hơn `notifyDataSetChanged`?
5. Memory leak xảy ra cụ thể ở đoạn code này thế nào? Chuỗi tham chiếu từ GC root đến Activity là gì?
6. `WeakReference` giải quyết leak như thế nào? Có nhược điểm gì không?
7. LeakCanary hoạt động dựa trên cơ chế gì?
8. Sampling và Tracing trong CPU Profiler khác nhau ra sao?
9. Vì sao đo bản debug lại không chính xác bằng bản release?
10. Số liệu Trước/Sau lấy từ đâu, đo trên thiết bị nào, lặp bao nhiêu lần?
11. Nếu muốn áp dụng vào app thật, bạn bắt đầu tối ưu từ đâu?
12. Baseline Profile là gì, giúp ích gì cho khởi động ứng dụng?

---

## 15. CHECKLIST CUỐI TRƯỚC KHI NỘP

### Báo cáo
- [ ] Có trang bìa, mục lục, danh mục hình/bảng
- [ ] Bố cục nhất quán (phông, cỡ chữ, heading, đánh số)
- [ ] Mọi hình rõ nét, có chú thích và **ghi nguồn**
- [ ] Dưới 3 lỗi chính tả (đã đọc chéo 2 lượt)
- [ ] Có bảng số liệu Trước/Sau cho cả 3 module
- [ ] Văn phong tự viết, mạch lạc, súc tích
- [ ] Có tài liệu tham khảo đầy đủ

### Slide
- [ ] Ít chữ, nhiều hình, nhất quán thiết kế
- [ ] Không chép nguyên văn từ báo cáo hay internet
- [ ] Đã tập thuyết trình, đúng thời gian

### Mind map
- [ ] Đủ ba nhánh chính (Jank, CPU, Memory) + quy trình + công cụ
- [ ] Chữ rõ, bố cục dễ nhìn, xuất độ phân giải cao

### Source code
- [ ] Tự viết, build và chạy được trên máy sạch
- [ ] Không crash ở mọi chức năng
- [ ] Có README hướng dẫn
- [ ] Đã xóa thư mục `build`, `.gradle` (nếu nộp zip)
- [ ] Git có lịch sử commit của các thành viên
- [ ] Mỗi người giải thích được code của mình

### Video
- [ ] Mỗi video **không quá 2 phút**
- [ ] Hình rõ, tiếng rõ hoặc có phụ đề
- [ ] Số liệu Profiler đọc được
- [ ] Có so sánh Bad vs Optimized

### Chung
- [ ] Đã xác nhận deadline và cách nộp với giảng viên
- [ ] Không có nội dung copy từ mạng/bạn khác
- [ ] Đặt tên file đúng quy định, nộp sớm

---

## TÀI LIỆU THAM KHẢO GỢI Ý (đọc để hiểu, rồi tự diễn đạt lại)

- Android Developers: Performance (developer.android.com/topic/performance)
- Android Developers: Android Profiler, Memory Profiler, CPU Profiler
- Android Developers: Slow rendering, Jank, ANR
- Android Developers: Macrobenchmark, Baseline Profiles, JankStats
- Perfetto documentation (perfetto.dev)
- LeakCanary documentation (square.github.io/leakcanary)
- Kotlin Coroutines Guide (kotlinlang.org)

> **Nhắc lại:** Tài liệu tham khảo dùng để học và đối chiếu. Báo cáo phải được viết bằng lời của nhóm, kèm ghi nguồn khi trích dẫn ý tưởng hoặc hình ảnh.
