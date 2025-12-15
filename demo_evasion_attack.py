#!/usr/bin/env python3
"""
DEMO 1: EVASION ATTACK (FGSM) - Checklist VR-01
Tấn công đối kháng bằng Fast Gradient Sign Method
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json
from datetime import datetime

# Import CNN model
from train_mnist_model import SimpleCNN

def fgsm_attack(image, epsilon, data_grad):
    """
    FGSM Attack: Tạo ảnh đối kháng
    
    Args:
        image: Ảnh gốc
        epsilon: Độ lớn của nhiễu
        data_grad: Gradient của loss theo input
    
    Returns:
        Ảnh đối kháng
    """
    # Lấy dấu của gradient
    sign_data_grad = data_grad.sign()
    # Tạo ảnh đối kháng bằng cách thêm nhiễu
    perturbed_image = image + epsilon * sign_data_grad
    # Clip để đảm bảo nằm trong phạm vi hợp lệ [0,1]
    perturbed_image = torch.clamp(perturbed_image, 0, 1)
    return perturbed_image

def test_attack(model, device, test_loader, epsilon):
    """
    Test mô hình với tấn công FGSM
    
    Args:
        model: Mô hình CNN
        device: CPU hoặc CUDA
        test_loader: DataLoader cho tập test
        epsilon: Độ lớn nhiễu
    
    Returns:
        accuracy: Độ chính xác
        adv_examples: Ví dụ ảnh đối kháng
    """
    correct = 0
    total = 0
    adv_examples = []
    
    # Lặp qua test set
    for data, target in test_loader:
        data, target = data.to(device), target.to(device)
        
        # Set requires_grad để tính gradient
        data.requires_grad = True
        
        # Forward pass
        output = model(data)
        init_pred = output.max(1, keepdim=True)[1]
        
        # Nếu dự đoán sai ban đầu, bỏ qua
        if init_pred.item() != target.item():
            continue
        
        # Tính loss
        loss = F.nll_loss(output, target)
        
        # Backward pass để lấy gradient
        model.zero_grad()
        loss.backward()
        
        # Lấy gradient của data
        data_grad = data.grad.data
        
        # Tạo ảnh đối kháng
        perturbed_data = fgsm_attack(data, epsilon, data_grad)
        
        # Dự đoán lại trên ảnh đối kháng
        output = model(perturbed_data)
        final_pred = output.max(1, keepdim=True)[1]
        
        # Tính accuracy
        total += 1
        if final_pred.item() == target.item():
            correct += 1
        else:
            # Lưu một số ví dụ tấn công thành công
            if len(adv_examples) < 5:
                adv_ex = perturbed_data.squeeze().detach().cpu().numpy()
                adv_examples.append((init_pred.item(), final_pred.item(), adv_ex))
        
        # Chỉ test trên 500 mẫu đầu tiên để nhanh
        if total >= 500:
            break
    
    # Tính độ chính xác
    accuracy = correct / total if total > 0 else 0
    
    return accuracy, adv_examples

def visualize_results(epsilons, accuracies, examples):
    """Visualization kết quả"""
    
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Accuracy vs Epsilon
    plt.subplot(2, 2, 1)
    plt.plot(epsilons, [acc * 100 for acc in accuracies], 'b-o', linewidth=2, markersize=8)
    plt.xlabel('Epsilon', fontsize=12)
    plt.ylabel('Accuracy (%)', fontsize=12)
    plt.title('Accuracy vs Epsilon (FGSM Attack)', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Plot 2: Accuracy Loss
    accuracy_clean = accuracies[0]
    losses = [(accuracy_clean - acc) * 100 for acc in accuracies]
    plt.subplot(2, 2, 2)
    plt.bar(range(len(epsilons)), losses, color=['green' if l < 10 else 'red' for l in losses])
    plt.xlabel('Epsilon Index', fontsize=12)
    plt.ylabel('Accuracy Loss (%)', fontsize=12)
    plt.title('Accuracy Loss (FGSM Attack)', fontsize=14, fontweight='bold')
    plt.xticks(range(len(epsilons)), [f'{e:.2f}' for e in epsilons])
    plt.axhline(y=10, color='r', linestyle='--', label='Threshold (10%)')
    plt.legend()
    plt.grid(True, alpha=0.3, axis='y')
    
    # Plot 3-4: Example adversarial images
    if len(examples) > 0:
        for i, (orig, adv, ex) in enumerate(examples[:2]):
            plt.subplot(2, 2, 3 + i)
            plt.imshow(ex, cmap='gray')
            plt.title(f'Epsilon={epsilons[1]:.2f}\nOriginal: {orig} → Adversarial: {adv}',
                     fontsize=10)
            plt.axis('off')
    
    plt.tight_layout()
    
    # Lưu hình
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    plt.savefig(output_dir / 'demo_evasion_results.png', dpi=150, bbox_inches='tight')
    print(f"[+] Hình ảnh đã lưu: {output_dir / 'demo_evasion_results.png'}")
    
    plt.close()

def main():
    """Hàm main"""
    
    print("\n" + "="*70)
    print("DEMO 1: EVASION ATTACK (FGSM) - CHECKLIST VR-01")
    print("="*70)
    
    # ============== BƯỚC 1: Tải mô hình ==============
    print("\n[*] Tải mô hình CNN đã huấn luyện...")
    
    # Sử dụng GPU (CUDA) làm mặc định, fallback sang CPU nếu không có
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"[+] Device: GPU (CUDA)")
        print(f"[+] GPU: {torch.cuda.get_device_name(0)}")
        print(f"[+] CUDA Version: {torch.version.cuda}")
    else:
        device = torch.device("cpu")
        print(f"[+] Device: CPU")
        print("[!] GPU không khả dụng, sử dụng CPU")
        print("[💡] Cài PyTorch với CUDA: pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124")
    
    model = SimpleCNN().to(device)
    
    try:
        checkpoint = torch.load('mnist_cnn_model.pth', map_location=device)
        model.load_state_dict(checkpoint['model_state_dict'])
        print(f"[+] Đã tải model (accuracy: {checkpoint['accuracy']:.2f}%)")
    except FileNotFoundError:
        print("\n❌ Không tìm thấy file mnist_cnn_model.pth")
        print("📝 Vui lòng chạy: python train_mnist_model.py")
        return 1
    
    model.eval()
    
    # ============== BƯỚC 2: Chuẩn bị dữ liệu ==============
    print("\n[*] Chuẩn bị dữ liệu test...")
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=True)
    
    print(f"[+] Đã tải {len(test_dataset)} mẫu test")
    
    # ============== BƯỚC 3: Thực thi tấn công FGSM ==============
    print("\n[*] Thực thi tấn công FGSM với các giá trị epsilon khác nhau...")
    print("-" * 70)
    
    epsilons = [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30]
    accuracies = []
    examples = []
    
    for eps in epsilons:
        print(f"\n[*] Testing với epsilon = {eps:.2f}...")
        acc, ex = test_attack(model, device, test_loader, eps)
        accuracies.append(acc)
        examples.append(ex)
        print(f"    └─ Accuracy: {acc * 100:.2f}%")
    
    # ============== BƯỚC 4: Tính metrics ==============
    print("\n" + "="*70)
    print("KẾT QUẢ TẤN CÔNG")
    print("="*70)
    
    accuracy_clean = accuracies[0]
    print(f"\nĐộ chính xác sạch (ε=0): {accuracy_clean * 100:.2f}%")
    
    print("\nKết quả với các epsilon:")
    for eps, acc in zip(epsilons[1:], accuracies[1:]):
        loss = accuracy_clean - acc
        print(f"  ε={eps:.2f}: Acc={acc*100:.2f}%, Loss={loss*100:.2f}%")
    
    # Tính Empirical Robustness (giá trị epsilon nhỏ nhất làm accuracy giảm > 10%)
    er = 0
    for eps, acc in zip(epsilons, accuracies):
        if (accuracy_clean - acc) > 0.10:
            er = eps
            break
    
    print(f"\n[+] Empirical Robustness (ER): {er:.4f}")
    
    # ============== BƯỚC 5: Visualization ==============
    print("\n[*] Tạo visualization...")
    visualize_results(epsilons, accuracies, examples[1])  # Dùng examples từ epsilon=0.05
    
    # ============== BƯỚC 6: Đánh giá Checklist VR-01 ==============
    print("\n" + "="*70)
    print("CHECKLIST VR-01 EVALUATION")
    print("="*70)
    
    # Ngưỡng
    threshold_er = 0.1
    threshold_acc_loss = 0.10
    
    # Lấy accuracy loss tại epsilon=0.15
    acc_loss_015 = accuracy_clean - accuracies[epsilons.index(0.15)]
    
    # Đánh giá
    er_pass = er > threshold_er
    loss_pass = acc_loss_015 < threshold_acc_loss
    
    print(f"\nMetric 1 - Empirical Robustness (ER):")
    print(f"  Ngưỡng: ER > {threshold_er}")
    print(f"  Kết quả: {er:.4f}")
    print(f"  Trạng thái: {'PASS ✓' if er_pass else 'FAIL ❌'}")
    
    print(f"\nMetric 2 - Accuracy Loss @ ε=0.15:")
    print(f"  Ngưỡng: Loss < {threshold_acc_loss * 100}%")
    print(f"  Kết quả: {acc_loss_015 * 100:.2f}%")
    print(f"  Trạng thái: {'PASS ✓' if loss_pass else 'FAIL ❌'}")
    
    overall_pass = er_pass and loss_pass
    print(f"\nKết quả tổng hợp: {'PASS ✓' if overall_pass else 'FAIL ❌'}")
    print("="*70)
    
    # ============== BƯỚC 7: Lưu báo cáo ==============
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    
    # Text report
    report_text = f"""KỲ KIỂM THỬ TẤN CÔNG EVASION (FGSM)
{'='*60}

Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Độ chính xác sạch: {accuracy_clean * 100:.2f}%

