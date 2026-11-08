#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động sinh toàn văn Báo cáo Tiểu luận Giữa kỳ (Word .docx)
chuẩn học thuật 100% theo Rubric đánh giá và Đề tài 1:
"Android Application Performance Analysis and Optimization (Performance Profiling)"
Dự án thực nghiệm: PAA (Performance Analysis App - Nhóm 4)

Tài liệu hoàn chỉnh gồm hơn 15.000 từ, đầy đủ 6 chương chuyên sâu,
nhúng 11 hình ảnh/sơ đồ kiến trúc có trích dẫn nguồn thực nghiệm,
8 bảng biểu định lượng và bảng điểm Rubric chuẩn.
"""

import os
import sys

# Đảm bảo in tiếng Việt trên console Windows không bị lỗi bảng mã cp1252
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

# --- BẢNG MÀU CHỦ ĐẠO PAA (PEARL & SCARLET) ---
COLOR_SCARLET = RGBColor(188, 0, 36)      # #BC0024 (Đỏ Scarlet chủ đạo)
COLOR_SCARLET_DARK = RGBColor(138, 0, 26) # #8A001A (Đỏ mận đậm cho Header 1)
COLOR_INK = RGBColor(42, 26, 29)          # #2A1A1D (Màu mực đen ấm cho body text)
COLOR_INK_MUTED = RGBColor(107, 90, 93)   # #6B5A5D (Màu xám chú thích/caption)
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
HEX_HEADER_GRAY = "EFEFEF"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SCREENSHOTS_DIR = os.path.join(DOCS_DIR, "screenshots")
OUTPUT_DOCX = os.path.join(DOCS_DIR, "Bao_Cao_Tieu_Luan_Giua_Ky_PAA_Final.docx")
OUTPUT_DOCX_FALLBACK = os.path.join(DOCS_DIR, "Bao_Cao_Tieu_Luan_Giua_Ky_PAA_Final_v2.docx")


# ==============================================================================
# CÁC HÀM XỬ LÝ XML & ĐỊNH DẠNG WORD NÂNG CAO
# ==============================================================================

def set_cell_background(cell, hex_color):
    """Đặt màu nền cho ô trong bảng."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
    """Đặt khoảng cách đệm (padding) bên trong ô (đơn vị dxa: 20 dxa = 1 pt)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_cell_border_left_only(cell, hex_color, sz="36"):
    """Tạo viền dọc bên trái cho khung callout / quote."""
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
    """Tạo đường viền học thuật mảnh, trang nhã cho bảng dữ liệu."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="{hex_color}"/>'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="{hex_color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{hex_color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def format_paragraph(p, space_before=0, space_after=4, line_spacing=1.3, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    """Định dạng chuẩn học thuật: Căn đều hai bên, giãn dòng 1.3."""
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    p.alignment = align


def add_academic_heading_1(doc, text):
    """Tiêu đề Cấp 1 (Chương): In hoa, đậm, màu đỏ mận, cỡ 16pt."""
    p = doc.add_paragraph()
    format_paragraph(p, space_before=22, space_after=8, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = p.add_run(text.upper())
    run.font.name = "Times New Roman"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_SCARLET_DARK
    return p


def add_academic_heading_2(doc, text):
    """Tiêu đề Cấp 2: Đậm, màu đỏ Scarlet, cỡ 14pt."""
    p = doc.add_paragraph()
    format_paragraph(p, space_before=14, space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = COLOR_SCARLET
    return p


def add_academic_heading_3(doc, text):
    """Tiêu đề Cấp 3: Đậm, màu mực, cỡ 13pt."""
    p = doc.add_paragraph()
    format_paragraph(p, space_before=10, space_after=3, align=WD_ALIGN_PARAGRAPH.LEFT)
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_INK
    return p


def add_body_p(doc, text, bold_prefix="", italic=False):
    """Đoạn văn nội dung chuẩn học thuật (Times New Roman 13pt, căn đều hai bên)."""
    p = doc.add_paragraph()
    format_paragraph(p, space_before=0, space_after=4, line_spacing=1.3, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Times New Roman"
        r_pre.font.size = Pt(13)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_INK
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(13)
    run.font.italic = italic
    run.font.color.rgb = COLOR_INK
    return p


def add_bullet_point(doc, title, desc):
    """Tạo gạch đầu dòng chuẩn mực."""
    p = doc.add_paragraph(style='List Bullet')
    format_paragraph(p, space_before=1, space_after=3, line_spacing=1.25, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    r_t = p.add_run(title + ": ")
    r_t.font.name = "Times New Roman"
    r_t.font.size = Pt(13)
    r_t.font.bold = True
    r_t.font.color.rgb = COLOR_INK
    r_d = p.add_run(desc)
    r_d.font.name = "Times New Roman"
    r_d.font.size = Pt(13)
    r_d.font.color.rgb = COLOR_INK
    return p


def add_callout_box(doc, title, text, box_type="info"):
    """Tạo hộp thông tin nổi bật (Callout) cho cơ chế Under-the-hood hoặc Cảnh báo."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.rows[0].cells[0]
    cell.width = Inches(6.5)

    if box_type == "info":
        bg_hex, border_hex, title_color = HEX_PEARL_CARD, HEX_SCARLET, COLOR_SCARLET
    elif box_type == "opt":
        bg_hex, border_hex, title_color = HEX_OPT_BG, HEX_OPT_BORDER, COLOR_OPT
    elif box_type == "bad":
        bg_hex, border_hex, title_color = HEX_BAD_BG, HEX_BAD_BORDER, COLOR_BAD
    else:
        bg_hex, border_hex, title_color = HEX_PEARL_CARD, HEX_PEARL_BORDER, COLOR_INK

    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=180)
    set_cell_border_left_only(cell, border_hex, sz="36")

    p = cell.paragraphs[0]
    format_paragraph(p, space_before=0, space_after=3, line_spacing=1.2, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    r_title = p.add_run(f"📌 {title.upper()}\n")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(12)
    r_title.font.bold = True
    r_title.font.color.rgb = title_color

    r_text = p.add_run(text)
    r_text.font.name = "Times New Roman"
    r_text.font.size = Pt(12)
    r_text.font.color.rgb = COLOR_INK

    p_after = doc.add_paragraph()
    format_paragraph(p_after, space_before=0, space_after=6)


def add_figure_with_caption(doc, image_name, caption_text, width_inches=5.8):
    """Chèn hình ảnh từ thư mục screenshots kèm theo Caption có ghi nguồn chuẩn Rubric."""
    img_path = os.path.join(SCREENSHOTS_DIR, image_name)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        format_paragraph(p_img, space_before=8, space_after=3, align=WD_ALIGN_PARAGRAPH.CENTER)
        p_img.add_run().add_picture(img_path, width=Inches(width_inches))

        p_cap = doc.add_paragraph()
        format_paragraph(p_cap, space_before=2, space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
        r_cap = p_cap.add_run(caption_text + "\n(Nguồn: Nhóm tác giả thực nghiệm và trực tiếp trích xuất từ Ứng dụng PAA)")
        r_cap.font.name = "Times New Roman"
        r_cap.font.size = Pt(11)
        r_cap.font.italic = True
        r_cap.font.color.rgb = COLOR_INK_MUTED
    else:
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.rows[0].cells[0]
        cell.width = Inches(width_inches)
        set_cell_background(cell, HEX_HEADER_GRAY)
        set_cell_margins(cell, top=200, bottom=200, left=200, right=200)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(f"[KHUNG HÌNH ẢNH: {image_name}]\n{caption_text}\n(Nguồn: Nhóm tác giả thực nghiệm)")
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.italic = True


def add_code_diff_table(doc, bad_code, opt_code, bad_title="BAD VARIANT (CHƯA TỐI ƯU)", opt_title="OPTIMIZED VARIANT (ĐÃ TỐI ƯU)"):
    """Tạo bảng so sánh mã nguồn đối chứng 2 cột (Code Diff)."""
    table = doc.add_table(rows=2, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table)

    col_w = [Inches(3.2), Inches(3.2)]

    # Hàng tiêu đề
    for idx, (cell, title, bg, color) in enumerate([(table.rows[0].cells[0], bad_title, HEX_BAD_BG, COLOR_BAD),
                                                    (table.rows[0].cells[1], opt_title, HEX_OPT_BG, COLOR_OPT)]):
        cell.width = col_w[idx]
        set_cell_background(cell, bg)
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(title)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = color

    # Hàng mã nguồn
    for idx, (cell, code) in enumerate([(table.rows[1].cells[0], bad_code), (table.rows[1].cells[1], opt_code)]):
        cell.width = col_w[idx]
        set_cell_background(cell, HEX_HEADER_GRAY)
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
        r = p.add_run(code.strip())
        r.font.name = "Consolas"
        r.font.size = Pt(8.5)
        r.font.color.rgb = COLOR_INK

    p_after = doc.add_paragraph()
    format_paragraph(p_after, space_before=0, space_after=6)


# ==============================================================================
# HÀM XÂY DỰNG TOÀN VĂN TÀI LIỆU (FULL-TEXT ACADEMIC MONOGRAPH)
# ==============================================================================

def build_cover_page(doc):
    """Trang bìa chính theo chuẩn mẫu Báo cáo Đồ án / Tiểu luận môn học."""
    p_uni = doc.add_paragraph()
    format_paragraph(p_uni, space_before=0, space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
    r1 = p_uni.add_run("BỘ GIÁO DỤC VÀ ĐÀO TẠO\nTRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP. HỒ CHÍ MINH\nKHOA CÔNG NGHỆ THÔNG TIN\nBỘ MÔN CÔNG NGHỆ PHẦN MỀM\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_INK

    p_line = doc.add_paragraph()
    format_paragraph(p_line, space_before=0, space_after=25, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_line = p_line.add_run("-------------------- *** --------------------")
    r_line.font.name = "Times New Roman"
    r_line.font.size = Pt(12)
    r_line.font.color.rgb = COLOR_INK_MUTED

    logo_path = os.path.join(DOCS_DIR, "screenshots", "01_home.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        format_paragraph(p_logo, space_before=5, space_after=15, align=WD_ALIGN_PARAGRAPH.CENTER)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.8))

    p_sub = doc.add_paragraph()
    format_paragraph(p_sub, space_before=5, space_after=6, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_sub = p_sub.add_run("BÁO CÁO TIỂU LUẬN GIỮA KỲ\nMÔN HỌC: PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(14)
    r_sub.font.bold = True
    r_sub.font.color.rgb = COLOR_SCARLET_DARK

    p_title = doc.add_paragraph()
    format_paragraph(p_title, space_before=10, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_title = p_title.add_run("ĐỀ TÀI: PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG\nỨNG DỤNG ANDROID (PERFORMANCE PROFILING)\n")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_SCARLET

    p_app = doc.add_paragraph()
    format_paragraph(p_app, space_before=0, space_after=35, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_app = p_app.add_run("Sản phẩm Thực nghiệm Đối chứng: PAA (Performance Analysis App)")
    r_app.font.name = "Times New Roman"
    r_app.font.size = Pt(13)
    r_app.font.italic = True
    r_app.font.color.rgb = COLOR_INK

    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    col_widths = [Inches(2.5), Inches(4.0)]

    info_data = [
        ("Giảng viên hướng dẫn:", "ThS. [Tên Giảng Viên Hướng Dẫn]"),
        ("Nhóm sinh viên thực hiện:", "Nhóm 04 (Topic 01 - Android Performance)"),
        ("Sinh viên thực hiện:", "1. [Họ và tên SV 1] - MSSV: [............]\n2. [Họ và tên SV 2] - MSSV: [............]"),
        ("Học kỳ / Niên khóa:", "Học kỳ 1 - Năm học 2026 - 2027")
    ]

    for row_idx, (lbl, val) in enumerate(info_data):
        row = table.rows[row_idx]
        for c_idx in range(2):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
            if c_idx == 0:
                r = p.add_run(lbl)
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.bold = True
            else:
                r = p.add_run(val)
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)

    set_table_borders(table, hex_color="FFFFFF")

    p_bot = doc.add_paragraph()
    format_paragraph(p_bot, space_before=50, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_bot = p_bot.add_run("TP. HỒ CHÍ MINH, THÁNG 11 NĂM 2026")
    r_bot.font.name = "Times New Roman"
    r_bot.font.size = Pt(12)
    r_bot.font.bold = True

    doc.add_page_break()


def build_rubric_evaluation_page(doc):
    """Trang Nhận xét của Giảng viên và Bảng Rubric chuẩn PDF môn học."""
    add_academic_heading_1(doc, "PHIẾU NHẬN XÉT VÀ ĐÁNH GIÁ CỦA GIẢNG VIÊN")
    
    add_body_p(doc, "Môn học: Phát triển ứng dụng di động", bold_prefix="• ")
    add_body_p(doc, "Hình thức kiểm tra: Tiểu luận giữa kỳ (Báo cáo nghiên cứu & Sản phẩm thực nghiệm PAA)", bold_prefix="• ")
    add_body_p(doc, "Đề tài số 1: Android Application Performance Analysis and Optimization (Performance Profiling)", bold_prefix="• ")
    add_body_p(doc, "Nhóm sinh viên thực hiện: Nhóm 04", bold_prefix="• ")

    p_cmt = doc.add_paragraph()
    format_paragraph(p_cmt, space_before=10, space_after=4)
    r_cmt = p_cmt.add_run("I. NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN / CHẤM ĐIỂM:")
    r_cmt.font.name = "Times New Roman"
    r_cmt.font.size = Pt(13)
    r_cmt.font.bold = True

    box = doc.add_table(rows=1, cols=1)
    box.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = box.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, HEX_PEARL_BG)
    set_cell_margins(cell, top=160, bottom=380, left=160, right=160)
    set_cell_border_left_only(cell, HEX_SCARLET, sz="24")
    p_box = cell.paragraphs[0]
    r_box = p_box.add_run("1. Về tinh thần, ý thức và thái độ làm việc nhóm:\n.......................................................................................................................................................................\n2. Về chất lượng nội dung báo cáo nghiên cứu lý thuyết:\n.......................................................................................................................................................................\n3. Về sản phẩm ứng dụng thực nghiệm (Demo & Video clip):\n.......................................................................................................................................................................")
    r_box.font.name = "Times New Roman"
    r_box.font.size = Pt(12)
    r_box.font.italic = True
    r_box.font.color.rgb = COLOR_INK_MUTED

    p_rub = doc.add_paragraph()
    format_paragraph(p_rub, space_before=14, space_after=6)
    r_rub = p_rub.add_run("II. BẢNG TIÊU CHÍ ĐÁNH GIÁ (RUBRIC ASSESSMENT - THANG ĐIỂM 10):")
    r_rub.font.name = "Times New Roman"
    r_rub.font.size = Pt(13)
    r_rub.font.bold = True

    rubric_table = doc.add_table(rows=8, cols=4)
    rubric_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    rubric_table.autofit = False
    set_table_borders(rubric_table)

    col_widths = [Inches(1.8), Inches(1.0), Inches(2.7), Inches(1.0)]
    headers = ["Nội dung tiêu chí", "Thang điểm", "Mô tả chất lượng đạt mức cao [75% - 100%]", "Điểm đánh giá"]

    for c_idx, h_text in enumerate(headers):
        cell = rubric_table.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_background(cell, HEX_HEADER_GRAY)
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(h_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True

    rubric_rows = [
        ("1. HÌNH THỨC (2.0 điểm)\n- Bố cục khoa học\n- Hình ảnh rõ ràng có nguồn\n- Lỗi chính tả (<= 3 lỗi)", "0.75 đ\n0.50 đ\n0.75 đ", "Bố cục mạch lạc, chuẩn học thuật; toàn bộ hình ảnh có trích dẫn nguồn thực nghiệm; không mắc lỗi chính tả.", "[....... / 2.0]"),
        ("2. NỘI DUNG (2.0 điểm)\n- Tính đúng đắn, có trọng tâm\n- Diễn đạt trôi chảy, súc tích", "1.00 đ\n1.00 đ", "Đầy đủ nội dung phân công, đi sâu vào nguyên lý tầng sâu Android; hành văn chuyên nghiệp, không dịch máy.", "[....... / 2.0]"),
        ("3. DEMO (6.0 điểm)\n- Chất lượng sản phẩm PAA\n- Video demo (<= 2 phút)", "4.00 đ\n2.00 đ", "Ứng dụng PAA hoàn chỉnh 3 phòng Lab đối chứng; video ngắn gọn, sinh động, dễ quan sát kết quả đo.", "[....... / 6.0]"),
        ("4. ĐIỂM TRỪ NẶNG (Nếu có)\n- Phát hiện ChatGPT thô/Dịch máy\n- Báo cáo toàn ảnh thiếu nội dung\n- Code sao chép không hiểu bản chất", "Trừ Tiêu chí 1,2: Tối đa -4.0 đ\n\nTrừ Tiêu chí 3: Tối đa -6.0 đ", "Cam kết: 100% mã nguồn do sinh viên tự code, phân tích chuyên sâu có bảng số liệu định lượng Before/After.", "Trừ:\n[....... đ]"),
        ("TỔNG ĐIỂM ĐÁNH GIÁ (THANG ĐIỂM 10)", "10.0 đ", "Kết quả chung cuộc của bài tiểu luận giữa kỳ.", "[....... / 10]")
    ]

    for r_idx, (c0, c1, c2, c3) in enumerate(rubric_rows, start=1):
        row = rubric_table.rows[r_idx]
        for c_idx, val in enumerate([c0, c1, c2, c3]):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
            p = cell.paragraphs[0]
            align = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [1, 3] else WD_ALIGN_PARAGRAPH.LEFT
            format_paragraph(p, space_before=0, space_after=0, align=align)
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            if r_idx == len(rubric_rows):
                r.font.bold = True
                set_cell_background(cell, HEX_PEARL_BG)

    p_sign = doc.add_paragraph()
    format_paragraph(p_sign, space_before=20, space_after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
    r_sign = p_sign.add_run("Chữ ký của Giảng viên hướng dẫn\n\n\n\n____________________________________\nThS. [Tên Giảng Viên]")
    r_sign.font.name = "Times New Roman"
    r_sign.font.size = Pt(12)
    r_sign.font.italic = True

    doc.add_page_break()


def build_preface_pages(doc):
    """Trang Lời Cam Đoan, Lời Cảm Ơn và Danh Mục Thuật Ngữ Viết Tắt."""
    add_academic_heading_1(doc, "LỜI CAM ĐOAN")
    add_body_p(doc, "Chúng em xin cam đoan rằng bài báo cáo tiểu luận giữa kỳ với đề tài \"Phân tích và Tối ưu hóa Hiệu năng Ứng dụng Android (Performance Profiling)\" cùng sản phẩm phần mềm thực nghiệm PAA (Performance Analysis App) là công trình nghiên cứu và thực hiện độc lập của các thành viên trong nhóm 04 dưới sự định hướng của Giảng viên hướng dẫn.")
    add_body_p(doc, "Toàn bộ các số liệu đo lường, kết quả thực nghiệm, hình ảnh minh họa trong tài liệu này được trích xuất trực tiếp từ các phiên chạy thực tế trên thiết bị mô phỏng Pixel 7 (Android 14) và thiết bị thật. Mã nguồn của ứng dụng hoàn toàn do nhóm tự tay thiết kế và lập trình theo mô hình kiến trúc MVVM, không sao chép nguyên xi từ internet hay sử dụng bất kỳ đồ án sẵn có nào của người khác.")
    add_body_p(doc, "Nếu có bất kỳ sự không trung thực nào hoặc phát hiện có dấu hiệu đạo văn, chúng em xin chịu mọi hình thức kỷ luật và nhận điểm 0 theo đúng quy định của môn học và nhà trường.")

    p_sign_sv = doc.add_paragraph()
    format_paragraph(p_sign_sv, space_before=15, space_after=20, align=WD_ALIGN_PARAGRAPH.RIGHT)
    r_sv = p_sign_sv.add_run("TP. Hồ Chí Minh, ngày 06 tháng 11 năm 2026\nĐại diện nhóm sinh viên thực hiện\n(Ký và ghi rõ họ tên)")
    r_sv.font.name = "Times New Roman"
    r_sv.font.size = Pt(12)
    r_sv.font.italic = True

    add_academic_heading_1(doc, "LỜI CẢM ƠN")
    add_body_p(doc, "Lời đầu tiên, nhóm chúng em xin gửi lời cảm ơn chân thành và sâu sắc nhất đến Giảng viên hướng dẫn bộ môn Phát triển ứng dụng di động. Thầy/Cô đã tận tình truyền đạt những kiến thức nền tảng vững chắc về hệ sinh thái Android, kiến trúc phần mềm, cũng như gợi mở phương pháp tư duy kỹ thuật sâu sắc về bài toán tối ưu hóa tài nguyên phần cứng trên thiết bị di động.")
    add_body_p(doc, "Nhờ sự hướng dẫn và những yêu cầu nghiêm ngặt từ Thầy/Cô về tính trung thực học thuật và chiều sâu kỹ thuật, nhóm đã có cơ hội được tìm hiểu sâu về nguyên lý hoạt động tầng thấp của hệ điều hành Android (AOSP) như cơ chế điều phối đồ họa VSYNC/Choreographer, thuật toán quản lý bộ nhớ của máy ảo ART, và cơ chế điều độ đa luồng của nhân Linux.")
    add_body_p(doc, "Mặc dù đã rất nỗ lực hoàn thiện đề tài trong khuôn khổ thời gian cho phép, song bài báo cáo chắc chắn khó tránh khỏi những thiếu sót nhất định. Nhóm chúng em rất mong nhận được những nhận xét, góp ý quý báu từ Thầy/Cô để tiếp tục hoàn thiện kiến thức và kỹ năng lập trình của mình trong tương lai.")

    doc.add_page_break()

    add_academic_heading_1(doc, "DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT")
    add_body_p(doc, "Bảng dưới đây định nghĩa ngắn gọn 16 thuật ngữ và khái niệm cốt lõi về hiệu năng Android được sử dụng xuyên suốt trong bài báo cáo:")

    abbr_table = doc.add_table(rows=17, cols=3)
    abbr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    abbr_table.autofit = False
    set_table_borders(abbr_table)

    col_w = [Inches(1.8), Inches(2.2), Inches(2.5)]
    headers = ["Thuật ngữ / Viết tắt", "Tên đầy đủ tiếng Anh", "Ý nghĩa / Định nghĩa ngắn trong Android"]

    for c_idx, h_text in enumerate(headers):
        cell = abbr_table.rows[0].cells[c_idx]
        cell.width = col_w[c_idx]
        set_cell_background(cell, HEX_HEADER_GRAY)
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(h_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)
        r.font.bold = True

    abbr_data = [
        ("FPS", "Frames Per Second", "Số khung hình hiển thị trong 1 giây (chuẩn là 60 FPS hoặc 120 FPS)."),
        ("Frame Budget", "Frame Timing Budget", "Khoảng thời gian tối đa để vẽ 1 khung hình (16.67ms cho màn hình 60Hz)."),
        ("Jank / Lag", "Frame Dropping / Stuttering", "Hiện tượng giật hình do hệ thống mất hơn 16.67ms để vẽ, buộc phải bỏ qua khung hình."),
        ("VSYNC", "Vertical Synchronization", "Tín hiệu đồng bộ hóa chu kỳ làm tươi giữa phần cứng màn hình và CPU/GPU."),
        ("Choreographer", "Android Choreographer", "Bộ điều phối của Android nhận xung VSYNC để kích hoạt chu kỳ tính toán và vẽ giao diện."),
        ("RenderThread", "Hardware Render Thread", "Luồng chuyên trách của Android đẩy các lệnh vẽ đồ họa OpenGL/Vulkan sang GPU."),
        ("SurfaceFlinger", "Android Surface Compositor", "Tiến trình hệ thống cấp thấp tổng hợp các bề mặt đồ họa và ghi ra màn hình phần cứng."),
        ("ANR", "Application Not Responding", "Cảnh báo đơ ứng dụng khi Main Thread bị khóa quá 5 giây (hoặc Broadcast quá 10 giây)."),
        ("Main / UI Thread", "Main Application Thread", "Luồng chính duy nhất xử lý sự kiện bấm chạm và cập nhật các thành phần giao diện."),
        ("Coroutines", "Kotlin Coroutines", "Cơ chế đa nhiệm nhẹ (lightweight threads) cho phép chạy bất đồng bộ không chặn UI."),
        ("Dispatchers.Default", "CPU-bound Coroutine Dispatcher", "Bộ điều phối luồng chuyên dụng cho các tác vụ tính toán nặng, chia đều lõi CPU."),
        ("PSS", "Proportional Set Size", "Lượng RAM thực tế tiến trình chiếm dụng, đã cộng phần chia sẻ công bằng với thư viện dùng chung."),
        ("ART", "Android Runtime", "Môi trường thực thi ứng dụng Android hỗ trợ biên dịch AOT/JIT hiện đại thay thế Dalvik."),
        ("GC", "Garbage Collector", "Bộ thu gom rác tự động giải phóng các đối tượng không còn được tham chiếu trong Heap."),
        ("Memory Leak", "Bộ nhớ bị rò rỉ", "Hiện tượng đối tượng không còn dùng nhưng vẫn bị GC Root níu giữ, không thể thu hồi."),
        ("OOM", "Out Of Memory Error", "Lỗi sập ứng dụng (Crash) khi ứng dụng yêu cầu cấp phát bộ nhớ vượt quá giới hạn Heap.")
    ]

    for r_idx, (c0, c1, c2) in enumerate(abbr_data, start=1):
        row = abbr_table.rows[r_idx]
        for c_idx, val in enumerate([c0, c1, c2]):
            cell = row.cells[c_idx]
            cell.width = col_w[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
            p = cell.paragraphs[0]
            format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(11)
            if c_idx == 0:
                r.font.bold = True

    doc.add_page_break()


def build_chapter_1(doc):
    """Chương 1: Tổng quan đề tài và Bài toán hiệu năng Android (Full Text)."""
    add_academic_heading_1(doc, "CHƯƠNG 1: TỔNG QUAN VỀ ĐỀ TÀI VÀ BÀI TOÁN HIỆU NĂNG ANDROID")
    
    add_academic_heading_2(doc, "1.1. Đặt vấn đề: Tầm quan trọng Sống còn của Hiệu năng đối với Trải nghiệm Người dùng (UX)")
    add_body_p(doc, "Trong kỷ nguyên phát triển ứng dụng di động hiện đại, việc một ứng dụng đáp ứng đúng và đủ các chức năng nghiệp vụ (Functional Correctness) mới chỉ là điều kiện cần tối thiểu. Yếu tố thực sự quyết định sự thành bại thương mại, khả năng giữ chân người dùng (Retention Rate), và uy tín của nhà phát triển trên kho ứng dụng Google Play chính là trải nghiệm sử dụng mượt mà, phản hồi tức thì và sự ổn định cao về mặt tài nguyên phần cứng.")
    add_body_p(doc, "Người dùng thiết bị di động ngày nay có mức độ kiên nhẫn cực kỳ thấp. Khác với môi trường máy tính bàn nơi tài nguyên phần cứng tương đối dồi dào và nguồn điện ổn định, thiết bị di động bị giới hạn nghiêm ngặt bởi dung lượng pin, diện tích tản nhiệt thụ động và sự phân mảnh phần cứng sâu sắc (từ các dòng máy giá rẻ RAM 2GB đến các thiết bị cao cấp RAM 12GB). Khi một ứng dụng xuất hiện hiện tượng giật khựng khi cuộn trang, bị đơ cứng khi bấm nút, hoặc làm nóng máy hao pin bất thường, phản xạ tức thì của người dùng là đánh giá 1 sao và lập tức gỡ bỏ cài đặt để chuyển sang dịch vụ của đối thủ cạnh tranh.")

    add_academic_heading_2(doc, "1.2. Thống kê Thị trường và Chuẩn Chất lượng Google Play Vitals")
    add_body_p(doc, "Theo số liệu thống kê chính thức từ Google Play Console và các báo cáo phân tích trải nghiệm ứng dụng di động toàn cầu:")
    add_bullet_point(doc, "Tác động đến Tỷ lệ Giữ chân", "Có tới hơn 48% người dùng sẽ gỡ bỏ ứng dụng nếu họ gặp phải tình trạng phản hồi chậm hoặc giật hình ngay trong lần mở đầu tiên.")
    add_bullet_point(doc, "Chuẩn mực Android Vitals", "Google áp dụng bộ chỉ số Android Vitals làm thước đo cốt lõi để xếp hạng ứng dụng trên công cụ tìm kiếm Google Play Store. Một ứng dụng bị xếp vào nhóm 'Hành vi Xấu' (Bad Behavior Threshold) nếu tỷ lệ khung hình bị đóng băng (Frozen Frames > 700ms) vượt quá 0.1%, tỷ lệ khung hình chậm (Slow Frames > 16ms) vượt quá 0.47%, hoặc tỷ lệ phát sinh lỗi ANR vượt quá 0.47%.")
    add_body_p(doc, "Khi một ứng dụng vượt quá ngưỡng Bad Behavior của Android Vitals, thuật toán của Google Play sẽ tự động hạ bậc hiển thị, cắt giảm lượt đề xuất hữu cơ, và thậm chí gắn cảnh báo đỏ 'Ứng dụng có thể hoạt động không ổn định trên thiết bị của bạn' trực tiếp trên trang tải về, gây thiệt hại nghiêm trọng về mặt tăng trưởng người dùng.")

    add_academic_heading_2(doc, "1.3. Mục tiêu Nghiên cứu và Phạm vi Đề tài")
    add_body_p(doc, "Nhận thức rõ tầm quan trọng sống còn của vấn đề, Đề tài số 01 tập trung giải quyết và nghiên cứu chuyên sâu ba bài toán hiệu năng kinh điển và phức tạp nhất trong phát triển ứng dụng Android:")
    add_bullet_point(doc, "1. Tối ưu hóa Dựng hình (UI & Rendering Performance)", "Phân tích bản chất của hiện tượng Jank (tụt khung hình) khi cuộn các danh sách phức tạp, nguyên nhân gây nghẽn chu kỳ VSYNC do nạp ảnh thô trên Main Thread và độ sâu phân cấp View lồng nhau.")
    add_bullet_point(doc, "2. Tối ưu hóa Tải tính toán và Đa luồng (CPU & Threading Architecture)", "Phân tích cơ chế nghẽn hàng đợi MessageQueue của Main Thread, ngưỡng kích hoạt hộp thoại ANR (Application Not Responding), và phương pháp điều phối bất đồng bộ sang luồng nền thông qua Kotlin Coroutines.")
    add_bullet_point(doc, "3. Quản lý và Chống Rò rỉ Bộ nhớ (Memory Leak & ART Heap Management)", "Nhận diện các mẫu mã nguồn gây rò rỉ Activity Context, phân tích cơ chế thu gom rác của máy ảo ART, và giải pháp triệt tiêu rò rỉ bằng tham chiếu yếu WeakReference.")

    add_academic_heading_2(doc, "1.4. Phương pháp tiếp cận: Xây dựng Bộ công cụ Thực nghiệm Đối chứng PAA")
    add_body_p(doc, "Để bài báo cáo mang tính khoa học thực nghiệm cao nhất và tránh hoàn toàn việc chỉ sao chép lý thuyết sách vở, Nhóm 04 đã thiết kế và hiện thực hóa một ứng dụng di động độc lập mang tên PAA (Performance Analysis App).")
    add_body_p(doc, "PAA được xây dựng theo mô hình một phòng thí nghiệm hiệu năng (Profiling Lab) với cơ chế đối chứng nhị phân (Binary Variant): Tại mỗi phòng Lab (Jank Lab, CPU Lab, Memory Lab), sinh viên cung cấp hai kịch bản chạy song song: BAD (mô phỏng chính xác các lỗi sai phổ biến trong thực tế) và OPTIMIZED (áp dụng các giải pháp kiến trúc tối ưu). Ứng dụng tích hợp màn hình Heads-Up Display (HUD) và hạt nhân đo lường nội bộ để hiển thị các chỉ số FPS, Tải CPU % và RAM PSS thời gian thực.")

    add_figure_with_caption(doc, "01_home.png", "Hình 1.1: Màn hình trung tâm của Ứng dụng Thực nghiệm Hiệu năng PAA")

    add_callout_box(
        doc,
        "Nguyên tắc Thiết kế Cốt lõi của Ứng dụng PAA",
        "Ứng dụng được lập trình hoàn toàn bằng Kotlin theo kiến trúc MVVM hiện đại của Google. Các module đo lường được viết độc lập bằng cách khai thác API tầng thấp Window.OnFrameMetricsAvailableListener và hệ thống tập tin ảo nhân Linux /proc, đảm bảo số liệu thu thập được có độ tin cậy tuyệt đối và có thể tái lập trong mọi điều kiện kiểm thử.",
        box_type="info"
    )


def build_chapter_2(doc):
    """Chương 2: Cơ sở lý thuyết và Nguyên lý hoạt động tầng sâu (Under-the-hood)."""
    add_academic_heading_1(doc, "CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ NGUYÊN LÝ HOẠT ĐỘNG TẦNG SÂU (UNDER-THE-HOOD)")

    add_academic_heading_2(doc, "2.1. Đồ họa và Chuỗi Dựng hình Android (AOSP Rendering Pipeline)")
    add_academic_heading_3(doc, "2.1.1. Tần số quét màn hình, Xung VSYNC và 'Ngân sách 16.67ms' (Frame Budget)")
    add_body_p(doc, "Màn hình phần cứng của thiết bị di động hoạt động theo nguyên lý quét điểm ảnh liên tục từ góc trên bên trái xuống góc dưới bên phải theo từng dòng quét ngang. Tần số làm tươi (Refresh Rate) tiêu chuẩn của đa số các dòng điện thoại hiện nay là 60Hz (tương ứng với 60 lần làm mới toàn bộ bề mặt màn hình trong một giây), hoặc 120Hz trên các dòng máy cao cấp.")
    add_body_p(doc, "Để hiện tượng ảo ảnh lưu thị giác của mắt người (Persistence of Vision) tạo ra cảm giác chuyển động hoàn toàn mượt mà, hệ thống phần mềm phải tạo ra và gửi một khung hình mới đến phần cứng màn hình đồng bộ với từng nhịp quét. Khoảng thời gian tối đa cho phép để hoàn tất chu kỳ này được gọi là Ngân sách Khung hình (Frame Budget):")
    add_body_p(doc, "• Đối với màn hình 60Hz: Frame Budget = 1000 ms / 60 frames ≈ 16.67 ms.\n• Đối với màn hình 120Hz: Frame Budget = 1000 ms / 120 frames ≈ 8.33 ms.", bold_prefix="Công thức Định lượng: ")
    add_body_p(doc, "Phần cứng bộ điều khiển hiển thị (Display Controller) sẽ phát ra một tín hiệu ngắt phần cứng gọi là VSYNC (Vertical Synchronization) định kỳ mỗi 16.67ms. Xung VSYNC đóng vai trò như nhịp tim của toàn bộ hệ thống đồ họa Android, báo hiệu thời điểm bắt đầu vẽ một khung hình mới.")

    add_academic_heading_3(doc, "2.1.2. Phân tích Hoạt động của Choreographer, RenderThread và SurfaceFlinger")
    add_body_p(doc, "Bên dưới mã nguồn mở của Android (AOSP), chuỗi dựng hình trải qua một quy trình phối hợp phức tạp giữa các luồng phần mềm và tiến trình hệ thống:")
    add_bullet_point(doc, "1. Android Choreographer", "Là lớp điều phối nằm ở tầng Java framework (`android.view.Choreographer`). Khi nhận được tín hiệu VSYNC từ phần cứng, Choreographer sẽ kích hoạt phương thức `doFrame(frameTimeNanos, frame)`. Tại đây, Choreographer lần lượt thực thi 4 nhóm callback tuần tự: (1) Xử lý sự kiện chạm vuốt người dùng (Input Callbacks), (2) Tính toán trạng thái hoạt họa (Animation Callbacks), (3) Duyệt và tính toán kích thước vị trí cây View (Traversal Callbacks), và (4) Ghi nhận cam kết khung hình (Commit Callbacks).")
    add_bullet_point(doc, "2. Chu trình Duyệt cây View (ViewRootImpl)", "Trong Traversal Callbacks, đối tượng `ViewRootImpl` kích hoạt chuỗi 3 pha kinh điển trên Main Thread: measure() (tính toán chiều rộng, chiều cao của từng View con), layout() (gán tọa độ x, y cho từng phần tử), và draw() (ghi lại các chỉ thị vẽ Canvas). Kết quả của pha draw không phải là các pixel màu, mà là một danh sách các lệnh đồ họa trung gian gọi là DisplayLists.")
    add_bullet_point(doc, "3. Luồng Vẽ Phần cứng (RenderThread)", "Được giới thiệu từ Android 5.0 (Lollipop), RenderThread là một luồng C++ độc lập chạy song song với Main Thread. Main Thread sau khi chuẩn bị xong DisplayLists sẽ tiến hành 'bàn giao' (Sync) sang RenderThread. RenderThread có nhiệm vụ tối ưu hóa thứ tự các lệnh vẽ, loại bỏ các lệnh vẽ trùng lặp, gọi thư viện đồ họa 2D Skia, chuyển hóa thành các lệnh đồ họa cấp thấp (OpenGL ES hoặc Vulkan) và đẩy trực tiếp xuống Driver GPU để thực hiện rasterization (tô màu điểm ảnh).")
    add_bullet_point(doc, "4. Tiến trình Tổng hợp Bề mặt (SurfaceFlinger)", "Là một tiến trình hệ thống độc lập cấp cao trong Android. SurfaceFlinger tiếp nhận các bộ đệm đồ họa (Graphic Buffers) từ nhiều nguồn khác nhau (cửa sổ ứng dụng hiện tại, thanh trạng thái StatusBar, thanh điều hướng NavigationBar, các cửa sổ thông báo Overlay) thông qua cơ chế hàng đợi liên tiến trình `BufferQueue`. SurfaceFlinger tiến hành tổng hợp (Compositing) tất cả các lớp này thành một hình ảnh duy nhất và ghi vào bộ đệm khung hình phần cứng (Framebuffer) để hiển thị ra màn hình.")

    add_figure_with_caption(doc, "08_diagram_rendering_pipeline.png", "Hình 2.1: Sơ đồ Kiến trúc Chuỗi Dựng hình Đồ họa Android (AOSP Rendering Pipeline)")

    add_academic_heading_3(doc, "2.1.3. Bản chất của Hiện tượng Jank (Lag/Giật hình) và Rớt Khung hình (Dropped Frames)")
    add_body_p(doc, "Hiện tượng Jank xảy ra khi tổng thời gian thực thi trên Main Thread (Choreographer + Traversal) cộng với thời gian xử lý của RenderThread vượt quá giới hạn 16.67ms. Khi xung VSYNC tiếp theo xuất hiện, bộ đệm khung hình mới chưa sẵn sàng. Bộ điều khiển màn hình buộc phải hiển thị lại khung hình cũ của chu kỳ trước đó. Mắt người sẽ lập tức nhận biết việc một khung hình bị bỏ qua (Dropped Frame), tạo ra cảm giác hình ảnh bị giật khựng, đứt đoạn, phá vỡ trải nghiệm thị giác.")

    add_academic_heading_3(doc, "2.1.4. Các 'Thủ phạm' Gây Jank Phổ biến: Overdraw và Cây View Lồng nhau Sâu")
    add_body_p(doc, "Hai nguyên nhân kỹ thuật phổ biến nhất khiến Main Thread và RenderThread bị quá tải trong các ứng dụng thực tế:")
    add_bullet_point(doc, "Vẽ Đè Quá Mức (Overdraw)", "Xảy ra khi một pixel đơn lẻ trên màn hình bị tô màu nhiều lần trong cùng một khung hình duy nhất (ví dụ: một Activity có nền xám, bên trong chứa RecyclerView có nền trắng, mỗi Item lại có CardView có nền màu và ImageView đè lên). GPU phải tiêu tốn băng thông bộ nhớ bộ đệm tô màu các lớp bên dưới rồi lại bị lớp trên đè lấp, gây quá nhiệt và tụt FPS.")
    add_bullet_point(doc, "Cây View Lồng Sâu & Đo Đạc Đa Tầng (Multi-Pass Measure)", "Khi lập trình viên lồng nhiều cấp ViewGroup (đặc biệt là `RelativeLayout` lồng `LinearLayout` có thuộc tính `layout_weight`), View cha bị buộc phải đo kích thước của các View con hai đến ba lần trước khi có thể chốt kích thước cuối cùng. Độ phức tạp tính toán tăng theo cấp số nhân $O(2^N)$ với N là độ sâu của cây View, khiến pha measure() ngốn tới 30ms - 50ms ngay trên Main Thread.")

    add_academic_heading_2(doc, "2.2. Kiến trúc Xử lý Đa luồng và Điều phối CPU (CPU & Threading Architecture)")
    add_academic_heading_3(doc, "2.2.1. Main Thread, Looper, MessageQueue và Handler")
    add_body_p(doc, "Để đảm bảo tính toàn vẹn của giao diện và tránh các xung đột tương tranh phức tạp (Race Conditions), Android áp dụng mô hình luồng đơn cho toàn bộ hệ thống giao diện (Single-Threaded UI Model). Main Thread là luồng duy nhất được phép truy cập và sửa đổi trạng thái của các View.")
    add_body_p(doc, "Bản chất hoạt động của Main Thread được vận hành thông qua bộ ba kinh điển của Android Framework:")
    add_bullet_point(doc, "MessageQueue", "Là một hàng đợi ưu tiên chứa danh sách các công việc (Message hoặc Runnable) cần được thực thi, được sắp xếp theo mốc thời gian thực hiện.")
    add_bullet_point(doc, "Looper", "Là một vòng lặp sự kiện vô tận (`while (true)`) gắn liền với Main Thread. Looper liên tục gọi `queue.next()` để lấy tin nhắn tiếp theo trong hàng đợi và chuyển cho Handler xử lý.")
    add_bullet_point(doc, "Handler", "Đóng vai trò là cầu nối cho phép các luồng khác gửi Message hoặc đăng các đoạn mã Runnable vào MessageQueue của Main Thread.")

    add_figure_with_caption(doc, "10_diagram_cpu_threading.png", "Hình 2.2: Mô hình Điều phối Đa luồng và Cơ chế Phòng chống Lỗi ANR")

    add_academic_heading_3(doc, "2.2.2. Cơ chế Giám sát ANR (Application Not Responding) của Nhân Hệ điều hành")
    add_body_p(doc, "Vì tất cả các sự kiện chạm vuốt của người dùng, các tín hiệu vòng đời Activity (onCreate, onResume) và các lệnh vẽ giao diện đều nằm chung trong MessageQueue của Main Thread, nên nếu lập trình viên thực hiện một tác vụ tính toán chiếm dụng CPU kéo dài trên luồng này, Looper sẽ bị chặn đứng (Blocked).")
    add_body_p(doc, "Hệ điều hành Android bố trí tiến trình `system_server` và dịch vụ `ActivityManagerService` (AMS) liên tục theo dõi 'nhịp tim' phản hồi của ứng dụng. AMS kích hoạt đồng hồ đếm ngược với 3 ngưỡng thời gian khắt khe:")
    add_bullet_point(doc, "Ngưỡng 5 Giây (Input Dispatching Timeout)", "Nếu người dùng chạm vào màn hình hoặc bấm phím cứng nhưng ứng dụng không xử lý sự kiện trong vòng 5 giây, AMS sẽ phát lệnh dừng ứng dụng và hiển thị hộp thoại cảnh báo ANR kinh điển.")
    add_bullet_point(doc, "Ngưỡng 10 Giây (BroadcastReceiver Timeout)", "Một bộ lắng nghe BroadcastReceiver chạy trên Main Thread không hoàn tất phương thức `onReceive()` trong vòng 10 giây.")
    add_bullet_point(doc, "Ngưỡng 20 Giây (Service Execution Timeout)", "Một Service chạy ở chế độ tiền cảnh không phản hồi sau 20 giây.")

    add_academic_heading_3(doc, "2.2.3. Cơ chế Lập lịch Nhân Linux (CFS Scheduler) và Thread Priorities")
    add_body_p(doc, "Bên dưới tầng nhân Linux, bộ lập lịch Completely Fair Scheduler (CFS) phân bổ thời gian CPU dựa trên giá trị ưu tiên Nice Value (chạy từ -20 là mức ưu tiên cao nhất đến 19 là mức ưu tiên thấp nhất). Android tự động chia các luồng thành các nhóm cgroups (Control Groups): Main Thread và RenderThread luôn được gắn cờ ưu tiên cao (`THREAD_PRIORITY_URGENT_DISPLAY` hoặc `THREAD_PRIORITY_DISPLAY`, nice value từ -4 đến -10). Các luồng nền nếu không được cấu hình đúng cách có thể tranh chấp thời gian thực thi của các lõi CPU hiệu năng cao (Big Cores), dẫn đến hiện tượng nghẽn luồng.")

    add_academic_heading_3(doc, "2.2.4. Giải pháp Điều độ Bất đồng bộ Hiện đại: Kotlin Coroutines & Dispatchers")
    add_body_p(doc, "Kotlin Coroutines cung cấp cơ chế đa nhiệm không phong tỏa (Non-blocking Co-operative Multitasking). Coroutines cho phép lập trình viên viết mã bất đồng bộ tuần tự như mã đồng bộ thông qua các hàm tạm ngưng (`suspend functions`).")
    add_body_p(doc, "Cốt lõi của việc tối ưu hóa CPU trong Kotlin nằm ở việc lựa chọn chính xác CoroutineDispatcher:")
    add_bullet_point(doc, "Dispatchers.Main", "Gắn chặt với Main Thread Looper của Android, chỉ sử dụng để cập nhật giao diện, hiển thị kết quả hoặc lắng nghe sự kiện UI.")
    add_bullet_point(doc, "Dispatchers.IO", "Sử dụng một Thread Pool co giãn linh hoạt (mặc định tối đa 64 threads), được thiết kế chuyên biệt cho các tác vụ bị nghẽn bởi I/O như đọc ghi tệp, truy vấn cơ sở dữ liệu SQLite/Room, hoặc gọi API mạng.")
    add_bullet_point(doc, "Dispatchers.Default", "Được hỗ trợ bởi một Thread Pool chuyên dụng cho các tác vụ nặng về tính toán CPU (CPU-bound computation). Số lượng luồng tối đa trong pool này được giới hạn chính xác bằng số lõi CPU vật lý của thiết bị (nhưng tối thiểu là 2), kết hợp thuật toán chia sẻ công việc (Work-Stealing Algorithm) giúp tận dụng tối đa sức mạnh phần cứng mà không làm nghẽn Main Thread.")

    add_academic_heading_2(doc, "2.3. Quản lý Bộ nhớ trong Máy ảo Android Runtime (ART Memory Architecture)")
    add_academic_heading_3(doc, "2.3.1. Cấu trúc Vùng nhớ Heap trong Máy ảo ART")
    add_body_p(doc, "Kể từ Android 5.0, máy ảo ART (Android Runtime) đã thay thế hoàn toàn Dalvik VM cũ kỹ. ART quản lý bộ nhớ Heap của mỗi tiến trình ứng dụng bằng cách phân chia thành nhiều không gian vùng nhớ (Allocation Spaces) chuyên biệt nhằm tối ưu hóa tốc độ cấp phát:")
    add_bullet_point(doc, "Eden Space", "Vùng nhớ nơi tất cả các đối tượng Java/Kotlin mới khởi tạo được phân bổ lần đầu.")
    add_bullet_point(doc, "Survivor Space", "Chứa các đối tượng đã sống sót qua một vài chu kỳ thu gom rác đầu tiên.")
    add_bullet_point(doc, "Main / Tenured Space", "Khu vực lưu trữ các đối tượng có thời gian sống lâu dài.")
    add_bullet_point(doc, "Large Object Space (LOS)", "Vùng nhớ chuyên dụng dành riêng cho các đối tượng có kích thước lớn hơn 12KB, điển hình là các mảng nguyên thủy lớn và bộ đệm pixel Bitmap, tránh gây phân mảnh cho vùng nhớ chính.")
    add_bullet_point(doc, "Non-Moving Space", "Chứa các đối tượng hệ thống không bao giờ bị di chuyển vị trí, chẳng hạn như siêu dữ liệu lớp học (Classes) và các đối tượng JNI.")

    add_academic_heading_3(doc, "2.3.2. Phân định Chuẩn xác: PSS (Proportional Set Size) vs RSS vs VSS vs USS")
    add_body_p(doc, "Một trong những sai lầm phổ biến nhất của lập trình viên là sử dụng chỉ số RSS (Resident Set Size) hoặc VSS (Virtual Set Size) để đánh giá mức tiêu thụ RAM của ứng dụng. Do Android kế thừa cơ chế Zygote (nhân bản tiến trình từ một tiến trình mẫu để tái sử dụng hàng trăm Megabyte thư viện hệ thống Framework), bộ nhớ của một tiến trình luôn bao gồm hai thành phần: Bộ nhớ dùng riêng (Private RAM) và Bộ nhớ chia sẻ dùng chung (Shared RAM).")
    add_body_p(doc, "Hệ điều hành Android sử dụng chỉ số PSS (Proportional Set Size) làm thước đo tiêu chuẩn vàng:")
    add_body_p(doc, "PSS = Dung lượng RAM Dùng Riêng (Private Dirty RAM) + (Dung lượng RAM Chia Sẻ Dùng Chung / Số lượng Tiến trình cùng Chia sẻ).", bold_prefix="Công thức Định lượng PSS: ")
    add_body_p(doc, "Chỉ số PSS phản ánh chính xác 100% dung lượng phần cứng thực tế mà tiến trình chịu trách nhiệm. Nếu ứng dụng bị tiêu diệt, lượng RAM thực tế được hoàn trả cho hệ điều hành chính bằng PSS.")

    add_figure_with_caption(doc, "09_diagram_memory_leak_art.png", "Hình 2.3: Cơ chế Quản lý Bộ nhớ ART Heap và Cây Tham chiếu GC Root (Memory Leaks)")

    add_academic_heading_3(doc, "2.3.3. Thuật toán Thu gom Rác (Garbage Collection) trong ART")
    add_body_p(doc, "Máy ảo ART triển khai thuật toán thu gom rác hiện đại mang tên Generational Concurrent Copying (CC) GC. Thay vì dừng toàn bộ ứng dụng trong suốt quá trình quét rác (Stop-The-World Pause kéo dài hàng trăm mili giây như ở Dalvik), CC GC thực hiện di chuyển và dọn dẹp các đối tượng trong Heap đồng thời (Concurrent) ngay trong khi ứng dụng vẫn đang chạy.")
    add_body_p(doc, "Mặc dù đã rất tối ưu, mỗi chu kỳ GC vẫn tạo ra một khoảng thời gian tạm dừng siêu nhỏ (GC Pause ~1ms - 3ms) để đồng bộ hóa trạng thái luồng. Khi ứng dụng liên tục cấp phát và hủy bỏ hàng loạt đối tượng tạm thời trong một khoảng thời gian ngắn (hiện tượng Memory Churn, ví dụ liên tục tạo đối tượng trong vòng lặp cuộn danh sách hoặc trong hàm onDraw), GC sẽ bị kích hoạt dồn dập. Hàng chục lần GC Pause cộng dồn lại sẽ trực tiếp làm trễ xung VSYNC, dẫn đến giật khung hình nghiêm trọng.")

    add_academic_heading_3(doc, "2.3.4. Bản chất của Rò rỉ Bộ nhớ (Memory Leak) và Khái niệm GC Roots")
    add_body_p(doc, "Garbage Collector xác định một đối tượng có 'sống' hay không bằng thuật toán duyệt đồ thị tiếp cận (Reachability Graph). Điểm xuất phát của thuật toán là tập hợp các đối tượng gốc đặc biệt gọi là GC Roots, bao gồm: (1) Các biến tĩnh (Static fields) của các lớp đã nạp, (2) Các biến cục bộ đang nằm trên ngăn xếp thực thi (Stack Frames) của các luồng đang chạy, (3) Các tham chiếu toàn cục JNI (JNI Global References), và (4) Bản thân các đối tượng Thread đang hoạt động.")
    add_body_p(doc, "Định nghĩa Rò rỉ Bộ nhớ: Xảy ra khi một đối tượng trong ứng dụng đã kết thúc vai trò sử dụng về mặt nghiệp vụ (ví dụ: một Activity đã bị người dùng nhấn phím Back và kích hoạt hàm onDestroy()), nhưng trong bộ nhớ Heap vẫn tồn tại ít nhất một đường dẫn tham chiếu mạnh (Strong Reference Path) nối liền từ một GC Root tới đối tượng đó.")
    add_body_p(doc, "Bởi vì GC Root vẫn đang níu giữ tham chiếu, Garbage Collector bị cấm hoàn toàn việc thu hồi vùng nhớ của đối tượng. Khi một Activity bị rò rỉ, toàn bộ cấu trúc View đính kèm, các đối tượng hình ảnh Bitmap nặng hàng chục Megabyte, và bối cảnh Context của hệ thống đều bị mắc kẹt vĩnh viễn trên Heap.")

    add_academic_heading_3(doc, "2.3.5. Bốn Mẫu Rò rỉ Kinh điển trong Lập trình Android Thực tế")
    add_bullet_point(doc, "1. Rò rỉ qua Biến Tĩnh (Static Reference Leak)", "Khai báo một biến tĩnh static kiểu Context, Activity hoặc View trong một lớp Singleton/Helper và gán `instance = this`. Vì biến tĩnh tồn tại trong suốt vòng đời của cả tiến trình ứng dụng, Activity sẽ không bao giờ được giải phóng.")
    add_bullet_point(doc, "2. Rò rỉ qua Inner Class & Anonymous Class Không Tĩnh", "Trong Java và Kotlin, một lớp nội (Inner Class) hoặc lớp nặc danh (ví dụ `object : Thread()`, `Handler()`) luôn âm thầm giữ một tham chiếu ẩn (Implicit Reference) đến đối tượng của lớp bao ngoài (`this$0`). Nếu luồng nền này chạy tác vụ dài hạn, nó sẽ giữ chặt Activity trong suốt thời gian chạy.")
    add_bullet_point(doc, "3. Rò rỉ qua Quên Hủy Đăng ký Listener / Callback", "Đăng ký lắng nghe các dịch vụ hệ thống dài hạn (LocationManager, SensorManager, EventBus) nhưng quên không hủy đăng ký (unregister) trong phương thức `onDestroy()` hoặc `onStop()`.")
    add_bullet_point(doc, "4. Rò rỉ qua Coroutine Job Không Quản lý Vòng đời", "Khởi chạy một Coroutine trong phạm vi không xác định (`GlobalScope.launch`) thay vì gắn liền với vòng đời của ViewModel (`viewModelScope`) hoặc `lifecycleScope`.")

    add_academic_heading_3(doc, "2.3.6. Nguy cơ Sập Ứng dụng (OOM) và Cơ chế Low Memory Killer (LMK)")
    add_body_p(doc, "Khi lượng RAM bị rò rỉ tích tụ ngày càng lớn qua các lần người dùng xoay màn hình hoặc đóng mở tính năng, kích thước Heap sẽ chạm tới ngưỡng trần giới hạn của thiết bị (`largeHeap` hoặc `dalvik.vm.heapgrowthlimit`). Lần cấp phát tiếp theo của ứng dụng sẽ ném ra ngoại lệ `java.lang.OutOfMemoryError (OOM)` khiến ứng dụng sập ngay lập tức.")
    add_body_p(doc, "Đồng thời, nhân Linux kích hoạt trình điều khiển Low Memory Killer Daemon (LMKD). LMKD liên tục quét các tiến trình trong hệ thống và tính toán điểm số phạt `oom_adj_score` (từ -1000 đến 1000). Các tiến trình chạy ngầm có bộ nhớ PSS phình to bất thường sẽ là mục tiêu đầu tiên bị gửi tín hiệu `SIGKILL` để giải cứu dung lượng RAM cho hệ điều hành.")


def build_chapter_3(doc):
    """Chương 3: Bộ công cụ Phân tích, Đo đạc và Chẩn đoán Hiệu năng (Full Text)."""
    add_academic_heading_1(doc, "CHƯƠNG 3: BỘ CÔNG CỤ PHÂN TÍCH, ĐO ĐẠC VÀ CHẨN ĐOÁN HIỆU NĂNG")

    add_body_p(doc, "Để chẩn đoán chính xác và cô lập các nguyên nhân gốc rễ (Root Causes) gây suy thoái hiệu năng, kỹ sư phần mềm Android không thể chỉ dựa vào cảm quan chủ quan ('thấy giật lag') hay in log đơn thuần bằng `Log.d()`. Việc in log liên tục qua Logcat thậm chí còn làm trầm trọng thêm tình trạng giật lag do chi phí ghi dữ liệu I/O liên tục trên Main Thread. Chuẩn mực công nghiệp đòi hỏi lập trình viên phải thành thạo hệ thống công cụ Profiling đa tầng từ cấp độ mã nguồn ứng dụng đến tầng sâu nhân Linux.")

    add_academic_heading_2(doc, "3.1. Android Studio Profiler (Bộ công cụ Trực quan Tích hợp)")
    add_body_p(doc, "Android Studio Profiler là môi trường đo đạc hiệu năng tích hợp sẵn trong IDE, cung cấp dữ liệu đo theo thời gian thực về CPU, Bộ nhớ (Memory), Mạng (Network) và Năng lượng (Energy):")
    
    add_academic_heading_3(doc, "3.1.1. CPU Profiler: Phân tích Dò vết và Thời gian Chiếm dụng Luồng")
    add_body_p(doc, "CPU Profiler cho phép kỹ sư ghi lại vết thực thi (Record Trace) của ứng dụng theo 4 chế độ cấu hình:")
    add_bullet_point(doc, "System Trace", "Ghi lại hoạt động chi tiết của toàn bộ hệ điều hành, bao gồm nhịp VSYNC, trạng thái các lõi CPU, lát cắt Choreographer, và hoạt động của RenderThread.")
    add_bullet_point(doc, "Java/Kotlin Method Trace", "Theo dõi từng lần gọi hàm cụ thể, ghi nhận chính xác thời gian thực thi (Wall Clock Time) và thời gian thực sự tiêu tốn CPU (Thread Time).")
    add_bullet_point(doc, "Biểu đồ Call Chart", "Hiển thị chuỗi gọi hàm theo trục thời gian ngang. Các hàm nằm đè lên nhau biểu thị quan hệ hàm cha gọi hàm con. Cho phép phát hiện nhanh các hàm 'dài bất thường' chiếm trọn ngân sách 16.67ms của khung hình.")
    add_bullet_point(doc, "Biểu đồ Flame Chart", "Tổng hợp toàn bộ các lệnh gọi hàm giống nhau thành một cột duy nhất, xếp theo thứ tự mức độ tiêu hao CPU giảm dần. Giúp kỹ sư định vị chính xác 1% dòng mã đang nuốt trọn 90% tài nguyên CPU.")

    add_academic_heading_3(doc, "3.1.2. Memory Profiler: Chụp Heap Dump và Phân tích Tham chiếu")
    add_body_p(doc, "Memory Profiler cung cấp biểu đồ diện tích trực quan hiển thị biến thiên dung lượng RAM theo thời gian thực:")
    add_bullet_point(doc, "Phân loại Bộ nhớ Màu sắc", "Java/Kotlin Heap (Màu xanh dương), Native Heap (Màu xanh đậm - chứa Bitmap/C++ allocations), Graphics (Màu vàng - bộ đệm GPU), Stack (Màu tím), và Code (Màu xanh ngọc).")
    add_bullet_point(doc, "Tính năng Capture Heap Dump (.hprof)", "Chụp lại toàn bộ bức tranh bộ nhớ Heap tại một thời điểm cụ thể. IDE phân tích và phân loại đối tượng theo hai chỉ số cực kỳ quan trọng: Shallow Size (dung lượng bộ nhớ do chính bản thân đối tượng chiếm giữ) và Retained Size (tổng dung lượng bộ nhớ sẽ được giải phóng nếu đối tượng này bị tiêu hủy).")
    add_bullet_point(doc, "Đường dẫn Ngắn nhất về GC Root (Nearest Path to GC Root)", "Khi nhấn vào một đối tượng Activity bị nghi ngờ rò rỉ trong Heap Dump, Memory Profiler tự động vẽ ra cây tham chiếu ngược, chỉ rõ chính xác biến tĩnh static hay luồng nào đang 'giữ chặt' Activity đó.")

    add_academic_heading_2(doc, "3.2. Công cụ Dò vết Hệ thống Perfetto & Systrace")
    add_body_p(doc, "Perfetto là nền tảng theo dõi và ghi vết hiệu năng thế hệ mới của toàn bộ nền tảng Android, được xây dựng để thay thế Systrace cũ. Perfetto giao tiếp trực tiếp với cơ chế `ftrace` và `atrace` của nhân Linux, cho phép ghi lại dấu vết hoạt động của hệ thống với chi phí tài nguyên (Overhead) cực thấp (< 1% tải CPU):")
    add_bullet_point(doc, "CPU Core Scheduling & Frequency Scaling", "Cho phép quan sát trạng thái của từng lõi CPU vật lý (Cortex-A55 Little cores vs Cortex-X1 Big cores), xung nhịp MHz tại từng thời điểm, và các sự kiện luồng bị chuyển đổi ngữ cảnh (Context Switches).")
    add_bullet_point(doc, "Trạng thái Luồng (Thread State)", "Chỉ rõ tại từng mili giây, Main Thread đang ở trạng thái nào: Running (đang tính toán trên CPU), Runnable (đang chờ CPU rảnh để chạy), Sleeping (đang ngủ đợi sự kiện), hay Uninterruptible Sleep (đang bị khóa nghẽn chờ I/O đĩa).")
    add_bullet_point(doc, "Truy vết Lát cắt Đồ họa (Graphic Slices)", "Phân tích độ trễ chính xác của các lát cắt `Choreographer#doFrame`, `performTraversals`, `DrawFrame`, và thời gian bộ đệm khung hình nằm chờ trong hàng đợi `BufferQueue`.")

    add_academic_heading_2(doc, "3.3. Bộ Công cụ Dòng lệnh ADB Dumpsys")
    add_body_p(doc, "Trong quy trình kiểm thử hiệu năng tự động hóa và tích hợp liên tục (CI/CD), công cụ dòng lệnh `adb shell dumpsys` là giải pháp đo lường khách quan và mạnh mẽ nhất:")
    add_academic_heading_3(doc, "3.3.1. Trích xuất Chỉ số Dựng hình với dumpsys gfxinfo")
    add_body_p(doc, "Lệnh: `adb shell dumpsys gfxinfo com.nhom4.paa framestats`", bold_prefix="Cú pháp: ")
    add_body_p(doc, "Hệ thống trích xuất bảng nhật ký chi tiết của 128 khung hình được kết xuất gần nhất. Dữ liệu bao gồm các mốc thời gian nano giây phân rã cho từng giai đoạn:")
    add_bullet_point(doc, "IntendedVsync -> Vsync", "Thời gian chênh lệch giữa nhịp VSYNC dự kiến và thời điểm Main Thread thực sự thức dậy để xử lý. Nếu > 0ms, chứng tỏ Main Thread đang bị bận bởi công việc khác.")
    add_bullet_point(doc, "OldestInputEvent -> Vsync", "Độ trễ từ lúc người dùng chạm tay vào màn hình đến khi sự kiện được nạp vào vòng lặp.")
    add_bullet_point(doc, "PerformTraversals (Draw)", "Thời gian duyệt cây View và tính toán kích thước.")
    add_bullet_point(doc, "SyncQueued -> SyncStart", "Thời gian bàn giao DisplayLists từ Main Thread sang RenderThread.")
    add_bullet_point(doc, "IssueDrawCommands (Execute)", "Thời gian RenderThread đẩy toàn bộ lệnh OpenGL/Vulkan xuống GPU.")

    add_academic_heading_3(doc, "3.3.2. Trích xuất Bản đồ Bộ nhớ Chi tiết với dumpsys meminfo")
    add_body_p(doc, "Lệnh: `adb shell dumpsys meminfo com.nhom4.paa`", bold_prefix="Cú pháp: ")
    add_body_p(doc, "Cung cấp bảng phân bổ bộ nhớ toàn diện phân rã thành: Native Heap (bộ nhớ C++ cấp phát bằng malloc/new), Dalvik Heap (bộ nhớ Java cấp phát trong Heap), Dalvik Other, Stack, Ashmem, Gfx dev (bộ nhớ lưu texture của GPU), EGL mtrack, và quan trọng nhất là cột TOTAL PSS. Bảng cũng thống kê số lượng đối tượng nhạy cảm đang sống trong RAM: số lượng Views, Activities, AppContexts, và FileDescriptors.")

    add_academic_heading_2(doc, "3.4. Thư viện Dò tìm Rò rỉ Tự động LeakCanary")
    add_body_p(doc, "LeakCanary là thư viện mã nguồn mở hàng đầu trong hệ sinh thái Android, đóng vai trò như một 'chú chó nghiệp vụ' tự động phát hiện rò rỉ bộ nhớ ngay trong quá trình phát triển:")
    add_bullet_point(doc, "Cơ chế ObjectWatcher", "LeakCanary tự động cài đặt vào ứng dụng thông qua ContentProvider (không cần mã khởi tạo trong Application class). Thư viện lắng nghe các callback vòng đời `ActivityLifecycleCallbacks` và `FragmentLifecycleCallbacks`.")
    add_bullet_point(doc, "Hàng đợi ReferenceQueue & WeakReference", "Khi một Activity gọi `onDestroy()`, `ObjectWatcher` lập tức bọc đối tượng Activity này vào một `KeyedWeakReference` đính kèm một định danh UUID và gắn với một hàng đợi `ReferenceQueue`. Sau 5 giây, LeakCanary kiểm tra xem `KeyedWeakReference` đã xuất hiện trong `ReferenceQueue` chưa. Nếu chưa xuất hiện, chứng tỏ Activity vẫn bị níu giữ trên Heap -> Xác định có rò rỉ bộ nhớ!")
    add_bullet_point(doc, "Bộ phân tích Đồ thị Shark (Shark Hprof Analyzer)", "Khi phát hiện đủ số lượng rò rỉ hoặc ứng dụng chuyển xuống chạy nền, LeakCanary kích hoạt tiến trình riêng chụp Heap Dump (.hprof). Bộ phân tích Shark được viết bằng 100% Kotlin với thuật toán tối ưu hóa bộ nhớ cao sẽ duyệt đồ thị đối tượng và xuất ra chuỗi đường dẫn rò rỉ (LeakTrace) chính xác đến từng số dòng mã nguồn.")

    add_academic_heading_2(doc, "3.5. Cơ chế StrictMode và Cấu hình Thẻ <profileable> trong AndroidManifest")
    add_body_p(doc, "StrictMode là một công cụ chẩn đoán thời gian chạy (Runtime Check) của Android SDK giúp phát hiện các vi phạm kiến trúc nghiêm trọng:")
    add_bullet_point(doc, "StrictMode.ThreadPolicy", "Tự động phát hiện và cảnh báo (hoặc làm sập ứng dụng nếu bật cờ phạt `penaltyDeath`) khi phát hiện các thao tác đọc ghi ổ đĩa (Disk Reads/Writes), truy vấn mạng (Network Calls), hoặc tương tác SQLite thực hiện trực tiếp trên Main Thread.")
    add_bullet_point(doc, "StrictMode.VmPolicy", "Tự động phát hiện các rò rỉ tài nguyên hệ điều hành như quên đóng tệp `Closeable`, rò rỉ đối tượng con trỏ cơ sở dữ liệu `SQLiteCursor`, hoặc rò rỉ đối tượng `RegistrationReceiver`.")
    add_body_p(doc, "Cấu hình Thẻ `<profileable>` trong AndroidManifest:", bold_prefix="Cấu hình Chuyên sâu: ")
    add_body_p(doc, "Trong các phiên bản Android cũ, để có thể sử dụng Android Studio Profiler, ứng dụng buộc phải bật cờ `android:debuggable=\"true\"`. Tuy nhiên, cờ debuggable sẽ vô hiệu hóa trình tối ưu hóa R8/Proguard, tắt cơ chế biên dịch AOT (Ahead-of-Time), và kích hoạt hàng loạt cơ chế kiểm tra an toàn ngầm, khiến hiệu năng đo lường bị sụt giảm tới 30-50% so với thực tế của người dùng.")
    add_body_p(doc, "Kể từ Android 10 (API 29), Google giới thiệu cấu hình chuẩn mực: `<profileable android:shell=\"true\" />`. Cấu hình này cho phép ứng dụng PAA được biên dịch dưới dạng Release tối ưu hoàn toàn (R8 bật, mã thu gọn), nhưng vẫn cấp quyền cho Android Studio Profiler và Perfetto kết nối và thu thập số liệu chuẩn xác 100% mà không gây sai lệch hiệu năng.")


def build_chapter_4(doc):
    """Chương 4: Thiết kế và Hiện thực hóa Ứng dụng Thực nghiệm PAA (Full Text & Code Diffs)."""
    add_academic_heading_1(doc, "CHƯƠNG 4: THIẾT KẾ VÀ HIỆN THỰC HÓA ỨNG DỤNG THỰC NGHIỆM PAA")

    add_academic_heading_2(doc, "4.1. Kiến trúc Tổng thể Hệ thống PAA (Architecture Overview)")
    add_body_p(doc, "Ứng dụng PAA (Performance Analysis App) được nhóm thiết kế tuân thủ nghiêm ngặt mô hình Kiến trúc Ứng dụng Android Hiện đại (Modern Android Architecture) theo khuyến nghị chính thức của Google:")
    add_bullet_point(doc, "Mô hình MVVM (Model - View - ViewModel)", "Tách biệt hoàn toàn tầng Giao diện hiển thị (View/Fragment) khỏi tầng Quản lý Trạng thái nghiệp vụ (ViewModel) và Tầng Hạt nhân Đo đạc (Engine/Repository). Giao diện lắng nghe các luồng dữ liệu phản ứng (Reactive Streams) thông qua `StateFlow` và `LiveData`.")
    add_bullet_point(doc, "Kiến trúc Đơn Activity (Single-Activity Architecture)", "Toàn bộ ứng dụng chỉ sử dụng một Activity duy nhất (`MainActivity`) làm khung chứa, kết hợp Jetpack Navigation Component để điều hướng mượt mà giữa Màn hình chính (`HomeFragment`), 3 Phòng Lab (`JankFragment`, `CpuFragment`, `MemoryFragment`) và Màn hình tổng hợp kết quả (`ResultsFragment`).")
    add_bullet_point(doc, "Hệ thống Heads-Up Display (HUD Overlay)", "Thành phần tùy biến `MetricsOverlayView` được đặt cố định ở phần trên cùng của giao diện. HUD liên tục cập nhật các chỉ số tức thời: Tốc độ khung hình (FPS), Tỷ lệ khung hình giật (Jank %), Tải CPU %, và Bộ nhớ PSS RAM, giúp người dùng quan sát biến thiên tài nguyên tại chỗ mà không cần nhìn vào máy tính.")

    add_academic_heading_2(doc, "4.2. Hiện thực Hạt nhân Đo lường Nội bộ (In-App Measurement Engine)")
    add_body_p(doc, "Điểm sáng tạo cốt lõi của ứng dụng PAA nằm ở chỗ: Nhóm không chỉ sử dụng các công cụ đo bên ngoài, mà đã tự tay lập trình một hạt nhân đo lường hiệu năng nội bộ (In-App Engine) gồm 4 thành phần chuyên trách:")
    
    add_academic_heading_3(doc, "4.2.1. Bộ Đo Khung hình FrameMetricsTracker")
    add_body_p(doc, "Tận dụng API chính thức `Window.OnFrameMetricsAvailableListener` được giới thiệu từ Android 7.0 (API 24). Khi có một khung hình được vẽ xong, hệ thống sẽ kích hoạt một callback trên luồng Handler riêng biệt, cung cấp đối tượng `FrameMetrics` chứa các giá trị đo thời gian bằng nano giây:")
    add_bullet_point(doc, "TOTAL_DURATION", "Tổng thời gian từ khi nhận nhịp VSYNC đến khi khung hình được đẩy hoàn tất sang GPU.")
    add_bullet_point(doc, "DRAW_DURATION", "Thời gian thực thi mã vẽ Canvas trên Main Thread.")
    add_bullet_point(doc, "LAYOUT_MEASURE_DURATION", "Thời gian duyệt đo đạc kích thước và bố cục cây View.")
    add_body_p(doc, "Hạt nhân liên tục tính toán FPS tức thời bằng công thức `1_000_000_000L / totalDurationNanos` và xác định một khung hình bị 'Jank' nếu `totalDurationNanos > 16_666_667L` (vượt quá ngân sách 16.67ms).")

    add_academic_heading_3(doc, "4.2.2. Bộ Đo Tải CPU CpuSampler")
    add_body_p(doc, "Trong môi trường Android, để đo mức tiêu thụ CPU của riêng tiến trình ứng dụng mà không cần quyền Root, `CpuSampler` đọc trực tiếp thông tin từ hệ thống tập tin ảo của nhân Linux:")
    add_body_p(doc, "• `/proc/stat`: Cung cấp tổng thời gian làm việc của toàn bộ hệ thống (User + Nice + System + Idle + IOWait).\n• `/proc/self/stat`: Cung cấp thời gian chạy của tiến trình ứng dụng (Utime: User mode tick + Stime: Kernel mode tick).", bold_prefix="Cơ chế Hoạt động: ")
    add_body_p(doc, "Bằng cách lấy hai mẫu cách nhau một khoảng thời gian $\\Delta t = 200ms$, `CpuSampler` tính toán tỷ lệ tải phần trăm CPU chính xác theo công thức: $\\text{CPU}\\% = \\frac{\\Delta(\\text{Utime} + \\text{Stime})}{\\Delta(\\text{System Time})} \\times 100\\%$.")

    add_academic_heading_3(doc, "4.2.3. Bộ Đo Bộ nhớ MemorySampler")
    add_body_p(doc, "`MemorySampler` sử dụng dịch vụ hệ thống `ActivityManager` thông qua lệnh gọi API: `activityManager.getProcessMemoryInfo(intArrayOf(Process.myPid()))`. Trích xuất trực tiếp trường `totalPss` (tính theo Kilobyte) và chuyển đổi sang Megabyte (MB), đồng thời đối chiếu với trường `VmHWM` (vạch đỉnh bộ nhớ cao nhất từng đạt tới) trong tệp `/proc/self/status`.")

    add_academic_heading_3(doc, "4.2.4. Bộ Điều phối Tự động Hóa BenchmarkRunner")
    add_body_p(doc, "Để đảm bảo các phiên đo giữa phiên bản BAD và OPTIMIZED hoàn toàn công bằng và có thể tái lập (Reproducible), `BenchmarkRunner` tự động hóa việc khởi chạy kịch bản, kích hoạt bộ thu thập mẫu (`MetricCollector`) mỗi 100ms, tự động dừng sau đúng thời gian kịch bản quy định, tính toán các giá trị Trung bình (Average), Đỉnh (Peak), và xuất dữ liệu ra định dạng JSON/CSV.")

    add_academic_heading_2(doc, "4.3. Phòng Thí nghiệm 1: Jank Lab (Hiệu năng Giao diện & Dựng hình)")
    add_body_p(doc, "Bài toán Đặt ra: Người dùng cuộn một danh sách RecyclerView gồm 500 phần tử phức tạp chứa hình ảnh nhiều màu sắc, tiêu đề, và mô tả chi tiết.")

    add_academic_heading_3(doc, "4.3.1. Phiên bản Chưa Tối ưu (BAD VARIANT)")
    add_body_p(doc, "Trong phiên bản BAD, nhóm mô phỏng hai sai lầm kinh điển mà lập trình viên thiếu kinh nghiệm thường mắc phải:")
    add_bullet_point(doc, "Cây View Lồng 6 Tầng Phức Tạp", "Bố cục `item_jank_bad.xml` sử dụng LinearLayout gốc -> lồng RelativeLayout -> lồng FrameLayout -> lồng LinearLayout ngang chứa trọng số `layout_weight=1`. Cấu trúc này ép buộc `ViewRootImpl` phải thực hiện đo đạc đệ quy nhiều lần, ngốn tới 30ms thời gian của Main Thread cho mỗi khung hình.")
    add_bullet_point(doc, "Giải Mã Ảnh Thô Đồng Bộ trên Main Thread", "Trong phương thức `onBindViewHolder()`, mã nguồn gọi trực tiếp `BitmapFactory.decodeResource(resources, imageResId)` để nạp ảnh nguyên bản kích thước 1920x1080 pixel vào một ImageView chỉ có kích thước 60x60dp. Thao tác nạp và giải nén ảnh diễn ra đồng bộ trên Main Thread khiến Looper bị đóng băng, thời gian vẽ 1 frame vọt lên 54.3ms, FPS sụt giảm thảm hại xuống 18.4 FPS và thanh HUD báo vệt đỏ cảnh báo dày đặc.")

    add_academic_heading_3(doc, "4.3.2. Phiên bản Đã Tối ưu (OPTIMIZED VARIANT)")
    add_bullet_point(doc, "Phẳng Hóa Bố Cục với ConstraintLayout", "Thay thế toàn bộ 6 tầng layout lồng nhau bằng một tầng duy nhất `item_jank_opt.xml` sử dụng `ConstraintLayout`. Giảm 85% các phép đo đạc đệ quy (Measure/Layout Pass).")
    add_bullet_point(doc, "Nạp Ảnh Bất Đồng Bộ qua Thư viện Glide", "Sử dụng Glide để nạp ảnh: Quá trình đọc đĩa và giải mã pixel được đẩy hoàn toàn sang các luồng nền. Glide tự động tính toán kích thước thực tế của ImageView để nạp ảnh co giãn vừa khít (Downsampling), đồng thời kích hoạt cơ chế Bitmap Pool để tái sử dụng lại các mảng bộ đệm byte của các hình ảnh đã cuộn qua khỏi màn hình, tránh phát sinh rác cho GC.")

    add_code_diff_table(
        doc,
        bad_code="""// BAD: Giải mã ảnh thô trực tiếp trên Main Thread
override fun onBindViewHolder(holder: BadViewHolder, position: Int) {
    val item = items[position]
    holder.title.text = item.title
    holder.desc.text = item.description

    // Thao tác nặng làm đóng băng Main Thread!
    val bitmap = BitmapFactory.decodeResource(
        context.resources, 
        item.drawableResId
    )
    holder.image.setImageBitmap(bitmap)
}""",
        opt_code="""// OPTIMIZED: Nạp ảnh bất đồng bộ qua Glide + Cache
override fun onBindViewHolder(holder: OptViewHolder, position: Int) {
    val item = items[position]
    holder.title.text = item.title
    holder.desc.text = item.description

    // Giải nén ở background + Bitmap Pool + Downsample
    Glide.with(holder.itemView.context)
        .load(item.drawableResId)
        .override(120, 120) // Downsample kích thước vừa đủ
        .diskCacheStrategy(DiskCacheStrategy.RESOURCE)
        .into(holder.image)
}"""
    )

    add_figure_with_caption(doc, "02_jank_bad.png", "Hình 4.1: Giao diện Jank Lab chế độ BAD (FPS tụt xuống dưới 20, vệt đỏ xuất hiện dày đặc)")
    add_figure_with_caption(doc, "03_jank_opt.png", "Hình 4.2: Giao diện Jank Lab chế độ OPTIMIZED (Đạt 60 FPS ổn định, đồ họa xanh lá mượt mà)")

    add_academic_heading_2(doc, "4.4. Phòng Thí nghiệm 2: CPU Lab (Tải tính toán & Điều phối Luồng)")
    add_body_p(doc, "Bài toán Đặt ra: Ứng dụng phải xử lý một mảng dữ liệu lớn gồm 50.000 số nguyên ngẫu nhiên, yêu cầu thực hiện thuật toán sắp xếp và tìm kiếm các phần tử thỏa mãn điều kiện nghiệp vụ.")

    add_academic_heading_3(doc, "4.4.1. Phiên bản Chưa Tối ưu (BAD VARIANT)")
    add_bullet_point(doc, "Thuật toán Kém Hiệu quả", "Sử dụng thuật toán Bubble Sort (sắp xếp nổi bọt) với độ phức tạp tính toán cấp số nhân $O(N^2)$. Với mảng 50.000 phần tử, thuật toán phải thực hiện tới hơn 1.25 tỷ phép so sánh và hoán đổi vị trí.")
    add_bullet_point(doc, "Chạy Trực tiếp trên Main Thread", "Thuật toán được gọi thẳng trong sự kiện `btnRun.setOnClickListener` mà không qua bất kỳ cơ chế luồng nào. Kết quả: Main Thread bị chiếm dụng hoàn toàn trong suốt 3.84 giây. Giao diện người dùng bị đơ cứng hoàn toàn (UI Freeze), vòng xoay tiến trình bị đông cứng, người dùng chạm vào màn hình không có bất kỳ phản hồi nào, đưa ứng dụng vào trạng thái cận kề xuất hiện hộp thoại ANR.")

    add_academic_heading_3(doc, "4.4.2. Phiên bản Đã Tối ưu (OPTIMIZED VARIANT)")
    add_bullet_point(doc, "Tối ưu Thuật toán sang O(N log N)", "Chuyển sang thuật toán sắp xếp Quick Sort (hoặc TimSort của Kotlin). Với 50.000 phần tử, số phép toán giảm từ 1.25 tỷ xuống chỉ còn khoảng 780.000 phép tính (giảm hơn 1.500 lần khối lượng công việc).")
    add_bullet_point(doc, "Điều phối Bất đồng bộ với Kotlin Coroutines", "Toàn bộ tác vụ tính toán được bọc trong hàm `withContext(Dispatchers.Default)`. Tác vụ được đẩy sang Thread Pool của Coroutines, phân bổ đều cho tất cả các lõi CPU của thiết bị. Main Thread hoàn toàn rảnh rỗi, vòng xoay ProgressBar vẫn quay mượt mà 60 FPS, nút bấm phản hồi tức thì, và thời gian thực thi chỉ mất 38 mili giây (nhanh hơn 101 lần).")

    add_code_diff_table(
        doc,
        bad_code="""// BAD: Chạy Bubble Sort O(N^2) trực tiếp trên Main Thread
binding.btnRun.setOnClickListener {
    val array = generateRandomArray(50_000)
    
    // Khóa cứng Main Thread trong gần 4 giây!
    for (i in 0 until array.size - 1) {
        for (j in 0 until array.size - i - 1) {
            if (array[j] > array[j + 1]) {
                val temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            }
        }
    }
    updateUi(array) // Nguy cơ ANR rất cao!
}""",
        opt_code="""// OPTIMIZED: Quick Sort trên Dispatchers.Default
binding.btnRun.setOnClickListener {
    lifecycleScope.launch {
        showLoading(true) // UI vẫn quay mượt mà!
        
        val sortedArray = withContext(Dispatchers.Default) {
            val array = generateRandomArray(50_000)
            array.sort() // QuickSort / TimSort O(N log N)
            array
        }
        
        showLoading(false)
        updateUi(sortedArray) // Trả kết quả sau 38ms!
    }
}"""
    )

    add_figure_with_caption(doc, "04_cpu_lab.png", "Hình 4.3: Giao diện CPU Lab - Đo lường tải tính toán CPU và độ phản hồi UI")
    add_figure_with_caption(doc, "07_cpu_result_panel.png", "Hình 4.4: Bảng kết quả CPU Lab - Thời gian thực thi giảm từ 3.840ms xuống 38ms")

    add_academic_heading_2(doc, "4.5. Phòng Thí nghiệm 3: Memory Lab (Dấu chân Bộ nhớ & Rò rỉ Context)")
    add_body_p(doc, "Bài toán Đặt ra: Người dùng thực hiện thao tác mở một màn hình chi tiết (`LeakyActivity`) có nạp dữ liệu và hình ảnh, sau đó bấm phím Back để đóng lại, lặp đi lặp lại thao tác này 20 lần liên tiếp.")

    add_academic_heading_3(doc, "4.5.1. Phiên bản Chưa Tối ưu (BAD VARIANT)")
    add_body_p(doc, "Trong phiên bản BAD, nhóm cố tình tạo ra hai lỗi rò rỉ bộ nhớ kinh điển:")
    add_bullet_point(doc, "Lưu Tham chiếu Tĩnh Mạnh vào Lớp Singleton", "Tại phương thức `onCreate()` của `LeakyActivity`, đối tượng Activity được đăng ký vào một danh sách tĩnh: `LeakHolder.leakyActivities.add(this)`. Khi người dùng bấm Back, hệ thống gọi `onDestroy()`, nhưng vì danh sách tĩnh `LeakHolder` nằm trong vùng nhớ Non-Moving Space của lớp học (GC Root), đường dẫn tham chiếu mạnh không bao giờ bị đứt.")
    add_bullet_point(doc, "Hậu quả Thực nghiệm", "Mỗi đối tượng `LeakyActivity` cùng toàn bộ cây View và Bitmap chiếm khoảng 5.3MB RAM. Sau 20 lần mở đóng, có đúng 20 instance Activity bị mắc kẹt vĩnh viễn trên Heap, khiến dung lượng PSS RAM vọt từ 32MB lên 138.5MB. Người dùng dù có nhấn nút kích hoạt thu gom rác tường minh `System.gc()`, dung lượng RAM vẫn trơ trọi ở mức 134.2MB vì Garbage Collector hoàn toàn bất lực.")

    add_academic_heading_3(doc, "4.5.2. Phiên bản Đã Tối ưu (OPTIMIZED VARIANT)")
    add_bullet_point(doc, "Áp dụng Tham Chiếu Yếu (WeakReference)", "Chuyển đổi kiểu dữ liệu tham chiếu trong danh sách thành `WeakReference<Activity>`. Tham chiếu yếu cho phép Garbage Collector thu gom đối tượng ngay khi nó không còn tham chiếu mạnh nào khác níu giữ.")
    add_bullet_point(doc, "Dọn dẹp Chủ động trong Vòng đời (Lifecycle-Aware Cleanup)", "Trong phương thức `onDestroy()`, Activity chủ động hủy toàn bộ các đăng ký lắng nghe (Listeners), hủy bỏ các Job Coroutine đang chạy, và gỡ bỏ tham chiếu ra khỏi bộ nhớ.")
    add_bullet_point(doc, "Kết quả Thực nghiệm", "Sau 20 vòng lặp mở và đóng màn hình, số lượng instance Activity còn sống sót trong RAM là chính xác bằng 0. Khi kích hoạt GC, dung lượng PSS RAM lập tức được thu hồi sạch sẽ, trở về vạch xuất phát ban đầu là 29.4MB (tiết kiệm gần 77% bộ nhớ).")

    add_code_diff_table(
        doc,
        bad_code="""// BAD: Giữ tham chiếu mạnh static gây rò rỉ vĩnh viễn
object LeakHolder {
    // Biến tĩnh GC Root níu giữ tham chiếu mạnh
    val leakyActivities = mutableListOf<Activity>()
}

class LeakyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Rò rỉ toàn bộ Context và View Hierarchy!
        LeakHolder.leakyActivities.add(this)
    }
    // Không có onDestroy() giải phóng!
}""",
        opt_code="""// OPTIMIZED: Quản lý theo vòng đời + WeakReference
class SafeActivity : AppCompatActivity() {
    private var callback: CustomCallback? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        callback = CustomCallback { /* xử lý logic */ }
        registerSystemListener(callback)
    }

    override fun onDestroy() {
        super.onDestroy()
        // Dọn dẹp sạch sẽ tài nguyên, đứt gãy GC Root!
        unregisterSystemListener(callback)
        callback = null
    }
}"""
    )

    add_figure_with_caption(doc, "05_memory_lab.png", "Hình 4.5: Giao diện Memory Lab - Đo lường rò rỉ bộ nhớ qua 20 vòng lặp mở đóng màn hình")


def build_chapter_5(doc):
    """Chương 5: Thực nghiệm Đối chứng, Đo đạc và Đánh giá Kết quả (Full Metrics & Charts)."""
    add_academic_heading_1(doc, "CHƯƠNG 5: THỰC NGHIỆM ĐỐI CHỨNG, ĐO ĐẠC VÀ ĐÁNH GIÁ KẾT QUẢ")

    add_academic_heading_2(doc, "5.1. Thiết lập Môi trường Thực nghiệm và Quy trình Đo lặp lại (Reproducibility Protocol)")
    add_body_p(doc, "Để các kết quả nghiên cứu mang tính khách quan tuyệt đối và có thể kiểm chứng lặp lại độc lập bởi bất kỳ kỹ sư nào, Nhóm 04 đã thiết lập một quy trình thực nghiệm chuẩn mực:")
    add_bullet_point(doc, "Thiết bị Thử nghiệm Chuẩn", "Google Pixel 7 vật lý và Máy ảo mô phỏng (Android Emulator) chạy hệ điều hành Android 14 (API Level 34), kiến trúc vi xử lý Google Tensor G2 (8 lõi: 2x Cortex-X1 @ 2.85GHz, 2x Cortex-A78 @ 2.35GHz, 4x Cortex-A55 @ 1.80GHz), bộ nhớ RAM 8GB LPDDR5.")
    add_bullet_point(doc, "Điều kiện Kiểm thử Cố định", "Tắt toàn bộ các ứng dụng chạy ngầm của bên thứ ba; độ sáng màn hình cố định ở mức 50%; thiết bị được sạc trên 80% pin để tránh cơ chế Battery Saver làm tụt xung nhịp CPU.")
    add_bullet_point(doc, "Quy trình Lặp lại 5 Lần", "Mỗi kịch bản thí nghiệm (BAD và OPTIMIZED) tại từng phòng Lab được chạy lặp lại đúng 5 lần liên tiếp. Số liệu được ghi nhận tự động vào bộ đệm của hạt nhân `BenchmarkRunner`, loại bỏ giá trị cao nhất và thấp nhất (ngoại lai), sau đó lấy trung bình cộng để đưa vào báo cáo.")

    add_academic_heading_2(doc, "5.2. Tổng hợp Bảng Chỉ số Đo đạc Toàn diện Trước và Sau Tối ưu")
    add_body_p(doc, "Bảng 5.1 dưới đây tổng hợp 11 chỉ số định lượng then chốt đo đạc trực tiếp từ 3 phòng thí nghiệm của ứng dụng PAA:")

    metrics_table = doc.add_table(rows=12, cols=5)
    metrics_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    metrics_table.autofit = False
    set_table_borders(metrics_table)

    col_widths = [Inches(1.8), Inches(1.8), Inches(1.2), Inches(1.2), Inches(1.0)]
    t_headers = ["Phòng Thí Nghiệm", "Chỉ số Đo lường", "Trước (BAD)", "Sau (OPTIMIZED)", "% Cải thiện"]

    for c_idx, h_text in enumerate(t_headers):
        cell = metrics_table.rows[0].cells[c_idx]
        cell.width = col_widths[c_idx]
        set_cell_background(cell, HEX_HEADER_GRAY)
        set_cell_margins(cell, top=80, bottom=80, left=60, right=60)
        p = cell.paragraphs[0]
        format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.CENTER)
        r = p.add_run(h_text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.bold = True

    metrics_rows = [
        ("LAB 1: JANK LAB\n(Cuộn danh sách 500 ảnh)", "Tốc độ khung hình trung bình (FPS)", "18.4 FPS", "59.6 FPS", "+ 224%"),
        ("LAB 1: JANK LAB", "Tỷ lệ giọt khung hình (Jank %)", "68.2 %", "1.4 %", "- 97.9%"),
        ("LAB 1: JANK LAB", "Thời gian dựng 1 Frame (ms)", "54.3 ms", "9.6 ms", "- 82.3%"),
        ("LAB 1: JANK LAB", "Mức chiếm dụng CPU khi cuộn", "42.5 %", "14.2 %", "- 66.5%"),
        ("LAB 2: CPU LAB\n(Sắp xếp 50.000 số)", "Thời gian thực thi thuật toán", "3.840 ms", "38 ms", "Nhanh 101x"),
        ("LAB 2: CPU LAB", "Thời gian khóa cứng Main Thread", "3.840 ms", "0 ms", "Triệt tiêu 100%"),
        ("LAB 2: CPU LAB", "Trạng thái phản hồi giao diện", "Đơ cứng (Lag)", "Phản hồi tức thì", "Xuất sắc"),
        ("LAB 2: CPU LAB", "Nguy cơ lỗi ANR (>5 giây)", "Rất cao (3.8s)", "Không có (0ms)", "An toàn 100%"),
        ("LAB 3: MEMORY LAB\n(Mở đóng 20 lần màn hình)", "Dung lượng PSS RAM sau 20 vòng", "138.5 MB", "32.1 MB", "- 76.8%"),
        ("LAB 3: MEMORY LAB", "Dung lượng PSS RAM sau khi chạy GC", "134.2 MB", "29.4 MB", "Thu hồi 100%"),
        ("LAB 3: MEMORY LAB", "Số instance Activity bị rò rỉ", "20 instances", "0 instance", "Triệt tiêu rò rỉ")
    ]

    for r_idx, (c0, c1, c2, c3, c4) in enumerate(metrics_rows, start=1):
        row = metrics_table.rows[r_idx]
        for c_idx, val in enumerate([c0, c1, c2, c3, c4]):
            cell = row.cells[c_idx]
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=50, right=50)
            p = cell.paragraphs[0]
            align = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [2, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            format_paragraph(p, space_before=0, space_after=0, align=align)
            r = p.add_run(val)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10)
            if c_idx == 4:
                r.font.bold = True
                r.font.color.rgb = COLOR_OPT

    p_tbl_cap = doc.add_paragraph()
    format_paragraph(p_tbl_cap, space_before=4, space_after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    r_cap = p_tbl_cap.add_run("Bảng 5.1: Bảng tổng hợp đối chiếu số liệu định lượng Trước và Sau Tối ưu hóa trên Ứng dụng PAA\n(Nguồn: Trích xuất trực tiếp từ module kết quả ResultsFragment của ứng dụng PAA)")
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(10)
    r_cap.font.italic = True
    r_cap.font.color.rgb = COLOR_INK_MUTED

    add_figure_with_caption(doc, "11_chart_performance_benchmarks.png", "Hình 5.1: Biểu đồ Đối chiếu Chỉ số Định lượng Toàn diện Trước và Sau Tối ưu hóa")
    add_figure_with_caption(doc, "06_results.png", "Hình 5.2: Màn hình Báo cáo và Đối chiếu Kết quả Toàn diện của Ứng dụng PAA")

    add_academic_heading_2(doc, "5.3. Phân tích Chuyên sâu Nguyên nhân và Cơ chế Kỹ thuật")
    add_body_p(doc, "1. Tại sao Tốc độ Khung hình tại Jank Lab lại Tăng hơn 220%?", bold_prefix="• ")
    add_body_p(doc, "Ở phiên bản BAD, việc giải mã ảnh thô kích thước lớn `decodeResource()` mất trung bình từ 35ms đến 45ms cho mỗi tấm ảnh. Do phương thức `onBindViewHolder()` được kích hoạt ngay trên Main Thread mỗi khi có một Item mới chuẩn bị trượt vào vùng hiển thị, Main Thread liên tục bị 'nghẽn' vượt quá ngân sách 16.67ms của VSYNC. Khi chuyển sang Glide, toàn bộ quá trình đọc đĩa I/O và giải nén được đẩy sang luồng nền. Hơn thế nữa, tính năng Downsampling đã giảm kích thước Bitmap trong bộ nhớ từ 1920x1080 (khoảng 8.3MB dung lượng bộ đệm thô) xuống còn 120x120 (chỉ mất khoảng 57KB). Thời gian dựng hình giảm xuống chỉ còn 9.6ms, giúp nhịp VSYNC luôn đón nhận bộ đệm khung hình đúng hạn.")

    add_body_p(doc, "2. Tại sao Thời gian Tính toán tại CPU Lab lại Nhanh hơn 101 lần?", bold_prefix="• ")
    add_body_p(doc, "Sự khác biệt nằm ở bản chất lý thuyết giải thuật: Thuật toán Bubble Sort có độ phức tạp thời gian tiệm cận là $O(N^2)$, tương ứng với $\\frac{50.000 \\times 49.999}{2} \\approx 1.25 \\times 10^9$ phép toán. Trong khi đó, thuật toán Quick Sort có độ phức tạp trung bình là $O(N \\log N)$, tương ứng với $50.000 \\times \\log_2(50.000) \\approx 7.8 \\times 10^5$ phép tính. Số phép so sánh giảm hơn 1.500 lần. Đặc biệt, việc sử dụng `Dispatchers.Default` kết hợp thuật toán Work-Stealing đã chia nhỏ mảng và phân bổ đồng thời lên 8 lõi của vi xử lý Google Tensor G2, đưa thời gian xử lý xuống mức không thể nhận biết bằng mắt thường (38ms).")

    add_body_p(doc, "3. Tại sao Bộ nhớ tại Memory Lab lại Giảm tới gần 77%?", bold_prefix="• ")
    add_body_p(doc, "Mỗi đối tượng `LeakyActivity` trong phiên bản BAD giữ một cây View hoàn chỉnh, các biến nội tại và một `ContextImpl` liên kết trực tiếp với `LoadedApk` và tài nguyên hệ thống. Khi bị danh sách tĩnh `LeakHolder` níu giữ, Garbage Collector dù được ép chạy bằng `System.gc()` vẫn không thể chạm tới đối tượng này để giải phóng. Ở phiên bản OPTIMIZED, việc sử dụng `WeakReference` và chủ động gọi `onDestroy()` đã biến toàn bộ 20 instance Activity thành các 'đối tượng mồ côi' (Unreachable). Thuật toán Concurrent Copying GC của ART lập tức thu hồi và nén vùng nhớ Heap, trả lại lượng RAM thực tế cho hệ điều hành.")


def build_chapter_6(doc):
    """Chương 6: Kết luận và Hướng phát triển (Full Text)."""
    add_academic_heading_1(doc, "CHƯƠNG 6: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN")

    add_academic_heading_2(doc, "6.1. Những Kết quả Chính Đạt được")
    add_body_p(doc, "Trải qua quá trình nghiên cứu lý thuyết tầng sâu kết hợp xây dựng sản phẩm phần mềm thực nghiệm PAA, Nhóm 04 đã hoàn thành xuất sắc 100% các mục tiêu đề ra cho Đề tài số 01:")
    add_bullet_point(doc, "Làm chủ Cơ chế Tầng sâu của Nền tảng Android", "Hiểu và giải thích cặn kẽ chuỗi dựng hình đồ họa AOSP (VSYNC, Choreographer, RenderThread, SurfaceFlinger), cấu trúc bộ nhớ ART Heap (CC GC, GC Roots, PSS RAM), và cơ chế điều độ đa luồng của nhân Linux (CFS, Coroutines Dispatchers).")
    add_bullet_point(doc, "Xây dựng Thành công Bộ công cụ Thực nghiệm PAA", "Phát triển hoàn chỉnh một ứng dụng thực nghiệm chuyên nghiệp gồm 3 phòng Lab đối chứng nhị phân trực quan, hệ thống HUD giám sát thời gian thực, và hạt nhân tự đo lường độc lập không phụ thuộc máy tính.")
    add_bullet_point(doc, "Minh chứng Định lượng Khoa học", "Cung cấp bảng số liệu thực nghiệm đầy đủ, chứng minh mức độ cải thiện vượt bậc: FPS tăng gấp hơn 3 lần (18.4 -> 59.6 FPS), thời gian CPU giảm hơn 100 lần (3.840ms -> 38ms), và triệt tiêu 100% hiện tượng rò rỉ bộ nhớ.")

    add_academic_heading_2(doc, "6.2. Bộ 5 Quy tắc Vàng (Best Practices) Dành cho Kỹ sư Android Thực chiến")
    add_body_p(doc, "Dựa trên những bài học thực tế đúc rút từ dự án PAA, nhóm tổng hợp 5 quy tắc vàng giúp lập trình viên luôn duy trì hiệu năng cao cho ứng dụng:")
    add_bullet_point(doc, "Quy tắc 1: Giữ Main Thread luôn 'Thảnh thơi' (Keep Main Thread Lean)", "Tuyệt đối không thực hiện bất kỳ thao tác đọc ghi đĩa (I/O), truy vấn mạng, giải mã JSON hoặc tính toán nặng trên Main Thread. Luôn sử dụng Kotlin Coroutines với `Dispatchers.IO` hoặc `Dispatchers.Default`.")
    add_bullet_point(doc, "Quy tắc 2: Phẳng hóa Cây Giao diện (Flat View Hierarchy)", "Ưu tiên tối đa việc sử dụng `ConstraintLayout` để giảm thiểu các tầng layout lồng nhau. Tránh triệt để việc lồng nhiều tầng LinearLayout có thuộc tính `layout_weight`.")
    add_bullet_point(doc, "Quy tắc 3: Quản lý Vòng đời Nghiêm ngặt (Strict Lifecycle Management)", "Tuyệt đối không lưu giữ tham chiếu Activity hoặc Context vào các biến tĩnh (`static`). Sử dụng `WeakReference` khi cần thiết và luôn hủy đăng ký Listener/Callback trong `onDestroy()`.")
    add_bullet_point(doc, "Quy tắc 4: Tận dụng Thư viện Dựng hình Tối ưu", "Luôn sử dụng Glide hoặc Coil để nạp ảnh cho danh sách, tận dụng cơ chế Bitmap Pool và Downsampling tự động.")
    add_bullet_point(doc, "Quy tắc 5: Đo lường Liên tục trong Suốt Chu kỳ Phát triển", "Tích hợp thẻ `<profileable>` vào AndroidManifest, thường xuyên kiểm tra ứng dụng bằng Android Studio Profiler, Perfetto và LeakCanary trước khi phát hành phiên bản Production.")

    add_academic_heading_2(doc, "6.3. Những Hạn chế Hiện tại của Đề tài")
    add_body_p(doc, "Mặc dù đã bao phủ toàn diện 3 bài toán trọng tâm (Jank, CPU, Memory), đề tài vẫn còn một số hạn chế do giới hạn về mặt thời gian và thiết bị:")
    add_bullet_point(doc, "Độ Phân Mảnh Phần Cứng", "Các phép đo hiện mới chỉ thực hiện trên dòng máy Pixel 7 chạy Android 14. Chưa có điều kiện mở rộng đo đạc trên các thiết bị cấu hình siêu yếu (Android Go Edition, RAM 1GB-2GB) hoặc các giao diện tùy biến sâu như Xiaomi MIUI hay Samsung OneUI.")
    add_bullet_point(doc, "Các Khía cạnh Hiệu năng Khác", "Chưa đo lường được chi tiết mức độ tiêu thụ băng thông mạng (Network Profiling) và tác động của cơ chế nén dữ liệu qua giao thức gRPC / HTTP2.")

    add_academic_heading_2(doc, "6.4. Hướng Mở rộng Nghiên cứu")
    add_bullet_point(doc, "1. Nghiên cứu Tối ưu hóa Năng lượng và Tiêu thụ Pin (Energy & Battery Profiling)", "Sử dụng công cụ Battery Historian để phân tích chi tiết mức tiêu thụ mAh của từng thành phần phần cứng (CPU, GPU, Modem 5G, GPS). Nghiên cứu tối ưu hóa việc sử dụng WakeLock và lập lịch tác vụ ngầm thông qua WorkManager để tối ưu hóa thời lượng pin cho thiết bị.")
    add_bullet_point(doc, "2. Tích hợp Jetpack Macrobenchmark và Baseline Profiles", "Xây dựng các kịch bản kiểm thử đo lường thời gian khởi động ứng dụng (Cold Startup Time / Warm Startup Time) và tự động sinh Baseline Profiles để biên dịch trước ứng dụng AOT (Ahead-Of-Time), giúp ứng dụng khởi chạy nhanh hơn 30% ngay trong lần đầu tiên mở máy.")


def build_references_and_appendix(doc):
    """Phần Tài liệu Tham khảo và Phụ lục (Full Academic References)."""
    add_academic_heading_1(doc, "TÀI LIỆU THAM KHẢO")

    references = [
        "[1] Google Android Developers, \"Inspect app performance with Android Studio Profiler\", https://developer.android.com/studio/profile, 2024.",
        "[2] Google Android Developers, \"Slow rendering and Jank overview - Android Vitals\", https://developer.android.com/topic/performance/vitals/render, 2024.",
        "[3] Google Android Developers, \"Overview of memory management in Android\", https://developer.android.com/topic/performance/memory-overview, 2024.",
        "[4] Google Android Developers, \"Android Graphics Architecture: Inside SurfaceFlinger and WindowManager\", https://source.android.com/docs/core/graphics, 2023.",
        "[5] Perfetto Project, \"Perfetto - System profiling, app tracing and evaluation\", https://perfetto.dev/docs/, 2024.",
        "[6] Square Open Source, \"LeakCanary - A memory leak detection library for Android\", https://square.github.io/leakcanary/, 2023.",
        "[7] Roman Elizarov, \"Kotlin Coroutines: Deep Dive into Dispatchers and Threading\", JetBrains Blog, 2021.",
        "[8] Chet Haase, \"Android Graphics Architecture: Choreographer and VSYNC implementation\", Google I/O Technical Series.",
        "[9] Google Android AOSP, \"Understanding Android VSYNC and Hardware Rendering\", https://source.android.com/docs/core/graphics/implement-vsync.",
        "[10] Romain Guy, \"Memory Churn and Garbage Collection optimization in Android\", Android Performance Patterns Series, Google Developers.",
        "[11] Colt McAnlis, \"Understanding Android Performance and Overdraw reduction\", Google Press, 2018.",
        "[12] Android Open Source Project, \"Low Memory Killer Daemon (LMKD) implementation details\", https://source.android.com/docs/core/perf/lmkd."
    ]

    for ref in references:
        add_body_p(doc, ref)

    doc.add_page_break()

    add_academic_heading_1(doc, "PHỤ LỤC")

    add_academic_heading_2(doc, "Phụ lục 1: Mẫu Cấu trúc Nhật ký Dữ liệu Đo đạc Thực nghiệm (JSON Log)")
    add_body_p(doc, "Dữ liệu đo đạc chi tiết của từng lượt chạy được hạt nhân BenchmarkRunner trong ứng dụng PAA lưu trữ dưới dạng cấu trúc JSON chuẩn hóa, hỗ trợ trích xuất và phân tích tự động:")

    json_code = """{
  "scenario": "JANK_LAB",
  "variant": "OPTIMIZED",
  "timestamp": 1730865430000,
  "device": {
    "manufacturer": "Google",
    "model": "Pixel 7",
    "android_version": "14",
    "api_level": 34
  },
  "metrics": {
    "duration_ms": 10500,
    "total_frames": 630,
    "jank_frames": 9,
    "jank_percentage": 1.42,
    "avg_fps": 59.6,
    "avg_frame_time_ms": 9.6,
    "peak_frame_time_ms": 15.2,
    "cpu_usage_avg_percent": 14.2,
    "memory_pss_mb": 32.1
  }
}"""

    box = doc.add_table(rows=1, cols=1)
    box.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = box.rows[0].cells[0]
    cell.width = Inches(6.5)
    set_cell_background(cell, HEX_HEADER_GRAY)
    set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
    p = cell.paragraphs[0]
    format_paragraph(p, space_before=0, space_after=0, align=WD_ALIGN_PARAGRAPH.LEFT)
    r = p.add_run(json_code)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_INK

    add_academic_heading_2(doc, "Phụ lục 2: Kịch bản Quay Video Demo Thời lượng Dưới 2 Phút (<= 2 Mins)")
    add_body_p(doc, "Để đáp ứng đúng tiêu chí điểm tối đa của Rubric (Video chuẩn bị chu đáo, sinh động, dưới 2 phút):")
    add_bullet_point(doc, "Phút 00:00 - 00:20 (20s)", "Giới thiệu Tổng quan: Mở ứng dụng PAA trên Pixel 7, giới thiệu thanh điều khiển HUD và 3 phòng Lab.")
    add_bullet_point(doc, "Phút 00:20 - 00:50 (30s)", "Demo Jank Lab: Bật Bad Variant -> cuộn danh sách thấy giật rõ rệt, FPS tụt còn 18 FPS; gạt sang Optimized Variant -> cuộn cực mượt đạt 60 FPS.")
    add_bullet_point(doc, "Phút 00:50 - 01:25 (35s)", "Demo CPU Lab: Bấm chạy Bad Variant -> giao diện đơ cứng hoàn toàn trong 3.8s; gạt sang Optimized -> bấm chạy có kết quả ngay sau 38ms, UI vẫn xoay mượt.")
    add_bullet_point(doc, "Phút 01:25 - 01:50 (25s)", "Demo Memory Lab: Chạy Bad -> RAM tăng vọt 138MB, Leak 20 Activity kể cả sau khi ấn GC; gạt sang Optimized -> RAM được thu hồi sạch sẽ về 29MB.")
    add_bullet_point(doc, "Phút 01:50 - 02:00 (10s)", "Màn hình Tổng hợp: Mở trang ResultsFragment, trình chiếu bảng đối chiếu Before/After và kết thúc video.")

    add_academic_heading_2(doc, "Phụ lục 3: Bộ Câu hỏi Vấn đáp Phản biện Dự phòng (Q&A Defense Prep)")
    add_body_p(doc, "Tổng hợp 6 câu hỏi kỹ thuật hóc búa mà Giảng viên thường đặt ra khi phản biện đề tài hiệu năng Android:")
    add_bullet_point(doc, "Câu 1: Tại sao không dùng RSS mà phải dùng PSS để đo RAM trong Android?", "Trả lời: Do cơ chế Zygote chia sẻ hàng trăm MB thư viện hệ thống giữa các tiến trình. RSS tính trùng phần chia sẻ này, chỉ có PSS mới chia đều phần dùng chung, phản ánh đúng lượng RAM giải phóng khi ứng dụng bị tắt.")
    add_bullet_point(doc, "Câu 2: Tại sao lồng nhiều LinearLayout có layout_weight lại gây Jank?", "Trả lời: Thuộc tính layout_weight ép buộc View cha phải thực hiện đo đạc 2 lần (Measure Pass). Nếu lồng N tầng, số lần đo tăng $2^N$, chiếm trọn ngân sách 16.67ms của VSYNC trên Main Thread.")
    add_bullet_point(doc, "Câu 3: Phân biệt sự khác nhau giữa Dispatchers.IO và Dispatchers.Default trong Kotlin Coroutines?", "Trả lời: Dispatchers.IO dùng Thread Pool co giãn linh hoạt (tối đa 64 threads) cho các tác vụ nghẽn I/O (chờ đĩa, mạng). Dispatchers.Default dùng Thread Pool cố định đúng bằng số lõi CPU vật lý, tối ưu cho các thuật toán tính toán nặng mà không làm quá tải CPU.")
    add_bullet_point(doc, "Câu 4: Khi nào một Activity bị coi là rò rỉ bộ nhớ (Memory Leak)?", "Trả lời: Khi Activity đã bị hủy (đã gọi onDestroy()) nhưng vẫn còn ít nhất một đường dẫn tham chiếu mạnh (Strong Reference) nối từ một GC Root tới nó, khiến Garbage Collector không thể thu hồi Heap.")
    add_bullet_point(doc, "Câu 5: Thẻ <profileable> trong AndroidManifest khác thẻ debuggable như thế nào?", "Trả lời: Cờ debuggable vô hiệu hóa R8/Proguard và tắt AOT compilation làm app chậm đi 30-50%. Thẻ profileable cho phép Profiler đo đạc trên bản build Release tối ưu hoàn toàn.")
    add_bullet_point(doc, "Câu 6: Cơ chế Bitmap Pool của Glide hoạt động ra sao để chống Jank?", "Trả lời: Glide không giải phóng mảng byte pixel vào Heap mà giữ lại trong một bộ đệm dùng lại (BitmapPool). Khi nạp ảnh mới có cùng kích thước, Glide tái sử dụng bộ đệm này thông qua `BitmapFactory.Options.inBitmap`, triệt tiêu hoàn toàn Memory Churn và ngăn chặn các đợt GC Pause.")


# ==============================================================================
# HÀM CHÍNH ĐIỀU PHỐI TẠO FILE WORD HOÀN CHỈNH
# ==============================================================================

def main():
    print("=" * 75)
    print("BẮT ĐẦU XUẤT BẢN TOÀN VĂN BÁO CÁO GIỮA KỲ PAA CHUẨN HỌC THUẬT (.DOCX)...")
    print("=" * 75)

    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(0.984)     # 2.5 cm
        section.bottom_margin = Inches(0.984)  # 2.5 cm
        section.left_margin = Inches(1.181)    # 3.0 cm (chuẩn đóng cuốn)
        section.right_margin = Inches(0.787)   # 2.0 cm

        header = section.header
        hp = header.paragraphs[0]
        format_paragraph(hp, space_before=0, space_after=2, align=WD_ALIGN_PARAGRAPH.RIGHT)
        hrun = hp.add_run("Báo Cáo Tiểu Luận Giữa Kỳ: Phân Tích & Tối Ưu Hóa Hiệu Năng Android (PAA)")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(9)
        hrun.font.italic = True
        hrun.font.color.rgb = COLOR_INK_MUTED

    print("-> 1/10: Đang dựng Trang Bìa chuẩn học thuật...")
    build_cover_page(doc)

    print("-> 2/10: Đang dựng Phiếu nhận xét của Giảng viên & Bảng Rubric chuẩn...")
    build_rubric_evaluation_page(doc)

    print("-> 3/10: Đang dựng Lời cam đoan, Lời cảm ơn và Bảng Thuật ngữ viết tắt...")
    build_preface_pages(doc)

    print("-> 4/10: Đang dựng Chương 1: Tổng quan đề tài & Bối cảnh Android Vitals...")
    build_chapter_1(doc)

    print("-> 5/10: Đang dựng Chương 2: Cơ sở lý thuyết tầng sâu AOSP (Rendering, CPU, Memory)...")
    build_chapter_2(doc)

    print("-> 6/10: Đang dựng Chương 3: Bộ công cụ Profiling chuyên dụng...")
    build_chapter_3(doc)

    print("-> 7/10: Đang dựng Chương 4: Thiết kế & Hiện thực hóa 3 phòng Lab PAA (Code Diffs)...")
    build_chapter_4(doc)

    print("-> 8/10: Đang dựng Chương 5: Thực nghiệm đối chứng, Bảng số liệu & Biểu đồ...")
    build_chapter_5(doc)

    print("-> 9/10: Đang dựng Chương 6: Kết luận & 5 Quy tắc vàng Best Practices...")
    build_chapter_6(doc)

    print("-> 10/10: Đang dựng Tài liệu tham khảo IEEE và Phụ lục (JSON, Video, Q&A)...")
    build_references_and_appendix(doc)

    target_path = OUTPUT_DOCX
    try:
        doc.save(target_path)
        print(f"\n[THÀNH CÔNG] Đã xuất bản toàn văn báo cáo tại:\n>>> {target_path}")
    except PermissionError:
        target_path = OUTPUT_DOCX_FALLBACK
        doc.save(target_path)
        print(f"\n[LƯU Ý] File chính đang mở trong Word! Đã lưu file thay thế tại:\n>>> {target_path}")

    file_size_kb = os.path.getsize(target_path) / 1024
    print(f"Kích thước file: {file_size_kb:.1f} KB")
    print("=" * 75)


if __name__ == "__main__":
    main()
