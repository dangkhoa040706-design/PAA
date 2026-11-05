# QUY TRÌNH ĐO VÀ BIỂU MẪU QUẢN LÝ NHÓM

> Đi kèm: `docs/Dac_ta_PAA.md` (đặc tả), `files/So_lieu_do_mau.xlsx` (bảng ghi số liệu), `files/gen_data.py` + thư mục `files/images/` (dữ liệu test cố định).
> Ứng dụng chính thức: **PAA (Performance Analysis App)**.
> Các con số trong ví dụ chỉ để minh họa, **không phải kết quả thật**.

## MỤC LỤC

1. Cách dùng bộ dữ liệu test (script + file có sẵn)
2. Chuẩn bị môi trường (checklist D)
3. **Quy trình đo (measurement protocol)**
4. Quy trình đo riêng cho từng module
5. Quản lý bằng chứng (thư mục `evidence/`)
6. Cách đưa số liệu vào báo cáo
7. Quy ước làm việc nhóm
8. Bảng phân công và tiến độ
9. Checklist kiểm thử
10. Nhật ký lỗi (bug log)
11. Bảng nguồn tài nguyên
12. Danh sách tài liệu cần đọc và mẫu ghi chú

---

## 1. CÁCH DÙNG BỘ DỮ LIỆU TEST

### 1.1. Có gì sẵn

| File | Nội dung | Dùng cho |
|---|---|---|
| `du_lieu_test/items.json` | 500 item (`id`, `title`, `description`, `imageName`), sinh với seed cố định | Jank Lab |
| `du_lieu_test/cpu_data.csv` | 50.000 số nguyên (`index`, `value`), phạm vi giá trị nhỏ hơn n/2 nên chắc chắn có phần tử trùng | CPU Lab |
| `du_lieu_test/images/img_01.jpg ... img_30.jpg` | 30 ảnh 3000x2000 do **script tự tạo** (không dính bản quyền) | Jank Lab, Memory Lab |
| `gen_data.py` | Script sinh lại tất cả, tham số tùy chỉnh | Khi cần đổi số lượng/kích thước |

### 1.2. Cách đưa vào project Android
1. Chép cả thư mục `du_lieu_test/` vào `app/src/main/assets/` (đổi tên thư mục nếu thích, nhớ sửa đường dẫn trong code).
2. Trong code, đọc `items.json` và `cpu_data.csv` từ `assets` bằng `AssetManager` (phần viết code do nhóm tự làm).
3. Mỗi `imageName` trong `items.json` trỏ tới một ảnh trong thư mục `images/` (ảnh được dùng lặp vòng nếu số item nhiều hơn số ảnh).

### 1.3. Quy tắc bắt buộc
- **Cả nhóm dùng CÙNG một bộ file.** Hãy đưa chúng vào Git một lần rồi mọi người dùng chung. Không để mỗi người tự chạy script trên máy mình, vì ảnh có thể khác từng byte nếu phiên bản thư viện khác nhau (hai file `.json` và `.csv` thì luôn giống nhau với cùng seed).
- **Không đổi dữ liệu giữa lần đo BAD và OPTIMIZED.**
- Nếu muốn đổi kích thước/số lượng, chạy lại script, rồi **đo lại tất cả** từ đầu.

### 1.4. Chạy script
```
pip install pillow numpy
python gen_data.py                                  # mặc định: 500 item, 50.000 số, 30 ảnh 3000x2000
python gen_data.py --items 800 --cpu 100000         # đổi số lượng
python gen_data.py --images 20 --width 2400 --height 1600 --quality 80   # ảnh nhẹ hơn
python gen_data.py --no-images                      # chỉ sinh json và csv
```

**Lưu ý về dung lượng:** bộ mặc định khoảng 16 MB, đủ nhẹ để đưa vào APK. Ảnh càng lớn thì bản Bad càng dễ thấy giật, nhưng máy yếu có thể gặp `OutOfMemoryError` khi decode (đây cũng là một hiện tượng đáng ghi lại trong báo cáo).

