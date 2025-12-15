# 🚀 Hướng dẫn cài đặt GPU (CUDA 12.4) cho Demo

## 📋 Tổng quan

Demo thực tế có thể chạy trên **GPU** hoặc **CPU**:
- 🔥 **GPU (CUDA)**: Nhanh hơn **10-50x**, khuyến nghị cho huấn luyện
- 💻 **CPU**: Chậm hơn nhưng không cần GPU

---

## ✅ Yêu cầu hệ thống

### Để sử dụng GPU:
- ✅ GPU NVIDIA (GTX/RTX series)
- ✅ NVIDIA Driver mới nhất
- ✅ CUDA 12.4 compatible
- ✅ Tối thiểu 4GB VRAM

### Chỉ dùng CPU:
- ✅ Python 3.8+
- ✅ RAM 4GB+

---

## 🎯 Cài đặt nhanh

### Option 1: Script tự động (Khuyến nghị)

#### Windows:
```bash
# Chạy script cài đặt
install_pytorch_gpu.bat
```

#### Linux/Mac:
```bash
# Cho phép thực thi
chmod +x install_pytorch_gpu.sh

# Chạy script
./install_pytorch_gpu.sh
```

---

### Option 2: Cài đặt thủ công

#### Bước 1: Gỡ PyTorch cũ (nếu có)
```bash
pip uninstall torch torchvision torchaudio
```

#### Bước 2: Cài PyTorch với CUDA 12.4
```bash
# GPU version (CUDA 12.4)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# Hoặc CPU version (nếu không có GPU)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### Bước 3: Cài dependencies khác
```bash
pip install numpy matplotlib scikit-learn
```

---

## 🔍 Kiểm tra GPU

### Chạy script kiểm tra:
```bash
python check_gpu.py
```

### Output mong đợi (nếu có GPU):
```
======================================================================
KIỂM TRA GPU VÀ CUDA
======================================================================

[✓] PyTorch đã được cài đặt
[+] PyTorch version: 2.x.x

[✓] GPU (CUDA) KHẢ DỤNG!
[+] CUDA version: 12.4
[+] cuDNN version: 90101

[📊] Thông tin GPU:

  GPU 0: NVIDIA GeForce RTX 3060
    ├─ Memory: 12.00 GB
    ├─ Compute Capability: 8.6
    └─ Multi Processors: 28

[🔧] Test GPU performance...
[+] Matrix multiplication (1000x1000): 2.45ms
[✓] GPU hoạt động tốt!

======================================================================
✅ SYSTEM READY - Có thể sử dụng GPU!
======================================================================
```

### Output nếu KHÔNG có GPU:
```
[!] GPU KHÔNG KHẢ DỤNG
[!] PyTorch đang chạy trên CPU

[🔍] Nguyên nhân có thể:
  1. PyTorch được cài với CPU version
  2. Driver NVIDIA chưa cài hoặc quá cũ
  3. CUDA toolkit chưa cài đặt
  4. Máy không có GPU NVIDIA

[💡] Cách khắc phục:
  ...
```

---

## 🐛 Troubleshooting

### 1. "NVIDIA driver not found"

**Nguyên nhân:** Driver NVIDIA chưa cài hoặc quá cũ.

**Giải pháp:**
1. Tải driver mới nhất: https://www.nvidia.com/Download/index.aspx
2. Cài đặt và khởi động lại máy
3. Kiểm tra: `nvidia-smi`

---

### 2. "CUDA out of memory"

**Nguyên nhân:** GPU không đủ VRAM.

**Giải pháp:**
```python
# Trong train_mnist_model.py, giảm batch_size
model, accuracy = train_model(batch_size=32)  # Thay vì 128
```

---

### 3. "torch.cuda.is_available() returns False"

**Nguyên nhân:** PyTorch được cài CPU version.

**Giải pháp:**
```bash
# Gỡ và cài lại GPU version
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

### 4. "ImportError: DLL load failed"

**Nguyên nhân:** Thiếu Visual C++ Redistributable (Windows).

**Giải pháp:**
1. Tải: https://aka.ms/vs/17/release/vc_redist.x64.exe
2. Cài đặt và khởi động lại

---

### 5. GPU không được sử dụng trong demo

