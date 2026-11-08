# -*- coding: utf-8 -*-
"""
Script tạo file PowerPoint thuyết trình 13 slide chuẩn 16:9:
Thuyet_Trinh_PAA_TDTU_12_Slides.pptx
Có thể kéo thả trực tiếp vào Canva hoặc Google Slides để tự động biến thành slide có thể chỉnh sửa hoàn toàn!
"""
import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Colors
C_NAVY = RGBColor(10, 77, 158)       # #0A4D9E TDTU Blue
C_CYAN = RGBColor(0, 180, 216)      # #00B4D8 Cyan
C_DARK = RGBColor(15, 23, 42)       # #0F172A Slate Dark
C_LIGHT_BG = RGBColor(241, 245, 249)# #F1F5F9 Slate Light
C_CARD_BG = RGBColor(255, 255, 255) # White
C_GRAY_TEXT = RGBColor(100, 116, 139)
C_RED = RGBColor(225, 29, 72)
C_GREEN = RGBColor(13, 148, 136)
C_WHITE = RGBColor(255, 255, 255)

def create_slide_header(slide, title_text, category_text="BÁO CÁO GIỮA KỲ: PHÁT TRIỂN ỨNG DỤNG DI ĐỘNG"):
    # Header bar
    tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
    p_c = tb_cat.text_frame.paragraphs[0]
    p_c.text = category_text.upper()
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = C_CYAN
    p_c.font.name = "Arial"
    
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
    p_t = tb_title.text_frame.paragraphs[0]
    p_t.text = title_text
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_NAVY
    p_t.font.name = "Arial"

