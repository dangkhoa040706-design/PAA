#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động sinh file Word (.docx) chuyên nghiệp, đẹp mắt
cho tài liệu "Cẩm Nang Toàn Diện Dự Án PAA (Performance Analysis App)".
Phiên bản 2.0: Bổ sung Từ điển thuật ngữ nhanh và Cơ chế bình dân học vụ cho 3 Lab.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# --- MÀU SẮC CHỦ ĐẠO PAA ---
COLOR_SCARLET = RGBColor(188, 0, 36)      # #BC0024 (Chính)
COLOR_SCARLET_DARK = RGBColor(138, 0, 26) # #8A001A (Đậm / Header)
COLOR_INK = RGBColor(42, 26, 29)          # #2A1A1D (Chữ chính)
COLOR_INK_MUTED = RGBColor(107, 90, 93)   # #6B5A5D (Chữ phụ)
COLOR_OPT = RGBColor(26, 112, 52)         # #1A7034 (Xanh lá tối ưu)
COLOR_BAD = RGBColor(188, 0, 36)          # #BC0024 (Đỏ lỗi)

HEX_SCARLET = "BC0024"
HEX_SCARLET_DARK = "8A001A"
HEX_PEARL_BG = "FBF8EE"
HEX_PEARL_CARD = "F7F3E8"
HEX_PEARL_BORDER = "CFC5A6"
HEX_OPT_BG = "EAF5EC"
HEX_OPT_BORDER = "1A7034"
HEX_BAD_BG = "FDF0F2"
HEX_BAD_BORDER = "BC0024"

BASE_DIR = r"D:\MOBI GK"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SCREENSHOTS_DIR = os.path.join(DOCS_DIR, "screenshots")
DESIGN_DIR = os.path.join(BASE_DIR, "design")
OUTPUT_DOCX = os.path.join(DOCS_DIR, "Huong_Dan_Toan_Dien_PAA.docx")


def set_cell_background(cell, hex_color):
    """Đặt màu nền cho cell trong table."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Đặt khoảng đệm (padding) trong cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_border_left_only(cell, hex_color, sz="36"):
    """Tạo viền bên trái cho thẻ callout / quote."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{hex_color}"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)


def set_table_borders(table, hex_color=HEX_PEARL_BORDER):
    """Tạo viền mờ tinh tế cho bảng dữ liệu."""
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


def format_paragraph(p, space_before=0, space_after=5, line_spacing=1.15):
    """Định dạng khoảng cách dòng và đoạn văn bản."""
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing


def add_heading_1(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=16, space_after=8)
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_SCARLET_DARK
    return p


def add_heading_2(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=12, space_after=5)
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_SCARLET
    return p


def add_heading_3(doc, text):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=8, space_after=3)
    run = p.add_run(text)
    run.font.name = "Segoe UI"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = COLOR_INK
    return p


def add_body_p(doc, text, bold_prefix="", italic=False, color=COLOR_INK):
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=4)
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = "Segoe UI"
        r_b.font.size = Pt(10)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_INK
    r = p.add_run(text)
    r.font.name = "Segoe UI"
    r.font.size = Pt(10)
    r.font.italic = italic
    r.font.color.rgb = color
    return p


