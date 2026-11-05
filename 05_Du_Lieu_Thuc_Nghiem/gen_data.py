#!/usr/bin/env python3
"""
Sinh dữ liệu test CỐ ĐỊNH (có seed) cho app demo hiệu năng Android.

Tạo ra:
  1) items.json     : danh sách item giả cho RecyclerView (Jank Lab)
  2) cpu_data.csv   : dãy số nguyên giả cho bài toán CPU (CPU Lab)
  3) images/*.jpg   : ảnh test độ phân giải lớn do script TỰ TẠO (không dính bản quyền)

Cách dùng:
  python gen_data.py                 # dùng tham số mặc định
  python gen_data.py --items 500 --cpu 50000 --images 30 --width 3000 --height 2000

Sau khi chạy: chép thư mục output vào app/src/main/assets/ của project Android.
Ghi nguồn trong báo cáo: "Ảnh test do nhóm tự sinh bằng script (seed cố định)".

Yêu cầu: Python 3, pip install pillow numpy
"""
import argparse
import csv
import json
import os
import random

import numpy as np
from PIL import Image, ImageDraw

SEED = 20260101  # đổi nếu muốn, nhưng phải GIỮ NGUYÊN giữa các lần đo

WORDS = [
    "Mountain", "River", "Forest", "Ocean", "Desert", "Valley", "Island",
    "Sunrise", "Sunset", "Canyon", "Glacier", "Meadow", "Harbor", "Bridge",
    "Lantern", "Compass", "Anchor", "Harvest", "Horizon", "Whisper",
]
ADJ = ["Quiet", "Golden", "Hidden", "Ancient", "Bright", "Misty", "Silent", "Wild"]


def gen_items(n, n_images, out_dir):
    rnd = random.Random(SEED)
    items = []
    for i in range(n):
        title = f"{rnd.choice(ADJ)} {rnd.choice(WORDS)} #{i + 1}"
        # mô tả dài vừa phải để việc đo/bind có ý nghĩa
        desc = " ".join(rnd.choice(WORDS).lower() for _ in range(rnd.randint(12, 24)))
        items.append({
            "id": i + 1,
            "title": title,
            "description": desc,
            "imageName": f"img_{(i % n_images) + 1:02d}.jpg",
        })
    with open(os.path.join(out_dir, "items.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    return len(items)


def gen_cpu(n, out_dir):
    # Phạm vi nhỏ hơn n để chắc chắn có phần tử trùng (phục vụ bài toán tìm trùng)
    rng = np.random.default_rng(SEED)
    data = rng.integers(0, max(10, n // 2), size=n)
    with open(os.path.join(out_dir, "cpu_data.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["index", "value"])
        for i, v in enumerate(data):
            w.writerow([i, int(v)])
    return n


def gen_images(count, width, height, out_dir, quality):
    img_dir = os.path.join(out_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    rng = np.random.default_rng(SEED)
    # Dùng ảnh nhỏ rồi phóng to + nhiễu nhẹ để có chi tiết mà file không quá nặng
    sw, sh = width // 20, height // 20
    for k in range(count):
        c1 = rng.integers(30, 255, size=3)
        c2 = rng.integers(30, 255, size=3)
        gx = np.linspace(0, 1, sw)[None, :, None]
        gy = np.linspace(0, 1, sh)[:, None, None]
        t = (gx + gy) / 2.0
        base = c1[None, None, :] * (1 - t) + c2[None, None, :] * t
        base += rng.normal(0, 18, size=(sh, sw, 3))
        base = np.clip(base, 0, 255).astype(np.uint8)
        img = Image.fromarray(base).resize((width, height), Image.BICUBIC)

        d = ImageDraw.Draw(img)
        for _ in range(12):
            x0 = int(rng.integers(0, width - 200))
            y0 = int(rng.integers(0, height - 200))
            x1 = x0 + int(rng.integers(100, width // 3))
            y1 = y0 + int(rng.integers(100, height // 3))
            color = tuple(int(x) for x in rng.integers(0, 255, size=3))
            if rng.random() < 0.5:
                d.ellipse([x0, y0, x1, y1], outline=color, width=int(rng.integers(4, 14)))
            else:
                d.rectangle([x0, y0, x1, y1], outline=color, width=int(rng.integers(4, 14)))
        d.text((40, 40), f"TEST IMAGE {k + 1:02d}  {width}x{height}", fill=(255, 255, 255))
        img.save(os.path.join(img_dir, f"img_{k + 1:02d}.jpg"), "JPEG", quality=quality)
    return count


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", default="du_lieu_test", help="thư mục xuất")
    p.add_argument("--items", type=int, default=500)
    p.add_argument("--cpu", type=int, default=50000)
    p.add_argument("--images", type=int, default=30)
    p.add_argument("--width", type=int, default=3000)
    p.add_argument("--height", type=int, default=2000)
    p.add_argument("--quality", type=int, default=85)
    p.add_argument("--no-images", action="store_true", help="bỏ qua việc tạo ảnh")
    a = p.parse_args()

    os.makedirs(a.out, exist_ok=True)
    n_items = gen_items(a.items, a.images, a.out)
    n_cpu = gen_cpu(a.cpu, a.out)
    print(f"items.json   : {n_items} item")
    print(f"cpu_data.csv : {n_cpu} dòng")
    if not a.no_images:
        n_img = gen_images(a.images, a.width, a.height, a.out, a.quality)
        print(f"images/      : {n_img} anh {a.width}x{a.height}")
    print(f"SEED = {SEED} (giữ nguyên để kết quả lặp lại được)")


if __name__ == "__main__":
    main()