**Ghi nguồn trong báo cáo (đạt tiêu chí hình ảnh):** "Ảnh test do nhóm tự sinh bằng script `gen_data.py` (seed cố định), không sử dụng ảnh từ internet."

---

## 2. CHUẨN BỊ MÔI TRƯỜNG (CHECKLIST D)

| # | Việc cần làm | Xong |
|---|---|---|
| D1 | Cài Android Studio bản ổn định mới nhất, SDK Platform, SDK Tools. Build thử một project mẫu | ☐ |
| D2 | Có ít nhất 1 máy Android thật. Bật Developer Options và USB Debugging | ☐ |
| D3 | Ghi lại thông tin máy: hãng/model, Android/API, RAM, tần số quét màn hình (60/90/120 Hz) vào sheet `ThietBi` | ☐ |
| D4 | `adb devices` thấy máy. Thử `adb shell dumpsys gfxinfo <package>` được | ☐ |
| D5 | Tạo Git repository chung, mỗi người một nhánh | ☐ |
| D6 | Cài công cụ ghi màn hình (scrcpy hoặc ghi màn hình hệ thống) | ☐ |
| D7 | Cài công cụ vẽ sơ đồ/mind map (draw.io, XMind hoặc Miro) | ☐ |
| D8 | Cài phần mềm dựng video | ☐ |
| D9 | Có bảng quản lý công việc (Trello, Notion hoặc Google Sheets) | ☐ |
| D10 | Có thư mục chung (Drive/OneDrive) cho báo cáo, ảnh, video, bản đo | ☐ |

**Lưu ý tần số quét:** ngưỡng frame phụ thuộc màn hình (60 Hz khoảng 16,67 ms; 90 Hz khoảng 11,1 ms; 120 Hz khoảng 8,3 ms). Ghi rõ tần số quét của máy đo trong báo cáo vì nó ảnh hưởng tới số liệu jank.

---

## 3. QUY TRÌNH ĐO (MEASUREMENT PROTOCOL)

Mục tiêu: **số liệu Trước/Sau đáng tin cậy, ai làm lại cũng ra kết quả tương đương.**

### 3.1. Nguyên tắc chung

| # | Nguyên tắc | Lý do |
|---|---|---|
| 1 | Chỉ so sánh BAD với OPTIMIZED trên **cùng thiết bị, cùng bản build, cùng dữ liệu, cùng kịch bản** | Loại bỏ nhiễu |
| 2 | Đo trên **máy thật** (máy ảo chỉ để test chức năng) | Máy ảo cho số liệu GPU/CPU không phản ánh thực tế |
| 3 | Đo Jank và CPU trên bản **không debuggable** (release hoặc profileable) | Bản debug chậm hơn rõ rệt, làm sai lệch số liệu |
| 4 | Mỗi phiên bản đo **tối thiểu 5 lần** chính thức, chưa tính 1 lần chạy khởi động (warm-up) | Giảm ảnh hưởng ngẫu nhiên |
| 5 | **Xen kẽ** thứ tự: BAD, OPT, BAD, OPT, ... | Tránh máy nóng dần làm lệch nghiêng về một phía |
| 6 | **Không xóa lần đo xấu một cách âm thầm.** Nếu bỏ một lần, ghi lý do ở cột Ghi chú và đo bù | Minh bạch, tránh bị nghi ngờ chỉnh số |
| 7 | Mỗi lần đo có **bằng chứng** (ảnh/trace) lưu trong `evidence/` | Chứng minh tự làm và có thể kiểm tra lại |

### 3.2. Loại build cho từng mục đích

| Mục đích | Build | Ghi chú |
|---|---|---|
| Phát triển, bắt lỗi | debug (có LeakCanary, StrictMode) | Không dùng đo tốc độ |
| Đo Jank, CPU | release hoặc build `profileable`, không debuggable | Để dùng Profiler/Perfetto trên bản không debug, thêm thẻ `<profileable android:shell="true"/>` trong manifest (yêu cầu Android 10 trở lên) |
| Đo Memory leak (đếm instance, heap dump) | debug được chấp nhận | Leak do tham chiếu, không phụ thuộc tốc độ. Vẫn ghi rõ loại build |

