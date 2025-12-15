@echo off
REM Script cài đặt PyTorch với GPU support (CUDA 12.4) cho Windows
REM Chạy trong virtual environment nếu có

echo ============================================================
echo CÀI ĐẶT PYTORCH VỚI GPU (CUDA 12.4)
echo ============================================================
echo.

echo [*] Kiểm tra Python...
python --version
if errorlevel 1 (
    echo [!] Python không tìm thấy!
    echo [!] Vui lòng cài Python 3.8+ trước
    pause
    exit /b 1
)

echo.
echo [*] Gỡ PyTorch cũ (nếu có)...
pip uninstall -y torch torchvision torchaudio

echo.
echo [*] Cài đặt dependencies cơ bản...
pip install numpy>=1.21.0 matplotlib>=3.4.0 scikit-learn>=1.0.0

echo.
echo ============================================================
echo [*] Cài đặt PyTorch với CUDA 12.4...
echo ============================================================
echo.
echo [!] Đang download (~2-3GB)... Có thể mất vài phút!
echo.

pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

if errorlevel 1 (
    echo.
    echo [!] CÀI ĐẶT THẤT BẠI!
    echo [!] Thử cài CPU version thay vì GPU?
    echo.
    choice /C YN /M "Cài CPU version"
    if errorlevel 2 goto end
    pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
)

echo.
echo ============================================================
echo [*] Kiểm tra cài đặt...
echo ============================================================
echo.

python check_gpu.py

echo.
echo ============================================================
echo HOÀN TẤT CÀI ĐẶT!
echo ============================================================
echo.
echo [+] Bây giờ bạn có thể chạy:
echo     python train_mnist_model.py
echo     python demo_evasion_attack.py
echo.

:end
pause

