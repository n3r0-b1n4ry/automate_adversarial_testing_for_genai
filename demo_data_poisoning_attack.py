#!/usr/bin/env python3
"""
DEMO 2: DATA POISONING ATTACK - Checklist SR-03
Tấn công đầu độc dữ liệu huấn luyện trên SVM
"""

import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from pathlib import Path
import json
from datetime import datetime

def train_clean_svm(X_train, y_train, X_test, y_test):
    """
    Huấn luyện SVM trên dữ liệu sạch
    
    Returns:
        model: SVM đã huấn luyện
        accuracy: Độ chính xác
    """
    print("[*] Huấn luyện SVM trên dữ liệu sạch...")
    svm = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
    svm.fit(X_train, y_train)
    
    y_pred = svm.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"[+] Độ chính xác trên dữ liệu sạch: {accuracy * 100:.2f}%")
    
    return svm, accuracy

def create_poisoned_data(X_train, y_train, n_poison=15):
    """
    Tạo dữ liệu độc
    
    Args:
        X_train: Dữ liệu huấn luyện
        y_train: Nhãn huấn luyện
        n_poison: Số lượng mẫu độc
    
    Returns:
        X_poisoned: Dữ liệu đã thêm độc
        y_poisoned: Nhãn đã thêm độc
    """
    # Lấy các mẫu lớp 1 (chữ số 9)
    poison_indices = np.where(y_train == 1)[0][:n_poison]
    
    # Tạo mẫu độc: lấy ảnh lớp 1 nhưng gán nhãn 0
    X_poison = X_train[poison_indices].copy()
    y_poison = np.zeros(n_poison)  # Gán nhãn sai
    
    # Thêm vào tập huấn luyện
    X_poisoned = np.vstack([X_train, X_poison])
    y_poisoned = np.hstack([y_train, y_poison])
    
    return X_poisoned, y_poisoned

def visualize_results(cm_clean, cm_poisoned, acc_clean, acc_poisoned, X_poison):
    """Visualization kết quả"""
    
    fig = plt.figure(figsize=(15, 10))
    
    # Plot 1: Confusion Matrix - Clean
    plt.subplot(2, 3, 1)
    plt.imshow(cm_clean, cmap='Blues', interpolation='nearest')
    plt.title(f'Confusion Matrix (Clean)\nAccuracy: {acc_clean*100:.2f}%', 
             fontsize=12, fontweight='bold')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.colorbar()
    for i in range(2):
        for j in range(2):
            plt.text(j, i, str(cm_clean[i, j]), 
                    ha='center', va='center', 
                    color='white' if cm_clean[i, j] > cm_clean.max() / 2 else 'black',
                    fontsize=14, fontweight='bold')
    
    # Plot 2: Confusion Matrix - Poisoned
    plt.subplot(2, 3, 2)
    plt.imshow(cm_poisoned, cmap='Reds', interpolation='nearest')
    plt.title(f'Confusion Matrix (Poisoned)\nAccuracy: {acc_poisoned*100:.2f}%', 
             fontsize=12, fontweight='bold')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.colorbar()
    for i in range(2):
        for j in range(2):
            plt.text(j, i, str(cm_poisoned[i, j]), 
                    ha='center', va='center', 
                    color='white' if cm_poisoned[i, j] > cm_poisoned.max() / 2 else 'black',
                    fontsize=14, fontweight='bold')
    
    # Plot 3: Accuracy Comparison
    plt.subplot(2, 3, 3)
    categories = ['Clean', 'Poisoned']
    accuracies = [acc_clean * 100, acc_poisoned * 100]
    colors = ['green', 'red']
    bars = plt.bar(categories, accuracies, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    plt.ylabel('Accuracy (%)', fontsize=12)
    plt.title('Accuracy Comparison', fontsize=12, fontweight='bold')
    plt.ylim([0, 105])
    plt.axhline(y=50, color='orange', linestyle='--', linewidth=2, label='Random Guess (50%)')
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    
    # Thêm giá trị lên thanh bar
    for i, (bar, v) in enumerate(zip(bars, accuracies)):
        plt.text(bar.get_x() + bar.get_width()/2, v + 2, 
                f'{v:.1f}%', ha='center', fontsize=12, fontweight='bold')
    
    # Plot 4-6: Example poison samples
    for i in range(min(3, len(X_poison))):
        plt.subplot(2, 3, 4 + i)
        plt.imshow(X_poison[i].reshape(8, 8), cmap='gray')
        plt.title(f'Poison Sample {i+1}\n(Class 9 → Labeled as 5)', fontsize=10)
        plt.axis('off')
    
    plt.tight_layout()
    
    # Lưu hình
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / 'demo_poisoning_results.png', dpi=150, bbox_inches='tight')
    print(f"[+] Hình ảnh đã lưu: {output_dir / 'demo_poisoning_results.png'}")
    
    plt.close()

