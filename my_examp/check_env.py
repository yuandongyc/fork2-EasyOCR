import os
import sys

def check_environment():
    print("=" * 60)
    print("EasyOCR 环境检查")
    print("=" * 60)
    
    print("\n1. 检查虚拟环境:")
    print(f"   Python 路径: {sys.executable}")
    print(f"   Python 版本: {sys.version}")
    
    print("\n2. 检查 EasyOCR:")
    try:
        import easyocr
        print(f"   ✓ EasyOCR 已安装")
        print(f"   版本: 1.7.2")
    except ImportError:
        print("   ✗ EasyOCR 未安装")
        return False
    
    print("\n3. 检查 PyTorch:")
    try:
        import torch
        print(f"   ✓ PyTorch 已安装")
        print(f"   版本: {torch.__version__}")
        print(f"   CUDA 可用: {torch.cuda.is_available()}")
    except ImportError:
        print("   ✗ PyTorch 未安装")
        return False
    
    print("\n4. 检查模型文件:")
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    print(f"   模型目录: {model_dir}")
    
    models_to_check = [
        ('cn/chinese_sim.pth', '中文简体模型'),
        ('latin/latin.pth', '英文/拉丁语模型')
    ]
    
    all_models_exist = True
    for model_path, model_name in models_to_check:
        full_path = os.path.join(model_dir, model_path)
        if os.path.exists(full_path):
            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            print(f"   ✓ {model_name}: {size_mb:.2f} MB")
        else:
            print(f"   ✗ {model_name}: 不存在")
            all_models_exist = False
    
    print("\n5. 检查示例图片:")
    examples_dir = os.path.join(os.path.dirname(__file__), '..', 'examples')
    print(f"   示例目录: {examples_dir}")
    
    images_to_check = [
        ('chinese.jpg', '中文示例'),
        ('english.png', '英文示例')
    ]
    
    all_images_exist = True
    for img_path, img_name in images_to_check:
        full_path = os.path.join(examples_dir, img_path)
        if os.path.exists(full_path):
            size_kb = os.path.getsize(full_path) / 1024
            print(f"   ✓ {img_name}: {size_kb:.2f} KB")
        else:
            print(f"   ✗ {img_name}: 不存在")
            all_images_exist = False
    
    print("\n" + "=" * 60)
    if all_models_exist and all_images_exist:
        print("✓ 环境检查通过！可以运行示例。")
    else:
        print("✗ 环境检查失败！请检查缺失的文件。")
    print("=" * 60)
    
    return all_models_exist and all_images_exist

if __name__ == '__main__':
    check_environment()