> Lưu ý: tùy phiên bản Android Studio, thao tác ký/chọn loại build có thể khác nhau chút. Nhóm kiểm tra theo tài liệu chính thức của Android Developers.

### 3.3. Chuẩn bị máy trước mỗi đợt đo

- [ ] Sạc từ 50% trở lên (hoặc cắm sạc và ghi chú), tắt chế độ tiết kiệm pin
- [ ] Tắt thông báo, bật chế độ không làm phiền
- [ ] Đóng mọi ứng dụng khác (xóa khỏi đa nhiệm)
- [ ] Độ sáng màn hình cố định, tắt tự động điều chỉnh độ sáng
- [ ] Tắt/giữ nguyên Wi-Fi và Bluetooth một cách nhất quán giữa các lần đo
- [ ] Máy không nóng: nghỉ 1 đến 2 phút giữa các lần đo
- [ ] Khởi động lại máy nếu bộ nhớ bị phân mảnh sau nhiều lần đo
- [ ] Cài đặt animation hệ thống giữ nguyên, không thay đổi giữa các đợt đo
- [ ] Ghi lại cả ngày giờ và thiết bị vào sheet NhatKyDo

### 3.4. Các bước cho một lần đo (khung chung)

1. **Đóng hẳn ứng dụng:** `adb shell am force-stop <package>`
2. **Mở lại ứng dụng**, vào đúng module và phiên bản cần đo.
3. **Đặt lại bộ đếm** (nếu dùng gfxinfo): `adb shell dumpsys gfxinfo <package> reset`
4. **Chạy kịch bản đo tự động** bằng nút "Chạy đo" (không thao tác tay, để kết quả lặp lại).
5. **Thu thập số liệu** ngay khi kịch bản kết thúc (xem mục 4).
6. **Chụp bằng chứng** (ảnh Profiler/overlay/terminal) và đặt tên đúng quy ước (mục 5).
7. **Ghi một dòng** vào sheet `NhatKyDo`.
8. **Nghỉ** 1 đến 2 phút, đổi phiên bản, lặp lại.

### 3.5. Mẫu lịch đo cho 1 module (5 lần mỗi phiên bản)

| Thứ tự | Phiên bản | Ghi chú |
|---|---|---|
| 0 | BAD | Warm-up, **không tính** |
| 1 | BAD | Lần 1 |
| 2 | OPTIMIZED | Lần 1 (cũng cần warm-up riêng nếu OPT dùng thư viện tải ảnh) |
| 3 | BAD | Lần 2 |
| 4 | OPTIMIZED | Lần 2 |
| ... | ... | Cho đến khi đủ 5 lần mỗi bên |

### 3.6. Cách tính và đánh giá

- Báo cáo **trung bình** của 5 lần, kèm **min và max** (sheet `TongHop` tính sẵn).
- Công thức cải thiện:
  - Chỉ số "càng thấp càng tốt" (jank %, thời gian, RAM, leak): `(BAD - OPT) / BAD`
  - Chỉ số "càng cao càng tốt" (FPS): `(OPT - BAD) / BAD`
- **Kiểm tra độ ổn định:** `(max - min) / trung bình` không vượt ngưỡng nhóm đặt (mặc định 20% trong file Excel). Nếu vượt, tìm nguyên nhân (máy nóng, app nền, thông báo) rồi đo lại.
- Nếu cải thiện nhỏ hơn mức dao động giữa các lần đo thì **chưa kết luận được** là có tối ưu. Cần làm lỗi Bad rõ hơn hoặc tăng khối lượng dữ liệu.

### 3.7. Lệnh ADB hữu ích

