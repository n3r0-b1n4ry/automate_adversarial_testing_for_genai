#!/usr/bin/env python3
"""
Script kiểm tra GPU và hướng dẫn cài đặt PyTorch với CUDA 12.4
"""

def check_gpu():
    """Kiểm tra GPU và in thông tin chi tiết"""
    
    print("\n" + "="*70)
    print("KIỂM TRA GPU VÀ CUDA")
    print("="*70)
    
    try:
        import torch
        print("\n[✓] PyTorch đã được cài đặt")
        print(f"[+] PyTorch version: {torch.__version__}")
        
        # Kiểm tra CUDA
        if torch.cuda.is_available():
            print("\n[✓] GPU (CUDA) KHẢ DỤNG!")
            print(f"[+] CUDA version: {torch.version.cuda}")
            print(f"[+] cuDNN version: {torch.backends.cudnn.version()}")
            
            # Thông tin GPU
            print(f"\n[📊] Thông tin GPU:")
            for i in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(i)
                print(f"\n  GPU {i}: {torch.cuda.get_device_name(i)}")
                print(f"    ├─ Memory: {props.total_memory / 1e9:.2f} GB")
                print(f"    ├─ Compute Capability: {props.major}.{props.minor}")
                print(f"    └─ Multi Processors: {props.multi_processor_count}")
            
            # Test GPU
            print("\n[🔧] Test GPU performance...")
            try:
                x = torch.randn(1000, 1000).cuda()
                y = torch.randn(1000, 1000).cuda()
                import time
                start = time.time()
                z = torch.matmul(x, y)
                torch.cuda.synchronize()
                elapsed = time.time() - start
                print(f"[+] Matrix multiplication (1000x1000): {elapsed*1000:.2f}ms")
                print("[✓] GPU hoạt động tốt!")
            except Exception as e:
                print(f"[!] Lỗi khi test GPU: {e}")
            
            print("\n" + "="*70)
            print("✅ SYSTEM READY - Có thể sử dụng GPU!")
            print("="*70)
            
        else:
            print("\n[!] GPU KHÔNG KHẢ DỤNG")
            print("[!] PyTorch đang chạy trên CPU")
            
            # Kiểm tra lý do
            print("\n[🔍] Nguyên nhân có thể:")
            print("  1. PyTorch được cài với CPU version")
            print("  2. Driver NVIDIA chưa cài hoặc quá cũ")
            print("  3. CUDA toolkit chưa cài đặt")
            print("  4. Máy không có GPU NVIDIA")
            
            # Hướng dẫn cài đặt
            print("\n[💡] Cách khắc phục:")
            print("\n  Bước 1: Gỡ PyTorch hiện tại")
            print("    pip uninstall torch torchvision")
            
            print("\n  Bước 2: Cài PyTorch với CUDA 12.4")
            print("    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124")
            
            print("\n  Bước 3: Kiểm tra lại")
            print("    python check_gpu.py")
            
            print("\n" + "="*70)
            print("⚠️  ĐANG DÙNG CPU - Demo sẽ chạy chậm hơn")
            print("="*70)
            
    except ImportError:
        print("\n[✗] PyTorch chưa được cài đặt!")
        print("\n[📝] Hướng dẫn cài đặt:")
        
        print("\n1️⃣  CÀI VỚI GPU (CUDA 12.4) - Khuyến nghị:")
        print("    pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124")
        
        print("\n2️⃣  CÀI VỚI CPU (không cần GPU):")
        print("    pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu")
        
        print("\n3️⃣  Sau khi cài, chạy lại:")
        print("    python check_gpu.py")
        
        print("\n" + "="*70)
    
    except Exception as e:
        print(f"\n[✗] Lỗi không xác định: {e}")
        import traceback
        traceback.print_exc()

def check_nvidia_driver():
    """Kiểm tra NVIDIA driver"""
    import subprocess
    
    print("\n" + "="*70)
    print("KIỂM TRA NVIDIA DRIVER")
    print("="*70)
    
    try:
        result = subprocess.run(['nvidia-smi'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("\n[✓] NVIDIA Driver đã được cài đặt")
            print("\n" + result.stdout)
        else:
            print("\n[✗] nvidia-smi không chạy được")
            print("[!] Có thể driver chưa cài hoặc không đúng")
    except FileNotFoundError:
        print("\n[✗] nvidia-smi không tìm thấy")
        print("[!] NVIDIA Driver chưa được cài đặt")
        print("\n[💡] Tải driver tại: https://www.nvidia.com/Download/index.aspx")
    except subprocess.TimeoutExpired:
        print("\n[!] nvidia-smi timeout")
    except Exception as e:
        print(f"\n[!] Lỗi: {e}")

def main():
    """Main function"""
    
    print("\n" + "="*70)
    print("🔍 CÔNG CỤ KIỂM TRA GPU VÀ CUDA CHO DEMO THỰC TẾ")
    print("="*70)
    
    # Check NVIDIA driver
    check_nvidia_driver()
    
    # Check GPU
    check_gpu()
    
    # Tóm tắt
    print("\n" + "="*70)
    print("📚 TÀI LIỆU THAM KHẢO")
    print("="*70)
    print("  • PyTorch installation: https://pytorch.org/get-started/locally/")
    print("  • NVIDIA drivers: https://www.nvidia.com/Download/index.aspx")
    print("  • CUDA toolkit: https://developer.nvidia.com/cuda-downloads")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

