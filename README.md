# 🛡️ AI Security Demo - Kiểm thử An toàn Đối kháng Tự động

> **Dự án demo kiểm thử an toàn hệ thống AI theo tiêu chuẩn ISO 23894:2023**

Dự án này cung cấp các kịch bản demo thực tế cho việc kiểm thử an toàn hệ thống AI, minh họa ba loại tấn công đối kháng phổ biến: **Evasion Attack**, **Data Poisoning** và **Prompt Injection**. Mục tiêu nhằm đánh giá tính bền vững (robustness) của các mô hình AI và phát hiện các lỗ hổng tiềm ẩn.

---

## 📋 Mục lục

- [Tính năng](#-tính-năng)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
- [Hướng dẫn sử dụng](#-hướng-dẫn-sử-dụng)
- [Kịch bản tấn công](#-kịch-bản-tấn-công)
- [Kết quả và báo cáo](#-kết-quả-và-báo-cáo)
- [Tài liệu tham khảo](#-tài-liệu-tham-khảo)
- [Giấy phép](#-giấy-phép)

---

## ✨ Tính năng

- 🎯 **3 loại tấn công đối kháng**: Evasion, Data Poisoning, Prompt Injection
- 📊 **Metrics đánh giá chuẩn ISO 23894:2023**: VR-01, SR-01, SR-02, SR-03, PE-01
- 🚀 **Hỗ trợ GPU CUDA**: Tăng tốc huấn luyện và kiểm thử
- 📈 **Visualization tự động**: Biểu đồ và hình ảnh minh họa kết quả
- 📝 **Báo cáo chi tiết**: Xuất file TXT và JSON
- 🔄 **Tự động hóa 100%**: Script chạy toàn bộ quy trình

---

## 📂 Cấu trúc dự án

```
d:\code\cdcs\
├── 📄 README.md                          # Tài liệu hướng dẫn (file này)
├── 📄 config.json                        # Cấu hình dự án
├── 📄 CHANGELOG.md                       # Lịch sử thay đổi
│
├── 🔧 SCRIPTS CHÍNH
│   ├── train_mnist_model.py              # Huấn luyện mô hình CNN trên MNIST
│   ├── demo_evasion_attack.py            # Demo 1: Tấn công Evasion (FGSM)
│   ├── demo_data_poisoning_attack.py     # Demo 2: Tấn công Data Poisoning
│   ├── demo_prompt_injection_attack.py   # Demo 3: Tấn công Prompt Injection
│   ├── run_all_real_demos.py             # Chạy tự động tất cả demo
│   └── check_gpu.py                      # Kiểm tra GPU/CUDA
│
├── 📂 data/                              # Thư mục dữ liệu (MNIST - tự tải)
│
├── 📂 docs/                              # Tài liệu chi tiết
│   ├── FINAL_REPORT.md                   # Báo cáo đầy đủ
│   ├── EXECUTIVE_SUMMARY.md              # Tóm tắt điều hành
│   ├── EXPERIMENTAL_GUIDE.md             # Hướng dẫn thực nghiệm
│   ├── README_GPU_SETUP.md               # Hướng dẫn cài GPU
│   ├── README_REAL_DEMOS.md              # Hướng dẫn demo thực tế
│   └── ...
│
├── 📂 results/                           # Kết quả đầu ra
│   ├── demo_evasion_report.txt           # Báo cáo Evasion Attack
│   ├── demo_evasion_report.json          # Báo cáo JSON
│   ├── demo_evasion_results.png          # Biểu đồ kết quả
│   ├── demo_poisoning_report.txt         # Báo cáo Data Poisoning
│   ├── demo_poisoning_report.json        # Báo cáo JSON
│   ├── demo_poisoning_results.png        # Biểu đồ kết quả
│   ├── demo_injection_report.txt         # Báo cáo Prompt Injection
│   ├── demo_injection_report.json        # Báo cáo JSON
│   └── demo_injection_detailed.json      # Chi tiết responses
│
├── 📂 setup/                             # Cài đặt môi trường
│   ├── requirements.txt                  # Dependencies Python
│   ├── install_pytorch_gpu.bat           # Script cài PyTorch GPU (Windows)
│   └── install_pytorch_gpu.sh            # Script cài PyTorch GPU (Linux/Mac)
│
└── 📂 venv/                              # Môi trường ảo Python
```

---

## 💻 Yêu cầu hệ thống

### Phần mềm bắt buộc

| Thành phần | Phiên bản | Ghi chú |
|------------|-----------|---------|
| **Python** | 3.8+ | Khuyến nghị 3.10+ |
| **pip** | Mới nhất | Để cài packages |
| **Git** | Mới nhất | Để clone repo |

### Phần mềm tùy chọn (để tăng tốc)

| Thành phần | Phiên bản | Ghi chú |
|------------|-----------|---------|
| **NVIDIA GPU** | Compute Capability 5.0+ | GTX 1050 trở lên |
| **CUDA Toolkit** | 12.4 | Để sử dụng GPU |
| **cuDNN** | 8.x | Tăng tốc deep learning |

### Thư viện Python chính

- `torch` >= 2.0.0 (PyTorch)
- `torchvision` >= 0.15.0
- `scikit-learn` >= 1.0.0
- `numpy` >= 1.21.0
- `matplotlib` >= 3.4.0
- `openai` (cho demo Prompt Injection)

---

## 🚀 Cài đặt

### Bước 1: Clone dự án

```bash
git clone <repository-url>
cd cdcs
```

### Bước 2: Tạo môi trường ảo

```bash
# Tạo virtual environment
python -m venv venv

# Kích hoạt môi trường (Windows)
.\venv\Scripts\activate

# Kích hoạt môi trường (Linux/Mac)
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies

#### Tùy chọn A: Cài với GPU (CUDA 12.4) - Khuyến nghị

```bash
# Cài thư viện cơ bản
pip install numpy matplotlib scikit-learn openai

# Cài PyTorch với CUDA 12.4
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

#### Tùy chọn B: Cài CPU only (không cần GPU)

```bash
# Cài thư viện cơ bản
pip install numpy matplotlib scikit-learn openai

# Cài PyTorch CPU
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### Tùy chọn C: Cài tất cả từ requirements.txt

```bash
pip install -r setup/requirements.txt
```

### Bước 4: Kiểm tra GPU (tùy chọn)

```bash
python check_gpu.py
```

**Output mong đợi (nếu có GPU):**

```
[✓] GPU (CUDA) KHẢ DỤNG!
[+] CUDA version: 12.4
[+] GPU: NVIDIA GeForce RTX 3080
[✓] GPU hoạt động tốt!
```

---

## 🛠️ Hướng dẫn sử dụng

### Chạy nhanh - Tất cả demo (khuyến nghị)

```bash
python run_all_real_demos.py
```

Script này sẽ tự động:
1. ✅ Kiểm tra dependencies
2. ✅ Huấn luyện mô hình CNN trên MNIST
3. ✅ Chạy Demo 1: Evasion Attack (FGSM)
4. ✅ Chạy Demo 2: Data Poisoning Attack
5. ✅ Chạy Demo 3: Prompt Injection Attack
6. ✅ Tạo báo cáo và visualization

### Chạy từng bước riêng lẻ

#### 1. Huấn luyện mô hình cơ sở

```bash
python train_mnist_model.py
```

**Output:** File `mnist_cnn_model.pth` (~1MB)

#### 2. Chạy Demo Evasion Attack

```bash
python demo_evasion_attack.py
```

#### 3. Chạy Demo Data Poisoning

```bash
python demo_data_poisoning_attack.py
```

#### 4. Chạy Demo Prompt Injection

```bash
python demo_prompt_injection_attack.py
```

> ⚠️ **Lưu ý:** Demo 3 yêu cầu LLM API server chạy ở `http://127.0.0.1:8000/v1`. Nếu không có, demo sẽ báo lỗi kết nối.

---

## 🎯 Kịch bản tấn công

### Demo 1: Evasion Attack (FGSM) - Checklist VR-01

**Mô tả:** Sử dụng phương pháp Fast Gradient Sign Method (FGSM) để tạo adversarial examples đánh lừa mô hình CNN nhận diện chữ số viết tay.

| Thuộc tính | Giá trị |
|------------|---------|
| **Mô hình mục tiêu** | CNN (Convolutional Neural Network) |
| **Bộ dữ liệu** | MNIST (60,000 train, 10,000 test) |
| **Phương pháp tấn công** | FGSM |
| **Epsilon range** | 0.00 - 0.30 |
| **Metric** | Empirical Robustness (ER) |
| **Ngưỡng** | ER > 0.1 |

**Nguyên lý hoạt động:**
```
adversarial_image = original_image + ε × sign(∇_x Loss(θ, x, y))
```

---

### Demo 2: Data Poisoning Attack - Checklist SR-03

**Mô tả:** Tiêm nhiễm dữ liệu độc hại (label flipping) vào tập huấn luyện để làm sai lệch ranh giới quyết định của mô hình SVM.

| Thuộc tính | Giá trị |
|------------|---------|
| **Mô hình mục tiêu** | SVM (Support Vector Machine) |
| **Bộ dữ liệu** | Sklearn Digits (chữ số 5 và 9) |
| **Phương pháp tấn công** | Label Flipping |
| **Tỷ lệ nhiễm** | ~5% (15 mẫu) |
| **Metric** | Attack Success Rate (ASR) |
| **Ngưỡng** | ASR < 10% |

**Chiến lược tấn công:**
- Lấy mẫu thuộc class 9 (label = 1)
- Gán nhãn sai thành class 5 (label = 0)
- Thêm vào tập train để làm nhiễu mô hình

---

### Demo 3: Prompt Injection Attack - Checklists SR-01, SR-02, PE-01

**Mô tả:** Kiểm thử các kỹ thuật tấn công prompt injection trên hệ thống Chatbot LLM để trích xuất thông tin nhạy cảm hoặc thay đổi hành vi.

| Thuộc tính | Giá trị |
|------------|---------|
| **Mô hình mục tiêu** | LLM Chatbot (Qwen3-4B) |
| **API Endpoint** | http://127.0.0.1:8000/v1 |
| **Số test cases** | 15 (7 direct + 3 indirect + 5 PII) |
| **Metrics** | JSR, Task Hijack Rate, PII Leakage |

**Các loại tấn công:**

| Loại | Checklist | Mô tả |
|------|-----------|-------|
| **Direct Injection** | SR-01 | Jailbreak, override system prompt |
| **Indirect Injection** | SR-02 | Task hijack qua external data |
| **PII Leakage** | PE-01 | Trích xuất thông tin nhạy cảm |

---

## 📊 Kết quả và báo cáo

Sau khi chạy, kết quả được lưu trong thư mục `results/`:

### Báo cáo văn bản

| File | Nội dung |
|------|----------|
| `demo_evasion_report.txt` | Kết quả Evasion Attack |
| `demo_poisoning_report.txt` | Kết quả Data Poisoning |
| `demo_injection_report.txt` | Kết quả Prompt Injection |

### Báo cáo JSON (dùng cho tích hợp)

| File | Nội dung |
|------|----------|
| `demo_evasion_report.json` | Metrics chi tiết + evaluation |
| `demo_poisoning_report.json` | Metrics chi tiết + evaluation |
| `demo_injection_report.json` | Metrics chi tiết + evaluation |
| `demo_injection_detailed.json` | Toàn bộ LLM responses |

### Visualization

| File | Nội dung |
|------|----------|
| `demo_evasion_results.png` | Biểu đồ Accuracy vs Epsilon |
| `demo_poisoning_results.png` | Confusion Matrix + Accuracy comparison |

### Ví dụ kết quả (Demo 1 - Evasion):

```json
{
  "demo_name": "Evasion Attack (FGSM)",
  "checklist": "VR-01",
  "accuracy_clean": 0.99,
  "empirical_robustness": 0.15,
  "evaluation": {
    "er_threshold": 0.1,
    "er_pass": true
  },
  "overall_status": "PASS"
}
```

---

## 📚 Tài liệu tham khảo

### Trong dự án

| File | Nội dung |
|------|----------|
| `docs/FINAL_REPORT.md` | Báo cáo nghiên cứu đầy đủ |
| `docs/EXECUTIVE_SUMMARY.md` | Tóm tắt điều hành (~3 phút đọc) |
| `docs/EXPERIMENTAL_GUIDE.md` | Hướng dẫn thực nghiệm chi tiết |
| `docs/README_GPU_SETUP.md` | Hướng dẫn cài đặt GPU |

### Bên ngoài

- 📖 [PyTorch Installation](https://pytorch.org/get-started/locally/)
- 📖 [FGSM Attack Paper](https://arxiv.org/abs/1412.6572)
- 📖 [ISO 23894:2023 - AI Risk Management](https://www.iso.org/standard/77304.html)
- 📖 [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

---

## ❓ Khắc phục sự cố

### Lỗi "No module named 'torch'"

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

### Lỗi "CUDA not available"

1. Kiểm tra GPU: `python check_gpu.py`
2. Gỡ PyTorch: `pip uninstall torch torchvision`
3. Cài lại với CUDA: 
   ```bash
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
   ```

### Lỗi "Cannot find mnist_cnn_model.pth"

```bash
python train_mnist_model.py
```

### Demo 3 lỗi "Connection refused"

Demo Prompt Injection yêu cầu LLM API server. Đảm bảo:
- Server đang chạy ở `http://127.0.0.1:8000/v1`
- Model đúng tên: `Qwen/Qwen3-4B-Thinking-2507`

### Chạy chậm (không có GPU)

Nếu không có GPU NVIDIA, code sẽ tự động fallback sang CPU. Thời gian chạy có thể lâu hơn 10-50x.

---

## 🔧 Cấu hình nâng cao

### Thay đổi model cho Demo 3

Sửa file `demo_prompt_injection_attack.py`:

```python
API_BASE_URL = "http://your-api-server:port/v1"
MODEL_NAME = "your-model-name"
```

### Thay đổi epochs huấn luyện

Sửa file `train_mnist_model.py`:

```python
train_model(num_epochs=10)  # Tăng từ 5 lên 10
```

### Thay đổi epsilon range

Sửa file `demo_evasion_attack.py`:

```python
epsilons = [0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
```

---

## 📄 Giấy phép

Dự án này được phát triển cho mục đích nghiên cứu và giáo dục.

---

## 👥 Đóng góp

Mọi đóng góp đều được hoan nghênh! Vui lòng:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

---

## 📞 Liên hệ

Nếu có câu hỏi hoặc góp ý, vui lòng tạo Issue trên repository.

---

**Được xây dựng với ❤️ cho cộng đồng AI Security**
