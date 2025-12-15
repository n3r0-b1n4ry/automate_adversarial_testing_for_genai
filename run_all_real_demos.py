#!/usr/bin/env python3
"""
Script chính để chạy tất cả các demo THỰC TẾ của Chương 4
"""

import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path

def print_header(text):
    """In header đẹp"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80 + "\n")

def run_script(script_name, description, optional=False):
    """
    Chạy một script Python
    
    Args:
        script_name: Tên file script
        description: Mô tả script
        optional: Có thể bỏ qua nếu lỗi
    
    Returns:
        True nếu thành công, False nếu thất bại
    """
    print(f"[🚀] {description}")
    print(f"[📄] Script: {script_name}")
    print("-" * 80)
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print(f"\n[✓] {description} - HOÀN THÀNH")
            return True
        else:
            print(f"\n[✗] {description} - LỖI (Exit code: {result.returncode})")
            if not optional:
                print("[!] Script này bắt buộc phải chạy thành công")
                return False
            else:
                print("[!] Script này là tùy chọn, tiếp tục...")
                return True
                
    except FileNotFoundError:
        print(f"\n[✗] Không tìm thấy file: {script_name}")
        return False
    except KeyboardInterrupt:
        print(f"\n[!] Đã dừng bởi người dùng")
        return False
    except Exception as e:
        print(f"\n[✗] Lỗi: {e}")
        return False

def check_dependencies():
    """Kiểm tra dependencies"""
    print_header("KIỂM TRA DEPENDENCIES")
    
    required = ['torch', 'torchvision', 'sklearn', 'numpy', 'matplotlib']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"[✓] {package:20s} - OK")
        except ImportError:
            print(f"[✗] {package:20s} - MISSING")
            missing.append(package)
    
    if missing:
        print(f"\n[!] Thiếu {len(missing)} package(s):")
        for pkg in missing:
            print(f"    - {pkg}")
        print("\n[📝] Để cài đặt:")
        print("    pip install -r requirements.txt")
        return False
    
    print("\n[✓] Tất cả dependencies đã được cài đặt!")
    return True

def main():
    """Hàm main"""
    
    print_header("CHƯƠNG 4: XÂY DỰNG KỊCH BẢN DEMO THỰC TẾ TRÊN HỆ THỐNG AI")
    print(f"[📅] Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[📁] Thư mục làm việc: {Path.cwd()}")
    
    # Kiểm tra dependencies
    if not check_dependencies():
        print("\n[❌] Vui lòng cài đặt dependencies trước!")
        return 1
    
    # Danh sách các demo
    demos = [
        {
            'script': 'train_mnist_model.py',
            'description': 'Huấn luyện CNN trên MNIST',
            'phase': 'PHASE 1: XÂY DỰNG MÔ HÌNH',
            'optional': False
        },
        {
            'script': 'demo_evasion_attack.py',
            'description': 'Demo 1 - FGSM Evasion Attack (Checklist VR-01)',
            'phase': 'PHASE 2: KIỂM THỬ EVASION ATTACK',
            'optional': False
        },
        {
            'script': 'demo_data_poisoning_attack.py',
            'description': 'Demo 2 - Data Poisoning Attack (Checklist SR-03)',
            'phase': 'PHASE 3: KIỂM THỬ DATA POISONING',
            'optional': False
        },
        {
            'script': 'demo_prompt_injection_attack.py',
            'description': 'Demo 3 - Prompt Injection Attack (Checklists SR-01/SR-02/PE-01)',
            'phase': 'PHASE 4: KIỂM THỬ PROMPT INJECTION',
            'optional': False
        }
    ]
    
    # Chạy từng demo
    results = {}
    current_phase = None
    
    for demo in demos:
        # In phase header nếu khác phase trước
        if demo['phase'] != current_phase:
            print_header(demo['phase'])
            current_phase = demo['phase']
        
        # Chạy script
        success = run_script(demo['script'], demo['description'], demo['optional'])
        results[demo['script']] = success
        
        if not success and not demo['optional']:
            print(f"\n[❌] Demo bắt buộc thất bại, dừng thực thi!")
            break
    
    # Tổng kết
    print_header("TÓM TẮT KẾT QUẢ THỰC NGHIỆM")
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    
    print(f"Tổng số demo: {total}")
    print(f"  ├─ Hoàn thành: {passed} ✓")
    print(f"  └─ Lỗi:        {failed} ✗")
    
    print("\nChi tiết thực thi:")
    for script, success in results.items():
        status = "✓ OK" if success else "✗ ERROR"
        print(f"  [{status}] {script}")
    
    print("\n💡 Lưu ý:")
    print("  - 'OK' = Demo chạy thành công (không crash)")
    print("  - 'ERROR' = Demo bị lỗi/crash")
    print("  - Kết quả PASS/FAIL checklist xem trong báo cáo JSON")
    
    # Kiểm tra artifacts
    results_dir = Path('results')
    if results_dir.exists():
        files = list(results_dir.glob('*'))
        print(f"\n[📊] Đã tạo {len(files)} file(s) trong thư mục results/:")
        for f in sorted(files):
            print(f"    - {f.name}")
    
    print(f"\n[📅] Thời gian kết thúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Kết luận
    if all(results.values()):
        print("\n[✅] Tất cả các demo đã chạy thành công!")
        print("\n[📝] Xem kết quả checklist:")
        print("    - results/demo_evasion_report.json")
        print("    - results/demo_poisoning_report.json")
        print("    - results/demo_injection_report.json")
        print("\n[📊] Xem visualization:")
        print("    - results/demo_evasion_results.png")
        print("    - results/demo_poisoning_results.png")
        return 0
    else:
        print("\n[❌] Một số demo gặp lỗi/crash. Vui lòng kiểm tra log ở trên.")
        print("[!] Lưu ý: FAIL checklist là kết quả mong đợi, không phải lỗi!")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n[!] Đã dừng bởi người dùng")
        sys.exit(1)
    except Exception as e:
        print(f"\n[❌] Lỗi không mong đợi: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

