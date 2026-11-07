import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

OUT_DIR = r"D:\MOBI GK\01_Bao_Cao_Nop_Bai"

# Brand Colors
C_NAVY = RGBColor(10, 77, 158)      # #0A4D9E TDTU Blue
C_SCARLET = RGBColor(188, 0, 36)    # #BC0024 PAA Scarlet
C_SLATE = RGBColor(30, 41, 59)      # #1E293B Dark Slate
C_GRAY = RGBColor(100, 116, 139)

def apply_tdtu_page_setup(doc):
    for s in doc.sections:
        s.top_margin = Inches(0.8)      # 20 mm
        s.bottom_margin = Inches(0.8)   # 20 mm
        s.left_margin = Inches(1.2)     # 30 mm (đóng gáy)
        s.right_margin = Inches(0.8)    # 20 mm

def set_font(run, name="Times New Roman", size=13, bold=False, italic=False, color=C_SLATE):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color

# =========================================================================
# FILE 0: 00_Trang_Bia_Va_Loi_Cam_Doan.docx
# =========================================================================
def create_cover_and_pledge():
    doc = docx.Document()
    apply_tdtu_page_setup(doc)

    # Header trường
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_after = Pt(2)
    r1 = p1.add_run("TỔNG LIÊN ĐOÀN LAO ĐỘNG VIỆT NAM\nTRƯỜNG ĐẠI HỌC TÔN ĐỨC THẮNG\nKHOA CÔNG NGHỆ THÔNG TIN")
    set_font(r1, "Times New Roman", 12, bold=True, color=C_NAVY)

    # Đường phân cách
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_after = Pt(24)
    r_div = p_div.add_run("-----------------------***-----------------------")
    set_font(r_div, "Times New Roman", 10, color=C_GRAY)

    # Logo placeholder / Label
    p_badge = doc.add_paragraph()
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_badge.paragraph_format.space_after = Pt(28)
    r_badge = p_badge.add_run("BÁO CÁO TIỂU LUẬN GIỮA KỲ\nHỌC PHẦN: PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG")
    set_font(r_badge, "Times New Roman", 14, bold=True, color=C_NAVY)

    # Tên đề tài
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(8)
    r_t = p_title.add_run("PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG\nỨNG DỤNG ANDROID")
    set_font(r_t, "Times New Roman", 18, bold=True, color=C_SCARLET)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(40)
    r_s = p_sub.add_run("Nghiên cứu Nguyên lý Tầng sâu AOSP & Thực nghiệm Bộ công cụ PAA (Performance Analysis App)")
    set_font(r_s, "Times New Roman", 13, italic=True, color=C_SLATE)

    # Khung thông tin SV & GVHD
    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    rows_data = [
        ("Giảng viên hướng dẫn:", "GV: TRẦN ĐẠI NHÂN"),
        ("Sinh viên thực hiện 1:", "Hoàng Thái Đăng Khoa – MSSV: 52400017"),
        ("Sinh viên thực hiện 2:", "Đinh Thanh Phong       – MSSV: 52400027")
    ]
    for idx, (label, val) in enumerate(rows_data):
        cell_lbl = table.cell(idx, 0)
        cell_lbl.width = Inches(2.2)
        p_l = cell_lbl.paragraphs[0]
        r_l = p_l.add_run(label)
        set_font(r_l, "Times New Roman", 12, bold=True, color=C_NAVY)

        cell_val = table.cell(idx, 1)
        cell_val.width = Inches(3.6)
        p_v = cell_val.paragraphs[0]
        r_v = p_v.add_run(val)
        set_font(r_v, "Times New Roman", 12, bold=False, color=C_SLATE)

    # Footer
    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_foot.paragraph_format.space_before = Pt(80)
    r_foot = p_foot.add_run("TP. HỒ CHÍ MINH, NĂM 2026")
    set_font(r_foot, "Times New Roman", 12, bold=True, color=C_SLATE)

    # --- NGẮT TRANG SANG LỜI CAM ĐOAN ---
    doc.add_page_break()

    p_cd_title = doc.add_paragraph()
    p_cd_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cd_title.paragraph_format.space_before = Pt(12)
    p_cd_title.paragraph_format.space_after = Pt(18)
    r_cd = p_cd_title.add_run("LỜI CAM ĐOAN")
    set_font(r_cd, "Times New Roman", 16, bold=True, color=C_NAVY)

    pledge_text = [
        "Chúng em xin cam đoan rằng bài báo cáo tiểu luận Giữa kỳ môn Phát triển Ứng dụng Di động với đề tài: \"Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (PAA)\" là công trình nghiên cứu và thực nghiệm hoàn toàn do chính nhóm chúng em thực hiện dưới sự định hướng và hướng dẫn tận tình của Giảng viên hướng dẫn – Thầy Trần Đại Nhân.",
        "Toàn bộ mã nguồn ứng dụng thực nghiệm PAA được nhóm hiện thực hóa độc lập bằng ngôn ngữ Kotlin trên nền tảng Android Studio. Các kết quả đo đạc định lượng về tốc độ khung hình (FPS), tỷ lệ giật khung hình (Jank %), mức độ chiếm dụng CPU và vùng nhớ RAM PSS đều được trích xuất trung thực từ các phiên chạy thực nghiệm trên thiết bị thật và máy ảo.",
        "Các số liệu, biểu đồ và tài liệu tham khảo được trích dẫn trong báo cáo đều có nguồn gốc rõ ràng từ tài liệu chính thức của Google Android Developers, mã nguồn mở AOSP và các công trình khoa học đã được công bố. Chúng em xin chịu hoàn toàn trách nhiệm trước Khoa Công nghệ Thông tin và Nhà trường nếu có bất kỳ sự không trung thực nào về mặt học thuật.",
        "TP. Hồ Chí Minh, ngày 07 tháng 11 năm 2026",
        "Sinh viên thực hiện đề tài"
    ]

    for idx, par in enumerate(pledge_text[:3]):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.first_line_indent = Inches(0.5)
        r = p.add_run(par)
        set_font(r, "Times New Roman", 13, color=C_SLATE)

    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_date.paragraph_format.space_before = Pt(20)
    r_d = p_date.add_run(pledge_text[3])
    set_font(r_d, "Times New Roman", 12, italic=True, color=C_SLATE)

    p_sign_lbl = doc.add_paragraph()
    p_sign_lbl.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sign_lbl.paragraph_format.space_after = Pt(40)
    r_sl = p_sign_lbl.add_run(pledge_text[4] + " (ký và ghi rõ họ tên)")
    set_font(r_sl, "Times New Roman", 12, bold=True, color=C_SLATE)

    # Chữ ký 2 SV
    t_sign = doc.add_table(rows=1, cols=2)
    t_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1 = t_sign.cell(0, 0)
    c1.width = Inches(3.0)
    p_c1 = c1.paragraphs[0]
    p_c1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c1 = p_c1.add_run("Hoàng Thái Đăng Khoa\n(MSSV: 52400017)")
    set_font(r_c1, "Times New Roman", 12, bold=True, color=C_NAVY)

    c2 = t_sign.cell(0, 1)
    c2.width = Inches(3.0)
    p_c2 = c2.paragraphs[0]
    p_c2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_c2 = p_c2.add_run("Đinh Thanh Phong\n(MSSV: 52400027)")
    set_font(r_c2, "Times New Roman", 12, bold=True, color=C_NAVY)

    out_file = os.path.join(OUT_DIR, "00_Trang_Bia_Va_Loi_Cam_Doan.docx")
    doc.save(out_file)
    print("Created:", out_file)