| Mục đích | Lệnh |
|---|---|
| Xem thiết bị kết nối | `adb devices` |
| Dừng hẳn app | `adb shell am force-stop <package>` |
| Reset thống kê frame | `adb shell dumpsys gfxinfo <package> reset` |
| Xem thống kê frame (tổng frame, frame jank, các percentile) | `adb shell dumpsys gfxinfo <package>` |
| Xem bộ nhớ của app | `adb shell dumpsys meminfo <package>` |
| Xem CPU tức thời | `adb shell top -n 1` (tìm dòng của package) |
| Chụp màn hình | `adb exec-out screencap -p > anh.png` |

> Định dạng đầu ra của `dumpsys` có thể khác nhau giữa các phiên bản Android. Hãy chạy thử trên máy của nhóm và xem phần nào chứa số cần lấy, đừng giả định.

---

## 4. QUY TRÌNH ĐO RIÊNG TỪNG MODULE

### 4.1. Jank Lab

| Hạng mục | Thiết lập đề xuất |
|---|---|
| Dữ liệu | `items.json` (500 item) + 30 ảnh test |
| Kịch bản | Cuộn tự động từ đầu đến cuối danh sách với tốc độ cố định, 3 lượt |
| Build | release/profileable |
| Chỉ số | % frame jank, frame time P95, FPS trung bình |
| Nguồn số liệu chính | `dumpsys gfxinfo` (đối chiếu với overlay trong app) |
| Bằng chứng | Ảnh Profile GPU Rendering (thanh cột), ảnh kết quả `gfxinfo`, ảnh Layout Inspector (so sánh số tầng view), ảnh Debug GPU Overdraw |

**Các bước phụ:**
1. Bật Profile GPU Rendering (On screen as bars) khi quay video.
2. Dùng Layout Inspector chụp cây view của một item ở BAD và OPT để minh họa số tầng giảm.
3. Bật Debug GPU Overdraw để minh họa vùng vẽ chồng.

### 4.2. CPU Lab

| Hạng mục | Thiết lập đề xuất |
|---|---|
| Dữ liệu | `cpu_data.csv` (50.000 số) |
| Kịch bản | Chạy bài toán đã chọn (ví dụ tìm phần tử trùng) trên toàn bộ dữ liệu |
| Build | release/profileable |
| Chỉ số | Thời gian thực thi (ms), % CPU trung bình, thời gian Main Thread bị chặn |
| Nguồn số liệu | Đo trong app + CPU Profiler (Sample/Trace) |
| Bằng chứng | Ảnh Flame Chart, bảng Top Down/Bottom Up thể hiện method tốn nhiều thời gian, ảnh trace Perfetto (nếu có) |

**Các bước phụ:**
1. Ghi lại **method nóng nhất** ở BAD và vị trí của nó ở OPT (hoặc đã biến mất).
2. Quan sát UI có đơ hay không khi chạy (dùng overlay FPS).
3. Nếu muốn thử ANR: tăng n đủ lớn để Main Thread bị chặn lâu, ghi lại hiện tượng (không dùng cho số liệu so sánh chính).

### 4.3. Memory Lab

| Hạng mục | Thiết lập đề xuất |
|---|---|
| Kịch bản | Tự mở và đóng màn hình con 20 lần, sau đó chờ vài giây và gọi GC thủ công |
| Build | debug được chấp nhận (có LeakCanary) |
| Chỉ số | RAM đỉnh (MB), RAM sau khi GC, số instance Activity/Fragment còn trong heap dump, số leak LeakCanary báo |
| Nguồn số liệu | Memory Profiler, Heap Dump, LeakCanary |
| Bằng chứng | Biểu đồ Memory Profiler, ảnh heap dump lọc theo tên lớp, ảnh leak trace của LeakCanary |

**Các bước phụ:**
1. Chụp **Heap Dump** sau lượt 20 ở cả BAD và OPT. Lọc theo tên lớp màn hình con, ghi số instance.
2. Chụp biểu đồ Memory Profiler trong cả kịch bản.
3. Chụp thông báo/leak trace của LeakCanary ở BAD, và ảnh "không còn leak" ở OPT.
4. Mỗi kiểu leak đã cài (singleton, Handler, binding) nên được kiểm chứng riêng, ghi rõ cái nào LeakCanary bắt được và cái nào chỉ thấy bằng heap dump.

