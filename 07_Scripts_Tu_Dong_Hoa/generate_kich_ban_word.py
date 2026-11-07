import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def main():
    doc = docx.Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

    C_NAVY = RGBColor(10, 77, 158)      # #0A4D9E TDTU Blue
    C_SCARLET = RGBColor(188, 0, 36)    # #BC0024 PAA Scarlet
    C_SLATE = RGBColor(30, 41, 59)      # #1E293B Dark Slate
    C_GRAY = RGBColor(100, 116, 139)

    def set_font(run, name='Arial', size=11, bold=False, italic=False, color=C_SLATE):
        run.font.name = name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color

    # Document Header
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run('KỊCH BẢN THUYẾT TRÌNH BÁO CÁO GIỮA KỲ TOÀN VĂN (17 SLIDES)\n')
    set_font(r, 'Arial', 16, bold=True, color=C_NAVY)
    r2 = p_title.add_run('ĐỀ TÀI: PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID (PAA)')
    set_font(r2, 'Arial', 12, bold=True, color=C_SCARLET)

    # Metadata
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(12)
    r_meta = p_meta.add_run(
        'Môn học: Phát triển Ứng dụng Di động | Trường ĐH Tôn Đức Thắng (TDTU) – Khoa CNTT\n'
        'Giảng viên hướng dẫn: GV: Trần Đại Nhân\n'
        'Sinh viên thực hiện: Hoàng Thái Đăng Khoa (52400017) & Đinh Thanh Phong (52400027)\n'
        'Thời lượng thuyết trình: 16 – 18 phút (Dự phòng 2 phút cho Q&A trong tổng 20 phút)'
    )
    set_font(r_meta, 'Arial', 9.5, italic=True, color=C_GRAY)

    with open(r'D:\MOBI GK\02_Slide_Thuyet_Trinh\Kich_Ban_Thuyet_Trinh_Chi_Tiet_Khoa_Phong.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_table = False
    table_data = []

    for line in lines:
        line_s = line.strip()
        if not line_s:
            continue
        if line_s.startswith('# ') or line_s.startswith('> '):
            continue
        elif line_s.startswith('## '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            r = p.add_run(line_s[3:])
            set_font(r, 'Arial', 13, bold=True, color=C_NAVY)
        elif line_s.startswith('### '):
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(line_s[4:])
            set_font(r, 'Arial', 11, bold=True, color=C_SCARLET)
        elif line_s.startswith('|'):
            if '---' in line_s:
                continue
            cols = [c.strip() for c in line_s.split('|')[1:-1]]
            if not in_table:
                in_table = True
                table_data = [cols]
            else:
                table_data.append(cols)
        else:
            if in_table:
                t = doc.add_table(rows=len(table_data), cols=len(table_data[0]))
                t.alignment = WD_TABLE_ALIGNMENT.CENTER
                for row_idx, row_vals in enumerate(table_data):
                    for col_idx, val in enumerate(row_vals):
                        cell = t.cell(row_idx, col_idx)
                        cell.text = val
                        for p_cell in cell.paragraphs:
                            for run_c in p_cell.runs:
                                if row_idx == 0:
                                    set_font(run_c, 'Arial', 9, bold=True, color=RGBColor(255, 255, 255))
                                else:
                                    set_font(run_c, 'Arial', 8.5, color=C_SLATE)
                        if row_idx == 0:
                            shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="0A4D9E"/>')
                            cell._tc.get_or_add_tcPr().append(shading_elm)
                        elif row_idx % 2 == 1:
                            shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
                            cell._tc.get_or_add_tcPr().append(shading_elm)
                in_table = False
                table_data = []
                doc.add_paragraph().paragraph_format.space_after = Pt(6)

            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(3)
            if line_s.startswith('>'):
                p.paragraph_format.left_indent = Inches(0.25)
                clean_text = line_s.replace('> *', '').replace('*', '').replace('>', '').strip()
                r = p.add_run(clean_text)
                set_font(r, 'Arial', 10.5, italic=True, color=RGBColor(15, 23, 42))
            elif line_s.startswith('* '):
                r = p.add_run(line_s[2:])
                set_font(r, 'Arial', 10, color=C_SLATE)
            else:
                r = p.add_run(line_s)
                set_font(r, 'Arial', 10, color=C_SLATE)

    doc_path = r'D:\MOBI GK\02_Slide_Thuyet_Trinh\Kich_Ban_Thuyet_Trinh_Chi_Tiet_Khoa_Phong.docx'
    doc.save(doc_path)
    print('Generated Word document successfully:', doc_path)

if __name__ == '__main__':
    main()