# =========================================================================
# FILE 1: 01_Loi_Cam_On.docx
# =========================================================================
def create_acknowledgement():
    doc = docx.Document()
    apply_tdtu_page_setup(doc)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(20)
    r_t = p_title.add_run("LỜI CẢM ƠN")
    set_font(r_t, "Times New Roman", 16, bold=True, color=C_NAVY)

    paragraphs = [
        "Để hoàn thành được đề tài báo cáo tiểu luận Giữa kỳ môn Phát triển Ứng dụng Di động này, nhóm chúng em đã nhận được sự quan tâm, chỉ dẫn và giúp đỡ vô cùng quý báu từ quý Thầy Cô, gia đình và bạn bè.",
        "Lời đầu tiên, nhóm chúng em xin được bày tỏ lòng biết ơn sâu sắc và chân thành nhất tới Giảng viên hướng dẫn – Thầy Trần Đại Nhân. Trong suốt quá trình học tập và triển khai đề tài, Thầy không chỉ truyền đạt cho chúng em những nền tảng kiến thức vững chắc về lập trình Android, mà còn luôn định hướng cho chúng em tư duy giải quyết vấn đề theo chuẩn mực kỹ thuật công nghiệp, khuyến khích chúng em đào sâu vào nguyên lý hệ điều hành và kiểm chứng mọi luận điểm bằng số liệu thực nghiệm khoa học. Những lời chỉ dẫn quý giá, những câu hỏi phản biện sắc sảo và sự động viên tận tình của Thầy chính là kim chỉ nam giúp chúng em xây dựng thành công ứng dụng PAA và hoàn thành báo cáo này.",
        "Nhóm chúng em cũng xin trân trọng gửi lời cảm ơn tới Ban Giám hiệu Trường Đại học Tôn Đức Thắng cùng toàn thể quý Thầy Cô Khoa Công nghệ Thông tin đã luôn tạo điều kiện học tập tốt nhất, cung cấp cơ sở vật chất hiện đại và xây dựng một môi trường học thuật năng động, sáng tạo để chúng em có cơ hội phát triển năng lực chuyên môn.",
        "Cuối cùng, chúng con xin gửi lời cảm ơn tới gia đình và bạn bè – những người đã luôn là hậu phương vững chắc, chia sẻ và đồng hành cùng chúng em trong suốt quá trình học tập và rèn luyện tại giảng đường đại học.",
        "Mặc dù nhóm đã nỗ lực hết mình để nghiên cứu và hoàn thiện đề tài một cách trọn vẹn nhất, song do thời gian và kinh nghiệm thực tế còn hạn chế, báo cáo chắc chắn không thể tránh khỏi những thiếu sót nhất định. Nhóm chúng em rất mong nhận được những lời nhận xét, góp ý và đánh giá quý báu từ Thầy Trần Đại Nhân để chúng em có thể rút kinh nghiệm, hoàn thiện kiến thức và nâng cao kỹ năng lập trình trong những chặng đường phát triển tiếp theo.",
        "Chúng em xin kính chúc Thầy Trần Đại Nhân luôn dồi dào sức khỏe, hạnh phúc và gặt hái được nhiều thành công hơn nữa trong sự nghiệp giảng dạy và nghiên cứu cao quý!"
    ]

    for par in paragraphs:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.first_line_indent = Inches(0.5)
        r = p.add_run(par)
        set_font(r, "Times New Roman", 13, color=C_SLATE)

    # Ký tên
    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_date.paragraph_format.space_before = Pt(16)
    r_d = p_date.add_run("TP. Hồ Chí Minh, tháng 11 năm 2026\nNhóm sinh viên thực hiện đề tài\n\n\n")
    set_font(r_d, "Times New Roman", 12, italic=True, color=C_SLATE)

    p_names = doc.add_paragraph()
    p_names.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_n = p_names.add_run("Hoàng Thái Đăng Khoa & Đinh Thanh Phong")
    set_font(r_n, "Times New Roman", 12, bold=True, color=C_NAVY)

    out_file = os.path.join(OUT_DIR, "01_Loi_Cam_On.docx")
    doc.save(out_file)
    print("Created:", out_file)

