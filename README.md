# Demo Kiểm thử An toàn AI (AI Security Demo)

Dự án này cung cấp các mã nguồn demo thực tế cho việc kiểm thử an toàn hệ thống AI, minh họa các kỹ thuật tấn công Evasion, Data Poisoning và Prompt Injection nhằm đánh giá tính bền vững của mô hình.

## 📂 Cấu trúc Dự án

d:\code\cdcs\
├── 📄 demo_data_poisoning_attack.py   # Demo tấn công đầu độc dữ liệu (Data Poisoning - SVM)
├── 📄 demo_evasion_attack.py          # Demo tấn công né tránh (Evasion Attack - FGSM trên CNN)
├── 📄 demo_prompt_injection_attack.py # Demo tấn công tiêm câu lệnh (Prompt Injection trên LLM giả định)
├── 📄 train_mnist_model.py            # Script huấn luyện mô hình CNN cơ sở trên bộ dữ liệu MNIST
├── 📄 run_all_real_demos.py           # Script chạy tự động toàn bộ quy trình demo
├── 📄 check_gpu.py                    # Kiểm tra trạng thái GPU (CUDA) để tăng tốc độ xử lý
├── 📂 data/                           # Thư mục chứa dữ liệu (MNIST)
├── 📂 docs/                           # Tài liệu báo cáo và hướng dẫn chi tiết
├── 📂 results/                        # Kết quả đầu ra (báo cáo text/json, biểu đồ ảnh)
└── 📂 setup/                          # Các file cài đặt môi trường## 🚀 Cài đặt Môi trường

Yêu cầu: Python 3.8+

1. **Tạo môi trường ảo (Khuyên dùng):**
   
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   2. **Cài đặt các thư viện phụ thuộc:**
   pip install -r setup/requirements.txt
   3. **Kiểm tra GPU (Tùy chọn):**
   python check_gpu.py
      *Lưu ý: Nếu không có GPU, code sẽ tự động chạy trên CPU.*

## 🛠️ Hướng dẫn Sử dụng

### 1. Huấn luyện Mô hình Cơ sở
Trước khi chạy các demo tấn công (đặc biệt là Evasion), bạn cần huấn luyện mô hình CNN. File `mnist_cnn_model.pth` sẽ được tạo ra sau khi chạy xong.

python train_mnist_model.py### 2. Chạy các Kịch bản Tấn công Riêng lẻ

**Kịch bản 1: Evasion Attack (Tấn công né tránh)**
Minh họa tấn công FGSM (Fast Gradient Sign Method) để đánh lừa mô hình nhận diện chữ viết tay.
python demo_evasion_attack.py**Kịch bản 2: Data Poisoning (Đầu độc dữ liệu)**
Minh họa việc tiêm nhiễm dữ liệu độc hại vào tập train làm sai lệch ranh giới quyết định của mô hình SVM (Label Flipping).
python demo_data_poisoning_attack.py**Kịch bản 3: Prompt Injection (Tiêm câu lệnh)**
Minh họa các kỹ thuật tấn công vào hệ thống Chatbot giả định để trích xuất thông tin nhạy cảm (PII) hoặc thay đổi hành vi.
python demo_prompt_injection_attack.py### 3. Chạy Toàn bộ Demo (Tự động)
Để chạy lần lượt tất cả các bước (huấn luyện -> tấn công -> báo cáo) trong một lần chạy:

python run_all_real_demos.py## 📊 Kết quả & Báo cáo

Sau khi thực thi, kết quả sẽ được lưu tự động trong thư mục `results/`:
*   **Báo cáo chi tiết:** Các file `_report.txt` và `_report.json` chứa các chỉ số đánh giá (Robustness, Attack Success Rate).
*   **Trực quan hóa:**
    *   `demo_evasion_results.png`: So sánh ảnh gốc và ảnh đối kháng.
    *   `demo_poisoning_results.png`: Biểu đồ thay đổi ranh giới phân lớp trước và sau khi bị đầu độc.

Tham khảo thêm thư mục `docs/` để đọc các báo cáo tổng hợp chi tiết (`FINAL_REPORT.md`, `EXECUTIVE_SUMMARY.md`).