---

## 5. QUẢN LÝ BẰNG CHỨNG (`evidence/`)

### 5.1. Cấu trúc thư mục

```
evidence/
├── jank/
│   ├── bad/
│   └── optimized/
├── cpu/
│   ├── bad/
│   └── optimized/
├── memory/
│   ├── bad/
│   └── optimized/
└── chung/        (ảnh thiết bị, ảnh cài đặt Developer Options, ...)
```

### 5.2. Quy ước đặt tên

`<module>_<variant>_run<so>_<loai>_<YYYYMMDD>.png`

| Ví dụ | Ý nghĩa |
|---|---|
| `jank_bad_run1_gfxinfo_20260101.png` | Ảnh gfxinfo lần 1 của Jank bản BAD |
| `cpu_opt_run3_flamechart_20260102.png` | Flame chart lần 3 của CPU bản OPTIMIZED |
| `memory_bad_run1_heapdump_20260103.png` | Heap dump Memory bản BAD |

### 5.3. Quy tắc chụp ảnh
- Chụp đủ rõ để đọc chữ và số, cắt bớt phần thừa, khoanh vùng quan trọng khi đưa vào báo cáo.
- Ảnh chụp của chính nhóm ghi nguồn: "Nguồn: nhóm tự thực hiện".
- Không chụp lộ thông tin cá nhân (tên máy cá nhân, tài khoản).
- Giữ **ảnh gốc** trong `evidence/`, bản đã chỉnh sửa dùng cho báo cáo để riêng.

---

## 6. CÁCH ĐƯA SỐ LIỆU VÀO BÁO CÁO

### 6.1. Mẫu mô tả môi trường đo (đặt đầu Chương 6)

| Hạng mục | Nội dung |
|---|---|
| Thiết bị | (hãng, model, Android/API, RAM, tần số quét) |
| Loại build | (release/profileable hoặc debug, ghi rõ từng module) |
| Dữ liệu | 500 item, 30 ảnh 3000x2000 (seed cố định) |
| Số lần đo | 5 lần mỗi phiên bản, đã bỏ 1 lần warm-up |
| Công cụ | (Android Studio Profiler, dumpsys gfxinfo, LeakCanary, ...) |

### 6.2. Mẫu bảng kết quả (ví dụ trống, nhóm điền số thật)

| Chỉ số | BAD (TB) | OPTIMIZED (TB) | Cải thiện |
|---|---|---|---|
| % frame jank | ? | ? | ? |
| Frame time P95 (ms) | ? | ? | ? |
| FPS trung bình | ? | ? | ? |

### 6.3. Gợi ý mỗi demo viết 5 ý
1. **Hiện tượng**: người dùng thấy gì (giật, đơ, tốn RAM).
2. **Phát hiện**: dùng công cụ nào, nhìn vào đâu.
3. **Nguyên nhân**: đoạn code nào gây ra và vì sao.
4. **Khắc phục**: sửa gì, vì sao hiệu quả.
5. **Kết quả**: số liệu Trước/Sau, nhận xét và hạn chế.

---

## 7. QUY ƯỚC LÀM VIỆC NHÓM

### 7.1. Git

| Mục | Quy ước |
|---|---|
| Nhánh chính | `main`: chỉ chứa bản chạy được |
| Nhánh tính năng | `feature/jank`, `feature/cpu`, `feature/memory`, `feature/overlay`, `feature/results` |
| Commit | Nhỏ, thường xuyên, thông điệp rõ, ví dụ: `feat(jank): add bad adapter with main-thread decode` |
| Tiền tố | `feat`, `fix`, `docs`, `refactor`, `test`, `chore` |
| Gộp nhánh | Qua Pull Request, ít nhất **1 người khác** xem trước khi gộp |
| Nguyên tắc | Mỗi thành viên **commit phần của mình** để có bằng chứng tự làm |

