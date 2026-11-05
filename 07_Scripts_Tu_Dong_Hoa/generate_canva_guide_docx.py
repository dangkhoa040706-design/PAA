# -*- coding: utf-8 -*-
"""
Script tạo file Word: Kich_Ban_Thuyet_Trinh_Canva_PAA.docx
Tài liệu hướng dẫn trực quan & kịch bản thuyết trình Canva cho nhóm Hoàng Thái Đăng Khoa & Đinh Thanh Phong
"""
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def set_cell_background(cell, color_hex):
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_callout(doc, title, text, bg_hex="F0F9FF", border_hex="0A4D9E"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    cell._tc.get_or_add_tcPr().append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(title + "\n")
    run_t.font.name = "Arial"
    run_t.font.size = Pt(11)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(10, 77, 158)
    
    run_b = p.add_run(text)
    run_b.font.name = "Arial"
    run_b.font.size = Pt(10)
    run_b.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def main():
    doc = docx.Document()
    
    # Page setup
    for sec in doc.sections:
        sec.top_margin = Inches(0.8)
        sec.bottom_margin = Inches(0.8)
        sec.left_margin = Inches(0.8)
        sec.right_margin = Inches(0.8)
        
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(4)
    r1 = p_title.add_run("KỊCH BẢN & HƯỚNG DẪN THIẾT KẾ SLIDE CANVA\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(18)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(10, 77, 158) # TDTU Blue
    
    r2 = p_title.add_run("Báo Cáo Giữa Kỳ: Phân Tích & Tối Ưu Hóa Hiệu Năng Ứng Dụng Android (PAA)\n")
    r2.font.name = "Arial"
    r2.font.size = Pt(13)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0, 150, 180)
    
    # Meta box
    add_callout(doc, "THÔNG TIN HỌC PHẦN & ĐỀ TÀI", 
        "• Môn học: Phát triển Ứng dụng Di động - Khoa CNTT - Đại học Tôn Đức Thắng (TDTU)\n"
        "• Sinh viên thực hiện: Hoàng Thái Đăng Khoa (52400017) & Đinh Thanh Phong (52400027)\n"
        "• Giảng viên hướng dẫn: GV: Trần Đại Nhân\n"
        "• Sản phẩm thực nghiệm: Ứng dụng PAA (Performance Analysis App) & Bộ đo HUD Overlay\n"
        "• Thư mục ảnh sẵn sàng tải lên Canva: D:\\MOBI GK\\04_Hinh_Anh_Va_So_Do\\\n",
        bg_hex="F8FAFC", border_hex="0A4D9E")
        
    # Agenda & Role Table
    p_h = doc.add_paragraph()
    r = p_h.add_run("1. BẢNG PHÂN CHIA THỜI GIAN & PHÂN VAI THUYẾT TRÌNH (8 - 10 PHÚT)")
    r.font.name = "Arial"
    r.font.size = Pt(12)
    r.font.bold = True
    r.font.color.rgb = RGBColor(10, 77, 158)
    
    tbl = doc.add_table(rows=9, cols=5)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    headers = ["Slide", "Tên Slide", "Người Thuyết Trình", "Thời Lượng", "Trọng Tâm"]
    widths = [Inches(0.6), Inches(1.8), Inches(1.4), Inches(0.9), Inches(2.2)]
    
    for i, col_w in enumerate(widths):
        tbl.columns[i].width = col_w
        cell = tbl.cell(0, i)
        set_cell_background(cell, "0A4D9E")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(headers[i])
        run.font.name = "Arial"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    data = [
        ("Slide 1", "Trang Bìa (Cover)", "Đăng Khoa", "45 giây", "Chào hỏi, giới thiệu nhóm, đề tài & sản phẩm PAA"),
        ("Slide 2", "Mục lục Báo cáo (Agenda)", "Đăng Khoa", "30 giây", "Tổng quan 4 trụ cột nội dung của buổi báo cáo"),
        ("Slide 3", "Đặt vấn đề & Android Vitals", "Đăng Khoa", "1 phút 30s", "Thống kê 48% gỡ app, chuẩn Vitals & 3 nút thắt"),
        ("Slide 4", "Nguyên lý Tầng sâu AOSP", "Thanh Phong", "2 phút", "VSYNC 16.67ms, Choreographer, Looper ANR, ART Heap"),
        ("Slide 5", "Hiện thực PAA & 3 Phòng Lab", "Thanh Phong", "2 phút", "Kiến trúc HUD Overlay, kịch bản Jank, CPU, Memory"),
        ("Slide 6", "Số liệu Đo đạc Đối chứng", "Thanh Phong", "1 phút 30s", "Bảng đối chứng Before vs After: FPS +224%, CPU x101, RAM -77%"),
        ("Slide 7", "5 Nguyên tắc Vàng (Best Practices)", "Đăng Khoa", "1 phút 15s", "Bộ quy chuẩn thực chiến dành cho lập trình viên"),
        ("Slide 8", "Kết luận & Lời cảm ơn", "Đăng Khoa", "45 giây", "Tổng kết đóng góp, định hướng mở rộng, Q&A"),
    ]
    
    for row_idx, row_data in enumerate(data, start=1):
        bg = "FFFFFF" if row_idx % 2 == 1 else "F1F5F9"
        for col_idx, text in enumerate(row_data):
            cell = tbl.cell(row_idx, col_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            if col_idx in [0, 3]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            run.font.name = "Arial"
            run.font.size = Pt(9)
            if col_idx == 2:
                run.font.bold = True
                run.font.color.rgb = RGBColor(10, 77, 158)
                
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # 8 SLIDES DETAILED BREAKDOWN
    slides_content = [
        {
            "num": 1,
            "title": "TRANG BÌA (COVER SLIDE)",
            "layout": "Khung bo góc Logo TDTU/IT ở trên; Tiêu đề lớn màu trắng; Badge tròn bên trái 'MOBI GK 2026'; Thẻ trắng chứa thông tin nhóm và GVHD; Ảnh nền cơ sở TDTU.",
            "text": "TIÊU ĐỀ CHÍNH:\nPHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID\n\nTIÊU ĐỀ PHỤ:\nNghiên cứu Nguyên lý Tầng sâu AOSP & Thực nghiệm Bộ công cụ PAA (Performance Analysis App)\n\nTHẺ THÔNG TIN TRẮNG:\n• Sinh viên thực hiện:\n  1. Hoàng Thái Đăng Khoa - MSSV: 52400017\n  2. Đinh Thanh Phong       - MSSV: 52400027\n• Giảng viên hướng dẫn:\n  GV: Trần Đại Nhân\n• Bộ môn: Phát triển Ứng dụng Di động - Khoa CNTT",
            "speaker": "Đăng Khoa (45 giây)",
            "speech": "Kính chào Thầy Trần Đại Nhân và toàn thể các bạn sinh viên đang có mặt trong buổi báo cáo ngày hôm nay. Em tên là Hoàng Thái Đăng Khoa, và đồng hành cùng em là bạn Đinh Thanh Phong. Hôm nay, nhóm chúng em xin phép được đại diện nhóm trình bày đề tài Báo cáo Giữa kỳ môn Phát triển Ứng dụng Di động với chủ đề: 'Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (Performance Profiling)' thông qua sản phẩm thực nghiệm là ứng dụng PAA do nhóm tự xây dựng. Sau đây, chúng em xin kính mời Thầy và các bạn cùng bước vào nội dung chi tiết của đề tài."
        },
        {
            "num": 2,
            "title": "MỤC LỤC & TỔNG QUAN NỘI DUNG (AGENDA)",
            "layout": "4 Thẻ chữ nhật bo góc viền xanh/nền trắng theo hàng ngang hoặc lưới 2x2. Mỗi thẻ có đánh số thứ tự 01, 02, 03, 04 và icon công nghệ tương ứng.",
            "text": "01. ĐẶT VẤN ĐỀ & CHUẨN ANDROID VITALS\n• Thực trạng hiệu năng và trải nghiệm người dùng\n• Tiêu chuẩn chất lượng kỹ thuật Google Play Vitals\n• 3 Nút thắt cốt lõi: UI Jank, Nghẽn CPU, Rò rỉ RAM\n\n02. CƠ SỞ LÝ THUYẾT TẦNG SÂU AOSP\n• Pipeline kết xuất đồ họa và nhịp VSYNC 16.67ms\n• Cơ chế xử lý đơn luồng Looper, MessageQueue và ANR\n• Quản lý bộ nhớ ART Heap và ảnh hưởng của Garbage Collection\n\n03. HIỆN THỰC BỘ CÔNG CỤ THỰC NGHIỆM PAA\n• Kiến trúc ứng dụng PAA & HUD Monitor đo thời gian thực\n• Thiết kế 3 Phòng Lab đối chứng: Jank, CPU và Memory\n• So sánh trực tiếp cơ chế: Chưa Tối Ưu (Bad) vs Tối Ưu (Optimized)\n\n04. KẾT QUẢ ĐỐI CHỨNG & BÀI HỌC KINH NGHIỆM\n• Đánh giá số liệu định lượng Before vs After chi tiết\n• Chứng minh khả năng vượt qua kiểm định Android Vitals\n• Đề xuất 5 Nguyên tắc Vàng tối ưu cho Lập trình viên Android",
            "speaker": "Đăng Khoa (30 giây)",
            "speech": "Bài báo cáo của nhóm chúng em được cấu trúc chặt chẽ qua 4 phần chính: Phần 1 phân tích bài toán thực tế và các chỉ số đo lường sống còn theo chuẩn Google Play Vitals. Phần 2 đi sâu vào nguyên lý hệ điều hành AOSP để giải thích tại sao hiện tượng giật lag, treo máy và sập ứng dụng lại xảy ra dưới góc độ kiến trúc máy tính. Phần 3 giới thiệu ứng dụng thực nghiệm PAA - nơi chúng em thiết kế 3 phòng Lab thực chiến mô phỏng trực tiếp cả hai trạng thái Bad và Optimized. Và cuối cùng ở Phần 4, nhóm sẽ công bố bảng số liệu đối chứng định lượng đo được trên thiết bị thật cùng 5 nguyên tắc vàng giúp lập trình viên viết code chuẩn hiệu năng ngay từ đầu."
        },
        {
            "num": 3,
            "title": "ĐẶT VẤN ĐỀ & BÀI TOÁN HIỆU NĂNG (PROBLEM STATEMENT)",
            "layout": "Hộp nổi bật ở trên: Thống kê 48% người dùng gỡ app. 3 Cột bên dưới: 3 Thẻ đỏ nhạt/xanh nhạt đại diện cho 3 vấn đề lớn (Jank, ANR, OOM) với icon cảnh báo.",
            "text": "HỘP THỐNG KÊ:\n'Hơn 48% người dùng gỡ cài đặt nếu ứng dụng phản hồi kém. Google Play sẽ giáng thứ hạng tìm kiếm nếu ứng dụng vượt ngưỡng Bad Behavior (> 0.47% tỷ lệ phiên giật lag).'\n\n1. HIỆN TƯỢNG JANK (GIẬT LAG):\n• Biểu hiện: Cuộn danh sách đứt quãng, hình ảnh giật cục.\n• Nguyên nhân: Quá trình Render vượt quá 16.67ms (mức 60 FPS).\n• Nguy cơ: Khung hình đóng băng (Frozen Frames > 700ms), người dùng mất cảm giác phản hồi mượt mà.\n\n2. NGHẼN CPU & LỖI TREO (ANR):\n• Biểu hiện: Màn hình đơ cứng, hiện hộp thoại 'Ứng dụng không phản hồi'.\n• Nguyên nhân: Thực thi thuật toán nặng trực tiếp trên Main Thread.\n• Nguy cơ: Chặn MessageQueue quá 5 giây kích hoạt cơ chế ANR của hệ thống.\n\n3. RÒ RỈ BỘ NHỚ (OUT OF MEMORY):\n• Biểu hiện: App chạy lâu càng lúc càng chậm, đột ngột bị văng (Crash).\n• Nguyên nhân: Tham chiếu tĩnh (static) giữ Activity đã bị hủy.\n• Nguy cơ: GC dọn dẹp liên tục gây khựng máy (GC Thrashing) và tràn Heap (OOM).",
            "speaker": "Đăng Khoa (1 phút 30 giây)",
            "speech": "Thưa Thầy và các bạn, tại sao hiệu năng lại là yếu tố sống còn của một ứng dụng di động? Theo nghiên cứu của Google và các tổ chức đo lường di động, có tới 48% người dùng sẵn sàng gỡ app chỉ sau lần đầu tiên trải nghiệm nếu gặp tình trạng giật lag. Đặc biệt, Google Play áp dụng chính sách Bad Behavior Threshold - nếu tỷ lệ phiên người dùng bị giật lag vượt quá 0.47%, ứng dụng sẽ bị phạt hạ bậc xếp hạng tìm kiếm. Vấn đề hiệu năng thực chất xoay quanh 3 nút thắt chí tử: Thứ nhất là UI Jank - rớt khung hình khi cuộn lướt. Thứ hai là ANR - ứng dụng bị đóng băng do nghẽn CPU trên luồng chính. Và thứ ba là Rò rỉ bộ nhớ - các biến rác âm thầm tích tụ cho đến khi gây sập ứng dụng vì tràn bộ nhớ OutOfMemory. Để hiểu rõ gốc rễ của 3 nút thắt này, bạn Đinh Thanh Phong sẽ giải trình nguyên lý tầng sâu của hệ điều hành Android ngay sau đây."
        },
        {
            "num": 4,
            "title": "CƠ SỞ LÝ THUYẾT: NGUYÊN LÝ TẦNG SÂU AOSP",
            "layout": "Bên trái: Chèn ảnh sơ đồ '08_diagram_rendering_pipeline.png'. Bên phải: 3 Hộp văn bản tóm tắt nguyên lý (VSYNC 16.67ms, Looper ANR, ART Heap GC).",
            "text": "1. PIPELINE ĐỒ HỌA & NHỊP VSYNC 16.67MS:\n• Tần số quét 60Hz tương ứng ngân sách 16.67ms cho mỗi khung hình (1000ms / 60).\n• Choreographer đồng bộ các giai đoạn: Input Event → Animation → View Traversal (Measure, Layout, Draw) → RenderThread đẩy sang GPU.\n• Nếu Main Thread bận quá 16.67ms → Bỏ lỡ xung VSYNC → Khung hình cũ bị giữ lại, sinh ra hiện tượng Jank.\n\n2. MÔ HÌNH LOOPER - MESSAGEQUEUE & ANR:\n• Main Thread vận hành theo vòng lặp vô tận (Looper) xử lý tuần tự từng thông điệp trong MessageQueue.\n• Thao tác đọc ghi Disk I/O, mạng hoặc thuật toán nặng chạy trên Main Thread sẽ chặn đứng (Block) chuỗi xử lý.\n• Ngưỡng ANR: Khóa tương tác người dùng quá 5 giây hoặc BroadcastReceiver quá 20 giây sẽ xuất hiện hộp thoại cảnh báo hệ thống.\n\n3. QUẢN LÝ BỘ NHỚ ART HEAP & THU GOM RÁC (GC):\n• Android Runtime (ART) phân chia không gian Heap theo thế hệ: Vùng cấp phát mới và Vùng đối tượng sống lâu.\n• Rò rỉ bộ nhớ (Memory Leak) xảy ra khi đối tượng lẽ ra đã chết (Activity đã onDestroy) nhưng vẫn còn đường dẫn kết nối với rễ GC Root (Static Reference, Background Thread).\n• Garbage Collector buộc phải chạy liên tục (GC Thrashing) kèm theo các quãng dừng (Stop-the-world) làm đứng hình giao diện và cạn kiệt bộ nhớ.",
            "speaker": "Thanh Phong (2 phút)",
            "speech": "Xin kính chào Thầy và các bạn, em là Đinh Thanh Phong. Em xin phép được tiếp nối phần trình bày với cơ sở lý thuyết tầng sâu của hệ điều hành Android. Đầu tiên, về đồ họa: Màn hình chuẩn 60Hz phát ra tín hiệu xung nhịp phần cứng VSYNC đều đặn mỗi 16.67ms. Trong đúng khoảng thời gian này, hệ thống phải hoàn thành trọn vẹn chu trình Traversal gồm Measure, Layout và Draw, sau đó đẩy sang RenderThread để gửi lệnh nạp khung hình vào GPU. Chỉ cần một View con lồng ghép quá sâu hoặc nạp ảnh thô quá nặng khiến thời gian tính toán vượt qua 16.67ms, hệ thống sẽ bỏ lỡ nhịp VSYNC và người dùng sẽ thấy ngay một khung hình bị đơ giật. Thứ hai, Android UI là mô hình đơn luồng tuần tự. Mọi thao tác chạm của người dùng đều xếp hàng vào MessageQueue. Nếu lập trình viên vô tình thực thi một vòng lặp nặng hay nạp dữ liệu trên Main Thread, hàng đợi sẽ bị đóng băng. Quá 5 giây không phản hồi, hệ điều hành sẽ kích hoạt cờ ANR. Cuối cùng, cơ chế dọn rác của máy ảo ART. Khi chúng ta khai báo một biến static giữ Activity, Garbage Collector sẽ không thể thu hồi vùng nhớ này vì nó vẫn kết nối tới GC Root. Hậu quả là dung lượng RAM tăng mất kiểm soát, GC phải gồng mình dọn rác liên tục gây ra hiện tượng giật cục và cuối cùng ném ra lỗi OutOfMemory."
        },
        {
            "num": 5,
            "title": "THIẾT KẾ & HIỆN THỰC BỘ CÔNG CỤ PAA",
            "layout": "Bên trái: 2 Ảnh chụp PAA ('01_home.png' và '03_jank_opt.png'). Bên phải: 3 Hộp chi tiết về 3 phòng Lab với công tắc chuyển đổi BAD vs OPTIMIZED.",
            "text": "KIẾN TRÚC PAA & HUD MONITOR THỜI GIAN THỰC:\n• Mô hình MVVM + Kotlin Coroutines + Material Design 3.\n• Tích hợp thanh HUD nổi (Overlay HUD Monitor) bắt trực tiếp xung nhịp qua FrameMetrics API, đo CPU từ /proc/stat và trích xuất RAM PSS thực tế.\n\nLAB 1: KIỂM THỬ GIAO DIỆN & RENDER JANK\n• Kịch bản BAD: Bố cục lồng nhau 6 tầng LinearLayout phức tạp + Nạp ảnh Bitmap thô độ phân giải cao trực tiếp từ bộ nhớ.\n• Kịch bản OPTIMIZED: Làm phẳng giao diện chỉ còn 1 tầng duy nhất với ConstraintLayout + Tích hợp thư viện Glide nạp ảnh bất đồng bộ và tự động scale kích thước.\n\nLAB 2: KIỂM THỬ XỬ LÝ & NGHẼN CPU\n• Kịch bản BAD: Thuật toán BubbleSort O(N^2) sắp xếp 25,000 phần tử chạy trực tiếp trên luồng chính (Main Thread Block).\n• Kịch bản OPTIMIZED: Thuật toán QuickSort O(N log N) được đẩy sang luồng nền thông qua Coroutines với Dispatchers.Default.\n\nLAB 3: KIỂM THỬ RÒ RỈ BỘ NHỚ (LEAK)\n• Kịch bản BAD: Giữ danh sách các Activity instances đã đóng bằng danh sách tĩnh (static companion object) ngăn cản GC.\n• Kịch bản OPTIMIZED: Áp dụng cơ chế tham chiếu yếu (WeakReference), chủ động dọn dẹp biến trong onDestroy và hỗ trợ ép thu hồi rác System.gc().",
            "speaker": "Thanh Phong (2 phút)",
            "speech": "Để chứng minh các lý thuyết trên một cách thực tế và minh bạch nhất, nhóm chúng em đã tự tay xây dựng ứng dụng thực nghiệm PAA - Performance Analysis App. Điểm đặc biệt nhất của PAA là thanh HUD Monitor chạy trực tiếp trên đỉnh màn hình. Thanh HUD này liên tục lắng nghe FrameMetrics API từ hệ điều hành để báo chính xác số FPS thực tế, số khung hình rớt Jank, % CPU sử dụng và lượng RAM chiếm dụng. Ứng dụng cung cấp 3 phòng Lab thực chiến: Ở Lab 1, chúng em cho ứng dụng cuộn danh sách: một bên là layout lồng 6 tầng nạp ảnh thô, và một bên là ConstraintLayout phẳng tối ưu cùng thư viện Glide. Ở Lab 2, chúng em sắp xếp 25.000 phần tử: một bên chạy BubbleSort chặn đứng UI Thread gây đơ cứng màn hình, và một bên dùng QuickSort đẩy sang Coroutines đa luồng. Ở Lab 3, chúng em mô phỏng rò rỉ bộ nhớ bằng cách cố tình giữ 10 Activity trong biến static, sau đó đối chứng với cơ chế tham chiếu yếu WeakReference. Và kết quả đo đạc thực tế trên thiết bị Pixel 7 đã mang lại những con số vô cùng ấn tượng ở slide tiếp theo."
        },
        {
            "num": 6,
            "title": "KẾT QUẢ THỰC NGHIỆM: ĐỐI CHỨNG ĐỊNH LƯỢNG",
            "layout": "Nửa trên: Bảng so sánh 5 cột có màu sắc nổi bật (Đỏ cho Bad, Xanh lá cho Optimized). Nửa dưới: Chèn ảnh biểu đồ cột '11_chart_performance_benchmarks.png'.",
            "text": "BẢNG SỐ LIỆU ĐỐI CHỨNG ĐỊNH LƯỢNG:\n• Tốc độ khung hình (FPS): 17.0 FPS (Bad) → 55.1 FPS (Optimized) | CẢI THIỆN +224.1%\n• Tỷ lệ Rớt Khung hình (Jank): 71.4% (Bad) → 35.7% (Optimized) | GIẢM 50.0%\n• Thời gian Xử lý CPU: 2,022 ms (Bad) → 20 ms (Optimized) | NHANH GẤP 101 LẦN\n• Chiếm dụng RAM (PSS): 88.0 MB (Bad) → 19.8 MB (Optimized) | TIẾT KIỆM 77.5%\n• Đánh giá Google Vitals: KHÔNG ĐẠT (Bad) → VƯỢT CHUẨN GOOGLE (Optimized)\n\nĐÁNH GIÁ CHỈ SỐ KỸ THUẬT NỔI BẬT:\n1. Độ mượt mà (Smoothness): FPS tăng từ 17.0 lên 55.1 FPS, triệt tiêu tình trạng lag giật khi lướt danh sách hình ảnh.\n2. Khả năng phản hồi (Responsiveness): Giải phóng Main Thread hoàn toàn, đưa thời gian tính toán từ 2.02 giây xuống chỉ còn 20 mili-giây, đẩy lùi 100% nguy cơ xảy ra lỗi ANR.\n3. Ổn định tài nguyên (Stability): Cơ chế WeakReference và dọn dẹp Lifecycle triệt tiêu hoàn toàn 10 thể hiện rò rỉ, giúp bộ nhớ PSS giảm mạnh từ 88MB xuống chỉ còn 19.8MB.",
            "speaker": "Thanh Phong (1 phút 30 giây)",
            "speech": "Kính thưa Thầy, đây là bảng số liệu đối chứng thực tế đo đạc trực tiếp trên thiết bị Pixel 7 chạy Android 14: Ở bài toán đồ họa: Bản chưa tối ưu do sử dụng layout lồng quá sâu chỉ đạt 17.0 FPS với tỷ lệ khung hình rớt lên tới 71.4%. Sau khi làm phẳng bố cục bằng ConstraintLayout và kết hợp Glide, tốc độ khung hình tăng vọt lên 55.1 FPS - tức là cải thiện tới 224%, tỷ lệ Jank giảm một nửa, mang lại cảm giác lướt chạm cực kỳ mượt mà. Ở bài toán CPU: Bản chưa tối ưu làm đơ toàn bộ giao diện trong 2.022 giây. Ngược lại, bản tối ưu sử dụng QuickSort trên Coroutines hoàn thành bài toán chỉ trong 20 mili-giây - nhanh gấp hơn 101 lần và giao diện hoàn toàn không hề bị khựng lại dù chỉ 1 frame. Và ở bài toán RAM: Khi chúng em đóng mở 10 màn hình, bản dính rò rỉ bộ nhớ giữ chặt 88 MB RAM. Nhưng bản tối ưu với WeakReference đã tự động giải phóng sạch sẽ các instance, đưa mức chiếm dụng về mức sàn an toàn là 19.8 MB - tiết kiệm tới 77.5% bộ nhớ. Những số liệu này đã chứng minh giải pháp tối ưu của nhóm đạt hiệu quả định lượng rõ rệt."
        },
        {
            "num": 7,
            "title": "5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID",
            "layout": "5 Hộp thẻ chữ nhật bo góc viền xanh/nền sáng được đánh số từ 01 đến 05, mỗi thẻ có biểu tượng icon gợi ý.",
            "text": "01. TUYỆT ĐỐI KHÔNG CHẶN MAIN THREAD\n• Luôn ủy thác mọi tác vụ tính toán nặng, đọc ghi tệp tin, mạng và cơ sở dữ liệu sang Background Threads bằng Kotlin Coroutines (Dispatchers.IO / Dispatchers.Default).\n\n02. LÀM PHẲNG CẤU TRÚC GIAO DIỆN\n• Thay thế toàn bộ các bố cục lồng nhau nhiều tầng bằng ConstraintLayout.\n• Sử dụng ViewStub để trì hoãn nạp các thành phần UI chưa dùng tới và tối ưu hóa ViewHolder trong RecyclerView.\n\n03. QUẢN LÝ VÒNG ĐỜI & CHỐNG RÒ RỈ RAM\n• Tuyệt đối không lưu trữ Activity/Context trong các biến static hoặc Singleton vô thời hạn.\n• Luôn sử dụng WeakReference và hủy bỏ các kết nối listener trong onDestroy().\n\n04. NẠP HÌNH ẢNH THÔNG MINH\n• Sử dụng các thư viện nạp ảnh hiện đại (Glide / Coil) với chuẩn màu Bitmap RGB_565.\n• Tự động nén kích thước ảnh tương thích với kích thước hiển thị thực tế của ImageView.\n\n05. CHỦ ĐỘNG PROFILING ĐỊNH KỲ\n• Định kỳ kiểm tra ứng dụng trước mỗi đợt phát hành bằng Android Studio Profiler, Perfetto và câu lệnh dumpsys gfxinfo để phát hiện sớm các hiện tượng thoái hóa hiệu năng.",
            "speaker": "Đăng Khoa (1 phút 15 giây)",
            "speech": "Thưa Thầy và các bạn, từ quá trình nghiên cứu lý thuyết đến hiện thực bộ công cụ PAA, nhóm chúng em đã đúc kết được 5 nguyên tắc vàng mà bất kỳ lập trình viên Android chuyên nghiệp nào cũng cần khắc cốt ghi tâm: Nguyên tắc số 1: Giữ Main Thread luôn thông thoáng. Mọi tính toán từ đọc ghi file đến gọi API đều phải đưa vào Coroutines. Nguyên tắc số 2: Triệt tiêu thói quen lồng nhiều tầng LinearLayout, hãy làm phẳng giao diện với ConstraintLayout. Nguyên tắc số 3: Tôn trọng vòng đời Activity, nói không với biến static giữ Context để tránh rò rỉ RAM. Nguyên tắc số 4: Không bao giờ nạp ảnh nguyên bản độ phân giải cao lên UI, luôn dùng Glide hoặc Coil để nạp ảnh bất đồng bộ. Và nguyên tắc số 5: Đo đạc trước khi tối ưu hóa - luôn sử dụng Android Profiler để đo lường định lượng thay vì phỏng đoán cảm tính."
        },
        {
            "num": 8,
            "title": "KẾT LUẬN & HƯỚNG PHÁT TRIỂN TIẾP THEO (Q&A)",
            "layout": "Phần trên: 2 Khối Đóng góp đề tài & Hướng mở rộng tương lai. Phần dưới: Lời cảm ơn trang trọng và thông báo phần Q&A.",
            "text": "ĐÓNG GÓP CỦA ĐỀ TÀI:\n• Làm sáng tỏ nguyên lý vận hành tầng sâu của hệ thống Android AOSP (Pipeline Render 16.67ms, Looper ANR, ART Heap GC).\n• Xây dựng thành công ứng dụng thực nghiệm PAA với giao diện trực quan và thanh HUD Monitor giám sát hiệu năng theo thời gian thực.\n• Cung cấp bộ số liệu đối chứng thực tế chứng minh hiệu quả tối ưu hóa vượt bậc (+224% FPS, giảm 101 lần thời gian CPU, tiết kiệm 77% RAM).\n\nHƯỚNG PHÁT TRIỂN TRONG TƯƠNG LAI:\n• Mở rộng bộ phân tích hiệu năng chuyên sâu cho giao diện hiện đại Jetpack Compose (Recomposition tracking).\n• Tự động hóa phát hiện rò rỉ bộ nhớ bằng cách tích hợp thư viện LeakCanary ngay trong ứng dụng PAA.\n• Bổ sung module đo đạc tiêu hao năng lượng pin (Battery Drain) và lưu lượng băng thông mạng (Network Profiling).\n\nLỜI CẢM ƠN & Q&A:\nXIN CHÂN THÀNH CẢM ƠN THẦY TRẦN ĐẠI NHÂN VÀ CÁC BẠN ĐÃ CHÚ Ý THEO DÕI!\nQ&A SESSION - Mời Thầy và các bạn đặt câu hỏi cho nhóm.",
            "speaker": "Đăng Khoa (45 giây)",
            "speech": "Để tổng kết lại, đề tài của nhóm chúng em không chỉ dừng lại ở mặt lý thuyết mà đã hiện thực hóa thành công sản phẩm PAA, mang đến một góc nhìn thực chứng rõ ràng về vai trò của việc tối ưu hóa hiệu năng di động. Trong tương lai, nhóm định hướng sẽ phát triển thêm các module phân tích Recomposition trên Jetpack Compose cũng như tích hợp phân tích tiêu hao pin và mạng. Chúng em xin gửi lời cảm ơn chân thành và sâu sắc nhất đến Giảng viên hướng dẫn - Thầy Trần Đại Nhân, đã tận tình chỉ dẫn và truyền đạt kiến thức cho chúng em trong suốt quá trình học tập môn Phát triển Ứng dụng Di động. Cảm ơn toàn thể các bạn đã chú ý lắng nghe bài thuyết trình của nhóm. Bây giờ, chúng em xin kính mời Thầy và các bạn cùng đặt câu hỏi để nhóm có cơ hội trao đổi và làm rõ hơn về đề tài. Em xin chân thành cảm ơn!"
        }
    ]
    
    for s in slides_content:
        # Heading 2 for each slide
        p_sh = doc.add_paragraph()
        p_sh.paragraph_format.space_before = Pt(14)
        p_sh.paragraph_format.space_after = Pt(4)
        r = p_sh.add_run(f"SLIDE {s['num']}: {s['title']}")
        r.font.name = "Arial"
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = RGBColor(10, 77, 158)
        
        # Details table
        tbl_s = doc.add_table(rows=4, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl_s.columns[0].width = Inches(1.8)
        tbl_s.columns[1].width = Inches(4.7)
        
        row_configs = [
            ("Bố cục Canva đề xuất:", s["layout"], "F8FAFC"),
            ("Nội dung Copy-Paste vào Slide:", s["text"], "FFFFFF"),
            ("Người phụ trách & Thời lượng:", s["speaker"], "F1F5F9"),
            ("Lời thoại thuyết trình (Speaker Notes):", s["speech"], "F0F9FF")
        ]
        
        for r_idx, (label, val, bg_c) in enumerate(row_configs):
            c0 = tbl_s.cell(r_idx, 0)
            c1 = tbl_s.cell(r_idx, 1)
            set_cell_background(c0, "E2E8F0")
            set_cell_background(c1, bg_c)
            set_cell_margins(c0, top=60, bottom=60, left=80, right=80)
            set_cell_margins(c1, top=60, bottom=60, left=80, right=80)
            
            p0 = c0.paragraphs[0]
            run0 = p0.add_run(label)
            run0.font.name = "Arial"
            run0.font.size = Pt(9)
            run0.font.bold = True
            run0.font.color.rgb = RGBColor(15, 23, 42)
            
            p1 = c1.paragraphs[0]
            run1 = p1.add_run(val)
            run1.font.name = "Arial"
            run1.font.size = Pt(9)
            if r_idx == 3:
                run1.font.italic = True
                run1.font.color.rgb = RGBColor(10, 77, 158)
                
        doc.add_paragraph().paragraph_format.space_after = Pt(8)
        
    out_path = r"D:\MOBI GK\02_Slide_Thuyet_Trinh\Kich_Ban_Thuyet_Trinh_Canva_PAA.docx"
    doc.save(out_path)
    print(f"File Word Kịch bản Canva đã được tạo thành công tại: {out_path}")

if __name__ == "__main__":
    main()
