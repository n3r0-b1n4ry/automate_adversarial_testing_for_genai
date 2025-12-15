# README - CHƯƠNG 4: XÂY DỰNG KỊCH BẢN DEMO TRÊN HỆ THỐNG AI GIẢ ĐỊNH

## 📋 Tổng Quan

Đây là hướng dẫn chi tiết để **xây dựng và chạy các thực nghiệm cho Chương 4** của đề tài:

> **"NGHIÊN CỨU VÀ ĐỀ XUẤT KHUNG PHƯƠNG PHÁP KIỂM THỬ ĐỐI KHÁNG TỰ ĐỘNG HỆ THỐNG AI THEO TIÊU CHUẨN ISO 23894:2023"**

Chương 4 bao gồm **3 kịch bản demo** minh họa khung AAT-ISO Framework trên các hệ thống AI giả định.

---

## 📚 Tài Liệu Đi Kèm

Bạn sẽ nhận được **4 tệp chính**:

### 1️⃣ **`demo_thuc_nghiem_Ch4.md`** (Mã nguồn chính - 3000+ dòng)
- ✅ Mã Python đầy đủ cho tất cả 3 Demo
- ✅ Hướng dẫn cài đặt môi trường
- ✅ Script huấn luyện, tấn công, đánh giá
- ✅ Visualizations và báo cáo

**Nội dung:**
```
├── Phần 1: Thiết lập môi trường
├── Phần 2: Hệ thống A - AI Dự đoán (CNN + MNIST)
│   ├── 2.1 Xây dựng mô hình
│   ├── 2.2 Demo 1: Evasion Attack (FGSM)
│   └── 2.3 Demo 2: Data Poisoning
├── Phần 3: Hệ thống B - AI Tạo sinh (Chatbot)
│   ├── 3.1 Xây dựng Chatbot
│   └── 3.2 Demo 3: Prompt Injection
├── Phần 4: Tích hợp và chạy tất cả
└── Phần 5: Hướng dẫn chạy
```

### 2️⃣ **`quick_demo.py`** (Demo nhanh - Chạy ngay!)
- ✅ Không cần cài đặt library phức tạp
- ✅ Kết quả mô phỏng trong ~30 giây
- ✅ Hoàn hảo để kiểm tra nhanh

**Chạy:**
```bash
python quick_demo.py
```

### 3️⃣ **`huong_dan_giai_thich.md`** (Giải thích chi tiết - 2000+ dòng)
- ✅ Nền tảng lý thuyết cho mỗi Demo
- ✅ Diễn giải chi tiết kết quả
- ✅ Ý nghĩa theo ISO 23894
- ✅ FAQ và biện pháp giảm thiểu rủi ro

**Nội dung:**
```
├── I. Tổng quan Chương 4
├── II. Giải thích Demo 1: Evasion Attack
├── III. Giải thích Demo 2: Data Poisoning
├── IV. Giải thích Demo 3: Prompt Injection
├── V. Tóm tắt chung
├── VI. Quy trình thực hiện
└── VII. FAQ & Câu hỏi thường gặp
```

### 4️⃣ **`huong_dan_thuc_hien.md`** (Hướng dẫn bước-theo-bước - 1000+ dòng)
- ✅ Hướng dẫn chi tiết từ A-Z
- ✅ Troubleshooting & giải quyết lỗi
- ✅ Bảng so sánh kết quả
- ✅ Tóm lược nhanh nhất

**Nội dung:**
```
├── Bước 1: Chuẩn bị môi trường
├── Bước 2: Chuẩn bị file Python
├── Bước 3: Chạy các thực nghiệm
├── Bước 4: Phân tích kết quả
├── Bước 5: Giải thích kết quả
├── Bước 6: Tạo báo cáo tổng hợp
├── Bước 7: Cleanup & tổ chức
├── Bước 8: Troubleshooting
└── Bước 9: Tóc lược nhanh
```

---

## 🚀 Bắt Đầu Nhanh (3 Cách)

### Cách 1: DEMO NHANH (30 giây) ⚡
```bash
# Không cần cài đặt phức tạp
python quick_demo.py

# Xem kết quả:
# DEMO 1: EVASION ATTACK SIMULATION (VR-01) → FAIL ❌
# DEMO 2: DATA POISONING ATTACK SIMULATION (SR-03) → FAIL ❌
# DEMO 3: PROMPT INJECTION ATTACK SIMULATION → FAIL ❌ (3/3)
```

### Cách 2: DEMO ĐẦY ĐỦ (5-10 phút) 🎯
```bash
# 1. Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Huấn luyện
python train_mnist_model.py

# 3. Chạy tấn công
python demo_evasion_attack.py
python demo_data_poisoning_attack.py
python demo_prompt_injection_attack.py

# 4. Xem kết quả
ls results/
```

### Cách 3: TẤT CẢ MỘT LẦN (Nếu có script wrapper) 🏃
```bash
python run_all_experiments.py
```