def add_bullet_p(doc, text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    format_paragraph(p, space_before=0, space_after=3)
    if bold_prefix:
        r_b = p.add_run(bold_prefix)
        r_b.font.name = "Segoe UI"
        r_b.font.size = Pt(10)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_INK
    r = p.add_run(text)
    r.font.name = "Segoe UI"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_INK
    return p


def add_callout_box(doc, title, content_lines, border_hex=HEX_SCARLET, bg_hex=HEX_PEARL_BG):
    """Tạo hộp ghi chú chuyên nghiệp có viền trái nổi bật."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)

    cell = table.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
    set_cell_border_left_only(cell, border_hex, sz="28")

    p = cell.paragraphs[0]
    format_paragraph(p, space_before=0, space_after=3)
    r_title = p.add_run(f"📌 {title}\n")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(10.5)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_SCARLET_DARK if border_hex != HEX_OPT_BORDER else COLOR_OPT

    for i, line in enumerate(content_lines):
        p_line = cell.add_paragraph()
        format_paragraph(p_line, space_before=0, space_after=2 if i < len(content_lines) - 1 else 0)
        r = p_line.add_run(line)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9.5)
        r.font.color.rgb = COLOR_INK

    p_spacer = doc.add_paragraph()
    format_paragraph(p_spacer, space_before=0, space_after=4)


def add_two_images_comparison(doc, img_path_1, cap_1, img_path_2, cap_2):
    """Đặt 2 ảnh màn hình điện thoại song song cạnh nhau với chú thích."""
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    col_w = Inches(3.1)
    table.columns[0].width = col_w
    table.columns[1].width = col_w

    for col_idx, (path, cap) in enumerate([(img_path_1, cap_1), (img_path_2, cap_2)]):
        cell_img = table.cell(0, col_idx)
        cell_img.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p_img = cell_img.paragraphs[0]
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        format_paragraph(p_img, space_before=2, space_after=2)
        if os.path.exists(path):
            p_img.add_run().add_picture(path, width=Inches(2.55))
        else:
            p_img.add_run(f"[Không tìm thấy ảnh: {os.path.basename(path)}]")

        cell_cap = table.cell(1, col_idx)
        p_cap = cell_cap.paragraphs[0]
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        format_paragraph(p_cap, space_before=2, space_after=6)
        r_cap = p_cap.add_run(cap)
        r_cap.font.name = "Segoe UI"
        r_cap.font.size = Pt(9)
        r_cap.font.italic = True
        r_cap.font.color.rgb = COLOR_INK_MUTED

    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders>')
    tblPr.append(borders)

    p_spacer = doc.add_paragraph()
    format_paragraph(p_spacer, space_before=0, space_after=4)


def add_single_image_centered(doc, img_path, caption):
    """Chèn 1 ảnh ở giữa trang kèm chú thích."""
    if os.path.exists(img_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        format_paragraph(p, space_before=4, space_after=2)
        p.add_run().add_picture(img_path, width=Inches(2.7))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        format_paragraph(p_cap, space_before=0, space_after=6)
        r = p_cap.add_run(caption)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9)
        r.font.italic = True
        r.font.color.rgb = COLOR_INK_MUTED


def build_document():
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # ========================== BÌA / HEADER ==========================
    logo_path = os.path.join(DESIGN_DIR, "PAA_2_logo_ten_trong_suot.png")
    if not os.path.exists(logo_path):
        logo_path = os.path.join(DESIGN_DIR, "PAA_1_logo_trong_suot.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        format_paragraph(p_logo, space_before=0, space_after=4)
        p_logo.add_run().add_picture(logo_path, width=Inches(2.2))

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    format_paragraph(p_title, space_before=0, space_after=2)
    r_title = p_title.add_run("CẨM NANG TOÀN DIỆN VẬN HÀNH & BÁO CÁO")
    r_title.font.name = "Segoe UI"
    r_title.font.size = Pt(19)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_SCARLET_DARK

    p_app = doc.add_paragraph()
    p_app.alignment = WD_ALIGN_PARAGRAPH.CENTER
    format_paragraph(p_app, space_before=0, space_after=4)
    r_app = p_app.add_run("ỨNG DỤNG PAA (Performance Analysis App)")
    r_app.font.name = "Segoe UI"
    r_app.font.size = Pt(13)
    r_app.font.bold = True
    r_app.font.color.rgb = COLOR_SCARLET

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    format_paragraph(p_sub, space_before=0, space_after=12)
    r_sub = p_sub.add_run("Môn học: Phát triển Ứng dụng Di động  |  Đề tài 1: Android Application Performance Analysis and Optimization\nHọc kỳ: Giữa kỳ  |  Nền tảng: Android (Kotlin, MVVM, Profiling Lab)")
    r_sub.font.name = "Segoe UI"
    r_sub.font.size = Pt(9.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_INK_MUTED

    p_line = doc.add_paragraph()
    format_paragraph(p_line, space_before=0, space_after=10)
    r_line = p_line.add_run("―" * 58)
    r_line.font.color.rgb = RGBColor(207, 197, 166)
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ========================== PHẦN 1 ==========================
    add_heading_1(doc, "1. TỔNG QUAN DỰ ÁN & BẢN CHẤT CỦA APP PAA")

    add_body_p(doc, "Nhiều sinh viên khi làm đề tài hiệu năng thường mắc sai lầm là xây dựng một ứng dụng nghiệp vụ phức tạp (như bán hàng, mạng xã hội) rồi cố gắng tối ưu. Cách tiếp cận này khiến lỗi hiệu năng diễn ra ngẫu nhiên, khó tái hiện lặp lại, và rất khó bảo vệ trước hội đồng chấm điểm.", bold_prefix="Vấn đề thực tế: ")

    add_body_p(doc, "PAA được xây dựng theo mô hình một \"Phòng thí nghiệm thực nghiệm hiệu năng\" (Performance Profiling Lab) độc lập. Thay vì che giấu lỗi, PAA chủ động tạo ra các bài toán thực nghiệm với 2 phiên bản đối chiếu:", bold_prefix="Bản chất của PAA: ")

    add_bullet_p(doc, "Chứa các lỗi hiệu năng kinh điển phổ biến nhất trên Android (Decode ảnh Main Thread, Layout 6 tầng overdraw, thuật toán O(n²), rò rỉ Activity).", bold_prefix="Phiên bản BAD (Lỗi cố ý): ")
    add_bullet_p(doc, "Áp dụng toàn bộ kiến trúc và kỹ thuật lập trình chuẩn mực của Google (Coil bất đồng bộ, ConstraintLayout phẳng 1 tầng, O(n) Coroutines Dispatchers.Default, WeakReference, dọn dẹp vòng đời).", bold_prefix="Phiên bản OPTIMIZED (Đã tối ưu): ")
    add_bullet_p(doc, "Hệ thống tự động chạy kịch bản đo đạc lặp lại (cuộn 3 vòng, tính toán 50.000 số, mở đóng 20 lần màn hình) để sinh ra số liệu định lượng khách quan.", bold_prefix="Cơ chế đo lường khoa học: ")

    # ========================== PHẦN 2 (MỚI): TỪ ĐIỂN THUẬT NGỮ NHANH ==========================
    add_heading_1(doc, "2. TỪ ĐIỂN ĐỊNH NGHĨA THUẬT NGỮ CỐT LÕI (CHEAT SHEET)")
    add_body_p(doc, "Dưới đây là bảng tổng hợp các thuật ngữ cốt lõi được định nghĩa siêu ngắn gọn, dễ nhớ, giúp bạn nắm vững bản chất và tự tin trả lời vấn đáp:")

    table_dict = doc.add_table(rows=8, cols=3)
    table_dict.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_dict.autofit = False
    set_table_borders(table_dict)

    dict_widths = [Inches(1.5), Inches(3.2), Inches(1.8)]
    for i, title in enumerate(["Thuật ngữ", "Định nghĩa siêu ngắn & Dễ hiểu", "Ngưỡng chuẩn Android"]):
        cell = table_dict.cell(0, i)
        cell.width = dict_widths[i]
        set_cell_background(cell, HEX_SCARLET_DARK)
        set_cell_margins(cell, top=90, bottom=90, left=110, right=110)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0)
        r = p.add_run(title)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    dict_data = [
        ("Jank (Lag / Rớt khung hình)", "Hiện tượng giao diện bị khựng khi thời gian vẽ một khung hình vượt quá ngân sách thời gian cho phép, khiến mắt người thấy giật.", "Vượt quá 16.67ms (ở màn 60Hz)\nhoặc 8.33ms (ở màn 120Hz)"),
        ("Overdraw (Vẽ đè điểm ảnh)", "Hiện tượng hệ thống phải tô màu một điểm ảnh trên màn hình nhiều lần trong cùng một frame do các View/Background lồng tầng đè lên nhau.", "Càng thấp càng tốt (1x: Tốt, 3x-4x: Rất tệ)"),
        ("UI Freeze / ANR", "Giao diện bị đơ cứng do Main Thread (luồng vẽ UI) bị chặn bởi tác vụ nặng (tính toán hoặc đọc ổ đĩa). Nếu đơ quá 5s sẽ báo hộp thoại ANR.", "ANR xuất hiện khi Main Thread bị block quá 5 giây"),
        ("Memory Leak (Rò rỉ RAM)", "Đối tượng đã kết thúc vòng đời (như Activity đã finish) nhưng vẫn bị một nơi khác giữ tham chiếu mạnh -> Bộ dọn rác GC không thể thu hồi -> Phình RAM.", "Số lượng instance rò rỉ phải bằng 0 sau khi GC dọn"),
        ("RAM PSS (Proportional Set Size)", "Thước đo dung lượng RAM chuẩn xác nhất của tiến trình: gồm toàn bộ RAM riêng (Private) cộng với phần RAM chia sẻ với hệ thống chia theo tỷ lệ.", "Đo bằng Debug.getMemoryInfo().totalPss (MB)"),
        ("Độ phức tạp O(n²) vs O(n)", "Với 50.000 phần tử: O(n²) cần 2.5 tỷ phép tính -> treo máy. O(n) chỉ cần 50.000 phép tính -> xong trong 15 mili-giây.", "Cải thiện tốc độ hơn 99%"),
        ("WeakReference (Tham chiếu yếu)", "Tham chiếu đặc biệt không cản trở bộ dọn rác (GC). Khi máy thiếu RAM hoặc Activity đã đóng, GC tự do thu hồi sạch sẽ.", "Giải pháp chống leak kinh điển trong Android"),
    ]

    for row_idx, row_data in enumerate(dict_data, start=1):
        bg = HEX_PEARL_CARD if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = table_dict.cell(row_idx, col_idx)
            cell.width = dict_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=70, bottom=70, left=100, right=100)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0)
            r = p.add_run(text)
            r.font.name = "Segoe UI"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_INK

    p_sp_dict = doc.add_paragraph()
    format_paragraph(p_sp_dict, space_before=4, space_after=4)

    # ========================== PHẦN 3 (MỚI): BÌNH DÂN HỌC VỤ ==========================
    add_heading_1(doc, "3. 'BÌNH DÂN HỌC VỤ' - APP THỰC TẾ ĐÃ LÀM GÌ Ở TỪNG PHÒNG LAB?")
    add_body_p(doc, "Để hiểu nhanh và giải thích trôi chảy cho người nghe, dưới đây là tóm tắt cực kỳ dễ hiểu về kịch bản thực nghiệm của từng phòng Lab:")

    add_callout_box(
        doc,
        "1. Jank Lab: App nạp 500 ảnh lớn rồi bắt cuộn, điều gì xảy ra?",
        [
            "• Dữ liệu: 500 item trong items.json cùng 30 bức ảnh lớn (3000x2000px, dung lượng nặng).",
            "• Bản BAD: Khi cuộn danh sách, mỗi item hiện lên app BẮT LUỒNG CHÍNH (Main Thread) vừa vẽ hình vừa phải đọc file từ ổ đĩa và decode bức ảnh to đùng. Thêm nữa, layout mỗi dòng bị lồng 6 tầng LinearLayout đè background lên nhau (Overdraw), và gọi notifyDataSetChanged() ép vẽ lại sạch sẽ cả danh sách -> Luồng chính nghẽn nặng, vẽ 1 frame mất 40-70ms -> Giật tung màn hình, FPS rớt thảm hại xuống 20-30.",
            "• Bản OPTIMIZED: Đưa thư viện Coil vào để đọc và decode ảnh NGẦM DƯỚI LUỒNG PHỤ, tự động thu nhỏ ảnh vừa khít khung 100x100dp. Đập bỏ layout 6 tầng, thay bằng 1 tầng phẳng duy nhất (ConstraintLayout). Dùng ListAdapter + DiffUtil chỉ vẽ lại item nào đổi -> Luồng chính rảnh tay chỉ việc vẽ -> Cuộn siêu mượt 60 FPS, % giật về 0%."
        ],
        border_hex=HEX_SCARLET,
        bg_hex=HEX_PEARL_BG
    )

    add_callout_box(
        doc,
        "2. CPU Lab: Dãy 50.000 số nguyên tìm trùng, đơ 3.5 giây vs 15 mili-giây",
        [
            "• Dữ liệu: Một file CSV chứa 50.000 số nguyên ngẫu nhiên (cpu_data.csv). Bài toán: Đếm có bao nhiêu số bị trùng và tính tổng các số đó.",
            "• Bản BAD: Dùng thuật toán 2 vòng lặp lồng nhau O(n²), lấy số thứ nhất đem so với 49.999 số còn lại; số thứ hai so tiếp... và BẮT LUỒNG CHÍNH chạy phép tính này -> Chiếm trọn 100% thời gian của luồng vẽ giao diện -> Đơ cứng màn hình 3.5 giây, bấm nút nào cũng liệt.",
            "• Bản OPTIMIZED: Đổi thuật toán sang O(n) dùng HashMap đếm tần suất đúng 1 lượt duyệt duy nhất. ĐẨY PHÉP TÍNH XUỐNG LUỒNG NỀN COROUTINES (Dispatchers.Default) và lưu cache -> Xong trong nháy mắt (15ms, nhanh gấp 200 lần), giao diện bấm mượt mà.",
            "• 🎯 Cùng một đáp số: Cả 2 bản đều cho ra chính xác: 12.012 số trùng, Tổng: 180.251.490. Khẳng định tối ưu thuật toán chuẩn xác mà không làm sai lệch nghiệp vụ!"
        ],
        border_hex=HEX_OPT_BORDER,
        bg_hex=HEX_OPT_BG
    )

    add_callout_box(
        doc,
        "3. Memory Lab: Mở đóng màn hình con 20 lần, RAM phình to vs Thu hồi sạch",
        [
            "• Dữ liệu: Một màn hình con LeakyActivity, mỗi lần mở lên sẽ tự động ngốn 5MB RAM giả lập.",
            "• Bản BAD: Khi bấm Chạy đo, app tự động mở và đóng màn hình này liên tục 20 lần. Bản BAD cố ý gài 3 bẫy: (1) Nhét Activity vào biến tĩnh Singleton LeakHolder không bao giờ xóa; (2) Hẹn giờ Handler postDelayed 10 phút; (3) Không hủy đăng ký sự kiện. Khi màn hình đóng lại (finish), bộ dọn rác GC của máy ảo Android muốn dọn cũng KHÔNG THỂ DỌN ĐƯỢC vì còn bị biến tĩnh giữ chặt -> RAM leo thang từ 60MB lên hơn 200MB, bấm nút 'Chạy GC' RAM vẫn trơ trơ, báo 20 instance còn kẹt.",
            "• Bản OPTIMIZED: Thay bằng WeakReference<Activity> (cho phép GC dọn tự do). Trong onDestroy() gọi hủy hết hẹn giờ và hủy đăng ký sự kiện -> Mở đóng 20 lần xong, bấm nút 'Chạy GC' là RAM lập tức tụt về ban đầu (~60MB), số rò rỉ báo 0."
        ],
        border_hex=HEX_SCARLET_DARK,
        bg_hex=HEX_PEARL_BG
    )

    # ========================== PHẦN 4 ==========================
    add_heading_1(doc, "4. HÌNH ẢNH GIAO DIỆN THỰC TẾ & HƯỚNG DẪN TỪNG MÀN HÌNH")
    add_body_p(doc, "Toàn bộ hình ảnh dưới đây được chụp trực tiếp từ ứng dụng PAA đang chạy thực tế trên máy ảo Pixel 7 (Android 14, 60Hz).")

    # 4.1 Dashboard
    add_heading_2(doc, "4.1. Màn hình Dashboard Chính (Home)")
    add_single_image_centered(
        doc,
        os.path.join(SCREENSHOTS_DIR, "01_home.png"),
        "Hình 1: Màn hình Dashboard trung tâm hiển thị thông số thiết bị và 3 module thực nghiệm"
    )
    add_bullet_p(doc, "Logo chính thức và tiêu đề nhận diện thương hiệu PAA (Scarlet & Pearl).", bold_prefix="Bộ nhận diện: ")
    add_bullet_p(doc, "Cho phép chọn nhanh 1 trong 3 phòng Lab (Jank Lab, CPU Lab, Memory Lab).", bold_prefix="3 Card điều hướng: ")
    add_bullet_p(doc, "Mở màn hình bảng tổng hợp so sánh số liệu Trước/Sau và xuất file CSV.", bold_prefix="Nút Kết quả: ")
    add_bullet_p(doc, "Trích xuất tự động Model máy, phiên bản Android (API), dung lượng RAM và tần số quét màn hình (Hz). Giúp người xem video demo biết ngay môi trường đo (ở màn hình 60Hz, ngân sách mỗi khung hình là 16.67ms).", bold_prefix="Thanh thông số phần cứng (Dưới cùng): ")

    # 4.2 Jank Lab
    add_heading_2(doc, "4.2. Jank Lab (Lag/Giật Giao Diện & Tối Ưu Render)")
    add_body_p(doc, "Dưới đây là hình ảnh so sánh trực quan giữa bản BAD và bản OPTIMIZED trong Jank Lab:")

    add_two_images_comparison(
        doc,
        os.path.join(SCREENSHOTS_DIR, "02_jank_bad.png"),
        "Hình 2A: Jank Lab bản BAD (Thanh đỏ, ảnh decode trực tiếp Main Thread)",
        os.path.join(SCREENSHOTS_DIR, "03_jank_opt.png"),
        "Hình 2B: Jank Lab bản OPTIMIZED (Thanh xanh, tải ảnh Coil, Layout phẳng)"
    )

    add_body_p(doc, "• Tại sao bản BAD bị lag giật? Trong RecyclerView, hàm onBindViewHolder bị ép đọc file từ Assets và giải mã Bitmap độ phân giải lớn trực tiếp trên Main Thread. Đồng thời layout lồng 6 tầng LinearLayout/RelativeLayout gây overdraw nặng và dùng notifyDataSetChanged() ép vẽ lại cả danh sách. Main Thread bị nghẽn làm thời gian vẽ frame vượt quá 16.67ms -> FPS tụt xuống 20-30, thanh HUD Overlay báo đỏ.", bold_prefix="Bản BAD: ")
    add_body_p(doc, "• Bản OPTIMIZED đã sửa thế nào? Toàn bộ ảnh được tải và giải mã bất đồng bộ ngoài Main Thread qua thư viện Coil (tự động downsample theo kích thước View). Layout được làm phẳng thành 1 tầng duy nhất bằng ConstraintLayout. Kế thừa ListAdapter kết hợp DiffUtil để chỉ vẽ lại item thay đổi -> Cuộn siêu mượt 60 FPS, % Jank giảm về 0%.", bold_prefix="Bản OPTIMIZED: ")

    # 4.3 CPU Lab
    add_heading_2(doc, "4.3. CPU Lab (Tải Tính Toán Nặng & Đơ Giao Diện)")
    add_body_p(doc, "Bài toán thực nghiệm: Tìm số lượng các phần tử bị trùng và tính tổng của chúng trên dãy 30.000 số nguyên ngẫu nhiên (có seed cố định):")

    add_two_images_comparison(
        doc,
        os.path.join(SCREENSHOTS_DIR, "04_cpu_lab.png"),
        "Hình 3A: CPU Lab chọn quy mô dữ liệu (10k, 30k, 50k)",
        os.path.join(SCREENSHOTS_DIR, "07_cpu_result_panel.png"),
        "Hình 3B: Bảng kết quả CPU & Thẻ xác minh kết quả khớp 100%"
    )

    add_bullet_p(doc, "Sử dụng thuật toán duyệt cặp 2 vòng lặp lồng nhau O(n²) chạy thẳng trên Main Thread. Làm đơ cứng giao diện (UI Freeze) trong khoảng 3.5 giây. Người dùng không thể chạm hay cuộn bất kỳ nút nào.", bold_prefix="Bản BAD: ")
    add_bullet_p(doc, "Sử dụng cấu trúc dữ liệu HashMap để đếm tần suất chỉ trong 1 lượt duyệt duy nhất O(n). Chạy trên luồng nền Coroutines (Dispatchers.Default) kèm bộ nhớ Cache -> Thời gian xử lý từ ~3500ms giảm còn ~15ms (Cải thiện >99%), UI mượt mà.", bold_prefix="Bản OPTIMIZED: ")
    add_bullet_p(doc, "Như trên Hình 3B, thẻ xanh lá hiển thị rõ: 'Tìm trùng: 12.012 số, Tổng: 180.251.490'. Cả hai bản đều cho ra chính xác từng con số, chứng minh tối ưu tốc độ mà không làm hỏng tính đúng đắn.", bold_prefix="Thẻ xác minh (Verification Card): ")

    # 4.4 Memory Lab
    add_heading_2(doc, "4.4. Memory Lab (Rò Rỉ Bộ Nhớ & LeakCanary)")
    add_single_image_centered(
        doc,
        os.path.join(SCREENSHOTS_DIR, "05_memory_lab.png"),
        "Hình 4: Memory Lab theo dõi RAM PSS thời gian thực và kịch bản mở đóng Activity"
    )

    add_bullet_p(doc, "Khi mở màn hình con LeakyActivity (cấp phát 5MB RAM giả lập mỗi lần), bản BAD đưa Activity vào Singleton LeakHolder qua tham chiếu mạnh, tạo Handler postDelayed 10 phút và không gỡ listener. Sau 20 lần mở đóng, Garbage Collector (GC) không thể thu hồi -> RAM leo thang vọt lên 180MB-220MB. Bấm 'Chạy GC' RAM vẫn không hạ, số leak báo 20.", bold_prefix="Bản BAD: ")
    add_bullet_p(doc, "Bản OPTIMIZED dùng WeakReference<Activity>, gọi handler.removeCallbacksAndMessages(null) và gỡ listener trong onDestroy() -> Khi GC chạy, RAM lập tức hạ về mức cơ sở, số leak báo 0.", bold_prefix="Bản OPTIMIZED: ")
    add_bullet_p(doc, "Ở bản build debug, thư viện LeakCanary tự động hiện thông báo phân tích đồ thị tham chiếu (Reference Retention Path) chỉ rõ dòng code gây leak.", bold_prefix="Tích hợp LeakCanary: ")

    # 4.5 Results
    add_heading_2(doc, "4.5. Màn hình Results (Bảng Đối Chiếu Trước/Sau & Xuất CSV)")
    add_single_image_centered(
        doc,
        os.path.join(SCREENSHOTS_DIR, "06_results.png"),
        "Hình 5: Màn hình Kết quả, đối chiếu Trước/Sau và lịch sử các lần đo"
    )

    add_bullet_p(doc, "Lọc kết quả đo theo từng phòng Lab (Jank / CPU / Memory).", bold_prefix="Chip lọc module: ")
    add_bullet_p(doc, "Tự động tính trung bình các lần đo của bản BAD và OPTIMIZED, hiển thị cột '% Cải thiện' màu xanh lá kèm dấu '+' (ví dụ: Jank giảm 94%, Thời gian CPU giảm 99%).", bold_prefix="Bảng so sánh đối đầu: ")
    add_bullet_p(doc, "Lưu danh sách từng lần đo vào file results.json trong bộ nhớ máy.", bold_prefix="Lịch sử chi tiết: ")
    add_bullet_p(doc, "Xuất toàn bộ bảng đo ra file CSV khớp 100% các cột của sheet NhatKyDo trong file Excel mẫu để đính kèm vào phụ lục báo cáo Word.", bold_prefix="Nút 'Xuất CSV': ")

    # ========================== PHẦN 5 ==========================
    add_heading_1(doc, "5. CƠ CHẾ KỸ THUẬT NỘI BỘ (DÀNH CHO BÁO CÁO MÃ NGUỒN)")

    table_tech = doc.add_table(rows=4, cols=4)
    table_tech.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_tech.autofit = False
    set_table_borders(table_tech)

    headers = ["Chỉ số đo", "Công cụ / Lớp phụ trách", "Nguyên lý kỹ thuật", "Đơn vị tính"]
    col_widths = [Inches(1.2), Inches(1.8), Inches(2.7), Inches(0.8)]

    for i, title in enumerate(headers):
        cell = table_tech.cell(0, i)
        cell.width = col_widths[i]
        set_cell_background(cell, HEX_SCARLET_DARK)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0)
        r = p.add_run(title)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    data_tech = [
        ("Frame Time, FPS, % Jank", "FrameMetricsTracker", "Window.OnFrameMetricsAvailableListener chạy trên HandlerThread riêng để không làm nặng Main Thread khi đo.", "ms, fps, %"),
        ("RAM Thực tế (PSS)", "MemorySampler", "Debug.getMemoryInfo(memInfo).totalPss: Thước đo chuẩn xác nhất trên Android gồm RAM riêng + RAM chia sẻ tỉ lệ.", "MB"),
        ("Tải CPU Tiến trình", "CpuSampler", "Process.getElapsedCpuTime() chia cho khoảng thời gian thực SystemClock.elapsedRealtime() và số nhân CPU.", "%"),
    ]

    for row_idx, row_data in enumerate(data_tech, start=1):
        bg = HEX_PEARL_CARD if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = table_tech.cell(row_idx, col_idx)
            cell.width = col_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0)
            r = p.add_run(text)
            r.font.name = "Segoe UI"
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_INK

    p_sp = doc.add_paragraph()
    format_paragraph(p_sp, space_before=4, space_after=4)

    # ========================== PHẦN 6 ==========================
    add_heading_1(doc, "6. KỊCH BẢN THỰC CHIẾN QUAY VIDEO DEMO (< 2 PHÚT)")
    add_body_p(doc, "Video demo là thành phần bắt buộc trong barem chấm điểm giữa kỳ (yêu cầu không quá 2 phút). Hãy quay màn hình điện thoại/máy ảo và thuyết minh theo kịch bản chuẩn dưới đây:")

    table_script = doc.add_table(rows=6, cols=3)
    table_script.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_script.autofit = False
    set_table_borders(table_script)

    script_widths = [Inches(1.0), Inches(2.5), Inches(3.0)]
    for i, title in enumerate(["Thời gian", "Thao tác trên màn hình", "Lời thoại thuyết minh gợi ý"]):
        cell = table_script.cell(0, i)
        cell.width = script_widths[i]
        set_cell_background(cell, HEX_SCARLET_DARK)
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0)
        r = p.add_run(title)
        r.font.name = "Segoe UI"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    script_data = [
        ("0:00 - 0:15", "Mở app tại Dashboard, chỉ vào dòng thông số thiết bị ở chân trang.", "\"Xin chào thầy cô, đây là app PAA - Phòng thí nghiệm phân tích hiệu năng của nhóm. Thiết bị đo là Pixel 7 chạy Android 14 với tần số quét 60Hz.\""),
        ("0:15 - 0:45", "Vào 1. Jank Lab. Chạy đo bản BAD (giật lag, FPS đỏ) -> Bấm Lưu. Gạt switch sang OPTIMIZED -> Chạy đo (mượt 60 FPS) -> Bấm Lưu.", "\"Đầu tiên là Jank Lab. Bản BAD decode ảnh lớn trên Main Thread làm FPS tụt xuống 25. Khi gạt sang OPTIMIZED dùng Coil và layout phẳng, danh sách cuộn siêu mượt 60 FPS.\""),
        ("0:45 - 1:15", "Vào 2. CPU Lab. Chạy đo bản BAD (đơ máy 3s) -> Bấm Lưu. Gạt sang OPTIMIZED -> Chạy đo (15ms) -> Chỉ vào thẻ xác minh -> Bấm Lưu.", "\"Tiếp theo là CPU Lab trên 30.000 số. Bản BAD O(n²) làm treo UI hơn 3 giây. Bản OPTIMIZED dùng Coroutines xử lý ngầm trong 15ms mà vẫn cùng một đáp số kiểm chứng.\""),
        ("1:15 - 1:45", "Vào 3. Memory Lab. Chạy đo bản BAD -> Bấm 'Chạy GC' (RAM không hạ). Đo bản OPTIMIZED -> Bấm 'Chạy GC' (RAM hạ ngay).", "\"Ở Memory Lab, bản BAD mở đóng 20 lần gây rò rỉ 20 Activity, GC không thu hồi được. Ở bản OPTIMIZED dùng WeakReference, RAM lập tức được giải phóng sau GC.\""),
        ("1:45 - 2:00", "Vào Màn hình Results, duyệt qua các tab module, chỉ vào cột % Cải thiện màu xanh lá -> Bấm nút 'Xuất CSV'.", "\"Cuối cùng là bảng kết quả đối chiếu Trước/Sau với mức cải thiện vượt trội, và nhóm em hỗ trợ xuất file CSV để đưa thẳng vào báo cáo.\""),
    ]

    for row_idx, row_data in enumerate(script_data, start=1):
        bg = HEX_PEARL_CARD if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, text in enumerate(row_data):
            cell = table_script.cell(row_idx, col_idx)
            cell.width = script_widths[col_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0)
            r = p.add_run(text)
            r.font.name = "Segoe UI"
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_INK

    p_sp2 = doc.add_paragraph()
    format_paragraph(p_sp2, space_before=4, space_after=4)

    # ========================== PHẦN 7 ==========================
    add_heading_1(doc, "7. BỘ CÂU HỎI VẤN ĐÁP THẦY CÔ THƯỜNG HỎI & CÁCH TRẢ LỜI")

    add_callout_box(
        doc,
        "Câu 1: Tại sao nhóm em đo RAM bằng chỉ số PSS thay vì Heap Size?",
        [
            "Trả lời: PSS (Proportional Set Size) là thước đo chuẩn xác nhất trên hệ điều hành Android. PSS bao gồm toàn bộ bộ nhớ riêng (Private Clean/Dirty) cộng với phần bộ nhớ chia sẻ với các tiến trình khác (được chia đều theo tỉ lệ).",
            "Nếu chỉ đo Java Heap, ta sẽ bỏ sót hoàn toàn phần bộ nhớ đồ họa (Graphic buffers) và bộ nhớ Native của Bitmap, vốn là nguyên nhân chính gây tràn bộ nhớ (OOM) trên Android."
        ],
        border_hex=HEX_OPT_BORDER,
        bg_hex=HEX_OPT_BG
    )

    add_callout_box(
        doc,
        "Câu 2: Hai thuật toán CPU khác nhau thì làm sao chứng minh tối ưu đúng?",
        [
            "Trả lời: Để việc đo lường khoa học và khách quan, hai thuật toán giải cùng một bài toán tìm phần tử trùng trên cùng một tập dữ liệu cố định (cpu_data.csv sinh với seed cố định).",
            "Thẻ xác minh (Verification Card) của PAA đã hiển thị kết quả đối chiếu: cả 2 bản đều cho ra chính xác 12.012 số trùng và tổng số 180.251.490. Điều này chứng minh thuật toán O(n) tăng tốc hơn 99% mà không làm sai lệch kết quả nghiệp vụ."
        ],
        border_hex=HEX_SCARLET,
        bg_hex=HEX_PEARL_BG
    )

    add_callout_box(
        doc,
        "Câu 3: Thẻ <profileable android:shell=\"true\" /> trong AndroidManifest có tác dụng gì?",
        [
            "Trả lời: Thẻ <profileable> cho phép các công cụ phân tích chuẩn của Google (Android Studio Profiler, Perfetto, Simpleperf) kết nối và ghi lại trace sâu trên bản build Release mà không cần bật debuggable=true.",
            "Nhờ vậy, nhóm đo đạc được số liệu hiệu năng chân thực của mã máy biên dịch tối ưu (AOT/R8) mà không bị chậm do trình gỡ lỗi (debugger overhead)."
        ],
        border_hex=HEX_SCARLET_DARK,
        bg_hex=HEX_PEARL_BG
    )

    # Lưu file Word (xử lý nếu file đang được mở trong Microsoft Word)
    try:
        doc.save(OUTPUT_DOCX)
        print("SUCCESS: File Word updated successfully at " + OUTPUT_DOCX)
    except PermissionError:
        v2_path = os.path.join(DOCS_DIR, "Huong_Dan_Toan_Dien_PAA_v2.docx")
        doc.save(v2_path)
        print("NOTICE: File dang mo trong Word, da luu ban moi nhat tai: " + v2_path)


if __name__ == "__main__":
    build_document()