# =========================================================================
# FILE 2: 02_Tom_Tat_Bao_Cao_Abstract.docx
# =========================================================================
def create_abstract():
    doc = docx.Document()
    apply_tdtu_page_setup(doc)

    # --- PHẦN TIẾNG VIỆT ---
    p_title_vn = doc.add_paragraph()
    p_title_vn.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title_vn.paragraph_format.space_before = Pt(10)
    p_title_vn.paragraph_format.space_after = Pt(16)
    r_tvn = p_title_vn.add_run("TÓM TẮT ĐỀ TÀI")
    set_font(r_tvn, "Times New Roman", 16, bold=True, color=C_NAVY)

    paragraphs_vn = [
        "Trong bối cảnh hệ sinh thái Android ngày càng mở rộng với hơn 24.000 mẫu thiết bị di động phân mảnh khốc liệt, bài toán tối ưu hóa hiệu năng ứng dụng (Performance Profiling & Optimization) đã trở thành điều kiện sống còn đối với mọi kỹ sư phần mềm. Một ứng dụng bị gián đoạn trải nghiệm người dùng, xuất hiện hiện tượng giật lag khung hình (UI Jank), treo đơ màn hình (Application Not Responding - ANR) hay rò rỉ bộ nhớ (Memory Leak) không chỉ khiến hơn 48% người dùng gỡ cài đặt trong 24 giờ đầu mà còn trực tiếp bị thuật toán Google Play Android Vitals giáng hạng hiển thị trên kho ứng dụng.",
        "Tiểu luận này tập trung nghiên cứu sâu về nguyên lý vận hành tầng kiến trúc của Android Open Source Project (AOSP), bao gồm: chu kỳ xung nhịp VSYNC 16.67ms của giao diện đồ họa, cơ chế điều phối hàng đợi thông điệp đơn luồng Looper/MessageQueue của Main UI Thread, và giải thuật thu gom rác bộ nhớ (Concurrent Copying Garbage Collection) trên máy ảo Android Runtime (ART).",
        "Trên cơ sở lý thuyết đó, nhóm tác giả đã thiết kế và xây dựng thành công ứng dụng thực nghiệm PAA (Performance Analysis App) bằng ngôn ngữ Kotlin theo kiến trúc Model-View-ViewModel (MVVM). Ứng dụng tích hợp hệ thống đo lường nội bộ thời gian thực độc quyền qua thanh HUD Monitor (Heads-Up Display) đọc trực tiếp từ FrameMetrics API và Debug.MemoryInfo, cho phép tái hiện và kiểm chứng đối chứng A/B giữa phiên bản Chưa tối ưu (BAD) và phiên bản Đã tối ưu (OPTIMIZED) trên cùng một phần cứng.",
        "Kết quả thực nghiệm trên 3 phòng Lab chẩn đoán chuyên sâu mang lại các bước nhảy vọt định lượng rõ rệt: (1) Ở Lab 1, việc tái cấu trúc layout phẳng bằng ConstraintLayout kết hợp nạp ảnh bất đồng bộ qua thư viện Coil giúp tốc độ khung hình tăng vọt +605% (từ 7.8 FPS lên 55.0 FPS), triệt tiêu hoàn toàn 100% tỷ lệ rớt khung hình (Jank từ 99.8% về 0.0%); (2) Ở Lab 2, nâng cấp thuật toán từ O(N²) sang HashMap O(N) kết hợp phân luồng nền bằng Kotlin Coroutines (Dispatchers.Default) giúp rút ngắn thời gian xử lý mảng 30.000 số nguyên hơn 91.9% (từ 1,582 ms xuống 128 ms, và đạt 0 - 3 ms khi có Cache Hit), giải phóng hoàn toàn luồng chính; (3) Ở Lab 3, áp dụng cơ chế tham chiếu yếu WeakReference và quản lý vòng đời onDestroy() đã giúp bộ dọn rác GC thu hồi thành công 19 MB RAM rác và triệt tiêu sạch sẽ 100% (20/20) instance Activity bị rò rỉ.",
        "Đề tài đúc kết thành 5 nguyên tắc vàng trong phát triển ứng dụng di động, đóng góp một công cụ thực nghiệm trực quan và bộ quy chuẩn kỹ thuật thực chiến có giá trị cao cho cộng đồng lập trình viên Android."
    ]

    for par in paragraphs_vn:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Inches(0.5)
        r = p.add_run(par)
        set_font(r, "Times New Roman", 13, color=C_SLATE)

    p_kw_vn = doc.add_paragraph()
    p_kw_vn.paragraph_format.space_before = Pt(6)
    p_kw_vn.paragraph_format.space_after = Pt(18)
    r_k1 = p_kw_vn.add_run("Từ khóa: ")
    set_font(r_k1, "Times New Roman", 13, bold=True, color=C_NAVY)
    r_k2 = p_kw_vn.add_run("Hiệu năng Android, Google Play Vitals, Render Jank, VSYNC 16.67ms, ANR, Rò rỉ bộ nhớ (Memory Leak), ART Heap, Kotlin Coroutines, PAA.")
    set_font(r_k2, "Times New Roman", 13, italic=True, color=C_SLATE)

    # --- NGẮT TRANG SANG PHẦN TIẾNG ANH ---
    doc.add_page_break()

    p_title_en = doc.add_paragraph()
    p_title_en.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title_en.paragraph_format.space_before = Pt(10)
    p_title_en.paragraph_format.space_after = Pt(16)
    r_ten = p_title_en.add_run("ABSTRACT")
    set_font(r_ten, "Times New Roman", 16, bold=True, color=C_NAVY)

    paragraphs_en = [
        "In the rapidly expanding Android ecosystem encompassing over 24,000 fragmented device models, mobile application performance profiling and optimization have become imperative engineering disciplines. Applications exhibiting user experience degradation—such as rendering latency (UI Jank), unresponsive main thread freezes (Application Not Responding - ANR), or memory leaks—suffer severe business penalties, with over 48% of users uninstalling within the first 24 hours, alongside algorithmic search penalties imposed by Google Play Android Vitals thresholds.",
        "This project conducts an in-depth investigation into core Android Open Source Project (AOSP) architectural mechanisms: the 16.67ms VSYNC rendering cadence across the traversal pipeline, the single-threaded Looper/MessageQueue dispatching mechanism on the Main UI Thread, and the Concurrent Copying Garbage Collection heuristics within the Android Runtime (ART) memory heap.",
        "Grounded in this theoretical foundation, the authors engineered the PAA (Performance Analysis App), a standalone diagnostic benchmarking utility built with Kotlin following the Model-View-ViewModel (MVVM) architecture. The application integrates an in-app real-time HUD (Heads-Up Display) profiling monitor powered directly by the hardware FrameMetrics API and Debug.MemoryInfo, enabling deterministic A/B contrast evaluations between unoptimized (BAD) and optimized (OPTIMIZED) implementations on identical runtime environments.",
        "Empirical benchmarks conducted across three specialized laboratories demonstrated substantial quantitative gains: (1) In Lab 1, layout flattening with ConstraintLayout coupled with asynchronous image downsampling via Coil propelled framerates by +605% (from 7.8 FPS to 55.0 FPS) and eliminated 100% of dropped frames (jank dropping from 99.8% to 0.0%); (2) In Lab 2, algorithmic restructuring from O(N²) to HashMap-based O(N) execution scheduled via Kotlin Coroutines (Dispatchers.Default) reduced execution time across 30,000 integers by over 91.9% (from 1,582 ms down to 128 ms, with 0 - 3 ms cache hits), liberating the main UI loop; (3) In Lab 3, lifecycle-bound WeakReference bindings and onDestroy() unregistration enabled ART GC to successfully reclaim 19 MB of leak payload and eradicate 100% (20/20) of leaked activity instances.",
        "The investigation synthesizes five core architectural principles, delivering an empirical benchmarking instrument and a battle-tested technical standard for modern Android software engineering."
    ]

    for par in paragraphs_en:
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Inches(0.5)
        r = p.add_run(par)
        set_font(r, "Times New Roman", 13, color=C_SLATE)

    p_kw_en = doc.add_paragraph()
    p_kw_en.paragraph_format.space_before = Pt(6)
    r_ek1 = p_kw_en.add_run("Keywords: ")
    set_font(r_ek1, "Times New Roman", 13, bold=True, color=C_NAVY)
    r_ek2 = p_kw_en.add_run("Android Performance, Google Play Vitals, Render Jank, VSYNC Cadence, Application Not Responding (ANR), Memory Leakage, ART Garbage Collection, Kotlin Coroutines, PAA.")
    set_font(r_ek2, "Times New Roman", 13, italic=True, color=C_SLATE)

    out_file = os.path.join(OUT_DIR, "02_Tom_Tat_Bao_Cao_Abstract.docx")
    doc.save(out_file)
    print("Created:", out_file)