### 7.2. Quy tắc review code
- Người review phải **hiểu** đoạn code đang duyệt. Nếu không hiểu thì hỏi tác giả giải thích (cũng là cách chuẩn bị cho câu hỏi của giảng viên).
- Kiểm tra: đặt tên, comment ở chỗ quan trọng, không còn code thử nghiệm bỏ lại, không hard-code chuỗi.

### 7.3. Quy tắc viết và dùng nguồn
- Không dán nội dung từ internet, từ bạn khác, từ công cụ dịch hoặc chatbot vào báo cáo.
- Đọc tài liệu rồi **tự viết lại bằng lời mình**, ghi nguồn đã đọc ở danh mục tham khảo.
- Mỗi người tự viết phần báo cáo của module mình phụ trách.

### 7.4. Họp nhóm (đề xuất 1 buổi mỗi tuần, 30 phút)

1. Mỗi người báo cáo: tuần qua làm gì, vướng gì (5 phút mỗi người).
2. **Giải thích code**: một thành viên trình bày một đoạn code chính cho cả nhóm.
3. Xem số liệu mới đo, kiểm tra độ ổn định.
4. Chốt việc tuần tới, người phụ trách, hạn.
5. Cập nhật bảng tiến độ.

---

## 8. BẢNG PHÂN CÔNG VÀ TIẾN ĐỘ

### 8.1. Bảng phân công (điền)

| Hạng mục | Người chính | Người review | Hạn | Trạng thái |
|---|---|---|---|---|
| Khung app, Home, điều hướng | | | | ☐ |
| Metrics Overlay + MetricsCollector | | | | ☐ |
| Jank Lab: bản BAD | | | | ☐ |
| Jank Lab: bản OPTIMIZED | | | | ☐ |
| CPU Lab: bản BAD | | | | ☐ |
| CPU Lab: bản OPTIMIZED | | | | ☐ |
| Memory Lab: bản BAD | | | | ☐ |
| Memory Lab: bản OPTIMIZED | | | | ☐ |
| Results + lưu kết quả | | | | ☐ |
| Kịch bản đo tự động (ScenarioRunner) | | | | ☐ |
| Đo và ghi số liệu | | | | ☐ |
| Báo cáo: Chương 1 đến 4 | | | | ☐ |
| Báo cáo: Chương 5 (từng module) | | | | ☐ |
| Báo cáo: Chương 6, 7 | | | | ☐ |
| Slide | | | | ☐ |
| Mind map | | | | ☐ |
| Kịch bản và quay video | | | | ☐ |
| Dựng video | | | | ☐ |
| Soát chính tả chéo | | | | ☐ |
| Đóng gói và nộp | | | | ☐ |

### 8.2. Mốc tiến độ (điều chỉnh theo deadline thật)

| Mốc | Tiêu chí hoàn thành | Ngày dự kiến | Thực tế |
|---|---|---|---|
| M1 (hết tuần 1) | Có đặc tả, repo, app khung chạy được, dữ liệu test | | |
| M2 (hết tuần 2) | 3 module bản BAD chạy, có số liệu baseline | | |
| M3 (hết tuần 3) | 3 module bản OPTIMIZED, bảng so sánh hoàn chỉnh | | |
| M4 (hết tuần 4) | Bản nháp đầy đủ báo cáo, slide, mind map, video thô | | |
| M5 (hết tuần 5) | Soát lỗi, đóng gói, nộp sớm 1 đến 2 ngày | | |

### 8.3. Bảng đóng góp thành viên (nộp kèm, chứng minh tự làm)

| Thành viên | Phần code phụ trách | Phần báo cáo phụ trách | Số commit | Ghi chú |
|---|---|---|---|---|
| | | | | |

---

## 9. CHECKLIST KIỂM THỬ

Chạy toàn bộ checklist **trước khi quay video** và **trước khi nộp**, trên ít nhất 1 máy thật.

