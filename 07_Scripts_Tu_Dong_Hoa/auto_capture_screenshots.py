#!/usr/bin/env python3
import subprocess
import time
import os
import sys
import xml.etree.ElementTree as ET

ADB = "/Users/dinhphong/Library/Android/sdk/platform-tools/adb"
OUT_DIR = os.path.abspath("04_Hinh_Anh_Va_So_Do")

def run_adb(cmd):
    full_cmd = f"{ADB} {cmd}"
    res = subprocess.run(full_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res.stdout.strip()

def get_node_center(resource_id):
    run_adb("shell uiautomator dump /sdcard/live_dump.xml")
    xml_str = run_adb("shell cat /sdcard/live_dump.xml 2>/dev/null")
    if not xml_str or not xml_str.startswith("<?xml"):
        # try again
        time.sleep(1)
        xml_str = run_adb("shell cat /sdcard/live_dump.xml 2>/dev/null")
    try:
        root = ET.fromstring(xml_str)
        for node in root.iter('node'):
            if resource_id in node.attrib.get('resource-id', ''):
                bounds = node.attrib.get('bounds')
                parts = bounds.replace('][', ',').replace('[', '').replace(']', '').split(',')
                x1, y1, x2, y2 = map(int, parts)
                return (x1 + x2) // 2, (y1 + y2) // 2
    except Exception as e:
        print(f"Error parsing xml: {e}")
    return None

def tap_id(resource_id, name=""):
    coords = get_node_center(resource_id)
    if coords:
        print(f"  Tap {name or resource_id}: {coords}")
        run_adb(f"shell input tap {coords[0]} {coords[1]}")
        time.sleep(1)
        return True
    else:
        print(f"  ⚠️ Could not find {resource_id}")
        return False

def tap_coords(x, y, name=""):
    print(f"  Tap {name}: ({x}, {y})")
    run_adb(f"shell input tap {x} {y}")
    time.sleep(1)

def capture(filename):
    out_path = os.path.join(OUT_DIR, filename)
    print(f"📸 Capturing: {filename}")
    subprocess.run(f"{ADB} exec-out screencap -p > '{out_path}'", shell=True)
    time.sleep(0.5)

def wait_for_idle(timeout=40):
    for i in range(timeout):
        time.sleep(1)
        run_adb("shell uiautomator dump /sdcard/wait_dump.xml")
        xml_str = run_adb("shell cat /sdcard/wait_dump.xml 2>/dev/null")
        if not xml_str:
            continue
        try:
            root = ET.fromstring(xml_str)
            for node in root.iter('node'):
                if 'btnRun' in node.attrib.get('resource-id', ''):
                    if node.attrib.get('enabled') == 'true':
                        print(f"    Done after {i+1}s")
                        return True
        except:
            pass
    print("    Timeout waiting for idle")
    return False

def main():
    print("=== BẮT ĐẦU CHẠY DEMO VÀ CHỤP LẠI TOÀN BỘ ẢNH THỰC TẾ ===")
    os.makedirs(OUT_DIR, exist_ok=True)

    # 1. Khởi động app
    print("\n1. Mở PAA MainActivity...")
    run_adb("shell am force-stop com.nhomx.paa.debug")
    time.sleep(1)
    run_adb("shell am start -n com.nhomx.paa.debug/com.nhomx.paa.MainActivity")
    time.sleep(2)

    # Chụp 01_home.png
    capture("01_home.png")

    # 2. VÀO JANK LAB
    print("\n2. Kiểm thử Jank Lab...")
    tap_id("cardJank", "Card Jank Lab")

    # Chạy đo Jank BAD (200 ảnh, 1 lượt)
    print("  Chạy đo Jank BAD...")
    tap_id("btnRun", "Nút Chạy đo (BAD)")
    wait_for_idle(30)
    capture("02_jank_bad.png")
    tap_id("btnSave", "Nút Lưu (BAD)")

    # Chuyển sang OPTIMIZED
    print("  Chuyển sang OPTIMIZED...")
    tap_id("swVariant", "Switch OPTIMIZED")
    print("  Chạy đo Jank OPTIMIZED...")
    tap_id("btnRun", "Nút Chạy đo (OPT)")
    wait_for_idle(30)
    capture("03_jank_opt.png")
    tap_id("btnSave", "Nút Lưu (OPT)")

    # Quay về Home
    tap_id("btnBack", "Nút Back")

    # 3. VÀO CPU LAB
    print("\n3. Kiểm thử CPU Lab...")
    tap_id("cardCpu", "Card CPU Lab")
    capture("04_cpu_lab.png")

    # Chạy đo CPU BAD
    print("  Chạy đo CPU BAD...")
    tap_id("btnRun", "Nút Chạy đo (BAD)")
    wait_for_idle(20)
    tap_id("btnSave", "Nút Lưu (BAD)")

    # Chuyển sang OPTIMIZED
    print("  Chuyển sang OPTIMIZED...")
    tap_id("swVariant", "Switch OPTIMIZED")
    print("  Chạy đo CPU OPTIMIZED...")
    tap_id("btnRun", "Nút Chạy đo (OPT)")
    wait_for_idle(10)
    capture("07_cpu_result_panel.png")
    tap_id("btnSave", "Nút Lưu (OPT)")

    # Quay về Home
    tap_id("btnBack", "Nút Back")

    # 4. VÀO MEMORY LAB
    print("\n4. Kiểm thử Memory Lab...")
    tap_id("cardMemory", "Card Memory Lab")

    # Chạy đo Memory BAD
    print("  Chạy đo Memory BAD (20 loops)...")
    tap_id("btnRun", "Nút Chạy đo (BAD)")
    wait_for_idle(30)
    tap_id("btnManualGc", "Nút Kích hoạt GC thủ công")
    time.sleep(1)
    tap_id("btnSave", "Nút Lưu (BAD)")

    # Chuyển sang OPTIMIZED
    print("  Chuyển sang OPTIMIZED...")
    tap_id("swVariant", "Switch OPTIMIZED")
    print("  Chạy đo Memory OPTIMIZED (20 loops)...")
    tap_id("btnRun", "Nút Chạy đo (OPT)")
    wait_for_idle(30)
    tap_id("btnManualGc", "Nút Kích hoạt GC thủ công")
    time.sleep(1)
    capture("05_memory_lab.png")
    tap_id("btnSave", "Nút Lưu (OPT)")

    # Quay về Home
    tap_id("btnBack", "Nút Back")

    # 5. VÀO MÀN HÌNH RESULTS
    print("\n5. Mở màn hình Results...")
    tap_id("btnResults", "Nút Xem Kết Quả")
    time.sleep(2)
    capture("06_results.png")

    print("\n=== HOÀN TẤT! ĐÃ LƯU TOÀN BỘ ẢNH CHỤP MỚI VÀO 04_Hinh_Anh_Va_So_Do ===")

if __name__ == "__main__":
    main()