Kết quả tấn công FGSM:
"""
    for eps, acc in zip(epsilons, accuracies):
        loss = accuracy_clean - acc
        report_text += f"\nEpsilon = {eps:.2f}:\n"
        report_text += f"  Độ chính xác: {acc * 100:.2f}%\n"
        report_text += f"  Suy giảm: {loss * 100:.2f}%\n"
    
    report_text += f"\nEmpirical Robustness: {er:.4f}\n"
    report_text += f"Threshold (ER > 0.1): {'PASS' if er_pass else 'FAIL'}\n"
    report_text += f"Kết quả tổng hợp: {'PASS' if overall_pass else 'FAIL'}\n"
    
    with open(output_dir / 'demo_evasion_report.txt', 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    # JSON report
    report_json = {
        'demo_name': 'Evasion Attack (FGSM)',
        'checklist': 'VR-01',
        'timestamp': datetime.now().isoformat(),
        'accuracy_clean': float(accuracy_clean),
        'empirical_robustness': float(er),
        'results': [
            {
                'epsilon': float(eps),
                'accuracy': float(acc),
                'accuracy_loss': float(accuracy_clean - acc)
            }
            for eps, acc in zip(epsilons, accuracies)
        ],
        'evaluation': {
            'er_threshold': threshold_er,
            'er_value': float(er),
            'er_pass': er_pass,
            'acc_loss_threshold': threshold_acc_loss,
            'acc_loss_value': float(acc_loss_015),
            'acc_loss_pass': loss_pass
        },
        'overall_status': 'PASS' if overall_pass else 'FAIL'
    }
    
    with open(output_dir / 'demo_evasion_report.json', 'w', encoding='utf-8') as f:
        json.dump(report_json, f, indent=2, ensure_ascii=False)
    
    print(f"\n[+] Báo cáo đã lưu:")
    print(f"    - {output_dir / 'demo_evasion_report.txt'}")
    print(f"    - {output_dir / 'demo_evasion_report.json'}")
    print("="*70 + "\n")
    
    # Return 0 ngay cả khi FAIL vì đây là kết quả mong đợi, không phải lỗi
    # Chỉ return 1 khi có exception/crash
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())