---

## 📊 Kết Quả Dự Kiến

### Demo 1: Evasion Attack (VR-01)
```
Hệ thống: CNN trên MNIST
Tấn công: FGSM
Kết quả: 
  • Empirical Robustness: 0.08 (< 0.1) → FAIL ❌
  • Accuracy Loss @ ε=0.15: 66.4% (>> 10%) → FAIL ❌
Output: demo_evasion_results.png, demo_evasion_report.txt
```

### Demo 2: Data Poisoning (SR-03)
```
Hệ thống: SVM (5 vs 9)
Tấn công: 15 mẫu độc
Kết quả:
  • Attack Success Rate: 43.2% (>> 10%) → FAIL ❌
  • Accuracy: 93.6% → 50.4% (tương đương đoán ngẫu nhiên)
Output: demo_poisoning_results.png, demo_poisoning_report.txt
```

### Demo 3: Prompt Injection (SR-01, SR-02, PE-01)
```
Hệ thống: Chatbot LLM
Tấn công: Direct Injection, Indirect Injection, PII Leakage
Kết quả:
  • SR-01 (Direct): 100% thành công → FAIL ❌
  • SR-02 (Indirect): 100% thành công → FAIL ❌
  • PE-01 (PII): 71.4% rò rỉ → FAIL ❌
Output: demo_injection_report.json
```

---

## 📁 Cấu Trúc File & Thư Mục

```
chapter4_demo/
├── README.md                         ← Bạn đang đọc
├── requirements.txt                  ← Dependencies
├── quick_demo.py                     ← Chạy nhanh
├── train_mnist_model.py              ← Huấn luyện CNN
├── demo_evasion_attack.py            ← Demo 1
├── demo_data_poisoning_attack.py     ← Demo 2
├── demo_prompt_injection_attack.py   ← Demo 3
├── chatbot_system.py                 ← Chatbot base
├── run_all_experiments.py            ← Master script (nếu có)
├── data/                             ← MNIST (tự động tạo)
├── results/                          ← Output (tự động tạo)
│   ├── demo_evasion_results.png
│   ├── demo_evasion_report.txt
│   ├── demo_poisoning_results.png
│   ├── demo_poisoning_report.txt
│   ├── demo_injection_report.json
│   └── CHAPTER4_FINAL_REPORT.txt
└── venv/                             ← Virtual environment
```

---

## 🔧 Yêu Cầu Hệ Thống

| Yêu cầu | Chi tiết |
|---------|---------|
| **Python** | >= 3.8 |
| **RAM** | Tối thiểu 4GB, Khuyến nghị 8GB+ |
| **Disk** | ~2GB (cho MNIST dataset) |
| **CPU** | Bất kỳ (GPU là tùy chọn) |
| **OS** | Linux, macOS, Windows |

---

## 📦 Cài Đặt Phụ Thuộc

### Tối thiểu (Chỉ quick_demo.py)
```bash
# Không cần gì cả, chỉ cần Python built-in
python quick_demo.py
```

### Standard (Demo thực tế)
```bash
pip install torch torchvision
pip install numpy scikit-learn matplotlib
pip install adversarial-robustness-toolbox
```

### Đầy đủ (Tất cả Demo)
```bash
pip install -r requirements.txt
```

### Các vấn đề cài đặt phổ biến

**Lỗi 1: "No module named 'torch'"**
```bash
pip install torch torchvision
```

**Lỗi 2: "secml installation failed"**
```bash
# Linux: sudo apt-get install build-essential python3-dev
# Mac: xcode-select --install
# Windows: Cài Visual Studio Build Tools
pip install secml --no-cache-dir
```

**Lỗi 3: "CUDA not available"**
→ Không sao, sẽ dùng CPU (chậm hơn nhưng ok)

---

## 🎓 Hướng Dẫn Đọc Tài Liệu

### Nếu bạn muốn...

**🏃 Chạy nhanh (1 phút):**
```
1. Đọc phần này
2. Chạy: python quick_demo.py
3. Hoàn thành!
```

**🎯 Hiểu từng chi tiết (30 phút):**
```
1. Đọc: huong_dan_giai_thich.md
2. Chạy: python demo_evasion_attack.py
3. Xem: results/*.png, results/*.txt
4. So sánh với lý thuyết
```

**🔬 Làm thực nghiệm đầy đủ (1 giờ):**
```
1. Đọc: huong_dan_thuc_hien.md (từng bước)
2. Thực hiện từng bước
3. Chạy: python train_mnist_model.py
4. Chạy: tất cả demo_*.py
5. Phân tích kết quả
```

**📚 Hiểu sâu (2-3 giờ):**
```
1. Đọc: demo_thuc_nghiem_Ch4.md (mã chi tiết)
2. Đọc: huong_dan_giai_thich.md (lý thuyết)
3. Thực hiện toàn bộ thí nghiệm
4. Tạo báo cáo tổng hợp
5. So sánh với Chương 1, 2, 3 của đề tài
```

