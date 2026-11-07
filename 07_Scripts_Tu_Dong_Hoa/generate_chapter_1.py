import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

OUT_DIR = r"D:\MOBI GK\01_Bao_Cao_Nop_Bai"

# Brand Colors (TDTU & PAA)
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

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run(text)
    set_font(r, "Times New Roman", 15, bold=True, color=C_NAVY)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    set_font(r, "Times New Roman", 13.5, bold=True, color=C_SCARLET)
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    set_font(r, "Times New Roman", 13, bold=True, color=C_NAVY)
    return p

def add_body_paragraph(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.first_line_indent = Inches(0.5)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        set_font(r_pre, "Times New Roman", 13, bold=True, color=C_SLATE)
    r = p.add_run(text)
    set_font(r, "Times New Roman", 13, color=C_SLATE)
    return p

def add_bullet_point(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.left_indent = Inches(0.7)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        set_font(r_pre, "Times New Roman", 13, bold=True, color=C_NAVY)
    r = p.add_run(text)
    set_font(r, "Times New Roman", 13, color=C_SLATE)
    return p

def build_chapter_1():
    doc = docx.Document()
    apply_tdtu_page_setup(doc)

    # =========================================================================
    # TIÊU ĐỀ CHƯƠNG
    # =========================================================================
    add_heading_1(doc, "CHƯƠNG I: TỔNG QUAN ĐỀ TÀI VÀ ĐẶT VẤN ĐỀ")

    # =========================================================================
    # 1.1. ĐẶT VẤN ĐỀ VÀ TÍNH CẤP THIẾT
    # =========================================================================
    add_heading_2(doc, "1.1. ĐẶT VẤN ĐỀ VÀ TÍNH CẤP THIẾT CỦA ĐỀ TÀI")

    add_heading_3(doc, "1.1.1. Thực trạng bùng nổ và sự phân mảnh phần cứng trong hệ sinh thái Android")
    add_body_paragraph(
        doc,
        "Hệ điều hành Android hiện nay đang giữ vững vị thế là nền tảng di động phổ biến nhất hành tinh, chiếm hơn 70% thị phần toàn cầu với hơn 3 tỷ thiết bị đang hoạt động. Tuy nhiên, đằng sau sự thống trị vượt bậc đó là một thực trạng thách thức vô cùng khốc liệt đối với các kỹ sư phát triển phần mềm: sự phân mảnh phần cứng (Hardware Fragmentation). Thống kê chính thức từ Google ghi nhận có hơn 24.000 mẫu mã thiết bị phần cứng khác nhau đang cùng tham gia vận hành hệ sinh thái Android, trải dài từ các dòng máy giá rẻ (Low-end/Entry-level) với cấu hình vi xử lý khiêm tốn, dung lượng RAM hạn hẹp 2GB - 3GB, cho tới các dòng điện thoại cao cấp (Flagship) trang bị vi xử lý đa nhân xung nhịp cao và màn hình tần số quét 120Hz."
    )
    add_body_paragraph(
        doc,
        "Khác với môi trường máy tính để bàn (Desktop) hay hệ sinh thái đóng kín của Apple iOS, thiết bị di động Android luôn phải hoạt động trong những giới hạn vật lý nghiêm ngặt: dung lượng pin hữu hạn, cơ chế tản nhiệt thụ động không quạt gió dẫn đến hiện tượng bóp nghẽn xung nhịp khi nhiệt độ tăng cao (Thermal Throttling), và dung lượng bộ nhớ RAM luôn bị chia sẻ gay gắt giữa hệ thống AOSP, các dịch vụ nền tảng Google Play Services và hàng chục tiến trình chạy ngầm. Trong bối cảnh đó, một ứng dụng di động chỉ 'hoạt động đúng tính năng' (Functional Correctness) là hoàn toàn chưa đủ. Nếu không được tối ưu hóa hiệu năng một cách khoa học ngay từ khâu thiết kế kiến trúc mã nguồn, ứng dụng sẽ nhanh chóng làm kiệt quệ tài nguyên phần cứng, gây ra những trải nghiệm gián đoạn tệ hại cho người sử dụng."
    )

    add_heading_3(doc, "1.1.2. Ba 'căn bệnh' hiệu năng kinh điển trên ứng dụng di động")
    add_body_paragraph(
        doc,
        "Trong thực tế kỹ thuật phát triển ứng dụng di động, các kỹ sư phần mềm thường xuyên phải đối mặt với 3 nút thắt hiệu năng kinh điển, được ví như 3 'căn bệnh' trầm kha tàn phá trải nghiệm người dùng:"
    )
    add_bullet_point(
        doc,
        ": Mắt người có thể cảm nhận sự giật cục khi nhịp hiển thị hình ảnh bị gián đoạn. Trên màn hình tiêu chuẩn tần số quét 60Hz, hệ thống phát tín hiệu đồng bộ dọc VSYNC mỗi 16.67ms (1000ms / 60). Luồng giao diện (Main UI Thread) bắt buộc phải hoàn tất toàn bộ chu trình đo đạc (Measure), sắp đặt vị trí (Layout) và kết xuất lệnh vẽ (Draw) trong khoảng thời gian này. Nếu bố cục giao diện bị lồng ghép quá sâu nhiều tầng, hoặc nhà phát triển sơ suất giải mã ảnh kích thước lớn trực tiếp trên luồng chính, thời gian xử lý khung hình sẽ vượt quá 16.67ms, dẫn đến việc khung hình bị bỏ rơi (Dropped Frame), gây ra hiện tượng khựng giật thị giác khó chịu.",
        bold_prefix="1. Hiện tượng khựng giật giao diện (UI Jank / Dropped Frames)"
    )
    add_bullet_point(
        doc,
        ": Luồng chính của Android vận hành dựa trên cơ chế hàng đợi thông điệp đơn luồng Looper/MessageQueue. Khi một tác vụ tính toán nặng có độ phức tạp thuật toán cao (như các giải thuật duyệt mảng O(N²)), các thao tác truy vấn cơ sở dữ liệu SQLite hoặc đọc ghi tập tin bị thực thi trực tiếp trên Main Thread, hàng đợi MessageQueue sẽ bị khóa cứng. Khi người dùng chạm tay vào màn hình hoặc bấm phím cứng mà hệ thống không thể phân phối sự kiện trong vòng 5 giây, hệ điều hành Android sẽ buộc phải kích hoạt hộp thoại cảnh báo hệ thống ANR, cho phép người dùng đóng cưỡng bức ứng dụng.",
        bold_prefix="2. Hiện tượng đóng băng màn hình và Lỗi ứng dụng không phản hồi (ANR - Application Not Responding)"
    )
    add_bullet_point(
        doc,
        ": Bộ nhớ RAM trên thiết bị di động được quản lý bởi máy ảo Android Runtime (ART) thông qua cơ chế thu gom rác tự động (Garbage Collection). Tuy nhiên, khi một đối tượng vòng đời ngắn (như Activity đã bị đóng - onDestroy) vẫn bị giữ lại bởi một đường dẫn tham chiếu mạnh (Strong Reference) xuất phát từ các điểm neo tĩnh (GC Root như biến static, Singleton, luồng ngầm Handler chạy trễ, hay Listener toàn cục không được hủy đăng ký), bộ dọn rác GC hoàn toàn bất lực không thể thu hồi vùng nhớ này. Hậu quả là dung lượng RAM PSS bị tích lũy phình to liên tục theo thời gian, ép GC phải chạy dọn dẹp cưỡng bức làm máy khựng lag, và cuối cùng dẫn đến thảm họa sập app đột ngột do tràn bộ nhớ (OutOfMemoryError Crash).",
        bold_prefix="3. Hiện tượng rò rỉ bộ nhớ (Memory Leak) và Lỗi tràn RAM (OutOfMemoryError)"
    )

    add_heading_3(doc, "1.1.3. Tác động kinh doanh sống còn đối với sản phẩm phần mềm")
    add_body_paragraph(
        doc,
        "Những khiếm khuyết về mặt hiệu năng không đơn thuần là câu chuyện kỹ thuật nội bộ, mà trực tiếp định đoạt sự sống còn về mặt thương mại của một sản phẩm công nghệ. Các báo cáo phân tích hành vi người dùng di động quy mô lớn đã chứng minh rằng:"
    )
    add_bullet_point(
        doc,
        " sẽ chủ động gỡ bỏ cài đặt ứng dụng ngay trong 24 giờ đầu tiên nếu họ gặp phải tình trạng ứng dụng bị khựng giật, phản hồi chậm trễ hoặc bị treo màn hình.",
        bold_prefix="Hơn 48% người dùng"
    )
    add_bullet_point(
        doc,
        " bị sụt giảm từ 4.5 sao xuống dưới mức 3.0 sao, xuất phát chủ yếu từ những lời phàn nàn về độ ổn định và tiêu hao pin, khiến ứng dụng mất đi hơn 70% lượng người dùng tiềm năng tải về tự nhiên.",
        bold_prefix="Điểm đánh giá trung bình (Store Rating)"
    )
    add_bullet_point(
        doc,
        " bị bào mòn nghiêm trọng khi doanh nghiệp phải tiêu tốn chi phí khổng lồ cho các chiến dịch quảng cáo thu hút người dùng mới (User Acquisition), nhưng tỷ lệ giữ chân (Retention Rate) lại rơi tự do vì trải nghiệm phần mềm nghèo nàn.",
        bold_prefix="Chỉ số tài chính và giá trị vòng đời khách hàng (LTV)"
    )

    # =========================================================================
    # 1.2. TIÊU CHUẨN GOOGLE PLAY ANDROID VITALS
    # =========================================================================
    add_heading_2(doc, "1.2. TIÊU CHUẨN ĐÁNH GIÁ CHẤT LƯỢNG GOOGLE PLAY ANDROID VITALS")

    add_heading_3(doc, "1.2.1. Bản chất hệ thống giám sát tự động của Google Play Services")
    add_body_paragraph(
        doc,
        "Để bảo vệ quyền lợi người tiêu dùng và nâng cao chất lượng toàn diện của kho ứng dụng, Google đã chính thức ban hành bộ tiêu chuẩn kỹ thuật mang tên Google Play Android Vitals. Đây là một hệ thống radar đo lường viễn thám tự động (Automated Telemetry System) được tích hợp ở tầng lõi của Google Play Services trên hàng tỷ thiết bị Android toàn cầu. Hệ thống này âm thầm ghi nhận dữ liệu thực tế (Real-world User Telemetry) về độ ổn định, tốc độ vẽ khung hình, thời gian khởi động app và tình trạng pin mà không làm ảnh hưởng đến tính riêng tư của người dùng."
    )

    add_heading_3(doc, "1.2.2. Ba ngưỡng cảnh báo đỏ kỹ thuật (Bad Behavior Thresholds)")
    add_body_paragraph(
        doc,
        "Google Play thiết lập các ranh giới kiểm soát chất lượng nghiêm ngặt gọi là các 'Ngưỡng hành vi xấu' (Bad Behavior Thresholds). Khi một ứng dụng chạm hoặc vượt qua các ngưỡng này, hệ thống sẽ tự động xếp ứng dụng vào diện cảnh báo nguy hiểm:"
    )
    add_bullet_point(
        doc,
        ": Được xác định khi một phiên sử dụng có trên 25% tổng số khung hình mất nhiều hơn 16.67ms để hoàn tất chu trình kết xuất. Ngưỡng cảnh báo đỏ của Google quy định tỷ lệ các phiên chậm trên toàn bộ cơ sở người dùng không được vượt quá mức cho phép.",
        bold_prefix="1. Tỷ lệ phiên kết xuất chậm (Slow Rendering Sessions):"
    )
    add_bullet_point(
        doc,
        ": Đây là chỉ số đo lường các khung hình bị đứng hình chết cứng nghiêm trọng với thời gian trễ vượt quá 700ms (tương đương với việc màn hình bị đơ hoàn toàn gần 1 giây). Ngưỡng đỏ tối đa cực kỳ khắt khe của Google quy định tỷ lệ phiên có khung hình đóng băng không được vượt quá 0.10%.",
        bold_prefix="2. Tỷ lệ phiên có khung hình đóng băng (Frozen Frames Sessions):"
    )
    add_bullet_point(
        doc,
        ": Chỉ số phản ánh tỷ lệ phiên sử dụng mà người dùng thực tế gặp phải lỗi treo app ANR. Lằn ranh đỏ tối đa do Google áp đặt trên Play Store là 0.47%. Bất kỳ ứng dụng nào vượt qua con số 0.47% này đều bị coi là sản phẩm có rủi ro kỹ thuật nghiêm trọng.",
        bold_prefix="3. Tỷ lệ treo ứng dụng do người dùng cảm nhận (User-perceived ANR Rate):"
    )

    add_heading_3(doc, "1.2.3. Hậu quả thuật toán đối với ứng dụng vi phạm")
    add_body_paragraph(
        doc,
        "Các chế tài thuật toán mà Google Play Store áp dụng đối với những ứng dụng vi phạm ngưỡng Android Vitals mang tính răn đe rất cao:"
    )
    add_bullet_point(
        doc,
        ": Thuật toán tìm kiếm của Play Store tự động hạ điểm chất lượng, giảm độ ưu tiên hiển thị ứng dụng khi người dùng tìm kiếm từ khóa liên quan.",
        bold_prefix="Giáng thứ hạng tìm kiếm (Search Ranking Penalty)"
    )
    add_bullet_point(
        doc,
        ": Mất hoàn toàn cơ hội xuất hiện trên các banner trang chủ, danh sách 'Lựa chọn của biên tập viên' (Editor's Choice) hay bảng xếp hạng ứng dụng thịnh hành.",
        bold_prefix="Bị loại khỏi các danh mục đề xuất nổi bật"
    )
    add_bullet_point(
        doc,
        ": Trên trang chi tiết cài đặt ứng dụng (Store Listing), Google Play sẽ hiển thị một dòng thông báo màu đỏ nổi bật trực tiếp tới người dùng chuẩn bị tải: 'Ứng dụng này có thể thường xuyên bị dừng hoặc giật lag trên thiết bị của bạn'.",
        bold_prefix="Hiển thị cảnh báo đỏ trực tiếp"
    )

    # =========================================================================
    # 1.3. MỤC TIÊU, ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU
    # =========================================================================
    add_heading_2(doc, "1.3. MỤC TIÊU, ĐỐI TƯỢNG VÀ PHẠM VI NGHIÊN CỨU")

    add_heading_3(doc, "1.3.1. Mục tiêu nghiên cứu")
    add_body_paragraph(
        doc,
        "Xuất phát từ tính cấp thiết về mặt kỹ thuật và thương mại nêu trên, đề tài tiểu luận hướng tới 3 mục tiêu cụ thể:"
    )
    add_bullet_point(
        doc,
        ": Đi sâu giải mã các cơ chế vận hành cốt lõi ở tầng thấp của AOSP, bao gồm cơ chế xung nhịp VSYNC, luồng RenderThread, hàng đợi thông điệp Looper/MessageQueue và thuật toán dọn rác phân thế hệ của máy ảo ART.",
        bold_prefix="1. Nghiên cứu lý thuyết nền tảng"
    )
    add_bullet_point(
        doc,
        ": Tự thiết kế và lập trình hoàn chỉnh một ứng dụng di động thực nghiệm (mang tên PAA) có khả năng mô phỏng trực quan 3 lỗi hiệu năng kinh điển và tích hợp sẵn bộ đo đạc phần cứng thời gian thực.",
        bold_prefix="2. Hiện thực hóa công cụ thực nghiệm"
    )
    add_bullet_point(
        doc,
        ": Kiểm chứng và chứng minh hiệu quả của các giải pháp tối ưu hóa thông qua các số liệu đo lường định lượng minh bạch (Before vs After), từ đó đúc kết thành bộ quy chuẩn thực chiến cho lập trình viên.",
        bold_prefix="3. Đo lường định lượng và chuẩn hóa giải pháp"
    )

    add_heading_3(doc, "1.3.2. Đối tượng và phạm vi nghiên cứu")
    add_bullet_point(
        doc,
        ": Hệ điều hành di động Android phiên bản từ Android 7.0 (API 24) đến Android 14 (API 34); kiến trúc máy ảo Android Runtime (ART); các API đo lường hiệu năng FrameMetrics, Debug.MemoryInfo và Process API.",
        bold_prefix="Đối tượng nghiên cứu"
    )
    add_bullet_point(
        doc,
        ": Ngôn ngữ lập trình Kotlin trên môi trường Android Studio; kiến trúc ứng dụng Model-View-ViewModel (MVVM); các thư viện thành phần Jetpack (RecyclerView, ListAdapter, DiffUtil, ConstraintLayout), thư viện bất đồng bộ Kotlin Coroutines và thư viện nạp ảnh hiện đại Coil.",
        bold_prefix="Phạm vi công nghệ"
    )

    # =========================================================================
    # 1.4. PHƯƠNG PHÁP NGHIÊN CỨU VÀ GIẢI PHÁP ĐỀ XUẤT (ỨNG DỤNG PAA)
    # =========================================================================
    add_heading_2(doc, "1.4. PHƯƠNG PHÁP NGHIÊN CỨU VÀ GIẢI PHÁP ĐỀ XUẤT (ỨNG DỤNG PAA)")

    add_heading_3(doc, "1.4.1. Phương pháp nghiên cứu thực nghiệm đối chứng định lượng (A/B Testing)")
    add_body_paragraph(
        doc,
        "Đề tài từ chối cách tiếp cận thuần túy lý thuyết giáo điều. Thay vào đó, nhóm áp dụng phương pháp nghiên cứu thực nghiệm đối chứng A/B (Comparative Empirical Benchmarking). Trên cùng một thiết bị phần cứng vật lý và trong cùng một điều kiện môi trường thực thi, nhóm xây dựng song song hai phiên bản mã nguồn:"
    )
    add_bullet_point(
        doc,
        ": Cố ý cài đặt các lỗi thiết kế phổ biến, vi phạm các quy tắc hiệu năng để tái hiện chân thực các hiện tượng gián đoạn.",
        bold_prefix="Phiên bản Chưa tối ưu (BAD)"
    )
    add_bullet_point(
        doc,
        ": Áp dụng triệt để các kỹ thuật kiến trúc chuẩn mực để sửa chữa và nâng cấp.",
        bold_prefix="Phiên bản Đã tối ưu (OPTIMIZED)"
    )

    add_heading_3(doc, "1.4.2. Khái quát giải pháp công cụ thực nghiệm PAA và hệ thống HUD")
    add_body_paragraph(
        doc,
        "Để thực thi phương pháp trên, nhóm đã tự tay xây dựng ứng dụng thực nghiệm PAA (Performance Analysis App). Ứng dụng sở hữu tính năng đột phá là thanh giám sát HUD Monitor (Heads-Up Display) bán trong suốt luôn nổi trên đỉnh màn hình trong suốt quá trình thao tác. Thay vì phụ thuộc vào việc kết nối cáp USB với máy tính để bật Android Studio Profiler, PAA đọc trực tiếp dữ liệu xung nhịp vẽ từ FrameMetrics API phần cứng và bộ nhớ PSS từ Debug.MemoryInfo, hiển thị liên tục 4 chỉ số: FPS, Jank %, RAM (MB) và CPU (%) theo nhịp 500ms kèm hệ thống đổi màu cảnh báo Xanh lá - Vàng - Đỏ."
    )
    add_body_paragraph(
        doc,
        "Ứng dụng phân bổ thành 3 phòng Lab chẩn đoán chuyên sâu, được kích hoạt thông qua các công tắc chuyển đổi BAD <-> OPTIMIZED tức thời:"
    )
    add_bullet_point(
        doc,
        ": Kiểm thử độ mượt mà khi cuộn danh sách 500 phần tử hình ảnh, đối chứng giữa layout lồng 6 tầng + decode ảnh thô trên Main Thread với ConstraintLayout phẳng 1 tầng + nạp ảnh Coil bất đồng bộ.",
        bold_prefix="Lab 1: Đồ họa & Cấu trúc View (Render Jank)"
    )
    add_bullet_point(
        doc,
        ": Kiểm thử bài toán xử lý dữ liệu trên 30.000 số nguyên, đối chứng giữa thuật toán O(N²) chạy trên Main Thread gây đơ máy 1.5 giây với thuật toán HashMap O(N) phân luồng nền qua Kotlin Coroutines (Dispatchers.Default) kèm bộ đệm Cache trả kết quả 0ms.",
        bold_prefix="Lab 2: Xử lý đa luồng & Tải tính toán CPU (ANR)"
    )
    add_bullet_point(
        doc,
        ": Kiểm thử hiện tượng rò rỉ vùng nhớ qua kịch bản tự động mở/đóng 20 Activity ngậm 5MB RAM, đối chứng giữa việc giữ biến static dính GC Root với giải pháp sử dụng WeakReference và dọn dẹp theo vòng đời onDestroy().",
        bold_prefix="Lab 3: Quản lý vòng đời & Rò rỉ vùng nhớ (Memory Leak)"
    )

    # =========================================================================
    # 1.5. PHÂN CÔNG NHIỆM VỤ THỰC HIỆN ĐỀ TÀI
    # =========================================================================
    add_heading_2(doc, "1.5. PHÂN CÔNG NHIỆM VỤ THỰC HIỆN ĐỀ TÀI")
    add_body_paragraph(
        doc,
        "Để đảm bảo tiến độ và chất lượng chuyên môn cao nhất, các thành viên trong nhóm đã được phân công trách nhiệm rõ ràng theo đúng năng lực và sở trường kỹ thuật, được tổng hợp trong Bảng 1.1:"
    )

    # Bảng phân công 1.1
    p_tbl_lbl = doc.add_paragraph()
    p_tbl_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tbl_lbl.paragraph_format.space_before = Pt(6)
    p_tbl_lbl.paragraph_format.space_after = Pt(4)
    r_tl = p_tbl_lbl.add_run("Bảng 1.1: Bảng phân công nhiệm vụ chi tiết thực hiện đề tài")
    set_font(r_tl, "Times New Roman", 11.5, bold=True, italic=True, color=C_NAVY)

    table_data = [
        ("STT", "Thành viên thực hiện", "MSSV", "Nhiệm vụ và Hạng mục đảm nhiệm chính", "Tỷ lệ đóng góp"),
        (
            "1",
            "Hoàng Thái Đăng Khoa\n(Trưởng nhóm)",
            "52400017",
            "• Nghiên cứu tổng quan bối cảnh và tiêu chuẩn Google Play Android Vitals.\n"
            "• Thiết kế phương pháp nghiên cứu và kịch bản kiểm thử đối chứng.\n"
            "• Phân tích kiến trúc giao diện, Layout Hierarchy và kỹ thuật tối ưu hóa Lab 1 (Render Jank).\n"
            "• Tổng hợp số liệu đo đạc, biên soạn báo cáo tiểu luận học thuật và thiết kế bộ Slide báo cáo.\n"
            "• Trình bày phần Mở đầu, Lab 1 và Đúc kết 5 Nguyên tắc vàng.",
            "50%"
        ),
        (
            "2",
            "Đinh Thanh Phong\n(Thành viên)",
            "52400027",
            "• Thiết kế kiến trúc mã nguồn ứng dụng PAA (Kotlin, MVVM, ViewBinding).\n"
            "• Xây dựng hạt nhân đo lường phần cứng FrameMetricsTracker, CpuSampler, MemorySampler và thanh HUD Monitor.\n"
            "• Hiện thực hóa thuật toán xử lý đa luồng Lab 2 (CPU & Coroutines) và quản lý vòng đời Lab 3 (Memory Leak & GC).\n"
            "• Thực hiện đo lường thực nghiệm trên thiết bị thật, xuất dữ liệu CSV/JSON.\n"
            "• Phụ trách phần trình bày Lab 2, Lab 3, Bảng số liệu và thực hiện Video Demo.",
            "50%"
        )
    ]

    t = doc.add_table(rows=len(table_data), cols=5)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    widths = [Inches(0.5), Inches(1.8), Inches(1.0), Inches(2.7), Inches(0.8)]

    for row_idx, row_vals in enumerate(table_data):
        for col_idx, val in enumerate(row_vals):
            cell = t.cell(row_idx, col_idx)
            cell.width = widths[col_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            
            r = p.add_run(val)
            if row_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(r, "Times New Roman", 10.5, bold=True, color=RGBColor(255, 255, 255))
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="0A4D9E"/>')
                cell._tc.get_or_add_tcPr().append(shd)
            else:
                if col_idx in [0, 2, 4]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                set_font(r, "Times New Roman", 10, bold=(col_idx == 1), color=C_SLATE)
                if row_idx % 2 == 1:
                    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
                    cell._tc.get_or_add_tcPr().append(shd)

    # =========================================================================
    # 1.6. BỐ CỤC BÁO CÁO TIỂU LUẬN
    # =========================================================================
    add_heading_2(doc, "1.6. BỐ CỤC CỦA BÁO CÁO TIỂU LUẬN")
    add_body_paragraph(
        doc,
        "Ngoài các phần mở đầu, lời cảm ơn và tóm tắt, nội dung chính của báo cáo tiểu luận được kết cấu mạch lạc thành 5 chương:"
    )
    add_bullet_point(
        doc,
        ": Giới thiệu bối cảnh phân mảnh, tính cấp thiết của hiệu năng, tiêu chuẩn Google Play Vitals, mục tiêu, phương pháp đối chứng, phân công nhiệm vụ và bố cục tài liệu.",
        bold_prefix="Chương I: Tổng quan đề tài và Đặt vấn đề"
    )
    add_bullet_point(
        doc,
        ": Trình bày kiến trúc tầng thấp của hệ điều hành AOSP, chu kỳ VSYNC 16.67ms, mô hình Looper/Handler đơn luồng, cơ chế quản lý bộ nhớ ART Heap và quy chuẩn kỹ thuật Google Vitals.",
        bold_prefix="Chương II: Cơ sở lý thuyết tầng sâu AOSP và Tiêu chuẩn Google Play Vitals"
    )
    add_bullet_point(
        doc,
        ": Trình bày chi tiết kiến trúc Model-View-ViewModel của ứng dụng PAA, thiết kế hệ thống giám sát HUD Monitor, phân tích nguyên nhân lỗi và giải pháp kỹ thuật của 3 phòng Lab thực nghiệm.",
        bold_prefix="Chương III: Phân tích kiến trúc và Xây dựng ứng dụng thực nghiệm PAA"
    )
    add_bullet_point(
        doc,
        ": Trình bày quy trình đo lường chuẩn hóa, công bố bảng tổng hợp số liệu đối chứng Before vs After, biểu đồ kiểm chuẩn phần cứng và phân tích chuyên sâu các kết quả thu được.",
        bold_prefix="Chương IV: Kết quả thực nghiệm và Đánh giá đối chứng định lượng"
    )
    add_bullet_point(
        doc,
        ": Tổng kết những đóng góp chính của đề tài, đúc kết 5 nguyên tắc vàng chuẩn công nghiệp cho lập trình viên Android và đề xuất các định hướng mở rộng nghiên cứu trong tương lai.",
        bold_prefix="Chương V: Kết luận, 5 Nguyên tắc vàng và Hướng phát triển"
    )

    out_file = os.path.join(OUT_DIR, "04_Chuong_I_Tong_Quan_De_Tai.docx")
    doc.save(out_file)
    print("Created successfully:", out_file)

if __name__ == "__main__":
    build_chapter_1()