def main():
    """Hàm main"""
    
    print("\n" + "="*70)
    print("DEMO 2: DATA POISONING ATTACK - CHECKLIST SR-03")
    print("="*70)
    
    # ============== BƯỚC 1: Tải và chuẩn bị dữ liệu ==============
    print("\n[*] Tải bộ dữ liệu digits (sklearn)...")
    digits = load_digits()
    X = digits.data / 16.0  # Chuẩn hóa [0, 1]
    y = digits.target
    
    # Lọc chỉ lấy 2 chữ số: 5 và 9
    mask = (y == 5) | (y == 9)
    X_binary = X[mask]
    y_binary = y[mask]
    y_binary = np.where(y_binary == 5, 0, 1)  # 5 -> 0, 9 -> 1
    
    print(f"[+] Dữ liệu nhị phân: {len(X_binary)} mẫu")
    print(f"    └─ Lớp 0 (chữ số 5): {np.sum(y_binary == 0)} mẫu")
    print(f"    └─ Lớp 1 (chữ số 9): {np.sum(y_binary == 1)} mẫu")
    
    # Chia dữ liệu
    X_train, X_test, y_train, y_test = train_test_split(
        X_binary, y_binary, test_size=0.2, random_state=42
    )
    
    print(f"\n[+] Chia dữ liệu:")
    print(f"    └─ Train: {len(X_train)} mẫu")
    print(f"    └─ Test: {len(X_test)} mẫu")
    
    # ============== BƯỚC 2: Huấn luyện trên dữ liệu SẠCH ==============
    print("\n" + "-"*70)
    svm_clean, accuracy_clean = train_clean_svm(X_train, y_train, X_test, y_test)
    
    # ============== BƯỚC 3: Tạo dữ liệu độc ==============
    print("\n" + "-"*70)
    print("[*] Tạo dữ liệu độc...")
    n_poison = 15
    X_train_poisoned, y_train_poisoned = create_poisoned_data(X_train, y_train, n_poison)
    
    poison_rate = (n_poison / len(X_train)) * 100
    print(f"[+] Số lượng mẫu độc: {n_poison}")
    print(f"[+] Tỷ lệ nhiễm bẩn: {poison_rate:.2f}%")
    print(f"[+] Loại: Mẫu lớp 9 được gán nhãn sai là 5")
    
    # ============== BƯỚC 4: Huấn luyện trên dữ liệu BỊ ĐẦU ĐỘC ==============
    print("\n" + "-"*70)
    print("[*] Huấn luyện SVM trên dữ liệu BỊ ĐẦU ĐỘC...")
    svm_poisoned = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
    svm_poisoned.fit(X_train_poisoned, y_train_poisoned)
    
    y_pred_poisoned = svm_poisoned.predict(X_test)
    accuracy_poisoned = accuracy_score(y_test, y_pred_poisoned)
    
    print(f"[+] Độ chính xác trên dữ liệu bị đầu độc: {accuracy_poisoned * 100:.2f}%")
    
    # ============== BƯỚC 5: Tính metrics ==============
    print("\n" + "="*70)
    print("KẾT QUẢ TẤN CÔNG")
    print("="*70)
    
    accuracy_drop = accuracy_clean - accuracy_poisoned
    asr = accuracy_drop  # Attack Success Rate
    
    print(f"\nĐộ chính xác sạch: {accuracy_clean * 100:.2f}%")
    print(f"Độ chính xác bị đầu độc: {accuracy_poisoned * 100:.2f}%")
    print(f"Mức suy giảm: {accuracy_drop * 100:.2f}%")
    print(f"Attack Success Rate (ASR): {asr * 100:.2f}%")
    
    # ============== BƯỚC 6: Visualization ==============
    print("\n[*] Tạo visualization...")
    
    y_pred_clean = svm_clean.predict(X_test)
    cm_clean = confusion_matrix(y_test, y_pred_clean)
    cm_poisoned = confusion_matrix(y_test, y_pred_poisoned)
    
    # Lấy một số mẫu độc để hiển thị
    poison_indices = np.where(y_train == 1)[0][:n_poison]
    X_poison_samples = X_train[poison_indices]
    
    visualize_results(cm_clean, cm_poisoned, accuracy_clean, accuracy_poisoned, X_poison_samples)
    
    # ============== BƯỚC 7: Đánh giá Checklist SR-03 ==============
    print("\n" + "="*70)
    print("CHECKLIST SR-03 EVALUATION")
    print("="*70)
    
    threshold_asr = 0.10  # ASR < 10%
    
    asr_pass = asr < threshold_asr
    
    print(f"\nMetric - Attack Success Rate (ASR):")
    print(f"  Ngưỡng: ASR < {threshold_asr * 100}%")
    print(f"  Kết quả: {asr * 100:.2f}%")
    print(f"  Trạng thái: {'PASS ✓' if asr_pass else 'FAIL ❌'}")
    
    print(f"\nMetric - Accuracy Drop:")
    print(f"  Kết quả: {accuracy_drop * 100:.2f}%")
    print(f"  Giải thích: Mô hình mất {accuracy_drop * 100:.2f}% độ chính xác sau khi bị đầu độc")
    
    overall_pass = asr_pass
    print(f"\nKết quả tổng hợp: {'PASS ✓' if overall_pass else 'FAIL ❌'}")
    print("="*70)
    
    # ============== BƯỚC 8: Lưu báo cáo ==============
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    
    # Text report
    report_text = f"""KỲ KIỂM THỬ TẤN CÔNG DATA POISONING
{'='*60}

Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Số lượng mẫu độc: {n_poison}
Tỷ lệ nhiễm bẩn: {poison_rate:.2f}%

Độ chính xác sạch: {accuracy_clean * 100:.2f}%
Độ chính xác bị đầu độc: {accuracy_poisoned * 100:.2f}%
Mức suy giảm: {accuracy_drop * 100:.2f}%
Attack Success Rate (ASR): {asr * 100:.2f}%

Ngưỡng ASR: < {threshold_asr * 100}%
Trạng thái: {'PASS' if asr_pass else 'FAIL'}
Kết quả tổng hợp: {'PASS' if overall_pass else 'FAIL'}
"""
    
    with open(output_dir / 'demo_poisoning_report.txt', 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    # JSON report
    report_json = {
        'demo_name': 'Data Poisoning Attack',
        'checklist': 'SR-03',
        'timestamp': datetime.now().isoformat(),
        'n_poison': n_poison,
        'poison_rate': float(poison_rate),
        'accuracy_clean': float(accuracy_clean),
        'accuracy_poisoned': float(accuracy_poisoned),
        'accuracy_drop': float(accuracy_drop),
        'asr': float(asr),
        'evaluation': {
            'asr_threshold': threshold_asr,
            'asr_value': float(asr),
            'asr_pass': asr_pass
        },
        'overall_status': 'PASS' if overall_pass else 'FAIL'
    }
    
    with open(output_dir / 'demo_poisoning_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_json, f, indent=2, ensure_ascii=False)
    
    print(f"\n[+] Báo cáo đã lưu:")
    print(f"    - {output_dir / 'demo_poisoning_report.txt'}")
    print(f"    - {output_dir / 'demo_poisoning_report.json'}")
    print("="*70 + "\n")
    
    # Return 0 ngay cả khi FAIL vì đây là kết quả mong đợi, không phải lỗi
    # Chỉ return 1 khi có exception/crash
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())