---

## ✅ Checklist Hoàn Thành

- [ ] Cài đặt Python 3.8+
- [ ] Tạo virtual environment
- [ ] Cài đặt dependencies
- [ ] Chạy quick_demo.py (kiểm tra)
- [ ] Chạy train_mnist_model.py
- [ ] Chạy demo_evasion_attack.py
- [ ] Chạy demo_data_poisoning_attack.py
- [ ] Chạy demo_prompt_injection_attack.py
- [ ] Xem kết quả trong `results/`
- [ ] Đọc báo cáo (*.txt, *.json)
- [ ] Hiểu kết quả (đọc huong_dan_giai_thich.md)
- [ ] Tạo báo cáo tổng hợp

---

## 🎯 Mục Tiêu Chương 4

```
├─ Chứng minh tính khả thi của AAT-ISO Framework
├─ Minh họa áp dụng các kỹ thuật tấn công
├─ Đánh giá hệ thống AI dựa trên Checklist
└─ Tạo bằng chứng thực tế về hiệu quả kiểm thử
```

---

## 💡 Điểm Quan Trọng

1. **Tất cả Demo đều FAIL** - Điều này là BÌNH THƯỜNG!
   - Mục đích là minh họa rủi ro
   - Không phải để nhạo báng hệ thống

2. **Khung AAT-ISO hoạt động tốt** ✓
   - Có thể phát hiện lỗ hổng
   - Có thể định lượng rủi ro
   - Có thể tự động hóa

3. **Metrics là khách quan** 📊
   - ER, ASR, JSR, PII Leak Rate
   - Có thể so sánh và bình luận
   - Có thể theo dõi tiến tiến

4. **Biện pháp giảm thiểu là có sẵn** 🛡️
   - Adversarial training
   - Data validation
   - Guardrails & filtering

---

## 📞 Hỗ Trợ

Nếu gặp lỗi:
1. Xem phần "Troubleshooting" trong `huong_dan_thuc_hien.md`
2. Kiểm tra yêu cầu hệ thống
3. Cập nhật pip: `pip install --upgrade pip`
4. Xóa cache: `pip install --no-cache-dir <package>`

---

## 📖 Tài Liệu Liên Quan

- 📄 Chương 1: Phân tích ISO 23894:2023
- 📄 Chương 2: Kỹ thuật tấn công & Metrics
- 📄 Chương 3: Checklist & AAT-ISO Framework
- 📄 **Chương 4: Kịch bản Demo** ← Bạn đang ở đây
- 📄 Chương 5: Kết luận & Hướng phát triển

---

## 📊 BÁO CÁO KẾT QUẢ THỰC NGHIỆM

Sau khi chạy thực nghiệm, tham khảo các báo cáo chi tiết:

### 🎯 [INDEX_REPORTS.md](INDEX_REPORTS.md) ← BẮT ĐẦU TỪ ĐÂY!
**Chỉ mục tổng hợp** - Hướng dẫn chọn tài liệu phù hợp với vai trò và mục đích của bạn.

### 📑 Các báo cáo chính:

| Tài liệu | Đối tượng | Thời gian | Nội dung |
|----------|-----------|-----------|----------|
| **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** | Quản lý, Leadership | 3 phút | Tóm tắt nhanh, rủi ro, action items |
| **[FINAL_REPORT.md](FINAL_REPORT.md)** | PM, Researcher, Auditor | 30 phút | Báo cáo đầy đủ kết quả 3 demos |
| **[EXPERIMENTAL_GUIDE.md](EXPERIMENTAL_GUIDE.md)** | Developer, Engineer, Sinh viên | 60 phút | Hướng dẫn kỹ thuật chi tiết, FAQ |

### 📊 Tóm tắt kết quả:

```
Demo 1 (CNN/MNIST)      VR-01      ❌ FAIL   [████████░░]  80%
Demo 2 (SVM Binary)     SR-03      ✅ PASS   [██████████] 100%
Demo 3 (Chatbot LLM)    SR-01/02   ❌ FAIL   [░░░░░░░░░░]   0%

Overall Security Score: 33% (1/3 PASS)
```

**🔴 RỦI RO CRITICAL:** Demo 3 (Chatbot) có lỗ hổng nghiêm trọng - 100% vulnerable với prompt injection!

**📖 Xem chi tiết:** [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)

---

## 🎉 Bắt Đầu Thôi!

```bash
# Cách nhanh nhất (30 giây)
python quick_demo.py

# Hoặc chạy từng Demo
python train_mnist_model.py
python demo_evasion_attack.py
```

**Chúc bạn thành công! 🚀**

---

**Tài liệu này được tạo để hỗ trợ Chương 4 của đề tài:**
> "Xây dựng Kịch bản Demo trên Hệ thống AI Giả định"

**Phiên bản:** 1.0  
**Ngày cập nhật:** Tháng 12, 2025