| Mã | Module | Thao tác | Kết quả mong đợi | Đạt | Ghi chú |
|---|---|---|---|---|---|
| T01 | Chung | Mở app lần đầu | Hiện Home, không crash | ☐ | |
| T02 | Chung | Chạm từng module, quay lại | Điều hướng đúng, không crash | ☐ | |
| T03 | Chung | Xoay màn hình ở từng màn | Không crash, trạng thái hợp lý | ☐ | |
| T04 | Chung | Bật/tắt Overlay | Hiện/ẩn đúng, không che nội dung | ☐ | |
| T05 | Jank | Bật BAD, cuộn danh sách | Thấy giật, overlay báo jank cao | ☐ | |
| T06 | Jank | Chuyển sang OPTIMIZED, cuộn | Mượt hơn rõ rệt | ☐ | |
| T07 | Jank | Chạy kịch bản đo | Chạy hết, có bảng kết quả | ☐ | |
| T08 | Jank | Hủy giữa chừng | Dừng, không lưu kết quả | ☐ | |
| T09 | Jank | Chuyển BAD/OPT khi đang chạy đo | Hủy phép đo, không crash | ☐ | |
| T10 | CPU | Chạy BAD với n mặc định | UI đơ, thời gian hiển thị | ☐ | |
| T11 | CPU | Chạy OPT với n mặc định | UI mượt, có progress, thời gian ngắn hơn | ☐ | |
| T12 | CPU | Kiểm tra kết quả tính toán | BAD và OPT cho **cùng kết quả đúng** | ☐ | |
| T13 | Memory | Mở/đóng màn hình con 20 lần ở BAD | RAM tăng dần, LeakCanary báo leak | ☐ | |
| T14 | Memory | Làm tương tự ở OPT | RAM ổn định, không báo leak | ☐ | |
| T15 | Memory | Từng kiểu leak kiểm chứng riêng | Mỗi kiểu có bằng chứng | ☐ | |
| T16 | Lưu | Lưu kết quả đo | Xuất hiện trong lịch sử | ☐ | |
| T17 | Results | Mở so sánh Trước/Sau | Bảng đúng, % cải thiện hợp lý | ☐ | |
| T18 | Results | Thiếu dữ liệu một phiên bản | Báo "Chưa có dữ liệu", không crash | ☐ | |
| T19 | Xuất | Xuất CSV/JSON (nếu làm) | File tạo được, mở được trên máy tính | ☐ | |
| T20 | Xóa | Xóa lịch sử, xác nhận | Danh sách rỗng, không crash | ☐ | |
| T21 | Chung | Tắt Wi-Fi/chế độ máy bay | App vẫn chạy bình thường | ☐ | |
| T22 | Chung | Chạy liên tục 10 phút | Không crash, không tăng RAM bất thường ở bản OPT | ☐ | |
| T23 | Chung | Cài APK trên máy sạch | Cài và chạy được | ☐ | |

**Điểm quan trọng nhất là T12:** hai phiên bản phải tính ra **cùng kết quả đúng**, nếu không thì so sánh Trước/Sau không có ý nghĩa.

---

## 10. NHẬT KÝ LỖI (BUG LOG)

Ghi mọi lỗi gặp phải. Đây cũng là nguyên liệu cho phần "Bài học rút ra" của báo cáo.

| Mã | Ngày | Người phát hiện | Module | Mô tả lỗi | Cách tái hiện | Nguyên nhân | Cách sửa | Trạng thái |
|---|---|---|---|---|---|---|---|---|
| BUG-01 | | | | | | | | Mở / Đã sửa |
| BUG-02 | | | | | | | | |

**Mẫu ví dụ (minh họa):**

| Mã | Mô tả lỗi | Nguyên nhân | Cách sửa |
|---|---|---|---|
| BUG-01 | Số liệu BAD và OPT lệch nhau bất thường ở lần đo đầu | Lần đầu thư viện tải ảnh chưa khởi tạo cache | Thêm 1 lần warm-up không tính vào số liệu |

---

## 11. BẢNG NGUỒN TÀI NGUYÊN (NFR-08)

Điền mọi thứ không do nhóm tự viết/tự tạo ra.