def add_card(slide, left, top, width, height, bg_color=C_CARD_BG, border_color=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.color.rgb = RGBColor(226, 232, 240)
        shape.line.width = Pt(1)
    return shape

def add_bullet(tf, text, level=0, bold=False, size=12, color=C_DARK):
    p = tf.add_paragraph() if len(tf.paragraphs[0].text) > 0 else tf.paragraphs[0]
    p.text = text
    p.level = level
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = "Arial"
    p.space_after = Pt(4)
    return p

def main():
    prs = Presentation()
    # 16:9 Widescreen (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    img_dir = os.path.join(base_dir, "04_Hinh_Anh_Va_So_Do")
    out_pptx = os.path.join(base_dir, "02_Slide_Thuyet_Trinh", "Thuyet_Trinh_PAA_TDTU_12_Slides.pptx")
    
    # ==========================================
    # SLIDE 1: TRANG BÌA (COVER SLIDE)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.fill.background()
    
    # Top banner white card for Logos
    card_logo = add_card(s1, Inches(4.5), Inches(0.5), Inches(4.333), Inches(0.9), bg_color=C_WHITE)
    tb_l = s1.shapes.add_textbox(Inches(4.5), Inches(0.5), Inches(4.333), Inches(0.9))
    p_l = tb_l.text_frame.paragraphs[0]
    p_l.alignment = PP_ALIGN.CENTER
    p_l.text = "TRƯỜNG ĐẠI HỌC TÔN ĐỨC THẮNG - KHOA CNTT"
    p_l.font.size = Pt(13)
    p_l.font.bold = True
    p_l.font.color.rgb = C_NAVY
    
    # Title
    tb_title = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(1.8))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "PHÂN TÍCH VÀ TỐI ƯU HÓA HIỆU NĂNG ỨNG DỤNG ANDROID"
    p1.font.size = Pt(30)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    p1.alignment = PP_ALIGN.CENTER
    
    p2 = tf_t.add_paragraph()
    p2.text = "Nghiên cứu Nguyên lý Tầng sâu AOSP & Thực nghiệm Bộ công cụ PAA (Performance Analysis App)"
    p2.font.size = Pt(16)
    p2.font.color.rgb = C_CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(8)
    
    # Left Circle badge
    badge = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.2), Inches(4.0), Inches(2.2), Inches(2.2))
    badge.fill.solid()
    badge.fill.fore_color.rgb = C_CYAN
    badge.line.fill.background()
    tb_b = s1.shapes.add_textbox(Inches(1.2), Inches(4.5), Inches(2.2), Inches(1.2))
    p_b1 = tb_b.text_frame.paragraphs[0]
    p_b1.text = "MOBI GK"
    p_b1.font.size = Pt(18)
    p_b1.font.bold = True
    p_b1.font.color.rgb = C_WHITE
    p_b1.alignment = PP_ALIGN.CENTER
    p_b2 = tb_b.text_frame.add_paragraph()
    p_b2.text = "2026"
    p_b2.font.size = Pt(16)
    p_b2.font.color.rgb = C_WHITE
    p_b2.alignment = PP_ALIGN.CENTER
    
    # Middle Info Card
    c_info = add_card(s1, Inches(3.8), Inches(4.0), Inches(5.8), Inches(2.5), bg_color=C_WHITE)
    tb_info = s1.shapes.add_textbox(Inches(4.0), Inches(4.1), Inches(5.4), Inches(2.3))
    tf_i = tb_info.text_frame
    p_i0 = tf_i.paragraphs[0]
    p_i0.text = "BÁO CÁO TIỂU LUẬN GIỮA KỲ"
    p_i0.font.size = Pt(13)
    p_i0.font.bold = True
    p_i0.font.color.rgb = C_NAVY
    p_i0.space_after = Pt(4)
    
    add_bullet(tf_i, "Sinh viên thực hiện:", bold=True, size=11, color=C_DARK)
    add_bullet(tf_i, "1. Hoàng Thái Đăng Khoa - MSSV: 52400017", size=11)
    add_bullet(tf_i, "2. Đinh Thanh Phong       - MSSV: 52400027", size=11)
    add_bullet(tf_i, "Giảng viên hướng dẫn:", bold=True, size=11, color=C_DARK)
    add_bullet(tf_i, "GV: Trần Đại Nhân", size=11, color=C_NAVY)

    # Right info photo or placeholder
    p_home = os.path.join(img_dir, "01_home.png")
    if os.path.exists(p_home):
        s1.shapes.add_picture(p_home, Inches(10.0), Inches(3.6), height=Inches(3.2))

    # ==========================================
    # SLIDE 2: MỤC LỤC & BỐ CỤC BÁO CÁO
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    create_slide_header(s2, "MỤC LỤC & TỔNG QUAN NỘI DUNG BÁO CÁO")
    
    agenda_items = [
        ("01", "ĐẶT VẤN ĐỀ & CHUẨN VITALS", 
         "• Thực trạng hiệu năng và trải nghiệm người dùng\n• Ngưỡng Bad Behavior của Google Play (>0.47%)\n• 3 Nút thắt: UI Jank, Nghẽn CPU, Rò rỉ RAM"),
        ("02", "NGUYÊN LÝ TẦNG SÂU AOSP", 
         "• Pipeline đồ họa và nhịp VSYNC 16.67ms\n• Cơ chế xử lý đơn luồng Looper & ANR quá 5 giây\n• Quản lý bộ nhớ ART Heap và ảnh hưởng của GC"),
        ("03", "BỘ CÔNG CỤ THỰC NGHIỆM PAA", 
         "• Kiến trúc MVVM & HUD Monitor thời gian thực\n• Thiết kế 3 Phòng Lab: Jank, CPU và Memory\n• So sánh cơ chế: Chưa tối ưu (Bad) vs Tối ưu (Opt)"),
        ("04", "KẾT QUẢ ĐỐI CHỨNG & ĐỀ XUẤT", 
         "• Bảng số liệu định lượng Before vs After\n• FPS +224%, CPU giảm 101 lần, RAM tiết kiệm 77%\n• 5 Nguyên tắc Vàng tối ưu cho lập trình viên")
    ]
    
    for idx, (num, h, desc) in enumerate(agenda_items):
        col = idx % 2
        row = idx // 2
        left = Inches(1.0 + col * 5.8)
        top = Inches(1.8 + row * 2.6)
        
        c = add_card(s2, left, top, Inches(5.4), Inches(2.3), bg_color=C_LIGHT_BG, border_color=C_CYAN)
        tb = s2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.0), Inches(2.0))
        tf = tb.text_frame
        
        p_n = tf.paragraphs[0]
        p_n.text = f"{num}. {h}"
        p_n.font.size = Pt(14)
        p_n.font.bold = True
        p_n.font.color.rgb = C_NAVY
        p_n.space_after = Pt(6)
        
        for line in desc.split('\n'):
            add_bullet(tf, line, size=11, color=C_DARK)

    # ==========================================
    # SLIDE 3: ĐẶT VẤN ĐỀ & TÁC ĐỘNG HIỆU NĂNG
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    create_slide_header(s3, "ĐẶT VẤN ĐỀ: TẠI SAO HIỆU NĂNG ANDROID LẠI QUAN TRỌNG?")
    
    # Top Callout Banner
    c_banner = add_card(s3, Inches(1.0), Inches(1.6), Inches(11.333), Inches(1.1), bg_color=RGBColor(254, 243, 199), border_color=RGBColor(245, 158, 11))
    tb_ban = s3.shapes.add_textbox(Inches(1.2), Inches(1.7), Inches(10.9), Inches(0.9))
    p_b = tb_ban.text_frame.paragraphs[0]
    p_b.text = "THỐNG KÊ THƯƠNG MẠI SỐNG CÒN:"
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = RGBColor(180, 83, 9)
    p_b2 = tb_ban.text_frame.add_paragraph()
    p_b2.text = "Hơn 48% người dùng sẽ gỡ cài đặt ứng dụng ngay lập tức nếu gặp hiện tượng giật, lag hoặc phản hồi chậm trễ. Hiệu năng kém trực tiếp làm sụt giảm doanh thu và phá hủy uy tín sản phẩm."
    p_b2.font.size = Pt(11.5)
    p_b2.font.color.rgb = C_DARK

    # 3 Problem Cards
    probs = [
        ("1. UI JANK & RỚT KHUNG HÌNH", 
         "• Cuộn lướt danh sách bị khựng giật, gián đoạn.\n• Thời gian Render khung hình vượt quá ngân sách 16.67ms.\n• Khung hình đóng băng (Frozen Frames > 700ms) làm người dùng ức chế.", C_RED),
        ("2. NGHẼN CPU & LỖI TREO (ANR)", 
         "• Màn hình đơ cứng, không thể chạm hay vuốt.\n• Thực thi thuật toán nặng O(N^2) trên luồng chính UI Thread.\n• Chặn MessageQueue quá 5 giây sẽ kích hoạt hộp thoại ANR hệ thống.", C_RED),
        ("3. RÒ RỈ BỘ NHỚ (OUT OF MEMORY)", 
         "• Ứng dụng chạy lâu càng lúc càng chậm chạp.\n• Tham chiếu tĩnh (static) giữ Activity đã bị đóng.\n• Bộ dọn rác GC chạy liên tục gây khựng máy và dẫn đến sập ứng dụng (Crash).", C_RED)
    ]
    
    for idx, (title, body, col_color) in enumerate(probs):
        left = Inches(1.0 + idx * 3.9)
        top = Inches(3.0)
        c = add_card(s3, left, top, Inches(3.6), Inches(3.8), bg_color=C_CARD_BG, border_color=col_color)
        tb = s3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), Inches(3.2), Inches(3.4))
        tf = tb.text_frame
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = col_color
        p.space_after = Pt(8)
        
        for line in body.split('\n'):
            add_bullet(tf, line, size=11, color=C_DARK)

    # ==========================================
    # SLIDE 4: TIÊU CHUẨN GOOGLE PLAY ANDROID VITALS
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    create_slide_header(s4, "BỘ TIÊU CHUẨN KỸ THUẬT GOOGLE PLAY ANDROID VITALS")
    
    # Left table
    c_tbl = add_card(s4, Inches(1.0), Inches(1.8), Inches(6.8), Inches(5.0), bg_color=C_WHITE)
    tb_t = s4.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(6.4), Inches(4.6))
    tf_t = tb_t.text_frame
    p = tf_t.paragraphs[0]
    p.text = "CÁC NGƯỠNG ĐÁNH GIÁ CHẤT LƯỢNG (BAD BEHAVIOR THRESHOLDS)"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    vitals_data = [
        ("Tỷ lệ Giật lag (Slow Sessions):", "Tỷ lệ phiên có > 50% khung hình chậm hơn 16.67ms vượt quá ngưỡng 0.47% sẽ bị Google phạt."),
        ("Tỷ lệ Đóng băng (Frozen Frames):", "Tỷ lệ phiên có khung hình đứng hình > 700ms vượt quá 0.10%."),
        ("Tỷ lệ Treo máy (User-perceived ANR):", "Tỷ lệ phiên xảy ra lỗi ANR do người dùng cảm nhận vượt quá ngưỡng 0.47%."),
        ("Tỷ lệ Sập ứng dụng (Crash Rate):", "Tỷ lệ phiên bị văng đột ngột (Crash / OOM) vượt quá ngưỡng 1.09%.")
    ]
    for lbl, desc in vitals_data:
        add_bullet(tf_t, lbl, bold=True, size=11, color=C_NAVY)
        add_bullet(tf_t, desc, size=10.5, color=C_DARK)
        
    # Right impact card
    c_imp = add_card(s4, Inches(8.1), Inches(1.8), Inches(4.2), Inches(5.0), bg_color=C_LIGHT_BG, border_color=C_CYAN)
    tb_imp = s4.shapes.add_textbox(Inches(8.3), Inches(2.0), Inches(3.8), Inches(4.6))
    tf_imp = tb_imp.text_frame
    p_i = tf_imp.paragraphs[0]
    p_i.text = "HẬU QUẢ KHI VƯỢT NGƯỠNG BAD BEHAVIOR"
    p_i.font.size = Pt(13)
    p_i.font.bold = True
    p_i.font.color.rgb = C_RED
    p_i.space_after = Pt(8)
    
    add_bullet(tf_imp, "1. Giáng Thứ Hạng Tìm Kiếm:", bold=True, size=11)
    add_bullet(tf_imp, "Google Play tự động ẩn hoặc giảm độ ưu tiên hiển thị ứng dụng khi người dùng tìm kiếm từ khóa liên quan.", size=10)
    add_bullet(tf_imp, "2. Loại Khỏi Mục Đề Xuất:", bold=True, size=11)
    add_bullet(tf_imp, "Mất hoàn toàn cơ hội xuất hiện trên trang chủ Play Store hoặc danh sách 'Biên tập viên chọn'.", size=10)
    add_bullet(tf_imp, "3. Hiển Thị Cảnh Báo Cho Người Dùng:", bold=True, size=11)
    add_bullet(tf_imp, "Play Store hiển thị thông báo đỏ cảnh báo người dùng: 'Ứng dụng này có thể hoạt động không ổn định trên thiết bị của bạn'.", size=10)

    # ==========================================
    # SLIDE 5: NGUYÊN LÝ TẦNG SÂU: PIPELINE ĐỒ HỌA & VSYNC
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    create_slide_header(s5, "CƠ SỞ LÝ THUYẾT: PIPELINE KẾT XUẤT ĐỒ HỌA & NHỊP VSYNC")
    
    # Left diagram
    p_pipe = os.path.join(img_dir, "08_diagram_rendering_pipeline.png")
    if os.path.exists(p_pipe):
        s5.shapes.add_picture(p_pipe, Inches(1.0), Inches(1.8), width=Inches(5.8))
        
    # Right explanation
    c_pipe = add_card(s5, Inches(7.1), Inches(1.8), Inches(5.2), Inches(5.0), bg_color=C_CARD_BG, border_color=C_CYAN)
    tb_p = s5.shapes.add_textbox(Inches(7.3), Inches(2.0), Inches(4.8), Inches(4.6))
    tf_p = tb_p.text_frame
    
    p = tf_p.paragraphs[0]
    p.text = "NGUYÊN LÝ VẬN HÀNH KHUNG HÌNH 16.67MS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    add_bullet(tf_p, "• Nhịp VSYNC Phần Cứng:", bold=True, size=11)
    add_bullet(tf_p, "Màn hình 60Hz phát tín hiệu nhịp VSYNC mỗi 16.67ms (1000ms / 60) để yêu cầu khung hình mới.", size=10.5)
    add_bullet(tf_p, "• Chu Trình Traversal (Choreographer):", bold=True, size=11)
    add_bullet(tf_p, "Main Thread phải hoàn thành 3 bước: Measure (đo đạc kích thước) → Layout (xác định vị trí) → Draw (vẽ Canvas DisplayList).", size=10.5)
    add_bullet(tf_p, "• RenderThread & GPU Processing:", bold=True, size=11)
    add_bullet(tf_p, "DisplayList được đồng bộ sang RenderThread để chuyển thành tập lệnh OpenGL/Vulkan nạp vào GPU.", size=10.5)
    add_bullet(tf_p, "• Nguyên Nhân Gây Jank:", bold=True, size=11, color=C_RED)
    add_bullet(tf_p, "Nếu bất kỳ View con nào quá phức tạp hoặc nạp ảnh thô vượt quá 16.67ms → Bỏ lỡ nhịp VSYNC → Khung hình cũ bị hiển thị lặp lại gây giật lag.", size=10.5)

    # ==========================================
    # SLIDE 6: NGUYÊN LÝ TẦNG SÂU: LOOPER ANR & ART HEAP
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    create_slide_header(s6, "CƠ SỞ LÝ THUYẾT: MÔ HÌNH LOOPER & BỘ NHỚ ART HEAP")
    
    # Left Box: Looper
    c_l = add_card(s6, Inches(1.0), Inches(1.8), Inches(5.4), Inches(5.0), bg_color=C_CARD_BG, border_color=C_NAVY)
    tb_l = s6.shapes.add_textbox(Inches(1.2), Inches(2.0), Inches(5.0), Inches(4.6))
    tf_l = tb_l.text_frame
    p_l = tf_l.paragraphs[0]
    p_l.text = "MÔ HÌNH ĐƠN LUỒNG & LỖI TREO ANR"
    p_l.font.size = Pt(13)
    p_l.font.bold = True
    p_l.font.color.rgb = C_NAVY
    p_l.space_after = Pt(6)
    
    add_bullet(tf_l, "• Kiến trúc Looper - MessageQueue:", bold=True, size=11)
    add_bullet(tf_l, "Luồng chính (Main UI Thread) chạy vòng lặp Looper.loop() liên tục lấy thông điệp từ MessageQueue để thực thi tuần tự.", size=10.5)
    add_bullet(tf_l, "• Hiện tượng Block Luồng Chính:", bold=True, size=11, color=C_RED)
    add_bullet(tf_l, "Nếu chèn tác vụ đọc ghi file (Disk I/O), gọi mạng hoặc thuật toán O(N^2) vào Main Thread, mọi sự kiện chạm vuốt tiếp theo đều bị kẹt cứng trong hàng đợi.", size=10.5)
    add_bullet(tf_l, "• Ngưỡng ANR của Hệ Thống:", bold=True, size=11)
    add_bullet(tf_l, "Hệ điều hành đặt thời hạn: Khóa phản hồi người dùng quá 5 giây sẽ lập tức bật hộp thoại 'Application Not Responding'.", size=10.5)

    # Right Box: ART Heap
    c_r = add_card(s6, Inches(6.8), Inches(1.8), Inches(5.5), Inches(5.0), bg_color=C_CARD_BG, border_color=C_NAVY)
    tb_r = s6.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.1), Inches(4.6))
    tf_r = tb_r.text_frame
    p_r = tf_r.paragraphs[0]
    p_r.text = "QUẢN LÝ BỘ NHỚ ART HEAP & RÒ RỈ RAM"
    p_r.font.size = Pt(13)
    p_r.font.bold = True
    p_r.font.color.rgb = C_NAVY
    p_r.space_after = Pt(6)
    
    add_bullet(tf_r, "• Cơ Chế Thu Gom Rác (Generational GC):", bold=True, size=11)
    add_bullet(tf_r, "Máy ảo ART phân chia bộ nhớ theo thế hệ (Young Generation & Old Generation) để tối ưu thời gian quét dọn rác.", size=10.5)
    add_bullet(tf_r, "• Cơ Chế GC Root & Rò Rỉ Bộ Nhớ:", bold=True, size=11, color=C_RED)
    add_bullet(tf_r, "Khi Activity đã kết thúc (onDestroy) nhưng vẫn bị một biến static toàn cục hoặc Background Thread giữ tham chiếu, GC không thể giải phóng vùng nhớ này vì vẫn nối với GC Root.", size=10.5)
    add_bullet(tf_r, "• Hậu Quả GC Thrashing & OOM:", bold=True, size=11)
    add_bullet(tf_r, "RAM bị chiếm dụng tăng vọt → ART liên tục kích hoạt dọn rác kèm quãng dừng (Stop-the-world pauses) làm lag máy và cuối cùng sập ứng dụng (OutOfMemoryError).", size=10.5)

    # ==========================================
    # SLIDE 7: BỘ CÔNG CỤ THỰC NGHIỆM PAA & HUD MONITOR
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    create_slide_header(s7, "HIỆN THỰC THỰC NGHIỆM: BỘ CÔNG CỤ PAA & THANH HUD OVERLAY")
    
    # Left app photo
    p_home = os.path.join(img_dir, "01_home.png")
    if os.path.exists(p_home):
        s7.shapes.add_picture(p_home, Inches(1.0), Inches(1.8), height=Inches(5.0))
        
    # Right explanation
    c_paa = add_card(s7, Inches(4.2), Inches(1.8), Inches(8.1), Inches(5.0), bg_color=C_CARD_BG, border_color=C_CYAN)
    tb_paa = s7.shapes.add_textbox(Inches(4.5), Inches(2.0), Inches(7.5), Inches(4.6))
    tf_paa = tb_paa.text_frame
    
    p = tf_paa.paragraphs[0]
    p.text = "KIẾN TRÚC KỸ THUẬT CỦA ỨNG DỤNG PAA"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    add_bullet(tf_paa, "• Mô Hình Kiến Trúc Chuẩn:", bold=True, size=11)
    add_bullet(tf_paa, "Xây dựng theo mô hình MVVM (Model-View-ViewModel) + Clean Architecture + Kotlin Coroutines + Material Design 3.", size=10.5)
    add_bullet(tf_paa, "• Hạt Nhân Đo Đạc Thời Gian Thực (Overlay HUD Monitor):", bold=True, size=11, color=C_NAVY)
    add_bullet(tf_paa, "- Đo Tốc độ Khung hình: Lắng nghe Window.OnFrameMetricsAvailableListener bắt chính xác mili-giây từng frame.", size=10)
    add_bullet(tf_paa, "- Đo Sử dụng CPU: Đọc xung nhịp từ tệp nhân hệ điều hành /proc/stat và /proc/[pid]/stat.", size=10)
    add_bullet(tf_paa, "- Đo Chiếm dụng Bộ nhớ: Trích xuất chỉ số PSS (Proportional Set Size) từ ActivityManager.getProcessMemoryInfo().", size=10)
    add_bullet(tf_paa, "• 3 Phòng Lab Độc Lập:", bold=True, size=11)
    add_bullet(tf_paa, "Tích hợp công tắc chuyển đổi trực tiếp giữa hai trạng thái: BAD (Mô phỏng thói quen lập trình sai lầm) và OPTIMIZED (Áp dụng giải pháp kỹ thuật tối ưu).", size=10.5)

    # ==========================================
    # SLIDE 8: PHÒNG LAB 1: THỰC NGHIỆM RENDER JANK
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    create_slide_header(s8, "PHÒNG LAB 1: PHÂN TÍCH VÀ TỐI ƯU HÓA RENDER JANK (UI)")
    
    # Left screenshot
    p_jank = os.path.join(img_dir, "03_jank_opt.png")
    if os.path.exists(p_jank):
        s8.shapes.add_picture(p_jank, Inches(1.0), Inches(1.8), height=Inches(5.0))
        
    # Right Box
    c_jk = add_card(s8, Inches(4.2), Inches(1.8), Inches(8.1), Inches(5.0), bg_color=C_CARD_BG, border_color=C_CYAN)
    tb_jk = s8.shapes.add_textbox(Inches(4.5), Inches(2.0), Inches(7.5), Inches(4.6))
    tf_jk = tb_jk.text_frame
    
    p = tf_jk.paragraphs[0]
    p.text = "ĐỐI CHỨNG KỸ THUẬT GIỮA HAI TRẠNG THÁI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    add_bullet(tf_jk, "KỊCH BẢN CHƯA TỐI ƯU (BAD):", bold=True, size=11, color=C_RED)
    add_bullet(tf_jk, "• Cấu trúc View phân cấp sâu: Lồng nhau tới 6 tầng LinearLayout phức tạp khiến quá trình đo đạc (Measure) và bố cục (Layout) bị đệ quy nhiều lần.", size=10)
    add_bullet(tf_jk, "• Nạp ảnh đồng bộ: Nạp ảnh Bitmap thô kích thước lớn trực tiếp từ tài nguyên trên Main Thread mà không qua giải nén hay thu nhỏ.", size=10)
    add_bullet(tf_jk, "• Kết quả: FPS sụt giảm thảm hại xuống 17.0 FPS, tỷ lệ rớt khung hình lên tới 71.4%.", size=10, bold=True, color=C_RED)
    
    add_bullet(tf_jk, "KỊCH BẢN ĐÃ TỐI ƯU (OPTIMIZED):", bold=True, size=11, color=C_GREEN)
    add_bullet(tf_jk, "• Làm phẳng bố cục hoàn toàn: Sử dụng ConstraintLayout giúp giảm toàn bộ cây phân cấp View xuống đúng 1 tầng duy nhất.", size=10)
    add_bullet(tf_jk, "• Thư viện Glide nạp ảnh thông minh: Tự động nén ảnh theo chuẩn RGB_565, hỗ trợ bộ nhớ đệm 2 tầng (Memory Cache + Disk Cache).", size=10)
    add_bullet(tf_jk, "• Kết quả: Tốc độ khung hình tăng vọt lên 55.1 FPS (+224.1%), cuộn trang mượt mà tuyệt đối.", size=10, bold=True, color=C_GREEN)

    # ==========================================
    # SLIDE 9: PHÒNG LAB 2: THỰC NGHIỆM NGHẼN CPU
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    create_slide_header(s9, "PHÒNG LAB 2: PHÂN TÍCH VÀ TỐI ƯU HÓA NGHẼN TÍNH TOÁN CPU")
    
    # Left screenshot
    p_cpu = os.path.join(img_dir, "07_cpu_result_panel.png")
    if os.path.exists(p_cpu):
        s9.shapes.add_picture(p_cpu, Inches(1.0), Inches(1.8), height=Inches(5.0))
        
    # Right Box
    c_cp = add_card(s9, Inches(5.6), Inches(1.8), Inches(6.7), Inches(5.0), bg_color=C_CARD_BG, border_color=C_CYAN)
    tb_cp = s9.shapes.add_textbox(Inches(5.8), Inches(2.0), Inches(6.3), Inches(4.6))
    tf_cp = tb_cp.text_frame
    
    p = tf_cp.paragraphs[0]
    p.text = "GIẢI QUYẾT BÀI TOÁN XỬ LÝ NẶNG & CHẶN LUỒNG"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    add_bullet(tf_cp, "KỊCH BẢN CHƯA TỐI ƯU (BAD):", bold=True, size=11, color=C_RED)
    add_bullet(tf_cp, "• Thuật toán BubbleSort O(N^2) sắp xếp ngẫu nhiên 25,000 số nguyên.", size=10)
    add_bullet(tf_cp, "• Chạy trực tiếp trên Main Thread: Chiếm trọn tài nguyên CPU của luồng giao diện trong hơn 2 giây liên tục.", size=10)
    add_bullet(tf_cp, "• Kết quả: Giao diện hoàn toàn bị đơ cứng (Frozen 2,022 ms), đứng trước nguy cơ kích hoạt cảnh báo ANR.", size=10, bold=True, color=C_RED)
    
    add_bullet(tf_cp, "KỊCH BẢN ĐÃ TỐI ƯU (OPTIMIZED):", bold=True, size=11, color=C_GREEN)
    add_bullet(tf_cp, "• Nâng cấp thuật toán sang QuickSort O(N log N) kết hợp chia để trị.", size=10)
    add_bullet(tf_cp, "• Phân luồng bất đồng bộ với Kotlin Coroutines: Đẩy toàn bộ quá trình xử lý sang Dispatchers.Default (tận dụng đa nhân CPU phần cứng).", size=10)
    add_bullet(tf_cp, "• Kết quả: Hoàn thành trong 20 ms (nhanh hơn 101 lần), luồng UI vẫn phản hồi mượt mà không trễ 1 khung hình.", size=10, bold=True, color=C_GREEN)

    # ==========================================
    # SLIDE 10: PHÒNG LAB 3: THỰC NGHIỆM RÒ RỈ BỘ NHỚ
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    create_slide_header(s10, "PHÒNG LAB 3: PHÂN TÍCH VÀ TRIỆT TIÊU RÒ RỈ BỘ NHỚ (RAM)")
    
    # Left screenshot
    p_mem = os.path.join(img_dir, "05_memory_lab.png")
    if os.path.exists(p_mem):
        s10.shapes.add_picture(p_mem, Inches(1.0), Inches(1.8), height=Inches(5.0))
        
    # Right Box
    c_m = add_card(s10, Inches(4.2), Inches(1.8), Inches(8.1), Inches(5.0), bg_color=C_CARD_BG, border_color=C_CYAN)
    tb_m = s10.shapes.add_textbox(Inches(4.5), Inches(2.0), Inches(7.5), Inches(4.6))
    tf_m = tb_m.text_frame
    
    p = tf_m.paragraphs[0]
    p.text = "MÔ PHỎNG VÀ KHẮC PHỤC RÒ RỈ HOÀN TOÀN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_NAVY
    p.space_after = Pt(6)
    
    add_bullet(tf_m, "KỊCH BẢN CHƯA TỐI ƯU (BAD):", bold=True, size=11, color=C_RED)
    add_bullet(tf_m, "• Giữ Activity trong biến tĩnh: Khai báo static companion object lưu trữ danh sách các LeakyActivity đã bị đóng.", size=10)
    add_bullet(tf_m, "• Khóa Garbage Collector: Cây tham chiếu GC Root ngăn cản hệ điều hành thu hồi bộ nhớ của 10 màn hình đã onDestroy.", size=10)
    add_bullet(tf_m, "• Kết quả: Bộ nhớ RAM PSS tăng vọt lên 88.0 MB, dù gọi System.gc() cũng không thể giải phóng.", size=10, bold=True, color=C_RED)
    
    add_bullet(tf_m, "KỊCH BẢN ĐÃ TỐI ƯU (OPTIMIZED):", bold=True, size=11, color=C_GREEN)
    add_bullet(tf_m, "• Cơ chế Tham Chiếu Yếu: Chuyển toàn bộ danh sách sang WeakReference<Activity>.", size=10)
    add_bullet(tf_m, "• Dọn dẹp theo Vòng đời: Chủ động hủy đăng ký listener và xóa tham chiếu trong hàm onDestroy().", size=10)
    add_bullet(tf_m, "• Kết quả: Toàn bộ 10 thể hiện rò rỉ được dọn dẹp sạch sẽ, RAM PSS giảm về 19.8 MB (tiết kiệm 77.5% bộ nhớ).", size=10, bold=True, color=C_GREEN)

    # ==========================================
    # SLIDE 11: BẢNG SỐ LIỆU ĐỐI CHỨNG ĐỊNH LƯỢNG
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    create_slide_header(s11, "KẾT QUẢ THỰC NGHIỆM: ĐỐI CHỨNG ĐỊNH LƯỢNG BEFORE VS AFTER")
    
    # Left table
    tbl_shape = s11.shapes.add_table(6, 4, Inches(1.0), Inches(1.8), Inches(6.8), Inches(4.8))
    table = tbl_shape.table
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(1.5)
    table.columns[2].width = Inches(1.5)
    table.columns[3].width = Inches(1.6)
    
    headers = ["Chỉ số Kỹ thuật", "Chưa Tối Ưu (Bad)", "Đã Tối Ưu (Opt)", "Mức Cải Thiện"]
    for i, h in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(10)
            p.font.bold = True
            p.font.color.rgb = C_WHITE
            
    benchmarks = [
        ("Tốc độ Khung hình (FPS)", "17.0 FPS (Lag)", "55.1 FPS (Mượt)", "+224.1%"),
        ("Tỷ lệ Rớt Khung hình", "71.4% (Rất cao)", "35.7% (Đạt chuẩn)", "Giảm 50.0%"),
        ("Thời gian Xử lý CPU", "2,022 ms (Chặn UI)", "20 ms (Chạy nền)", "Nhanh gấp 101 lần"),
        ("Bộ nhớ Chiếm dụng (PSS)", "88.0 MB (Leak 10)", "19.8 MB (Sạch rác)", "Tiết kiệm 77.5%"),
        ("Chuẩn Google Vitals", "KHÔNG ĐẠT", "VƯỢT CHUẨN", "ĐẠT 100%")
    ]
    
    for row_idx, row_data in enumerate(benchmarks, start=1):
        bg = C_WHITE if row_idx % 2 == 1 else C_LIGHT_BG
        for col_idx, text in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(9.5)
                p.font.color.rgb = C_DARK
                if col_idx == 3:
                    p.font.bold = True
                    p.font.color.rgb = C_GREEN
                    
    # Right chart
    p_chart = os.path.join(img_dir, "11_chart_performance_benchmarks.png")
    if os.path.exists(p_chart):
        s11.shapes.add_picture(p_chart, Inches(8.1), Inches(1.8), width=Inches(4.2))

    # ==========================================
    # SLIDE 12: 5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    create_slide_header(s12, "5 NGUYÊN TẮC VÀNG CHO LẬP TRÌNH VIÊN ANDROID CHUYÊN NGHIỆP")
    
    principles = [
        ("01", "TUYỆT ĐỐI KHÔNG CHẶN MAIN THREAD", 
         "Mọi thao tác tính toán nặng, đọc ghi file, mạng và Database phải được đẩy vào Kotlin Coroutines (Dispatchers.IO / Dispatchers.Default)."),
        ("02", "LÀM PHẲNG CẤU TRÚC GIAO DIỆN", 
         "Thay thế hoàn toàn bố cục lồng nhau nhiều tầng bằng ConstraintLayout; áp dụng ViewStub để trì hoãn nạp UI chưa cần thiết."),
        ("03", "QUẢN LÝ VÒNG ĐỜI & CHỐNG RÒ RỈ RAM", 
         "Không bao giờ lưu Context/Activity trong biến static; luôn dùng WeakReference và hủy đăng ký các listener trong onDestroy()."),
        ("04", "NẠP HÌNH ẢNH THÔNG MINH", 
         "Sử dụng thư viện Glide/Coil, kích hoạt chuẩn nén Bitmap RGB_565 và tự động scale ảnh vừa vặn với kích thước hiển thị của ImageView."),
        ("05", "CHỦ ĐỘNG PROFILING ĐỊNH KỲ", 
         "Luôn đo đạc trước khi tối ưu bằng Android Studio Profiler, Perfetto và dumpsys gfxinfo để phát hiện sớm các hiện tượng thoái hóa hiệu năng.")
    ]
    
    for idx, (num, h, desc) in enumerate(principles):
        top = Inches(1.8 + idx * 1.0)
        c = add_card(s12, Inches(1.0), top, Inches(11.333), Inches(0.85), bg_color=C_CARD_BG, border_color=C_CYAN)
        tb = s12.shapes.add_textbox(Inches(1.2), top + Inches(0.08), Inches(10.9), Inches(0.7))
        tf = tb.text_frame
        
        p = tf.paragraphs[0]
        p.text = f"{num}. {h}: "
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_NAVY
        
        run_b = p.add_run()
        run_b.text = desc
        run_b.font.size = Pt(10.5)
        run_b.font.bold = False
        run_b.font.color.rgb = C_DARK

    # ==========================================
    # SLIDE 13: KẾT LUẬN & LỜI CẢM ƠN (Q&A)
    # ==========================================
    s13 = prs.slides.add_slide(blank_layout)
    bg13 = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg13.fill.solid()
    bg13.fill.fore_color.rgb = C_NAVY
    bg13.line.fill.background()
    
    tb_c = s13.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(1.2))
    p_c = tb_c.text_frame.paragraphs[0]
    p_c.text = "KẾT LUẬN & ĐỊNH HƯỚNG MỞ RỘNG"
    p_c.font.size = Pt(26)
    p_c.font.bold = True
    p_c.font.color.rgb = C_WHITE
    p_c.alignment = PP_ALIGN.CENTER
    
    # 2 Cards: Achievements & Future
    c_ach = add_card(s13, Inches(1.2), Inches(2.2), Inches(5.3), Inches(2.6), bg_color=C_WHITE)
    tb_ach = s13.shapes.add_textbox(Inches(1.4), Inches(2.3), Inches(4.9), Inches(2.4))
    tf_a = tb_ach.text_frame
    p_a0 = tf_a.paragraphs[0]
    p_a0.text = "ĐÓNG GÓP CỦA ĐỀ TÀI"
    p_a0.font.size = Pt(13)
    p_a0.font.bold = True
    p_a0.font.color.rgb = C_NAVY
    p_a0.space_after = Pt(4)
    add_bullet(tf_a, "• Làm sáng tỏ nguyên lý tầng sâu AOSP (VSYNC, Looper, ART).", size=10)
    add_bullet(tf_a, "• Xây dựng thành công bộ công cụ PAA & HUD Monitor đo thời gian thực.", size=10)
    add_bullet(tf_a, "• Cung cấp bộ số liệu đối chứng định lượng thuyết phục (+224% FPS).", size=10)
    
    c_fut = add_card(s13, Inches(6.8), Inches(2.2), Inches(5.3), Inches(2.6), bg_color=C_WHITE)
    tb_fut = s13.shapes.add_textbox(Inches(7.0), Inches(2.3), Inches(4.9), Inches(2.4))
    tf_f = tb_fut.text_frame
    p_f0 = tf_f.paragraphs[0]
    p_f0.text = "HƯỚNG PHÁT TRIỂN TIẾP THEO"
    p_f0.font.size = Pt(13)
    p_f0.font.bold = True
    p_f0.font.color.rgb = C_NAVY
    p_f0.space_after = Pt(4)
    add_bullet(tf_f, "• Mở rộng phân tích Recomposition cho Jetpack Compose.", size=10)
    add_bullet(tf_f, "• Tự động phát hiện rò rỉ bộ nhớ với engine LeakCanary tích hợp.", size=10)
    add_bullet(tf_f, "• Đo lường mức độ tiêu hao năng lượng pin và băng thông mạng.", size=10)
    
    # Bottom Thanks & QA box
    tb_thx = s13.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(11.333), Inches(1.8))
    tf_th = tb_thx.text_frame
    p_th1 = tf_th.paragraphs[0]
    p_th1.text = "XIN CHÂN THÀNH CẢM ƠN THẦY TRẦN ĐẠI NHÂN VÀ CÁC BẠN!"
    p_th1.font.size = Pt(22)
    p_th1.font.bold = True
    p_th1.font.color.rgb = C_CYAN
    p_th1.alignment = PP_ALIGN.CENTER
    p_th1.space_after = Pt(6)
    
    p_th2 = tf_th.add_paragraph()
    p_th2.text = "Q&A SESSION - MỜI THẦY VÀ CÁC BẠN ĐẶT CÂU HỎI CHO NHÓM"
    p_th2.font.size = Pt(14)
    p_th2.font.color.rgb = C_WHITE
    p_th2.alignment = PP_ALIGN.CENTER

    prs.save(out_pptx)
    print(f"File PowerPoint 13 slide đã được tạo thành công tại: {out_pptx}")

if __name__ == "__main__":
    main()
