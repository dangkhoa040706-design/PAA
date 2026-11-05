# DỰ ÁN BÁO CÁO GIỮA KỲ: PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ANDROID (PAA)

> **Môn học:** Phát triển Ứng dụng Di động  
> **Trường:** Đại học Tôn Đức Thắng (TDTU) – Khoa Công nghệ Thông tin  
> **Giảng viên hướng dẫn:** **GV: Trần Đại Nhân**  
> **Nhóm sinh viên thực hiện:**  
> 1. **Hoàng Thái Đăng Khoa** – MSSV: **52400017**  
> 2. **Đinh Thanh Phong** – MSSV: **52400027**  
> **Sản phẩm thực nghiệm:** Ứng dụng PAA (Performance Analysis App)

---

## CẤU TRÚC THƯ MỤC DỰ ÁN ĐƯỢC CHUẨN HÓA

Toàn bộ dự án đã được sắp xếp khoa học, trực quan thành 7 thư mục chức năng chính được đánh số thứ tự từ `01` đến `07`, cùng thư mục mã nguồn Android `PAA`:

```text
D:\MOBI GK\
│
├── 📂 01_Bao_Cao_Nop_Bai/             --> TÀI LIỆU BÁO CÁO CHÍNH THỨC NỘP BÀI
│   ├── ⭐ Bao_Cao_Giua_Ky_PAA_TDTU_Template.docx  (Bản Word chính thức chuẩn 100% mẫu TDTU - 4 MB)
│   ├── Bao_Cao_Tieu_Luan_Giua_Ky_PAA_Final.docx   (Bản dự phòng format chuẩn Quốc tế)
│   ├── Huong_Dan_Toan_Dien_PAA_v2.docx            (Cẩm nang hướng dẫn sử dụng PAA bản Word)
│   └── Cam_nang_PAA_Toan_Dien.md                  (Cẩm nang hướng dẫn dạng Markdown)
│
├── 📂 02_Slide_Thuyet_Trinh/          --> SLIDE VÀ KỊCH BẢN THUYẾT TRÌNH BẢO VỆ
│   ├── ⭐ Thuyet_Trinh_PAA_TDTU_12_Slides.pptx    (Slide PowerPoint 13 trang chuẩn TDTU Blue 16:9)
│   ├── ⭐ Kich_Ban_Thuyet_Trinh_Canva_PAA.docx    (Kịch bản lời thoại chi tiết cho Khoa & Phong)
│   └── Kich_Ban_Thuyet_Trinh_Canva_PAA.md         (Kịch bản thuyết trình dạng Markdown)
│
├── 📂 03_De_Bai_Va_Rubric/            --> ĐỀ TÀI, TIÊU CHÍ ĐÁNH GIÁ & TEMPLATE MẪU
│   ├── Template_VN.docx                           (File Word mẫu chuẩn của Trường ĐH Tôn Đức Thắng)
│   ├── Rubric_Assessment_Midterm.pdf              (Phiếu chấm điểm Rubric của Thầy Trần Đại Nhân)
│   ├── Topic 01_Midterm.en.xlsx                   (File phân công Đề tài 01)
│   ├── Dac_ta_PAA.md                              (Tài liệu đặc tả yêu cầu kỹ thuật ứng dụng PAA)
│   ├── Ke_hoach_De_tai_1_Android_Performance.md   (Kế hoạch nghiên cứu đề tài)
│   └── Plan_Code_PAA.md                           (Kế hoạch lập trình kiến trúc PAA)
│
├── 📂 04_Hinh_Anh_Va_So_Do/           --> HÌNH ẢNH APP & 4 SƠ ĐỒ KIẾN TRÚC 300 DPI
│   ├── 01_home.png                                (Ảnh chụp Màn hình chính PAA + HUD Monitor)
│   ├── 02_jank_bad.png                            (Ảnh chụp Lab 1 - UI Jank bản Chưa Tối Ưu)
│   ├── 03_jank_opt.png                            (Ảnh chụp Lab 1 - UI Jank bản Đã Tối Ưu)
│   ├── 04_cpu_lab.png                             (Ảnh chụp Lab 2 - Nghẽn CPU thuật toán)
│   ├── 05_memory_lab.png                          (Ảnh chụp Lab 3 - Rò rỉ RAM Leak)
│   ├── 06_results.png                             (Ảnh chụp Bảng kết quả tổng hợp 3 Lab)
│   ├── 07_cpu_result_panel.png                    (Ảnh chụp Chi tiết đo CPU)
│   ├── 08_diagram_rendering_pipeline.png          (Sơ đồ Chu kỳ VSYNC 16.67ms & Pipeline Render)
│   ├── 09_diagram_memory_leak_art.png             (Sơ đồ Cây tham chiếu GC Root & ART Heap)
│   ├── 10_diagram_cpu_threading.png               (Sơ đồ Điều phối luồng Looper vs Coroutines)
│   ├── 11_chart_performance_benchmarks.png        (Biểu đồ cột so sánh định lượng Before vs After)
│   └── word/media/                                (Logo ĐH Tôn Đức Thắng & Logo Khoa CNTT)
│
├── 📂 05_Du_Lieu_Thuc_Nghiem/         --> DỮ LIỆU ĐO ĐẠC VÀ BỘ MẪU TEST
│   ├── So_lieu_do_mau.xlsx                        (Bảng tính Excel lưu trữ số liệu đo đạc thực tế)
│   ├── Quy_trinh_do_va_bieu_mau.md                (Quy trình thực nghiệm 3 Lab và biểu mẫu ghi chép)
│   ├── cpu_data.csv                               (Dữ liệu 25,000 số nguyên test CPU)
│   ├── items.json                                 (Dữ liệu danh sách item test Jank)
│   ├── gen_data.py                                (Script Python sinh dữ liệu giả lập)
│   └── images/                                    (Kho ảnh mẫu test RecyclerView)
│
├── 📂 06_Thiet_Ke_Giao_Dien/          --> NHẬN DIỆN THƯƠNG HIỆU & BẢNG MÀU UI
│   ├── colors.xml                                 (Mã màu Android định nghĩa Palette PAA)
│   ├── Bang_mau_PAA.md                            (Quy chuẩn phối màu thiết kế)
│   ├── palette.png                                (Ảnh swatch bảng màu UI)
│   ├── PAA_1_logo_trong_suot.png                  (Logo biểu tượng nền trong suốt)
│   ├── PAA_1_logo_trong_suot.svg                  (Logo vector)
│   ├── PAA_2_logo_ten_trong_suot.png              (Logo có chữ PAA)
│   ├── PAA_3_logo_nen_pearl.png                   (Logo nền màu ngọc trai)
│   └── PAA_3_logo_nen_pearl.svg                   (Logo vector nền pearl)
│
├── 📂 07_Scripts_Tu_Dong_Hoa/         --> BỘ SCRIPT PYTHON SINH TỰ ĐỘNG BÁO CÁO & SLIDE
│   ├── generate_tdtu_report.py                    (Script tự động sinh file Word mẫu TDTU)
│   ├── generate_paa_slides_pptx.py                (Script tự động sinh Slide PPTX 13 trang)
│   ├── generate_canva_guide_docx.py               (Script sinh Kịch bản thuyết trình Word)
│   ├── generate_diagrams.py                       (Script vẽ 4 sơ đồ kiến trúc 300 DPI)
│   ├── generate_final_report.py                   (Script sinh báo cáo định dạng chuẩn quốc tế)
│   ├── generate_docx.py                           (Script tạo docx cơ bản)
│   └── generate_report_skeleton.py                (Script dựng khung sườn báo cáo)
│
└── 📂 PAA/                            --> MÃ NGUỒN DỰ ÁN ANDROID STUDIO (KOTLIN)
    ├── app/                                       (Source code module chính)
    │   ├── src/main/java/com/nhomx/paa/           (Mã nguồn Kotlin theo kiến trúc MVVM)
    │   ├── src/main/res/                          (Tài nguyên layout, drawable, values)
    │   └── src/main/assets/                       (Dữ liệu test nạp sẵn trong app)
    ├── build.gradle.kts                           (Cấu hình Gradle root)
    └── settings.gradle.kts                        (Cấu hình Project settings)
```

---

## HƯỚNG DẪN NHANH DÀNH CHO NHÓM

1. **Nộp Báo cáo Giữa kỳ cho Thầy:**  
   Vào thư mục `01_Bao_Cao_Nop_Bai` lấy file:  
   👉 **`Bao_Cao_Giua_Ky_PAA_TDTU_Template.docx`**

2. **Thuyết trình Giữa kỳ:**  
   Vào thư mục `02_Slide_Thuyet_Trinh`:  
   👉 Kéo thả file **`Thuyet_Trinh_PAA_TDTU_12_Slides.pptx`** vào Canva hoặc Google Slides.  
   👉 Mở file **`Kich_Ban_Thuyet_Trinh_Canva_PAA.docx`** để luyện tập lời thoại cho Khoa và Phong.

3. **Chạy lại hoặc mở dự án Android Studio:**  
   Mở Android Studio $\rightarrow$ Open $\rightarrow$ Chọn thư mục **`D:\MOBI GK\PAA`**.
