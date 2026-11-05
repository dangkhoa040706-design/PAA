# BẢNG MÀU CHÍNH THỨC DỰ ÁN PAA (Performance Analysis App)

> **Căn cứ:** Khớp 100% với file thiết kế `palette.png` và file cấu hình gốc `colors.xml`.  
> **Brand Identity:** Deep Scarlet (`#BC0024`) + Pearl White (`#F0EAD6`).

---

## 1. THƯƠNG HIỆU & NỀN TẢNG (BRAND & BASE)

| Tên Resource | Mã HEX | Ghi chú & Ứng dụng |
|---|---|---|
| `paa_scarlet` | `#BC0024` | Màu chủ đạo (Brand Primary, Deep Scarlet) |
| `paa_scarlet_dark` | `#8A001A` | Status bar, trạng thái nhấn (pressed) |
| `paa_scarlet_container`| `#F6D5DB` | Nền đỏ nhạt (Soft red background) |
| `paa_pearl` | `#F0EAD6` | Màu ngọc trai (Pearl White) |

---

## 2. BỀ MẶT & CẤU TRÚC (SURFACES - LIGHT THEME)

| Tên Resource | Mã HEX | Ứng dụng giao diện |
|---|---|---|
| `paa_background` | `#F0EAD6` | Nền màn hình chính |
| `paa_surface` | `#FBF8EE` | Thẻ Card, BottomSheet, Dialog |
| `paa_surface_variant` | `#E6DEC5` | Chip lọc, Header bảng biểu |
| `paa_outline` | `#CFC5A6` | Đường viền (Border), đường phân cách (Divider) |

---

## 3. VĂN BẢN (TEXT & TYPOGRAPHY)

| Tên Resource | Mã HEX | Ứng dụng |
|---|---|---|
| `paa_ink` | `#2A1A1D` | Chữ chính (Main text), nút bấm chính (Primary button) |
| `paa_ink_secondary` | `#6B5A5D` | Chữ phụ, mô tả phụ, nhãn thứ cấp |
| `paa_on_scarlet` | `#F0EAD6` | Chữ nổi bật trên nền Scarlet |

---

## 4. NGỮ NGHĨA BIẾN THỂ ĐO LƯỜNG (SEMANTIC VARIANTS)

| Tên Resource | Mã HEX | Ứng dụng |
|---|---|---|
| `paa_bad` | `#BC0024` | Nhãn cảnh báo phiên bản **BAD** |
| `paa_bad_container` | `#F6D5DB` | Nền tag phiên bản BAD |
| `paa_opt` | `#1A7034` | Nhãn xác nhận phiên bản **OPTIMIZED** |
| `paa_opt_container` | `#D5E8D4` | Nền tag phiên bản OPTIMIZED |
| `paa_warning` | `#9A5B00` | Cảnh báo ngưỡng dao động / chú ý |
| `paa_warning_container`| `#F6E2B8` | Nền cảnh báo |

---

## 5. BIỂU ĐỒ & BẢNG SO SÁNH (CHARTS & COMPARE)

| Tên Resource | Mã HEX | Ứng dụng |
|---|---|---|
| `paa_chart_bad` | `#BC0024` | Cột/đường biểu diễn số liệu BAD |
| `paa_chart_opt` | `#1A7034` | Cột/đường biểu diễn số liệu OPTIMIZED |
| `paa_chart_neutral` | `#8C7F6B` | Đường trục (axis), đường lưới (gridline), mốc baseline |

---

## 6. METRICS OVERLAY (LUÔN DÙNG TONE TỐI ĐỂ RÕ KHI QUAY VIDEO)

| Tên Resource | Mã HEX | Ứng dụng |
|---|---|---|
| `paa_overlay_bg` | `#CC2A1A1D` | Nền lớp phủ (Ink độ mờ 80%) |
| `paa_overlay_text` | `#F0EAD6` | Màu chữ số liệu mặc định |
| `paa_overlay_good` | `#5FD08A` | Chỉ số FPS cao / Jank thấp (Mượt) |
| `paa_overlay_warn` | `#FFC24D` | Chỉ số tiệm cận ngưỡng (Cảnh báo) |
| `paa_overlay_bad` | `#FF6A82` | Chỉ số giật lag / quá tải (Nghiêm trọng) |

---

## 7. CHẾ ĐỘ TỐI (DARK THEME - `values-night/colors.xml`)

Đã cấu hình đồng bộ trong thư mục `PAA/app/src/main/res/values-night/colors.xml`:
* `paa_background`: `#1C1416`
* `paa_surface`: `#2A1F22`
* `paa_surface_variant`: `#3A2C30`
* `paa_outline`: `#54444A`
* `paa_ink`: `#F0EAD6`
* `paa_ink_secondary`: `#BDB09B`
* `paa_scarlet`: `#FF6A82`
* `paa_on_scarlet`: `#1C1416`
* `paa_bad`: `#FF6A82` | `paa_bad_container`: `#4A1620`
* `paa_opt`: `#5FD08A` | `paa_opt_container`: `#163A24`
* `paa_warning`: `#FFC24D` | `paa_warning_container`: `#4A3510`