**Kiểm tra:**
```python
python -c "import torch; print(torch.cuda.is_available())"
```

Nếu `False`:
- Xem lại bước cài đặt
- Chạy `python check_gpu.py` để chẩn đoán

---

## ⚡ So sánh Performance

| Task | CPU (i7) | GPU (RTX 3060) | Speedup |
|------|----------|----------------|---------|
| Huấn luyện 1 epoch | ~120s | ~8s | **15x** |
| FGSM Attack (500 samples) | ~45s | ~3s | **15x** |
| Tổng Demo 1 | ~8-10 phút | ~30 giây | **16-20x** |

**Kết luận:** GPU nhanh hơn **10-20x** so với CPU!

---

## 📊 Benchmark chi tiết

### Test: Matrix multiplication (1000x1000)

```python
import torch
import time

# CPU
x = torch.randn(1000, 1000)
start = time.time()
z = torch.matmul(x, x)
print(f"CPU: {(time.time() - start)*1000:.2f}ms")

# GPU
x = torch.randn(1000, 1000).cuda()
start = time.time()
z = torch.matmul(x, x)
torch.cuda.synchronize()
print(f"GPU: {(time.time() - start)*1000:.2f}ms")
```

**Kết quả mẫu:**
- CPU: ~45ms
- GPU: ~2ms
- **Speedup: 22x**

---

## 🎯 Sử dụng GPU trong Demo

Sau khi cài đặt GPU, các demo sẽ **TỰ ĐỘNG** sử dụng GPU:

```bash
# Huấn luyện với GPU
python train_mnist_model.py

# Demo tấn công với GPU
python demo_evasion_attack.py
```

**Log mẫu:**
```
[*] Thiết bị: GPU (CUDA)
[+] GPU: NVIDIA GeForce RTX 3060
[+] CUDA Version: 12.4
[+] GPU Memory: 12.00 GB
```

Nếu GPU không có, sẽ tự động chuyển CPU:
```
[*] Thiết bị: CPU
[!] GPU không khả dụng, đang sử dụng CPU (chậm hơn)
[💡] Để sử dụng GPU, cài PyTorch với CUDA:
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

## 📚 Tài liệu tham khảo

- **PyTorch installation:** https://pytorch.org/get-started/locally/
- **NVIDIA drivers:** https://www.nvidia.com/Download/index.aspx
- **CUDA toolkit:** https://developer.nvidia.com/cuda-downloads
- **cuDNN:** https://developer.nvidia.com/cudnn

---

## ❓ FAQ

### Q: Máy tôi có GPU AMD, có dùng được không?

**A:** Không. PyTorch với CUDA chỉ hỗ trợ GPU NVIDIA. GPU AMD cần ROCm (phức tạp hơn). Khuyến nghị dùng CPU.

---

### Q: Tôi có nhiều GPU, làm sao chọn GPU cụ thể?

**A:** Thêm vào đầu script:
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # Dùng GPU 0
```

---

### Q: GPU memory không đủ, làm sao?

**A:** Giảm batch size:
```python
# Trong train_mnist_model.py
model, accuracy = train_model(batch_size=32)  # Hoặc 16
```

---

### Q: Có cần cài CUDA Toolkit riêng không?

**A:** **KHÔNG CẦN!** PyTorch đã đi kèm CUDA. Chỉ cần:
1. NVIDIA Driver mới nhất
2. Cài PyTorch với CUDA: `pip install torch --index-url ...cu124`

---

### Q: Làm sao biết có đang dùng GPU?

**A:** Xem log khi chạy:
```
[*] Thiết bị: GPU (CUDA)  ← Đang dùng GPU
[*] Thiết bị: CPU         ← Đang dùng CPU
```

Hoặc check thủ công:
```bash
python check_gpu.py
```

---

## 🎊 Tổng kết

✅ **Đã cài GPU:** Chạy demo sẽ nhanh hơn 10-20x  
❌ **Không có GPU:** Demo vẫn chạy được trên CPU (chậm hơn)

**Next steps:**
```bash
# 1. Kiểm tra GPU
python check_gpu.py

# 2. Chạy demo
python train_mnist_model.py
python demo_evasion_attack.py

# 3. Xem kết quả
dir results\*.png
```

---

**Happy GPU Computing! 🚀**