# =========================================================================
# FILE 3: 03_Danh_Muc_Tu_Viet_Tat_Va_Ky_Hieu.docx
# =========================================================================
def create_abbreviations():
    doc = docx.Document()
    apply_tdtu_page_setup(doc)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(20)
    r_t = p_title.add_run("DANH MỤC CÁC TỪ VIẾT TẮT VÀ THUẬT NGỮ CHUYÊN NGÀNH")
    set_font(r_t, "Times New Roman", 15, bold=True, color=C_NAVY)

    abbreviations = [
        ("AOSP", "Android Open Source Project", "Dự án mã nguồn mở Android do Google dẫn dắt và phát triển."),
        ("ANR", "Application Not Responding", "Lỗi hộp thoại thông báo ứng dụng bị treo, đơ cứng không phản hồi thao tác người dùng quá 5 giây."),
        ("PSS", "Proportional Set Size", "Thước đo dung lượng bộ nhớ RAM thực tế chuẩn của Android, bao gồm RAM riêng và phần chia sẻ tương ứng giữa các tiến trình."),
        ("GC", "Garbage Collection / Garbage Collector", "Cơ chế và bộ thu gom rác tự động giải phóng các đối tượng không còn được sử dụng trong bộ nhớ Heap."),
        ("VSYNC", "Vertical Synchronization", "Tín hiệu đồng bộ hóa khung hình dọc phần cứng, phát nhịp mỗi 16.67ms (trên màn hình 60Hz) để kích hoạt chu trình vẽ khung hình mới."),
        ("FPS", "Frames Per Second", "Tốc độ khung hình trên một giây; chỉ số phản ánh độ mượt mà của giao diện chuyển động (chuẩn Android là 60 FPS)."),
        ("Jank", "UI Jank / Dropped Frame", "Hiện tượng khung hình bị mất nhịp do thời gian xử lý vượt quá ngân sách 16.67ms, gây khựng giật thị giác."),
        ("OOM", "Out of Memory (OutOfMemoryError)", "Lỗi sập ứng dụng nghiêm trọng khi máy ảo ART không còn đủ bộ nhớ Heap để cấp phát cho đối tượng mới."),
        ("HUD", "Heads-Up Display", "Thanh giao diện giám sát bán trong suốt nổi trên đỉnh màn hình, hiển thị liên tục các chỉ số phần cứng thời gian thực."),
        ("ART", "Android Runtime", "Môi trường máy ảo thực thi mã nhị phân ứng dụng (DEX bytecode) trên hệ điều hành Android từ phiên bản 5.0 trở lên."),
        ("MVVM", "Model - View - ViewModel", "Kiến trúc thiết kế phần mềm phân tách rõ ràng giữa Dữ liệu, Giao diện và Logic điều phối trung gian."),
        ("API", "Application Programming Interface", "Giao diện lập trình ứng dụng cung cấp các hàm và dịch vụ để tương tác với hệ thống."),
        ("PAA", "Performance Analysis App", "Ứng dụng thực nghiệm phân tích và tối ưu hóa hiệu năng Android do nhóm tự phát triển."),
        ("CPU", "Central Processing Unit", "Bộ vi xử lý trung tâm của thiết bị di động."),
        ("RAM", "Random Access Memory", "Bộ nhớ truy xuất ngẫu nhiên phục vụ lưu trữ dữ liệu tạm thời của các tiến trình đang hoạt động."),
        ("GC Root", "Garbage Collection Root", "Các điểm neo tham chiếu nền tảng (biến tĩnh static, luồng đang chạy, biến cục bộ) mà GC dùng làm gốc để dò tìm đối tượng sống.")
    ]

    table = doc.add_table(rows=len(abbreviations) + 1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Table Header
    headers = ["Ký hiệu / Từ viết tắt", "Tên tiếng Anh đầy đủ", "Ý nghĩa và Định nghĩa chuyên ngành"]
    widths = [Inches(1.4), Inches(2.2), Inches(3.0)]

    for col_idx, (text, w) in enumerate(zip(headers, widths)):
        cell = table.cell(0, col_idx)
        cell.width = w
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        set_font(r, "Times New Roman", 11, bold=True, color=RGBColor(255, 255, 255))
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="0A4D9E"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    # Table Body
    for row_idx, (abbr, en, desc) in enumerate(abbreviations, start=1):
        row_vals = [abbr, en, desc]
        for col_idx, (val, w) in enumerate(zip(row_vals, widths)):
            cell = table.cell(row_idx, col_idx)
            cell.width = w
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            
            r = p.add_run(val)
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(r, "Times New Roman", 10.5, bold=True, color=C_NAVY)
            elif col_idx == 1:
                set_font(r, "Times New Roman", 10.5, bold=True, color=C_SLATE)
            else:
                set_font(r, "Times New Roman", 10, color=C_SLATE)

            if row_idx % 2 == 0:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
                cell._tc.get_or_add_tcPr().append(shd)

    out_file = os.path.join(OUT_DIR, "03_Danh_Muc_Tu_Viet_Tat_Va_Ky_Hieu.docx")
    doc.save(out_file)
    print("Created:", out_file)

if __name__ == "__main__":
    create_cover_and_pledge()
    create_acknowledgement()
    create_abstract()
    create_abbreviations()
    print("All 4 front-matter docx files have been generated successfully!")