| Tài nguyên | Loại | Nguồn | Giấy phép | Dùng ở đâu |
|---|---|---|---|---|
| Ảnh test `img_01..30.jpg` | Ảnh | Nhóm tự sinh bằng `gen_data.py` | Tự tạo | Jank Lab, Memory Lab |
| `items.json`, `cpu_data.csv` | Dữ liệu | Nhóm tự sinh bằng `gen_data.py` | Tự tạo | Jank Lab, CPU Lab |
| Icon (nếu dùng) | Icon | (ví dụ: Material Icons) | (ghi theo trang nguồn) | |
| Thư viện Coil/Glide | Thư viện | (trang chính thức) | (ghi theo trang nguồn) | Bản OPTIMIZED |
| LeakCanary | Thư viện | (trang chính thức) | (ghi theo trang nguồn) | Bản debug |

---

## 12. DANH SÁCH TÀI LIỆU CẦN ĐỌC VÀ MẪU GHI CHÚ

> Đọc để **hiểu**, sau đó **tự tóm tắt bằng lời mình**. Không chép, không dịch máy. Hãy ghi lại link thật và ngày bạn đọc.
> Chưa kiểm tra lại từng đường dẫn chi tiết. Hãy tìm theo tên trang trên trang gốc.

| # | Chủ đề | Nên tìm ở | Cần rút ra |
|---|---|---|---|
| F1 | Tổng quan hiệu năng Android | Trang "Performance" của Android Developers (developer.android.com/topic/performance) | Danh mục các mảng hiệu năng, công cụ gợi ý |
| F2 | Slow rendering, jank, frame | Android Developers | Ngưỡng frame, nguyên nhân giật, cách đọc |
| F3 | Profile GPU Rendering, Overdraw | Android Developers | Cách bật, đọc thanh cột |
| F4 | Android Studio Profiler (CPU, Memory) | Android Developers | Cách ghi, đọc Flame Chart, heap dump |
| F5 | Perfetto / System Trace | perfetto.dev và Android Developers | Cách thu và đọc một trace cơ bản |
| F6 | ANR | Android Developers | Điều kiện xảy ra, cách tránh |
| F7 | Quản lý bộ nhớ, GC, leak | Android Developers | Heap, GC, nguyên nhân leak phổ biến |
| F8 | LeakCanary | Tài liệu LeakCanary (Square) | Cơ chế phát hiện, cách đọc leak trace |
| F9 | RecyclerView, ListAdapter, DiffUtil | Android Developers | Cơ chế tái sử dụng view, tính diff |
| F10 | Kotlin Coroutines, lifecycleScope | kotlinlang.org và Android Developers | Dispatchers, scope, hủy coroutine |
| F11 | Macrobenchmark, JankStats, Baseline Profile | Android Developers (Jetpack) | Cách đo startup/scroll (nếu làm bonus) |
| F12 | StrictMode | Android Developers | Các loại vi phạm phát hiện được |

### Mẫu ghi chú đọc tài liệu (mỗi tài liệu một bản)

| Mục | Nội dung |
|---|---|
| Tên tài liệu / link | |
| Ngày đọc | |
| Người đọc | |
| Tóm tắt bằng lời của mình (3 đến 5 câu) | |
| 3 điều mới học được | |
| Áp dụng vào đâu trong app/báo cáo | |
| Còn thắc mắc | |

---

## PHỤ LỤC: THỨ TỰ LÀM ĐỀ XUẤT TRONG 3 NGÀY ĐẦU

| Ngày | Việc |
|---|---|
| 1 | Họp nhóm, rà soát bảng quyết định (mục 15 của `Dac_ta_PAA.md`), tạo Git repo, thư mục chung, bảng phân công (mục 8.1) |
| 2 | Cài môi trường (mục 2), tạo project, đưa `du_lieu_test/` vào Git và `assets`, thử `dumpsys gfxinfo` trên máy thật |
| 3 | Điền sheet `ThietBi`, xây khung app (Home + 3 Fragment rỗng), bắt đầu F1 đến F4 |

*Hết tài liệu.*
