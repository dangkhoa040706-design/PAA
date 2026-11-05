#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động sinh CẨM NANG VẤN ĐÁP BẢO VỆ GIỮA KỲ - ỨNG DỤNG PAA
Dành cho: Hoàng Thái Đăng Khoa (52400017) & Đinh Thanh Phong (52400027)
Môn học: Phát triển ứng dụng di động - GV: Trần Đại Nhân

Nội dung bao gồm:
1. Bảng ánh xạ chi tiết từng vấn đề kỹ thuật vào Slide bài giảng & Số trang slide chính xác.
2. Cây thư mục toàn bộ file code và bảng giải mã tác dụng chi tiết của toàn bộ 41 file Kotlin + XML + Gradle.
3. Phân tích các công nghệ hiện đại "bên ngoài slide" và kịch bản lập luận điểm 10.
4. Bộ 50 câu hỏi vấn đáp chuyên sâu từ cơ bản đến nâng cao, câu hỏi đố và bẫy code.
"""

import os
import sys

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

BASE_DIR = r"D:\MOBI GK"
OUTPUT_DIR = os.path.join(BASE_DIR, "01_Bao_Cao_Nop_Bai")
OUTPUT_DOCX = os.path.join(OUTPUT_DIR, "Cam_Nang_Van_Dap_PAA_TDTU.docx")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Bảng màu chuẩn nhận diện TDTU
HEX_NAVY = "0A4D9E"       # TDTU Blue
HEX_SCARLET = "BC0024"    # PAA Scarlet
HEX_INK = "2A1A1D"        # Text color
HEX_INK_MUTED = "6B5A5D"
HEX_LIGHT_BG = "F8F9FA"   # Table alternate row
HEX_HEADER_BG = "EBF3FC"  # Header row light blue
HEX_BORDER = "CCCCCC"
HEX_OPT = "1A7034"
HEX_BAD = "BC0024"

COLOR_NAVY = RGBColor(10, 77, 158)
COLOR_SCARLET = RGBColor(188, 0, 36)
COLOR_INK = RGBColor(42, 26, 29)
COLOR_INK_MUTED = RGBColor(107, 90, 93)
COLOR_OPT = RGBColor(26, 112, 52)
COLOR_BAD = RGBColor(188, 0, 36)


def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, hex_color=HEX_BORDER):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="{hex_color}"/>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{hex_color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{hex_color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def format_paragraph(p, space_before=0, space_after=6, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing


def add_heading_1(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=16, space_after=8, line_spacing=1.15)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_NAVY
    return p


def add_heading_2(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=12, space_after=6, line_spacing=1.15)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = COLOR_SCARLET
    return p


def add_heading_3(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=8, space_after=4, line_spacing=1.15)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.italic = True
    run.font.color.rgb = COLOR_INK
    return p


def add_body_p(doc, text, bold_prefix="", italic=False, color=COLOR_INK):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=5, line_spacing=1.15)
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = "Times New Roman"
        r_b.font.size = Pt(13)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_NAVY if "Thầy" in bold_prefix or "Câu" in bold_prefix else COLOR_INK
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(13)
    r.font.italic = italic
    r.font.color.rgb = color
    return p


def add_callout(doc, text, bold_title=""):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)

    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F4FA")
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)

    # Viền trái dày màu Navy
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="{HEX_NAVY}"/>'
        f'  <w:top w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

    p = cell.paragraphs[0]
    format_paragraph(p, space_before=0, space_after=0, line_spacing=1.15)
    if bold_title:
        r_b = p.add_run(bold_title + " ")
        r_b.font.name = "Times New Roman"
        r_b.font.size = Pt(12)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_NAVY
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(12)
    r.font.italic = True
    r.font.color.rgb = COLOR_INK

    p_after = doc.add_paragraph()
    format_paragraph(p_after, space_before=0, space_after=4)


def main():
    print("Bắt đầu sinh tài liệu Cẩm nang vấn đáp PAA TDTU...")
    doc = Document()

    # Thiết lập kích thước A4 & lề chuẩn TDTU
    for section in doc.sections:
        section.page_width = Inches(8.27)   # A4 210mm
        section.page_height = Inches(11.69) # A4 297mm
        section.left_margin = Inches(1.18)  # 3.0 cm
        section.right_margin = Inches(0.79) # 2.0 cm
        section.top_margin = Inches(0.79)   # 2.0 cm
        section.bottom_margin = Inches(0.79)# 2.0 cm

    # =========================================================================
    # TRANG TIÊU ĐỀ
    # =========================================================================
    p_uni = doc.add_paragraph()
    format_paragraph(p_uni, space_before=0, space_after=2)
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_uni.add_run("TRƯỜNG ĐẠI HỌC TÔN ĐỨC THẮNG\nKHOA CÔNG NGHỆ THÔNG TIN")
    r_uni.font.name = "Times New Roman"
    r_uni.font.size = Pt(13)
    r_uni.font.bold = True
    r_uni.font.color.rgb = COLOR_NAVY

    p_line = doc.add_paragraph()
    format_paragraph(p_line, space_before=0, space_after=18)
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_line = p_line.add_run("—" * 25)
    r_line.font.color.rgb = COLOR_SCARLET

    p_title = doc.add_paragraph()
    format_paragraph(p_title, space_before=10, space_after=8)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_t1 = p_title.add_run("CẨM NANG VẤN ĐÁP BẢO VỆ GIỮA KỲ\n")
    r_t1.font.name = "Times New Roman"
    r_t1.font.size = Pt(20)
    r_t1.font.bold = True
    r_t1.font.color.rgb = COLOR_SCARLET

    r_t2 = p_title.add_run("ỨNG DỤNG PHÂN TÍCH VÀ TỐI ƯU HIỆU NĂNG ANDROID (PAA)")
    r_t2.font.name = "Times New Roman"
    r_t2.font.size = Pt(16)
    r_t2.font.bold = True
    r_t2.font.color.rgb = COLOR_NAVY

    p_sub = doc.add_paragraph()
    format_paragraph(p_sub, space_before=6, space_after=24)
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Ánh Xạ Lý Thuyết Slide Môn Học, Giải Mã Cây Thư Mục Toàn Bộ 41 File Code\nvà Bộ 50 Câu Hỏi Vấn Đáp Chuyên Sâu Tích Hợp Kịch Bản Điểm 10")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_INK_MUTED

    # Khung tác giả & GVHD
    table_meta = doc.add_table(rows=4, cols=2)
    table_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_meta.autofit = False
    table_meta.columns[0].width = Inches(2.2)
    table_meta.columns[1].width = Inches(4.3)
    meta_data = [
        ("Môn học:", "Phát triển Ứng dụng Di động (Mobile App Development)"),
        ("Giảng viên hướng dẫn:", "Thầy Trần Đại Nhân"),
        ("Nhóm sinh viên thực hiện:", "1. Hoàng Thái Đăng Khoa – MSSV: 52400017\n2. Đinh Thanh Phong – MSSV: 52400027"),
        ("Sản phẩm thực nghiệm:", "Ứng dụng Android PAA (Performance Analysis App)"),
    ]
    for row_idx, (k, v) in enumerate(meta_data):
        row = table_meta.rows[row_idx]
        set_cell_background(row.cells[0], HEX_LIGHT_BG)
        set_cell_background(row.cells[1], "FFFFFF")
        for c in row.cells:
            set_cell_margins(c, top=80, bottom=80, left=120, right=120)

        p0 = row.cells[0].paragraphs[0]
        format_paragraph(p0, space_before=0, space_after=0)
        r0 = p0.add_run(k)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(12)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_NAVY

        p1 = row.cells[1].paragraphs[0]
        format_paragraph(p1, space_before=0, space_after=0)
        r1 = p1.add_run(v)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(12)
        r1.font.bold = (row_idx in [1, 2])
        r1.font.color.rgb = COLOR_INK

    set_table_borders(table_meta)

    doc.add_page_break()

    # =========================================================================
    # PHẦN 1: BẢNG ÁNH XẠ TOÀN DIỆN TỪNG VẤN ĐỀ VÀO SLIDE CỦA THẦY
    # =========================================================================
    add_heading_1(doc, "PHẦN 1: BẢNG ÁNH XẠ TOÀN DIỆN TỪ SLIDE CỦA THẦY VÀO MÃ NGUỒN PAA")

    add_body_p(doc, 
        "Để chuẩn bị cho phần vấn đáp bảo vệ Giữa kỳ đạt kết quả xuất sắc nhất, toàn bộ các module và giải pháp kỹ thuật "
        "trong ứng dụng PAA đều được liên kết trực tiếp tới các bài giảng lý thuyết (Slide) và bài thực hành (Lab) do "
        "Thầy Trần Đại Nhân giảng dạy. Khi thầy đặt câu hỏi về nguồn gốc giải pháp hoặc cơ sở lý thuyết, sinh viên có thể "
        "dẫn chứng chính xác tên slide, số trang và dòng code tương ứng theo bảng dưới đây:")

    # Bảng ánh xạ tổng thể
    map_table = doc.add_table(rows=1, cols=5)
    map_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    map_table.autofit = False
    map_table.columns[0].width = Inches(1.1)
    map_table.columns[1].width = Inches(1.5)
    map_table.columns[2].width = Inches(1.6)
    map_table.columns[3].width = Inches(0.8)
    map_table.columns[4].width = Inches(1.5)

    headers = ["Module PAA", "Vấn đề kỹ thuật", "Slide bài giảng", "Số trang", "Vị trí trong mã nguồn"]
    hdr_row = map_table.rows[0]
    for idx, h in enumerate(headers):
        cell = hdr_row.cells[idx]
        set_cell_background(cell, HEX_NAVY)
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0)
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    mapping_rows = [
        ("Lab 1: UI Jank", "Ngân sách 16.67ms VSYNC & Quy tắc Thread", "8. AsyncTask and AsyncTaskLoader", "Slide 5, 9", "FrameMetricsTracker.kt (L38-40)\nConstants.kt"),
        ("Lab 1: UI Jank", "Cây View lồng sâu vs ConstraintLayout phẳng", "1.3 Graphical User Interfaces", "Slide 7, 20, 37", "item_photo_bad.xml\nitem_photo_good.xml"),
        ("Lab 1: UI Jank", "Cơ chế tái sử dụng View của RecyclerView", "5.3 Recycler View", "Slide 3, 5, 7, 10", "BadPhotoAdapter.kt\nGoodPhotoAdapter.kt"),
        ("Lab 2: CPU Lab", "Khóa Main Thread & Nguy cơ báo lỗi ANR", "8. AsyncTask and AsyncTaskLoader", "Slide 4, 6, 9", "BadCpuTask.kt (L26-42)\nCpuScenario.kt"),
        ("Lab 2: CPU Lab", "Điều phối tác vụ nặng sang Worker Thread", "8. AsyncTask and AsyncTaskLoader", "Slide 8, 9, 11", "GoodCpuTask.kt (L23-25)"),
        ("Lab 3: Memory", "Vòng đời Activity & Sự kiện onDestroy()", "2.2 Activity lifecycle and state", "Slide 7, 9, 24, 25", "LeakyActivity.kt (L76-90)\nLeakHolder.kt"),
        ("Lab 3: Memory", "Truyền tham số kiểm thử bằng Intent Extra", "6. Activities and Intents", "Slide 4, 15, 17", "MemoryScenario.kt (L67-72)\nLeakyActivity.kt"),
        ("Lưu trữ số liệu", "Lưu trữ nội bộ vào Internal Storage", "7.1. Storing Data", "Slide 5, 8, 13, 14", "JsonResultStore.kt (L11-12)"),
        ("Xuất báo cáo", "Chia sẻ file qua FileProvider", "7.3. Content Providers", "Slide 3, 6, 9", "AndroidManifest.xml\nExporter.kt (L47-60)"),
        ("Thực hành Lab", "Layout, RecyclerView, File, Thread", "Lab 02, 04, 06, 08", "Toàn bộ bài Lab", "Giao diện, Adapter, Lưu file, Luồng nền")
    ]

    for row_idx, r_data in enumerate(mapping_rows):
        row = map_table.add_row()
        bg_color = HEX_LIGHT_BG if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            r.font.color.rgb = COLOR_INK
            if c_idx == 0:
                r.font.bold = True

    set_table_borders(map_table)

    # Phân tích sâu 4 nhóm kiến thức
    add_heading_2(doc, "1.1. Chi tiết Ánh Xạ Phòng Lab 1: UI Jank Lab")
    add_body_p(doc, 
        "• Cơ sở lý thuyết ngân sách 16.67ms (Slide 5, Bài 8): Màn hình điện thoại làm tươi 60 lần/giây (60Hz). "
        "Mỗi khung hình chỉ có đúng 1000ms / 60 = 16.67ms để thực hiện toàn bộ chuỗi Measure -> Layout -> Draw. "
        "Nếu Main Thread xử lý quá 16.67ms, màn hình sẽ bị đóng băng (Frame Drop), gây hiện tượng khựng giật (Jank). "
        "Trong FrameMetricsTracker.kt (dòng 38-40), nhóm đã lập trình chính xác công thức này để đếm số jankCount.\n"
        "• Cây View phân cấp lồng nhau (Slide 7, 20 & 37, Bài 1.3): LinearLayout và RelativeLayout khi bị lồng nhiều tầng "
        "(item_photo_bad.xml lồng 6 tầng) sẽ kích hoạt thuật toán tính toán kích thước đệ quy cấp số nhân (Exponential Measure Pass), "
        "làm RenderThread quá tải. Giải pháp ở item_photo_good.xml là dùng ConstraintLayout phẳng 1 tầng đúng theo định nghĩa "
        "ở Slide 37: 'create large and complex layouts with a flat view hierarchy'.\n"
        "• Cơ chế ViewHolder (Slide 7-11, Bài 5.3): Slide nêu rõ ViewHolder dùng để tái sử dụng View đã cuộn qua. "
        "Trong BadPhotoAdapter.kt, nhóm cố tình nạp ảnh Bitmap nặng đồng bộ trong onBindViewHolder(), vi phạm nguyên tắc "
        "giữ hàm bind thật nhẹ. Bản GoodPhotoAdapter.kt giải quyết triệt để bằng cách đẩy việc nạp ảnh sang Coil ngoài luồng nền.")

    add_heading_2(doc, "1.2. Chi tiết Ánh Xạ Phòng Lab 2: CPU Computation Lab")
    add_body_p(doc, 
        "• Chặn đứng Main Thread & Hiểm họa ANR (Slide 4 & Slide 6, Bài 8): Slide 4 nêu rõ toàn bộ UI chạy trên 'main' thread. "
        "Slide 6 cảnh báo: 'If the UI waits too long for an operation to finish, it becomes unresponsive. The framework shows "
        "an Application Not Responding (ANR) dialog'. Trong BadCpuTask.kt, thuật toán đếm trùng O(N^2) với 30.000 số chạy thẳng "
        "trên Main Thread làm đóng băng MessageQueue trong ~2.5 giây.\n"
        "• Mô hình Worker Thread (Slide 8 & 11, Bài 8): Slide chỉ ra rằng mọi tác vụ tính toán dài hơi phải chuyển sang "
        "Worker Thread. Trong GoodCpuTask.kt, nhóm đã điều phối sang luồng Worker qua Coroutines Dispatchers.Default, "
        "đồng thời tối ưu thuật toán sang HashMap với độ phức tạp tuyến tính O(N), giải quyết bài toán chỉ trong vài mili-giây.")

    add_heading_2(doc, "1.3. Chi tiết Ánh Xạ Phòng Lab 3: Memory Leak Lab")
    add_body_p(doc, 
        "• Chu trình sống Activity & Sự kiện onDestroy() (Slide 7 & 24, Bài 2.2): Slide 24 định nghĩa onDestroy() là 'Final call "
        "before Activity is destroyed'. Trong LeakyActivity.kt, khi gọi finish(), Activity đi vào onDestroy(). Nhưng do "
        "LeakHolder.leakyActivities giữ một tham chiếu mạnh (Strong Reference) tĩnh (static), Garbage Collector (GC) của ART "
        "xem đây là một GC Root còn sống và KHÔNG THỂ THU HỒI đối tượng, dẫn đến rò rỉ 5MB RAM mỗi lần mở màn hình.\n"
        "• Giải pháp WeakReference & Dọn dẹp callback (Slide 25, Bài 2.2): Ở bản tối ưu, nhóm sử dụng WeakReference "
        "cho phép GC tự do dọn dẹp đối tượng, đồng thời trong onDestroy() chủ động hủy Handler.removeCallbacks() và gán "
        "dummyPayload = null để giải phóng bộ nhớ ngay lập tức.")

    add_heading_2(doc, "1.4. Chi tiết Ánh Xạ Lưu Trữ & Bài Tập Thực Hành")
    add_body_p(doc, 
        "• Lưu trữ nội bộ (Slide 5 & 13, Bài 7.1): Áp dụng hàm getFilesDir() để lưu kết quả đo vào Internal Storage dưới dạng "
        "file results.json an toàn, bảo mật và tự động xóa khi gỡ ứng dụng.\n"
        "• Bài tập thực hành trên lớp: Kế thừa trực tiếp kỹ năng thiết kế layout từ Lab 02, kỹ thuật RecyclerView từ Lab 04, "
        "kỹ thuật đọc/ghi file từ Lab 06, và tư duy đa luồng từ Lab 08.")

    doc.add_page_break()

    # =========================================================================
    # PHẦN 2: CÂY THƯ MỤC TOÀN BỘ FILE CODE VÀ BẢNG GIẢI MÃ TÁC DỤNG TỪNG FILE
    # =========================================================================
    add_heading_1(doc, "PHẦN 2: CÂY THƯ MỤC TOÀN BỘ FILE CODE & GIẢI MÃ TÁC DỤNG TỪNG FILE")

    add_body_p(doc, 
        "Mã nguồn ứng dụng PAA được tổ chức theo cấu trúc phân tầng kiến trúc MVVM (Model - View - ViewModel) sạch sẽ, "
        "phân tách rõ ràng giữa tầng dữ liệu (data), tầng đo lường hiệu năng (metrics), tầng kịch bản tự động (scenario), "
        "tầng giao diện (ui) và tầng tiện ích (util). Dưới đây là cây thư mục toàn bộ mã nguồn cùng bảng giải mã chi tiết "
        "tác dụng của 41 file Kotlin và các file tài nguyên liên quan:")

    # Sơ đồ ASCII Tree
    tree_text = (
        "PAA/\n"
        "├── app/\n"
        "│   ├── src/main/AndroidManifest.xml                  [Khai báo Activity, Provider, Profileable]\n"
        "│   ├── src/main/java/com/nhomx/paa/\n"
        "│   │   ├── MainActivity.kt                          [Host Activity chứa fragmentContainer & overlay]\n"
        "│   │   ├── PaaApplication.kt                        [Khởi tạo ứng dụng & cấu hình StrictMode]\n"
        "│   │   ├── core/                                    [Các định nghĩa và hằng số cốt lõi]\n"
        "│   │   │   ├── Constants.kt                         [Tham số chuẩn: 500 item, 50k số, 20 loop]\n"
        "│   │   │   ├── Module.kt                            [Enum: JANK, CPU, MEMORY]\n"
        "│   │   │   └── Variant.kt                           [Enum: BAD, OPTIMIZED]\n"
        "│   │   ├── data/                                    [Tầng truy xuất và lưu trữ dữ liệu]\n"
        "│   │   │   ├── AssetLoader.kt                       [Đọc items.json và cpu_data.csv từ assets]\n"
        "│   │   │   ├── MeasurementResult.kt                 [Data model kết quả đo kèm toJson / fromJson]\n"
        "│   │   │   ├── PhotoItem.kt                         [Data model một item ảnh trong danh sách]\n"
        "│   │   │   ├── ResultStore.kt                       [Interface kho lưu trữ kết quả đo]\n"
        "│   │   │   └── JsonResultStore.kt                   [Cài đặt lưu kết quả vào file results.json]\n"
        "│   │   ├── metrics/                                 [Hạt nhân thu thập chỉ số phần cứng & khung hình]\n"
        "│   │   │   ├── CpuSampler.kt                        [Đo % CPU tiến trình chuẩn hóa theo số nhân]\n"
        "│   │   │   ├── FrameMetricsTracker.kt               [Đo thời gian vẽ từng frame qua FrameMetrics API]\n"
        "│   │   │   ├── MemorySampler.kt                     [Đo RAM PSS thực tế và ART Heap (MB)]\n"
        "│   │   │   ├── MetricsCollector.kt                  [Điều phối lấy mẫu định kỳ 500ms qua Coroutines]\n"
        "│   │   │   ├── MetricsSnapshot.kt                   [Data model snapshot tức thời: FPS, Jank, RAM, CPU]\n"
        "│   │   │   └── Stats.kt                             [Hàm toán học: mean, percentile P50/P95, % cải thiện]\n"
        "│   │   ├── scenario/                                [Kịch bản thực nghiệm đo lường tự động]\n"
        "│   │   │   ├── ScenarioRunner.kt                    [Lớp trừu tượng quản lý trạng thái ScenarioState]\n"
        "│   │   │   ├── JankScenario.kt                      [Tự động cuộn 500 item x 3 lượt đo độ mượt]\n"
        "│   │   │   ├── CpuScenario.kt                       [Đo thời gian thực thi đối chứng O(N²) vs O(N)]\n"
        "│   │   │   └── MemoryScenario.kt                    [Tự động mở/đóng 10 màn hình đo rò rỉ RAM]\n"
        "│   │   ├── ui/                                      [Giao diện người dùng theo chuẩn MVVM]\n"
        "│   │   │   ├── home/HomeFragment.kt                 [Màn hình Dashboard chính dẫn vào 3 Lab]\n"
        "│   │   │   ├── jank/                                [Phòng Lab 1: Giật lag giao diện]\n"
        "│   │   │   │   ├── BadPhotoAdapter.kt               [Adapter chưa tối ưu: nạp ảnh đè Main Thread]\n"
        "│   │   │   │   ├── GoodPhotoAdapter.kt              [Adapter tối ưu: ListAdapter + DiffUtil + Coil]\n"
        "│   │   │   │   ├── PhotoDiffCallback.kt             [Thuật toán DiffUtil so sánh thay đổi item]\n"
        "│   │   │   │   ├── JankViewModel.kt                 [Quản lý trạng thái và danh sách ảnh]\n"
        "│   │   │   │   └── JankFragment.kt                  [Giao diện điều khiển Lab 1 & công tắc Bad/Opt]\n"
        "│   │   │   ├── cpu/                                 [Phòng Lab 2: Nghẽn CPU & ANR]\n"
        "│   │   │   │   ├── BadCpuTask.kt                    [Thuật toán O(N²) chạy trên Main Thread]\n"
        "│   │   │   │   ├── GoodCpuTask.kt                   [Thuật toán O(N) HashMap + Worker Thread + Cache]\n"
        "│   │   │   │   ├── CpuResult.kt                     [Data model kết quả đếm trùng và thời gian ms]\n"
        "│   │   │   │   ├── CpuViewModel.kt                  [Quản lý dữ liệu 10k/30k/50k số và kết quả CPU]\n"
        "│   │   │   │   └── CpuFragment.kt                   [Giao diện điều khiển Lab 2 & bảng xác minh đáp số]\n"
        "│   │   │   ├── memory/                              [Phòng Lab 3: Rò rỉ bộ nhớ Memory Leak]\n"
        "│   │   │   │   ├── LeakHolder.kt                    [Singleton giữ static reference mô phỏng rò rỉ]\n"
        "│   │   │   │   ├── LeakyActivity.kt                 [Màn hình thực nghiệm cấp phát 5MB RAM tự đóng]\n"
        "│   │   │   │   ├── MemoryViewModel.kt               [Quản lý trạng thái đo bộ nhớ]\n"
        "│   │   │   │   └── MemoryFragment.kt                [Giao diện điều khiển Lab 3 & nút kích hoạt GC]\n"
        "│   │   │   ├── overlay/MetricsOverlayView.kt        [Thanh HUD Monitor nổi thời gian thực đổi màu cảnh báo]\n"
        "│   │   │   └── results/                             [Màn hình tổng hợp và đối chứng định lượng]\n"
        "│   │   │       ├── ResultAdapter.kt                 [Hiển thị danh sách lịch sử các lần đo]\n"
        "│   │   │       ├── ResultsViewModel.kt              [Tính toán bảng so sánh Bad vs Opt & % cải thiện]\n"
        "│   │   │       └── ResultsFragment.kt               [Giao diện bảng so sánh, lọc module & xuất CSV]\n"
        "│   │   └── util/                                    [Tiện ích hệ thống]\n"
        "│   │       ├── DeviceInfo.kt                        [Trích xuất model máy, Android OS, RAM GB, Hz]\n"
        "│   │       └── Exporter.kt                          [Xuất file CSV chuẩn mẫu Excel qua FileProvider]\n"
        "│   └── src/test/java/com/nhomx/paa/StatsTest.kt     [Unit test kiểm chứng thuật toán toán học]\n"
        "└── build.gradle.kts / settings.gradle.kts           [Cấu hình Gradle root và phiên bản thư viện]"
    )

    p_tree = doc.add_paragraph()
    format_paragraph(p_tree, space_before=4, space_after=12)
    r_tr = p_tree.add_run(tree_text)
    r_tr.font.name = "Consolas"
    r_tr.font.size = Pt(9.5)
    r_tr.font.color.rgb = COLOR_INK

    add_heading_2(doc, "2.1. Bảng Giải Mã Chi Tiết Tác Dụng Của Toàn Bộ File Mã Nguồn")

    code_table = doc.add_table(rows=1, cols=4)
    code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    code_table.autofit = False
    code_table.columns[0].width = Inches(1.8)
    code_table.columns[1].width = Inches(1.1)
    code_table.columns[2].width = Inches(2.4)
    code_table.columns[3].width = Inches(1.2)

    headers_c = ["Tên File", "Gói (Package)", "Mục đích & Tác dụng chính", "Liên kết chính"]
    hdr_c = code_table.rows[0]
    for idx, h in enumerate(headers_c):
        cell = hdr_c.cells[idx]
        set_cell_background(cell, HEX_NAVY)
        set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0)
        r = p.add_run(h)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    files_data = [
        ("MainActivity.kt", "root", "Host Activity duy nhất chứa fragmentContainer điều hướng và overlayContainer chứa HUD Monitor nổi.", "HomeFragment, Overlay"),
        ("PaaApplication.kt", "root", "Khởi tạo app, thiết lập StrictMode ở bản debug để bắt vi phạm I/O đĩa/mạng trên Main Thread.", "Application, StrictMode"),
        ("Constants.kt", "core", "Lưu trữ hằng số dùng chung toàn app: số lượng item (500), số nguyên CPU (50k), chu kỳ leak (20).", "Toàn bộ app"),
        ("Module.kt", "core", "Enum định danh 3 phòng thí nghiệm: JANK, CPU, MEMORY.", "Results, Fragments"),
        ("Variant.kt", "core", "Enum xác định chế độ kiểm thử: BAD (có lỗi) hoặc OPTIMIZED (đã sửa).", "Adapters, Tasks, Scenarios"),
        ("PhotoItem.kt", "data", "Data class đại diện cho 1 phần tử ảnh trong danh sách: id, title, description, imageName.", "AssetLoader, Adapters"),
        ("MeasurementResult.kt", "data", "Data model kết quả đo chứa toàn bộ chỉ số định lượng; có hàm toJson() và fromJson().", "ResultStore, Exporter"),
        ("ResultStore.kt", "data", "Interface trừu tượng hóa kho dữ liệu: add, getAll, getByModule, delete, clear.", "JsonResultStore"),
        ("JsonResultStore.kt", "data", "Cài đặt ResultStore: đọc/ghi file results.json trong context.filesDir bằng org.json trên Dispatchers.IO.", "ViewModels"),
        ("AssetLoader.kt", "data", "Đọc file assets: nạp danh sách 500 ảnh từ items.json và mảng 50.000 số nguyên từ cpu_data.csv.", "Jank & Cpu ViewModel"),
        ("Stats.kt", "metrics", "Thư viện toán học: tính trung bình cộng, phân vị P50/P90/P95/P99 và % cải thiện hiệu năng.", "Metrics, Results"),
        ("MetricsSnapshot.kt", "metrics", "Data model chứa ảnh chụp chỉ số thời gian thực: fps, jankPercent, ramMb, cpuPercent.", "Overlay, Collector"),
        ("CpuSampler.kt", "metrics", "Đo thời gian CPU qua Process.getElapsedCpuTime() chia cho số nhân phần hardware.", "MetricsCollector"),
        ("MemorySampler.kt", "metrics", "Đo dung lượng RAM thực tế PSS qua Debug.MemoryInfo() và ART Java Heap.", "MetricsCollector, MemoryLab"),
        ("FrameMetricsTracker.kt", "metrics", "Lắng nghe OnFrameMetricsAvailableListener trên HandlerThread ngầm, đếm frame vượt 16.67ms.", "Collector, Scenarios"),
        ("MetricsCollector.kt", "metrics", "Điều phối lấy mẫu định kỳ 500ms bằng Coroutines, phát tín hiệu StateFlow lên HUD Overlay.", "3 Fragments"),
        ("ScenarioRunner.kt", "scenario", "Lớp trừu tượng quản lý vòng đời kịch bản đo tự động qua ScenarioState (Running, Finished).", "3 Scenarios"),
        ("JankScenario.kt", "scenario", "Tự động cuộn danh sách 500 phần tử qua lại 3 lượt liên tục với vận tốc cố định để đo FrameMetrics.", "JankFragment"),
        ("CpuScenario.kt", "scenario", "Đo thời gian thực thi thuật toán tìm phần tử trùng lặp trên mảng số nguyên giữa Bad và Opt.", "CpuFragment"),
        ("MemoryScenario.kt", "scenario", "Tự động mở/đóng LeakyActivity 10-20 lần, ép chạy System.gc() và lấy mẫu RAM PSS sau cùng.", "MemoryFragment"),
        ("HomeFragment.kt", "ui.home", "Dashboard chính hiển thị cấu hình phần cứng thiết bị và 3 thẻ điều hướng tới 3 phòng Lab.", "MainActivity"),
        ("BadPhotoAdapter.kt", "ui.jank", "Adapter cố ý gây lag: decode Bitmap thô trên Main Thread, cộng chuỗi nặng, gọi notifyDataSetChanged.", "JankFragment"),
        ("GoodPhotoAdapter.kt", "ui.jank", "Adapter tối ưu: kế thừa ListAdapter + DiffUtil, tải ảnh bất đồng bộ và downsample bằng Coil.", "JankFragment"),
        ("PhotoDiffCallback.kt", "ui.jank", "Cài đặt DiffUtil so sánh id và content của 2 item PhotoItem để tối ưu cập nhật danh sách.", "GoodPhotoAdapter"),
        ("JankViewModel.kt", "ui.jank", "Quản lý dữ liệu danh sách ảnh và trạng thái công tắc BAD/OPTIMIZED trong Lab 1.", "JankFragment"),
        ("JankFragment.kt", "ui.jank", "Màn hình giao diện Lab 1: điều khiển kịch bản cuộn tự động và hiển thị bảng kết quả FPS/Jank/P95.", "MainActivity, Scenarios"),
        ("BadCpuTask.kt", "ui.cpu", "Thuật toán ngây thơ 2 vòng lặp O(N²) quét mảng tìm trùng, chạy thẳng trên luồng chính gây đơ UI.", "CpuScenario"),
        ("GoodCpuTask.kt", "ui.cpu", "Thuật toán tối ưu dùng HashMap O(N) chạy trên Worker Thread Coroutines kết hợp bộ nhớ đệm Cache.", "CpuScenario"),
        ("CpuResult.kt", "ui.cpu", "Data model kết quả đầu ra bài toán CPU: số lượng trùng, tổng các số trùng và thời gian ms.", "CpuTasks, ViewModel"),
        ("CpuViewModel.kt", "ui.cpu", "Quản lý dữ liệu 10k/30k/50k số, nạp dữ liệu nền và lưu trữ kết quả đo CPU.", "CpuFragment"),
        ("CpuFragment.kt", "ui.cpu", "Giao diện Lab 2: chọn kích thước dữ liệu, công tắc Bad/Opt và bảng xác minh đáp số thuật toán.", "MainActivity"),
        ("LeakHolder.kt", "ui.memory", "Singleton lưu trữ static ArrayList giữ tham chiếu mạnh gây rò rỉ RAM (Bad) và WeakReference (Opt).", "LeakyActivity"),
        ("LeakyActivity.kt", "ui.memory", "Màn hình kiểm thử: cấp phát 5MB RAM, đăng ký listener/handler chạy ngầm, tự động đóng sau 350ms.", "MemoryScenario"),
        ("MemoryViewModel.kt", "ui.memory", "Quản lý trạng thái đo lường và lưu trữ kết quả của phòng Lab 3.", "MemoryFragment"),
        ("MemoryFragment.kt", "ui.memory", "Giao diện Lab 3: hiển thị đồng hồ RAM PSS, nút ép dọn rác System.gc() và số lượng instance bị leak.", "MainActivity"),
        ("MetricsOverlayView.kt", "ui.overlay", "Thanh HUD Monitor nổi trên cùng hiển thị FPS, Jank, RAM, CPU; đổi màu chỉ thị xanh/vàng/đỏ.", "MainActivity, 3 Labs"),
        ("ResultAdapter.kt", "ui.results", "Adapter hiển thị danh sách các lần đo đã lưu kèm badge màu và nút xóa bản ghi.", "ResultsFragment"),
        ("ResultsViewModel.kt", "ui.results", "Tính toán bảng đối đầu định lượng: giá trị trung bình Bad vs Opt và % cải thiện hiệu năng.", "ResultsFragment"),
        ("ResultsFragment.kt", "ui.results", "Màn hình kết quả: hiển thị bảng so sánh trực quan, lọc theo module, xuất CSV và xóa lịch sử.", "MainActivity"),
        ("DeviceInfo.kt", "util", "Trích xuất thông số phần cứng: Model máy, phiên bản Android OS, dung lượng RAM GB và tần số quét Hz.", "Home, Scenarios"),
        ("Exporter.kt", "util", "Tạo file CSV định dạng chuẩn mẫu Excel của trường và mở hộp thoại chia sẻ FileProvider.", "ResultsFragment"),
        ("StatsTest.kt", "test", "Unit test kiểm tra tính chính xác của các hàm toán học: mean, percentile P50/P90, improvementPercent.", "JUnit Runner")
    ]

    for row_idx, r_data in enumerate(files_data):
        row = code_table.add_row()
        bg_color = HEX_LIGHT_BG if row_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(r_data):
            cell = row.cells[c_idx]
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)
            r.font.color.rgb = COLOR_INK
            if c_idx == 0:
                r.font.bold = True
                r.font.color.rgb = COLOR_NAVY

    set_table_borders(code_table)

    doc.add_page_break()

    # =========================================================================
    # PHẦN 3: PHÂN TÍCH CÔNG NGHỆ HIỆN ĐẠI BÊN NGOÀI SLIDE & KỊCH BẢN BẢO VỆ
    # =========================================================================
    add_heading_1(doc, "PHẦN 3: CÁC CÔNG NGHỆ HIỆN ĐẠI BÊN NGOÀI SLIDE & KỊCH BẢN LẬP LUẬN ĐIỂM 10")

    add_body_p(doc, 
        "Hệ thống slide bài giảng của môn học dựa trên tài liệu chuẩn Android Developer Fundamentals V2 của Google từ thời "
        "kỳ Android 8-9 (dùng Java và các API truyền thống). Trong dự án PAA, nhóm đã chủ động nâng cấp lên các tiêu chuẩn "
        "Modern Android Development (MAD) năm 2024. Đây là các điểm sáng giá thể hiện tinh thần tự nghiên cứu và cập nhật công nghệ. "
        "Dưới đây là 6 công nghệ nằm ngoài slide cơ bản và kịch bản lập luận hoàn hảo trước Hội đồng chấm thi:")

    tech_list = [
        ("1. Sử dụng Kotlin Coroutines thay thế AsyncTask (Bài 8)",
         "AsyncTask", "Kotlin Coroutines (Dispatchers.Default, Dispatchers.Main, Dispatchers.IO)",
         "Trong Slide bài 8, Google hướng dẫn dùng AsyncTask để chia tách Main Thread và Worker Thread. "
         "Tuy nhiên, kể từ Android 11 (API 30), Google đã chính thức khai tử (deprecated) AsyncTask do class này "
         "rất dễ gây ra rò rỉ bộ nhớ (Memory Leak ngầm giữ tham chiếu Activity) và không tương thích tốt với chu trình sống hiện đại. "
         "Google khuyến nghị chuyển toàn bộ sang Kotlin Coroutines. Nhóm em đã áp dụng nguyên lý chia tách luồng của bài 8 "
         "nhưng triển khai bằng Coroutines để đảm bảo code an toàn, hiện đại và không bị cảnh báo lỗi thời."),

        ("2. Sử dụng ListAdapter & DiffUtil thay thế RecyclerView.Adapter thuần (Bài 5.3)",
         "RecyclerView.Adapter + notifyDataSetChanged()", "ListAdapter<T, VH> + DiffUtil.ItemCallback",
         "Ở Slide bài 5.3, khi dữ liệu thay đổi, cách gọi truyền thống notifyDataSetChanged() sẽ ép RecyclerView phải vẽ lại "
         "toàn bộ danh sách 500 phần tử, gây lãng phí chu kỳ CPU cực lớn và giật lag màn hình. "
         "Nhóm em đã tích hợp ListAdapter và thuật toán DiffUtil (dựa trên giải thuật phân rã của Eugene Myers). "
         "DiffUtil tự động chạy ngầm trên Background Thread để so sánh hai danh sách và chỉ phát lệnh cập nhật đúng các item "
         "thực sự có sự thay đổi (ItemAnimator), triệt tiêu hoàn toàn hiện tượng vẽ lại dư thừa."),

        ("3. Sử dụng ViewBinding thay thế findViewById() (Bài 1.3 & 5.3)",
         "findViewById(R.id.xxx)", "ViewBinding (ActivityMainBinding, ItemPhotoGoodBinding)",
         "Cơ chế findViewById() truyền thống phải duyệt toàn bộ cây View từ gốc (Tree Traversal), gây tốn kém thời gian "
         "và tiềm ẩn nguy cơ văng ứng dụng do NullPointerException nếu truyền sai ID. "
         "ViewBinding là tính năng chính thức của Android Gradle Plugin: tự động sinh ra các binding class có tính an toàn kiểu "
         "(Type safety) và an toàn rỗng (Null safety), đồng thời truy xuất trực tiếp các thành phần giao diện với độ phức tạp O(1)."),

        ("4. Tích hợp Thư viện Coil nạp ảnh bất đồng bộ (Lab 1)",
         "BitmapFactory.decodeStream() thủ công", "io.coil-kt:coil (ivPhotoGood.load)",
         "Việc giải mã ảnh Bitmap thô từ bộ nhớ đòi hỏi kỹ thuật Downsampling và quản lý bộ nhớ đệm đa tầng (Memory Cache & Disk Cache) "
         "rất phức tạp. Nếu tự viết code nạp ảnh trên Main Thread như ở bản BAD sẽ ngay lập tức gây lag khung hình. "
         "Nhóm đã tích hợp Coil – thư viện nạp ảnh hiện đại nhất được viết 100% bằng Kotlin và Coroutines do Google khuyên dùng, "
         "tự động co dãn ảnh theo đúng pixel hiển thị của ShapeableImageView, tiết kiệm hơn 80% RAM."),

        ("5. Khai thác FrameMetrics API đo lường chuẩn xác từ phần cứng",
         "Đo FPS bằng Timer thủ công hoặc đếm số frame ước lượng", "Window.OnFrameMetricsAvailableListener (API 24+)",
         "Các phương pháp đo FPS thông thường qua Timer chỉ đo được nhịp của ứng dụng chứ không phản ánh được thời gian phần cứng "
         "vẽ thực tế. Nhóm em đã nghiên cứu sâu vào tầng AOSP Framework để sử dụng FrameMetrics API (có từ Android 7.0 - API 24). "
         "Hệ thống lắng nghe trực tiếp từ Window trên một HandlerThread độc lập, bắt trọn từng nano-giây của 8 giai đoạn dựng hình "
         "(Measure, Layout, Draw, Sync, Command Issue, Swap Buffers) để phát hiện chính xác từng frame bị Jank."),

        ("6. Ứng dụng StrictMode và LeakCanary trong giám sát chất lượng",
         "Kiểm tra thủ công bằng mắt thường", "StrictMode (Android Framework) & LeakCanary (Square)",
         "Đây là các công cụ kiểm thử tiêu chuẩn công nghiệp: StrictMode được nhóm cấu hình trong PaaApplication.kt để tự động "
         "phát hiện và in cảnh báo đỏ lên Logcat nếu có bất kỳ dòng lệnh đọc/ghi ổ đĩa hoặc mạng nào lỡ chạy trên Main Thread; "
         "còn LeakCanary được cấu hình ở debugImplementation để tự động phân tích đồ thị Heap và xác minh hiện tượng rò rỉ Activity ở Lab 3.")
    ]

    for title, old_tech, new_tech, argument in tech_list:
        add_heading_2(doc, title)
        add_body_p(doc, old_tech, bold_prefix="• Công nghệ trong Slide: ")
        add_body_p(doc, new_tech, bold_prefix="• Công nghệ nâng cấp trong PAA: ")
        add_callout(doc, argument, bold_title="Kịch bản trả lời thầy:")

    doc.add_page_break()

    # =========================================================================
    # PHẦN 4: BỘ 50 CÂU HỎI VẤN ĐÁP ĐỈNH CAO KÈM LỜI GIẢI MẪU "ĐIỂM 10"
    # =========================================================================
    add_heading_1(doc, "PHẦN 4: BỘ 50 CÂU HỎI VẤN ĐÁP ĐỈNH CAO KÈM CÂU TRẢ LỜI MẪU ĐIỂM 10")

    add_body_p(doc, 
        "Bộ câu hỏi này được tổng hợp và phân loại chi tiết theo 4 cấp độ tư duy: từ câu hỏi nền tảng cơ bản, chuyên sâu 3 Lab, "
        "đối chiếu Slide vs Thực tế, cho đến các câu hỏi đố, câu hỏi bẫy code và những góc khuất kỹ thuật mà sinh viên thường bỏ qua. "
        "Mỗi câu đều có cấu trúc: Câu hỏi -> Mục đích kiểm tra của Thầy -> Vị trí mã nguồn/Slide liên quan -> Câu trả lời mẫu chuẩn mực.")

    # 50 câu hỏi
    qa_data = [
        # NHÓM 1: CƠ BẢN & KHÁI NIỆM (15 CÂU)
        (1, "Tại sao ngân sách hiển thị của một khung hình Android lại là 16.67 mili-giây?",
         "Kiểm tra hiểu biết về phần cứng màn hình và chu kỳ VSYNC.",
         "Slide 5, Bài 8 (AsyncTask & Thread) | Constants.kt",
         "Thưa thầy, đa số màn hình điện thoại hoạt động ở tần số quét 60Hz, nghĩa là hệ thống làm tươi màn hình 60 lần trong 1 giây. Do đó, thời gian tối đa để xử lý và hiển thị một khung hình là 1000ms / 60 = 16.666... ms (khoảng 16.67ms). Nếu bất kỳ thao tác đo đạc, vẽ hoặc tính toán nào trên Main Thread chiếm quá 16.67ms, GPU sẽ không có frame mới để hiển thị tại nhịp xung VSYNC tiếp theo, dẫn đến hiện tượng rớt khung hình (Jank)."),

        (2, "Khái niệm 'Jank' trong Android là gì và người dùng cảm nhận nó như thế nào?",
         "Kiểm tra định nghĩa cốt lõi của đề tài 1.",
         "Slide 5, Bài 8 | FrameMetricsTracker.kt",
         "Thưa thầy, Jank là hiện tượng khung hình bị trễ (drop frame) do ứng dụng mất nhiều hơn 16.67ms để vẽ một frame. Về mặt thị giác, người dùng sẽ cảm nhận màn hình bị khựng giật, giật cục khi cuộn danh sách hoặc hiệu ứng chuyển động bị đơ, làm giảm nghiêm trọng trải nghiệm người dùng."),

        (3, "Chỉ số P50, P90, P95, P99 trong đo lường hiệu năng có ý nghĩa gì?",
         "Kiểm tra kiến thức thống kê thực nghiệm và độ mượt ứng dụng.",
         "Stats.kt | ResultsViewModel.kt",
         "Thưa thầy, các chỉ số Percentile (phân vị) phản ánh mức độ ổn định của thời gian dựng hình: P50 là thời gian vẽ của 50% khung hình tốt nhất (trung vị); P90, P95 và P99 đại diện cho nhóm khung hình cá biệt bị vẽ lâu nhất. Trong đo lường chuyên nghiệp, P95 < 16.67ms là chuẩn vàng chứng minh 95% thời gian cuộn trang đạt độ mượt mà tuyệt đối."),

        (4, "ANR là gì? Sau bao nhiêu giây không phản hồi thì hệ điều hành sẽ bật hộp thoại ANR?",
         "Kiểm tra hiểu biết về cơ chế tự bảo vệ của hệ điều hành Android.",
         "Slide 6, Bài 8 (Users uninstall unresponsive apps)",
         "Thưa thầy, ANR là viết tắt của 'Application Not Responding'. Hệ điều hành Android sẽ hiển thị hộp thoại ANR khi Main Thread bị chặn không thể xử lý sự kiện trong vòng 5 giây đối với thao tác chạm/phím bấm của người dùng, hoặc quá 10 giây đối với BroadcastReceiver. Hệ điều hành cho phép người dùng chọn 'Đóng ứng dụng' hoặc 'Chờ tiếp'."),

        (5, "Tại sao các tác vụ I/O ổ đĩa hoặc tính toán nặng không được phép chạy trên Main Thread?",
         "Kiểm tra quy tắc vàng về đa luồng trong Android.",
         "Slide 4 & Slide 9, Bài 8 (Two rules for Android threads)",
         "Thưa thầy, theo Slide 4 và 9 bài 8, Main Thread (UI Thread) quản lý một hàng đợi thông điệp MessageQueue để xử lý tuần tự mọi sự kiện giao diện và vẽ khung hình. Nếu ta thực hiện tác vụ I/O hoặc vòng lặp nặng trên Main Thread, MessageQueue sẽ bị khóa cứng, toàn bộ việc vẽ và phản hồi tương tác người dùng bị đình trệ, gây lag hoặc ANR."),

        (6, "Cơ chế Garbage Collection (GC) trong máy ảo ART hoạt động như thế nào?",
         "Kiểm tra hiểu biết tầng sâu về máy ảo Android Runtime.",
         "Slide 24, Bài 2.2 | MemoryScenario.kt",
         "Thưa thầy, máy ảo ART sử dụng cơ chế GC đánh dấu và quét (Mark-and-Sweep) dựa trên cây tham chiếu GC Root. ART sẽ duyệt từ các gốc GC Root (luồng đang chạy, biến tĩnh static, stack frame). Đối tượng nào không còn đường dẫn tham chiếu từ GC Root sẽ được coi là 'rác' và bộ nhớ của nó sẽ được thu hồi."),

        (7, "Chỉ số RAM PSS (Proportional Set Size) khác gì so với Java Heap?",
         "Kiểm tra độ am hiểu về thước đo bộ nhớ chuẩn trên Android OS.",
         "MemorySampler.kt | Slide 7.1",
         "Thưa thầy, Java Heap chỉ là vùng nhớ do máy ảo ART cấp phát cho các đối tượng Java/Kotlin. Trong khi đó, PSS là thước đo thực tế của hệ điều hành Linux/Android: bao gồm toàn bộ vùng nhớ riêng của tiến trình (Private Clean + Private Dirty) cộng với phần bộ nhớ chia sẻ với các tiến trình khác được chia tỷ lệ theo số tiến trình dùng chung. PSS là chỉ số chính xác nhất để đo tác động bộ nhớ của app lên hệ điều hành."),

        (8, "Overdraw trong lập trình giao diện Android là gì?",
         "Kiểm tra kiến thức đồ họa GPU và tối ưu layout.",
         "Slide 1.3 | item_photo_bad.xml",
         "Thưa thầy, Overdraw là hiện tượng một điểm ảnh (pixel) trên màn hình bị GPU tô màu nhiều lần trong cùng một khung hình hiển thị (ví dụ: vẽ màu nền của Activity, đè lên màu nền của LinearLayout, rồi lại đè lên màu nền của CardView). Overdraw gây lãng phí băng thông bộ nhớ GPU và làm chậm quá trình rasterization."),

        (9, "View hierarchy (Cây phân cấp View) ảnh hưởng thế nào đến hiệu năng?",
         "Kiểm tra cơ chế chuỗi dựng hình Measure/Layout/Draw.",
         "Slide 1.3, Slide 37 | item_photo_bad.xml",
         "Thưa thầy, khi cây phân cấp View càng sâu và lồng nhiều tầng, hệ thống phải thực hiện duyệt cây đệ quy qua các pha measure() và layout(). Ở các ViewGroup như LinearLayout có thuộc tính layout_weight hoặc RelativeLayout, việc đo lường có thể bị lặp lại 2 lần trên mỗi View con, dẫn đến thời gian tính toán tăng theo cấp số nhân."),

        (10, "Adapter trong Android đóng vai trò gì theo định nghĩa bài giảng?",
         "Kiểm tra kiến thức từ bài giảng danh sách của Thầy.",
         "Slide 6, Bài 5.3 (What is an adapter?)",
         "Thưa thầy, theo Slide 6 bài 5.3, Adapter đóng vai trò là 'cầu nối trung gian' (Intermediary) giúp kết nối nguồn dữ liệu (Data) với thành phần hiển thị giao diện (View), chịu trách nhiệm tạo ra các Item View và gán dữ liệu từ nguồn vào View tương ứng."),

        (11, "Tại sao RecyclerView lại ưu việt hơn so với ListView truyền thống?",
         "Kiểm tra kiến thức so sánh giữa bài 5.1/5.2 và bài 5.3.",
         "Slide 3, Bài 5.3 (Recycler View)",
         "Thưa thầy, ListView truyền thống không bắt buộc dùng mẫu ViewHolder (dễ bị gọi findViewById liên tục gây lag) và cơ chế tái chế view hạn chế. RecyclerView bắt buộc sử dụng ViewHolder, tách rời LayoutManager (cho phép đổi linh hoạt giữa danh sách dọc, lưới, so le) và hỗ trợ Animation mượt mà khi thêm/xóa phần tử."),

        (12, "Tại sao xoay màn hình (Configuration Change) lại hủy Activity?",
         "Kiểm tra vòng đời Activity khi cấu hình thay đổi.",
         "Slide 27-28, Bài 2.2 (When does config change?)",
         "Thưa thầy, theo Slide 27-28 bài 2.2, khi xoay màn hình hoặc đổi ngôn ngữ, kích thước và tài nguyên hiển thị thay đổi. Android sẽ chủ động gọi onPause() -> onStop() -> onDestroy(), sau đó tạo lại Activity từ onCreate() -> onStart() -> onResume() để app nạp lại đúng tài nguyên giao diện tương ứng với cấu hình mới."),

        (13, "Vùng nhớ Internal Storage của ứng dụng có đặc tính gì?",
         "Kiểm tra kiến thức lưu trữ dữ liệu.",
         "Slide 5, Bài 7.1 (Internal Storage)",
         "Thưa thầy, theo Slide 5 bài 7.1, Internal Storage là vùng nhớ riêng tư của ứng dụng nằm trên bộ nhớ flash trong máy. Các ứng dụng khác không thể truy cập vào vùng này; và khi người dùng gỡ cài đặt ứng dụng, toàn bộ file trong Internal Storage sẽ tự động bị hệ thống xóa sạch."),

        (14, "Độ phức tạp O(N²) và O(N) trong xử lý dữ liệu khác nhau như thế nào về thời gian thực tế?",
         "Kiểm tra kiến thức giải thuật ứng dụng trong bài toán CPU.",
         "BadCpuTask.kt vs GoodCpuTask.kt",
         "Thưa thầy, với mảng N = 50.000 phần tử: Thuật toán O(N²) cần thực hiện tới 50.000 x 50.000 / 2 = 1.25 tỷ phép so sánh, trên điện thoại mất từ 2 đến 4 giây. Thuật toán O(N) chỉ duyệt mảng đúng 1 lần với 50.000 thao tác tra cứu bảng băm, hoàn thành chỉ trong khoảng 3 đến 8 mili-giây."),

        (15, "Tại sao thư mục assets lại thích hợp để lưu dữ liệu kiểm thử cố định?",
         "Kiểm tra cấu trúc dự án và cách nạp dữ liệu tĩnh.",
         "AssetLoader.kt | Constants.kt",
         "Thưa thầy, thư mục assets được đóng gói nguyên bản (raw bytes) vào file APK và không bị hệ thống biên dịch đổi tên thành ID resource như thư mục res. Do đó, ta có thể lưu các file dữ liệu lớn như items.json, cpu_data.csv và đọc bằng AssetManager theo đúng tên file để đảm bảo cả nhóm dùng chung dữ liệu test cố định."),

        # NHÓM 2: CHUYÊN SÂU 3 PHÒNG LAB (15 CÂU)
        (16, "Trong Lab 1, những nguyên nhân cụ thể nào đã khiến bản BAD bị giật lag?",
         "Kiểm tra chi tiết mã nguồn BadPhotoAdapter và layout.",
         "BadPhotoAdapter.kt | item_photo_bad.xml",
         "Thưa thầy, có 4 nguyên nhân cộng dồn: 1) Layout item_photo_bad.xml lồng 6 tầng LinearLayout/RelativeLayout gây quá tải pha measure/layout; 2) Đè 4 lớp màu nền gây Overdraw; 3) Giải mã ảnh Bitmap thô bằng BitmapFactory.decodeStream trực tiếp trên Main Thread trong onBindViewHolder(); 4) Vòng lặp cộng chuỗi String 50 lần gây phân mảnh bộ nhớ và kích hoạt GC liên tục."),

        (17, "Tại sao trong item_photo_bad.xml lại lồng tới 6 tầng layout? Điều đó mô phỏng thực tế ra sao?",
         "Kiểm tra tính chân thực của bài thực nghiệm so với thực tế lập trình viên thường mắc phải.",
         "item_photo_bad.xml | Slide 1.3",
         "Thưa thầy, trong thực tế, các lập trình viên mới thường có thói quen tiện đâu lồng đấy: tạo 1 LinearLayout chứa cả item, lồng LinearLayout thứ 2 để làm viền, lồng RelativeLayout để căn lề ảnh, lồng LinearLayout thứ 4 cho cụm chữ, và lồng thêm 2 LinearLayout con để chia hàng tiêu đề và phụ đề. Nhóm đã mô phỏng đúng thói quen sai lầm kinh điển này để làm bài học đối chứng."),

        (18, "Trong GoodPhotoAdapter, tại sao việc dùng ShapeableImageView + Coil lại tiết kiệm RAM hơn bản BAD?",
         "Kiểm tra hiểu biết về Bitmap downsampling.",
         "GoodPhotoAdapter.kt | item_photo_good.xml",
         "Thưa thầy, ở bản BAD, ảnh 3000x2000 khi giải nén đầy đủ chiếm tới 3000 x 2000 x 4 bytes = 24MB RAM cho mỗi tấm ảnh. Coil ở bản OPTIMIZED tự động đo kích thước thật của ImageView (100dp x 100dp) và giải mã ảnh thu nhỏ (Downsampling) vừa khít kích thước hiển thị, chỉ tốn khoảng vài trăm Kilobytes RAM, tiết kiệm hơn 95% bộ nhớ Bitmap."),

        (19, "DiffUtil trong ListAdapter hoạt động theo nguyên lý nào để không làm đứng màn hình?",
         "Kiểm tra giải thuật tính toán độ lệch dữ liệu ngầm.",
         "PhotoDiffCallback.kt | GoodPhotoAdapter.kt",
         "Thưa thầy, ListAdapter tích hợp AsyncListDiffer. Khi ta gọi submitList(newList), thuật toán DiffUtil sẽ tính toán độ chênh lệch giữa danh sách cũ và mới trên một Background Thread (sử dụng Dispatchers.Default). Sau khi có danh sách các vị trí cần thêm/sửa/xóa, nó mới bắn các thông báo tối ưu (notifyItemInserted, notifyItemRangeChanged) về Main Thread, không hề khóa UI."),

        (20, "Tại sao kịch bản JankScenario lại tự động cuộn 3 lượt và nghỉ 16ms mỗi bước cuộn?",
         "Kiểm tra tính khoa học của quy trình đo lường tự động.",
         "JankScenario.kt (L49-88)",
         "Thưa thầy, bước cuộn 25px kết hợp delay 16ms mô phỏng đúng tốc độ vuốt ngón tay tự nhiên của người dùng ở nhịp 60 khung hình/giây. Việc lặp lại đúng 3 chu kỳ cuộn lên cuộn xuống giúp loại bỏ sai số ngẫu nhiên ban đầu và đảm bảo mọi lần đo của bản BAD và bản OPTIMIZED đều chịu cùng một điều kiện tải cơ học như nhau."),

        (21, "Tại sao trong CpuScenario, nhóm lại chọn giới hạn N = 30.000 số nguyên thay vì 50.000?",
         "Kiểm tra kỹ năng cân bằng thực nghiệm để tránh crash hệ điều hành.",
         "CpuScenario.kt (L32) | Constants.kt",
         "Thưa thầy, với N = 50.000, thuật toán O(N²) trên điện thoại cấu hình tầm trung sẽ mất hơn 5.5 giây và hệ điều hành Android sẽ ngay lập tức bật hộp thoại ANR và kill tiến trình, làm mất toàn bộ số liệu đo. Nhóm đã cân bằng chọn N = 30.000 để bản BAD chạy mất ~2.5 giây: vừa đủ để người dùng thấy rõ độ đơ cứng của giao diện mà không làm sập ứng dụng."),

        (22, "Trong GoodCpuTask, nhóm sử dụng cấu trúc dữ liệu gì và tại sao?",
         "Kiểm tra kiến thức cấu trúc dữ liệu và giải thuật tối ưu.",
         "GoodCpuTask.kt (L34-52)",
         "Thưa thầy, nhóm sử dụng bảng băm HashMap<Int, Int>(n). Nhóm duyệt mảng đúng 1 vòng lặp để đếm tần suất xuất hiện của từng số với chi phí chèn và tra cứu trung bình là O(1). Sau đó, nhóm duyệt qua các entry của HashMap để lọc ra các số xuất hiện từ 2 lần trở lên. Tổng độ phức tạp thời gian đạt O(N) và không gian là O(N)."),

        (23, "Cơ chế In-memory Cache trong GoodCpuTask hoạt động như thế nào?",
         "Kiểm tra kỹ thuật tối ưu hóa thời gian thực thi nâng cao.",
         "GoodCpuTask.kt (L18-30)",
         "Thưa thầy, nhóm lưu kết quả CpuResult vào một HashMap cache với key là kích thước mảng n. Khi người dùng bấm chạy lại cùng một kích thước bài toán, hàm sẽ kiểm tra cache.containsKey(n) và trả về kết quả ngay lập tức trong 0ms (Cache Hit) mà không cần tính toán lại."),

        (24, "Trong Lab 3, tại sao lại dùng một Singleton LeakHolder để chứa Activity?",
         "Kiểm tra nguyên nhân gây rò rỉ GC Root.",
         "LeakHolder.kt | LeakyActivity.kt",
         "Thưa thầy, một Singleton tồn tại trong suốt vòng đời của tiến trình ứng dụng (Application Lifecycle). Khi ta lưu một Activity vào ArrayList tĩnh trong Singleton, Activity đó bị gắn chặt vào một GC Root vĩnh viễn. Kể cả khi Activity đã đóng và gọi onDestroy(), máy ảo ART vẫn thấy nó đang được tham chiếu nên không bao giờ thu hồi bộ nhớ."),

        (25, "Handler postDelayed gây rò rỉ bộ nhớ theo cơ chế nào?",
         "Kiểm tra hiểu biết sâu về Looper, Message và MessageQueue.",
         "LeakyActivity.kt (L53-58)",
         "Thưa thầy, khi gọi handler.postDelayed(runnable, 600_000L), một đối tượng Message được đưa vào hàng đợi MessageQueue của Main Looper. Đối tượng Message này giữ tham chiếu mạnh tới Runnable, và Runnable nội bộ ngầm giữ tham chiếu tới instance của Activity (outer class). Trong suốt 10 phút Message nằm chờ trong MessageQueue, toàn bộ Activity và cây View của nó không thể bị dọn rác."),

        (26, "Tại sao trong LeakyActivity lại cố tình cấp phát mảng byte 5MB (dummyPayload)?",
         "Kiểm tra kỹ năng tạo tải thực nghiệm để quan sát số liệu rõ nét.",
         "LeakyActivity.kt (L28, L43)",
         "Thưa thầy, một Activity rỗng chỉ chiếm khoảng vài chục đến vài trăm Kilobytes RAM, rất khó nhận biết rõ sự tăng trưởng trên biểu đồ Profiler giữa các lần đo. Việc cấp phát chủ động mảng byte 5MB (ByteArray(5*1024*1024)) giúp tạo ra bước nhảy bậc thang rõ rệt (+5MB mỗi lần mở) trên đồ thị RAM, giúp chứng minh hiện tượng rò rỉ bộ nhớ một cách trực quan và định lượng."),

        (27, "WeakReference khác gì so với Strong Reference thông thường?",
         "Kiểm tra kiến thức Java/Kotlin Memory Management.",
         "LeakHolder.kt (L27) | LeakyActivity.kt (L67)",
         "Thưa thầy, Strong Reference (tham chiếu mạnh) sẽ ngăn cản hoàn toàn Garbage Collector thu hồi đối tượng. Ngược lại, WeakReference (tham chiếu yếu) không ngăn cản GC: ngay khi một đối tượng chỉ còn được trỏ tới bởi các tham chiếu yếu, GC sẽ giải phóng nó ngay trong lần dọn rác tiếp theo. Bản OPTIMIZED dùng WeakReference<Activity> để vẫn tra cứu được instance khi nó còn sống mà không cản trở việc thu hồi khi nó đóng."),

        (28, "Tại sao trong MemoryScenario lại gọi System.gc() rồi chờ 1 giây trước khi đo lần cuối?",
         "Kiểm tra hiểu biết về tính bất đồng bộ của Garbage Collector.",
         "MemoryScenario.kt (L86-90)",
         "Thưa thầy, lệnh System.gc() chỉ là một lời đề nghị gửi tới máy ảo ART chứ không đảm bảo GC sẽ chạy đồng bộ ngay lập tức. Việc delay 1000ms giúp máy ảo ART có đủ thời gian hoàn tất chu kỳ thu gom rác trên luồng nền của nó, từ đó số liệu PSS RAM sau cùng đo được phản ánh chính xác lượng RAM thực sự còn sót lại."),

        (29, "Tại sao sau khi dọn rác ở bản OPTIMIZED, RAM không về mức 0MB mà là khoảng 19.8MB?",
         "Kiểm tra hiểu biết thực tế về cấu trúc bộ nhớ của hệ điều hành Android.",
         "ResultsViewModel.kt | So_lieu_do_mau.xlsx",
         "Thưa thầy, mức ~19.8MB là bộ nhớ nền cơ bản (Baseline Memory) của ứng dụng Android: bao gồm mã bytecode của ứng dụng, các thư viện AndroidX, font chữ, theme hệ thống và đối tượng Application Context luôn luôn thường trực trong tiến trình. Việc RAM trở về mức baseline này chứng tỏ 100% dung lượng leak của các Activity tạm thời đã được dọn sạch."),

        (30, "Làm thế nào để chứng minh đáp số của thuật toán ở CPU Lab giữa hai bản là hoàn toàn đồng nhất?",
         "Kiểm tra tính đúng đắn của logic nghiệp vụ sau khi tối ưu.",
         "CpuFragment.kt (L213-220) | CpuResult.kt",
         "Thưa thầy, trong CpuResult, nhóm em ghi lại cả duplicateCount (số lượng phần tử bị trùng) và sumDuplicates (tổng giá trị các số trùng). Cả bản BAD và bản OPTIMIZED khi chạy trên cùng một tập dữ liệu đều cho ra cùng một đáp số chính xác từng con số, chứng minh việc tối ưu thuật toán chỉ tăng tốc độ chứ không làm sai lệch kết quả."),

        # NHÓM 3: ĐỐI CHIẾU SLIDE VS THỰC TẾ (10 CÂU)
        (31, "Tại sao nhóm lại dùng Kotlin Coroutines trong khi Slide của Thầy dạy AsyncTask?",
         "Kiểm tra kiến thức cập nhật công nghệ và lý do loại bỏ API cũ.",
         "Slide 8 (AsyncTask) vs GoodCpuTask.kt",
         "Thưa thầy, Slide bài 8 dạy mô hình cốt lõi: phân tách giữa Main UI Thread và Background Worker Thread. Tuy nhiên, từ Android 11 (API 30), Google đã chính thức khai tử AsyncTask vì gây nhiều lỗi rò rỉ bộ nhớ ngầm và hiệu năng kém. Google khuyến nghị dùng Kotlin Coroutines. Nhóm em đã áp dụng đúng tinh thần chia tách luồng của bài 8 nhưng nâng cấp lên công nghệ Coroutines hiện đại nhất hiện nay."),

        (32, "Tại sao nhóm chọn minSdk là 24 trong build.gradle.kts?",
         "Kiểm tra sự am hiểu về các phiên bản Android API.",
         "app/build.gradle.kts (L11) | FrameMetricsTracker.kt",
         "Thưa thầy, nhóm chọn minSdk = 24 (Android 7.0 Nougat) vì đây là phiên bản hệ điều hành đầu tiên mà Google chính thức giới thiệu FrameMetrics API (Window.OnFrameMetricsAvailableListener). Nếu đặt minSdk thấp hơn 24, ứng dụng sẽ không thể lắng nghe được số liệu thời gian vẽ khung hình thực tế từ phần cứng."),

        (33, "Tại sao ứng dụng lại dùng ViewBinding thay vì findViewById như trong Slide?",
         "Kiểm tra lý do lựa chọn kiến trúc giao diện mới.",
         "Slide 1.3 vs build.gradle.kts",
         "Thưa thầy, findViewById() trong slide cũ có nhược điểm là tốn chi phí duyệt cây View và dễ gây lỗi văng app do NullPointerException lúc runtime nếu truyền sai ID. ViewBinding là công cụ chính thức của Google: tự sinh code Type-safe và Null-safe, giúp truy xuất View an toàn tuyệt đối với chi phí thời gian là O(1)."),

        (34, "Thanh HUD Monitor nổi (MetricsOverlayView) được tạo ra như thế nào mà không cần xin quyền hệ thống?",
         "Kiểm tra giải pháp thiết kế giao diện thông minh tránh xin quyền phiền hà.",
         "activity_main.xml (L13) | MetricsOverlayView.kt",
         "Thưa thầy, nếu tạo cửa sổ nổi đè lên các ứng dụng khác thì phải xin quyền nguy hiểm SYSTEM_ALERT_WINDOW (Draw over other apps). Nhóm em đã thiết kế thông minh bằng cách đặt FrameLayout overlayContainer nằm ngay trong layout gốc của MainActivity, nổi lên trên fragmentContainer. Nhờ đó, HUD Monitor luôn hiển thị trên mọi phòng Lab mà không cần xin thêm bất kỳ quyền hạn nhạy cảm nào từ người dùng."),

        (35, "Cơ chế StrictMode trong PaaApplication hoạt động như thế nào?",
         "Kiểm tra kỹ thuật bắt lỗi hiệu năng nâng cao.",
         "PaaApplication.kt (L12-30)",
         "Thưa thầy, StrictMode là công cụ của Android Framework dùng để phát hiện các thao tác sai nguyên tắc. Ở bản Debug, nhóm bật detectDiskReads, detectDiskWrites và penaltyLog. Khi có bất kỳ đoạn code nào lỡ đọc ghi file trên Main Thread, StrictMode sẽ lập tức in một thông báo cảnh báo màu đỏ kèm stack trace lên Logcat để lập trình viên sửa ngay."),

        (36, "Tại sao nhóm lại lưu kết quả vào file JSON nội bộ thay vì dùng Room Database?",
         "Kiểm tra lý do lựa chọn giải pháp kỹ thuật tối giản và thực dụng.",
         "JsonResultStore.kt vs Room",
         "Thưa thầy, nhóm sử dụng JsonResultStore với interface ResultStore trừu tượng. Việc dùng file JSON trong filesDir giúp giải pháp gọn nhẹ, phụ thuộc vào thư viện org.json có sẵn của Android, tránh được rủi ro cấu hình KSP phức tạp của Room Database trong phạm vi bài thi giữa kỳ. Nếu sau này cần nâng cấp lên Room, ta chỉ cần viết thêm một class triển khai interface ResultStore mà không làm ảnh hưởng tới các ViewModel."),

        (37, "FileProvider trong Android dùng để làm gì và tại sao không dùng Uri.fromFile()?",
         "Kiểm tra kiến thức bảo mật chia sẻ file trên Android 7.0+.",
         "AndroidManifest.xml | Exporter.kt (L47-51)",
         "Thưa thầy, kể từ Android 7.0 (API 24), hệ điều hành cấm chia sẻ trực tiếp đường dẫn file:// qua Intent vì sẽ ném ra lỗi FileUriExposedException. FileProvider là một ContentProvider đặc biệt giúp đóng gói đường dẫn file thành dạng content:// URI an toàn và cấp quyền đọc tạm thời (FLAG_GRANT_READ_URI_PERMISSION) cho các app khác (như Gmail, Drive) để nhận file CSV xuất ra."),

        (38, "Thẻ <profileable android:shell=\"true\" /> trong AndroidManifest có tác dụng gì?",
         "Kiểm tra hiểu biết về công cụ đo đạc chuyên sâu của Google.",
         "AndroidManifest.xml (L14)",
         "Thưa thầy, thẻ <profileable> cho phép các công cụ đo đạc hiệu năng chuyên sâu như Android Studio Profiler, Perfetto và Simpleperf có thể thu thập đầy đủ dữ liệu CPU, RAM, GPU ngay trên cả bản build Release mà không làm suy giảm hiệu năng như khi bật cờ android:debuggable=\"true\"."),

        (39, "Thư viện Coil có ưu điểm gì vượt trội so với thư viện Glide hay Picasso?",
         "Kiểm tra kiến thức so sánh thư viện của kỹ sư Android.",
         "GoodPhotoAdapter.kt | app/build.gradle.kts",
         "Thưa thầy, Coil (Coroutine Image Loader) được viết 100% bằng Kotlin và tích hợp sâu với Coroutines. Coil cực kỳ nhẹ (chỉ thêm ~2000 phương thức vào APK so với hơn 4000 của Glide), tự động tận dụng OkHttp và hỗ trợ mặc định các tính năng hiện đại như Extension Functions giúp cú pháp gọi ivPhotoGood.load() cực kỳ ngắn gọn."),

        (40, "Tại sao nhóm lại tách riêng kiến trúc thành MVVM thay vì viết chung trong Activity?",
         "Kiểm tra tư duy kiến trúc phần mềm sạch (Clean Architecture).",
         "ui/jank, ui/cpu, ui/memory",
         "Thưa thầy, nếu viết toàn bộ code vào Activity thì Activity sẽ trở thành 'God Object' (hàng ngàn dòng code hỗn tạp giữa logic đo, dữ liệu và giao diện). Nhóm tách theo MVVM: ViewModel giữ trạng thái StateFlow và sống sót qua các sự kiện cấu hình; Repository/Store quản lý dữ liệu; và Fragment chỉ thuần túy lắng nghe để cập nhật UI, giúp code dễ đọc, dễ bảo trì và dễ test."),

        # NHÓM 4: CÂU HỎI ĐỐ, BẪY CODE & GÓC KHUẤT ÍT ĐỂ Ý (10 CÂU)
        (41, "Tại sao trong MainActivity lại khóa cứng android:screenOrientation=\"portrait\"?",
         "Bẫy code: Kiểm tra lý do khóa hướng màn hình.",
         "AndroidManifest.xml (L19)",
         "Thưa thầy, đây là một chủ đích kỹ thuật quan trọng: Theo Slide 27-28 bài 2.2, khi xoay màn hình, Activity sẽ bị hủy và tạo lại từ đầu. Trong ứng dụng PAA, các kịch bản đo đạc tự động cần chạy liên tục (cuộn 3 lượt hoặc mở 10 màn hình). Nếu để xoay màn hình tự do, cảm biến xoay có thể kích hoạt Configuration Change giữa chừng, làm gián đoạn luồng đo và gây nhiễu loạn toàn bộ số liệu thống kê."),

        (42, "Trong CpuSampler, tại sao công thức tính % CPU lại phải chia cho Runtime.getRuntime().availableProcessors()?",
         "Bẫy toán học: Kiểm tra cách đo CPU trên thiết bị đa nhân.",
         "CpuSampler.kt (L48)",
         "Thưa thầy, Process.getElapsedCpuTime() trả về tổng thời gian CPU mà tiến trình sử dụng cộng dồn trên tất cả các nhân phần cứng. Trên điện thoại 8 nhân, nếu app chạy hết công suất 8 nhân trong 1 giây, delta CPU sẽ bằng 8 giây. Nếu ta không chia cho số nhân phần cứng (availableProcessors), tỷ lệ phần trăm tính ra sẽ lên tới 800%. Việc chia cho số nhân giúp chuẩn hóa chỉ số về thang đo chuẩn 0% - 100%."),

        (43, "Trong FrameMetricsTracker, tại sao lại có dòng code kiểm tra: if (frameMetrics.getMetric(FrameMetrics.FIRST_DRAW_FRAME) == 1L) return?",
         "Bẫy chi tiết: Kiểm tra hiểu biết về khung hình khởi tạo đầu tiên.",
         "FrameMetricsTracker.kt (L54-55)",
         "Thưa thầy, khung hình đầu tiên (First Draw Frame) của một màn hình luôn luôn mất rất nhiều thời gian (thường > 50ms) do hệ thống phải nạp mã XML từ đĩa, nạp font chữ và khởi tạo cấu trúc dữ liệu ban đầu. Nếu tính cả khung hình đầu tiên này vào bộ đo, chỉ số Jank % sẽ bị lệch lạc nghiêm trọng. Việc bỏ qua First Draw Frame giúp bộ đo chỉ phản ánh độ mượt thực tế khi người dùng đang cuộn trang."),

        (44, "Trong GoodCpuTask, tại sao hàm compute() có tham số useCache = true, nhưng trong CpuScenario nhóm lại truyền useCache = false?",
         "Bẫy logic kiểm thử: Kiểm tra sự trung thực và tính khoa học trong đo đạc benchmark.",
         "CpuScenario.kt (L61) vs GoodCpuTask.kt (L23)",
         "Thưa thầy, mục tiêu của kịch bản đo benchmark là so sánh thời gian thực thi thuật toán thuần túy giữa bản BAD O(N²) và bản OPTIMIZED O(N). Nếu ở CpuScenario ta bật useCache = true, từ lần bấm thứ hai trở đi thời gian sẽ luôn bằng 0ms do đọc từ RAM cache, điều đó không phản ánh đúng năng lực tính toán thật của thuật toán. Do đó, trong bài đo đối chứng, nhóm chủ động tắt cache (useCache = false) để đo đúng thời gian chạy O(N) thực tế (~3ms)."),

        (45, "Trong LeakyActivity, tại sao lại dùng delay 350ms rồi mới gọi finish() mà không gọi finish() ngay trong onCreate()?",
         "Bẫy chu trình sống: Kiểm tra hiểu biết về hiển thị giao diện.",
         "LeakyActivity.kt (L71-73)",
         "Thưa thầy, nếu ta gọi finish() ngay trong onCreate(), Activity sẽ lập tức chuyển sang onDestroy() mà chưa kịp chuyển sang trạng thái Resumed và chưa kịp hoàn thành việc gắn layout lên Window. Việc delay 350ms giúp Activity kịp hiển thị lên màn hình, hoàn thành toàn bộ chu trình sống onCreate -> onStart -> onResume, rồi mới chuyển sang onPause -> onStop -> onDestroy(), mô phỏng chính xác hành vi mở và xem màn hình của người dùng thực tế."),

        (46, "Trong build.gradle.kts, bản debug có applicationIdSuffix = \".debug\". Tại sao điều này không làm hỏng FileProvider?",
         "Bẫy cấu hình Gradle: Kiểm tra cách khai báo authority linh động.",
         "app/build.gradle.kts (L21) | AndroidManifest.xml (L35)",
         "Thưa thầy, trong AndroidManifest.xml, nhóm khai báo authority là android:authorities=\"${applicationId}.fileprovider\". Gradle sẽ tự động thay thế biến ${applicationId} theo đúng buildType: ở bản debug nó sẽ tự động trở thành com.nhomx.paa.debug.fileprovider. Trong Exporter.kt, nhóm lấy context.packageName + \".fileprovider\" nên hai giá trị này luôn luôn khớp nhau 100%, không bao giờ bị lỗi crash."),

        (47, "Trong JankScenario.kt, biến variant được khai báo cố định là Variant.BAD.name (dòng 112). Tại sao kết quả lưu lại vẫn phân biệt được BAD và OPTIMIZED?",
         "Bẫy code nội bộ: Kiểm tra khả năng nắm bắt luồng dữ liệu của chính nhóm.",
         "JankScenario.kt (L112) vs JankViewModel.kt (L38)",
         "Thưa thầy, JankScenario chỉ làm nhiệm vụ thuần túy là người chạy cuộn trang và thu thập số liệu phần cứng. Khi kết quả được trả về, trong JankViewModel.kt tại hàm setLastResult(result), nhóm đã sử dụng hàm copy của Kotlin: result.copy(variant = _variant.value.name). Lệnh này sẽ ghi đè chính xác chế độ đang được bật trên giao diện (BAD hoặc OPTIMIZED) trước khi lưu vào kết quả, đảm bảo số liệu luôn chuẩn xác."),

        (48, "Tại sao bộ đo FrameMetricsTracker lại phải chạy trên một HandlerThread riêng biệt thay vì dùng Coroutine hay Main Thread?",
         "Bẫy kiến trúc luồng: Kiểm tra yêu cầu kỹ thuật của Android API.",
         "FrameMetricsTracker.kt (L45-49)",
         "Thưa thầy, hàm Window.addOnFrameMetricsAvailableListener bắt buộc phải nhận một Handler có Looper hợp lệ để đẩy các callback dữ liệu khung hình vào. Nếu truyền Handler của Main Thread, chính việc xử lý các callback FrameMetrics sẽ làm nặng thêm Main Thread, gây ra hiện tượng 'bộ đo tự làm chậm hệ thống' (Observer Effect). Do đó, tạo riêng một HandlerThread ngầm là giải pháp tối ưu và chính xác nhất."),

        (49, "Tại sao khi bấm nút 'Dọn rác' (System.gc) ở bản BAD, dung lượng RAM hiển thị lại không hề suy giảm?",
         "Bẫy thực nghiệm: Kiểm tra bản chất của hiện tượng Memory Leak.",
         "MemoryFragment.kt (L79-84) | LeakHolder.kt",
         "Thưa thầy, lệnh System.gc() chỉ giải phóng những đối tượng không còn ai tham chiếu tới (Unreachable objects). Ở bản BAD, toàn bộ 10 Activity bị biến tĩnh trong LeakHolder giữ chặt tham chiếu mạnh, máy ảo ART xác định chúng vẫn là đối tượng đang được sử dụng nên tuyệt đối không được phép thu hồi. Do đó, dù có ép dọn rác bao nhiêu lần thì RAM vẫn giữ nguyên mức cao."),

        (50, "Nếu Thầy muốn nhóm cải tiến PAA lên một tầm cao mới nữa sau môn học này, nhóm sẽ làm thêm điều gì?",
         "Câu hỏi mở chốt hạ: Thể hiện tầm nhìn kỹ thuật và đam mê chuyên môn.",
         "Toàn bộ dự án PAA",
         "Thưa thầy, nếu có thêm thời gian, nhóm em sẽ mở rộng thêm 2 hướng: 1) Tích hợp thư viện Jetpack Benchmark (Macrobenchmark) để đo lường tốc độ khởi động app (Cold Startup Time) và viết kịch bản tối ưu hóa bằng Baseline Profiles; 2) Thêm phòng Lab thứ 4 về Network & Battery Profiling để đo lượng pin tiêu thụ và tối ưu hóa việc gộp các truy vấn mạng (Batching Requests) qua WorkManager.")
    ]

    for q_id, question, purpose, slide_ref, answer in qa_data:
        add_heading_2(doc, f"Câu {q_id}: {question}")
        add_body_p(doc, purpose, bold_prefix="• Mục đích Thầy hỏi: ", italic=True, color=COLOR_INK_MUTED)
        add_body_p(doc, slide_ref, bold_prefix="• Căn cứ Slide & Code: ", color=COLOR_NAVY)
        add_callout(doc, answer, bold_title="Trả lời chuẩn điểm 10:")

    # Lưu tài liệu
    print(f"Đang lưu tài liệu vào: {OUTPUT_DOCX}")
    doc.save(OUTPUT_DOCX)
    print("Xuất file Word thành công 100%!")

    # Copy một bản dự phòng sang docs/ nếu có
    docs_dir = os.path.join(BASE_DIR, "docs")
    if os.path.exists(docs_dir):
        backup_docx = os.path.join(docs_dir, "Cam_Nang_Van_Dap_PAA_TDTU.docx")
        doc.save(backup_docx)
        print(f"Đã lưu bản sao dự phòng tại: {backup_docx}")


if __name__ == "__main__":
    main()
