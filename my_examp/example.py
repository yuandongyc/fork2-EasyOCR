import easyocr
import os

def run_ocr_example():
    print("=" * 60)
    print("EasyOCR 示例 - 使用本地模型")
    print("=" * 60)
    
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    
    print(f"\n模型目录: {model_dir}")
    
    reader = easyocr.Reader(
        ['ch_sim', 'en'],
        gpu=False,
        model_storage_directory=model_dir,
        download_enabled=False
    )
    
    print("\n" + "=" * 60)
    print("示例 1: 识别中文图片")
    print("=" * 60)
    
    chinese_img = os.path.join(os.path.dirname(__file__), '..', 'examples', 'chinese.jpg')
    print(f"\n图片路径: {chinese_img}")
    
    if os.path.exists(chinese_img):
        print("正在识别...")
        result = reader.readtext(chinese_img)
        
        print(f"\n识别结果 (共 {len(result)} 个文本框):")
        print("-" * 60)
        for i, (bbox, text, confidence) in enumerate(result, 1):
            print(f"{i}. 文本: {text}")
            print(f"   置信度: {confidence:.4f}")
            print(f"   位置: {bbox}")
            print()
    else:
        print("图片文件不存在！")
    
    print("=" * 60)
    print("示例 2: 识别英文图片")
    print("=" * 60)
    
    english_img = os.path.join(os.path.dirname(__file__), '..', 'examples', 'english.png')
    print(f"\n图片路径: {english_img}")
    
    if os.path.exists(english_img):
        print("正在识别...")
        result = reader.readtext(english_img)
        
        print(f"\n识别结果 (共 {len(result)} 个文本框):")
        print("-" * 60)
        for i, (bbox, text, confidence) in enumerate(result, 1):
            print(f"{i}. 文本: {text}")
            print(f"   置信度: {confidence:.4f}")
            print(f"   位置: {bbox}")
            print()
    else:
        print("图片文件不存在！")
    
    print("=" * 60)
    print("示例 3: 简化输出 (只返回文本)")
    print("=" * 60)
    
    print("\n中文图片简化输出:")
    result_simple = reader.readtext(chinese_img, detail=0)
    for i, text in enumerate(result_simple, 1):
        print(f"{i}. {text}")
    
    print("\n英文图片简化输出:")
    result_simple = reader.readtext(english_img, detail=0)
    for i, text in enumerate(result_simple, 1):
        print(f"{i}. {text}")
    
    print("\n" + "=" * 60)
    print("识别完成！")
    print("=" * 60)

if __name__ == '__main__':
    run_ocr_example()