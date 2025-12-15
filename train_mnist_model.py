#!/usr/bin/env python3
"""
DEMO THỰC TẾ - Huấn luyện CNN trên MNIST
Chương 4: Xây dựng kịch bản demo trên hệ thống AI giả định
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os
from pathlib import Path

# ============== BƯỚC 1: Định nghĩa CNN Architecture ==============
class SimpleCNN(nn.Module):
    """CNN đơn giản cho phân loại MNIST"""
    
    def __init__(self):
        super(SimpleCNN, self).__init__()
        # Conv Layer 1
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        
        # Conv Layer 2
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, 2)
        
        # Fully Connected Layers
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x

def train_model(num_epochs=5, batch_size=128, learning_rate=0.001):
    """
    Huấn luyện CNN trên MNIST
    
    Args:
        num_epochs: Số epoch huấn luyện
        batch_size: Kích thước batch
        learning_rate: Learning rate
    
    Returns:
        model: Mô hình đã huấn luyện
        accuracy: Độ chính xác trên tập test
    """
    
    print("\n" + "="*70)
    print("HUẤN LUYỆN MÔ HÌNH CNN TRÊN MNIST")
    print("="*70)
    
    # ============== BƯỚC 2: Tải và chuẩn bị dữ liệu ==============
    print("\n[*] Đang tải bộ dữ liệu MNIST...")
    
    # Tạo thư mục data nếu chưa có
    data_dir = Path('./data')
    data_dir.mkdir(exist_ok=True)
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    
    try:
        train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
        test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    except Exception as e:
        print(f"[!] Lỗi khi tải MNIST: {e}")
        print("[!] Vui lòng kiểm tra kết nối internet hoặc tải thủ công")
        return None, 0
    
    print(f"[+] Đã tải: {len(train_dataset)} mẫu huấn luyện, {len(test_dataset)} mẫu test")
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
    
    # ============== BƯỚC 3: Khởi tạo mô hình ==============
    # Sử dụng GPU (CUDA) làm mặc định, fallback sang CPU nếu không có
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"\n[*] Thiết bị: GPU (CUDA)")
        print(f"[+] GPU: {torch.cuda.get_device_name(0)}")
        print(f"[+] CUDA Version: {torch.version.cuda}")
        print(f"[+] GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
    else:
        device = torch.device("cpu")
        print(f"\n[*] Thiết bị: CPU")
        print("[!] GPU không khả dụng, đang sử dụng CPU (chậm hơn)")
        print("[💡] Để sử dụng GPU, cài PyTorch với CUDA:")
        print("    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124")
    
    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # In thông tin mô hình
    total_params = sum(p.numel() for p in model.parameters())
    print(f"[+] Tổng số tham số: {total_params:,}")
    
    # ============== BƯỚC 4: Huấn luyện ==============
    print(f"\n[*] Bắt đầu huấn luyện ({num_epochs} epochs)...")
    print("-" * 70)
    
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for batch_idx, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # Statistics
            total_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            # In progress
            if (batch_idx + 1) % 100 == 0:
                print(f"  Epoch [{epoch+1}/{num_epochs}], "
                      f"Batch [{batch_idx+1}/{len(train_loader)}], "
                      f"Loss: {loss.item():.4f}")
        
        # Tính metrics cho epoch
        avg_loss = total_loss / len(train_loader)
        train_acc = 100 * correct / total
        
        print(f"\nEpoch [{epoch+1}/{num_epochs}] hoàn thành:")
        print(f"  ├─ Loss: {avg_loss:.4f}")
        print(f"  └─ Train Accuracy: {train_acc:.2f}%")
        print("-" * 70)
    
    # ============== BƯỚC 5: Đánh giá trên tập test ==============
    print("\n[*] Đánh giá trên tập test...")
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    accuracy_clean = 100 * correct / total
    print(f"\n[+] Độ chính xác trên tập test (sạch): {accuracy_clean:.2f}%")
    
    # ============== BƯỚC 6: Lưu mô hình ==============
    model_path = 'mnist_cnn_model.pth'
    torch.save({
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'accuracy': accuracy_clean,
        'epoch': num_epochs
    }, model_path)
    
    print(f"[+] Mô hình đã được lưu tại: {model_path}")
    print("="*70 + "\n")
    
    return model, accuracy_clean

def main():
    """Hàm main"""
    try:
        model, accuracy = train_model(num_epochs=5)
        
        if model is not None:
            print("\n✅ Huấn luyện thành công!")
            print(f"📊 Độ chính xác: {accuracy:.2f}%")
            print(f"💾 Model saved: mnist_cnn_model.pth")
            print("\n📝 Bước tiếp theo:")
            print("   python demo_evasion_attack.py")
        else:
            print("\n❌ Huấn luyện thất bại!")
            return 1
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n[!] Đã dừng bởi người dùng")
        return 1
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())

