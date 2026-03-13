import easyocr
import cv2
import numpy as np
import os

def draw_green_box_for_text():
    print("=" * 60)
    print("EasyOCR 示例 - 用绿框标记特定文本")
    print("=" * 60)
    
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    
    print(f"\n模型目录: {model_dir}")
    
    reader = easyocr.Reader(
        ['ch_sim', 'en'],
        gpu=False,
        model_storage_directory=model_dir,
        download_enabled=False
    )
    
    chinese_img = os.path.join(os.path.dirname(__file__), '..', 'examples', 'chinese.jpg')
    print(f"\n图片路径: {chinese_img}")
    
    if not os.path.exists(chinese_img):
        print("图片文件不存在！")
        return
    
    print("正在识别图片...")
    result = reader.readtext(chinese_img)
    
    target_text = "愚园路"
    print(f"\n目标文本: {target_text}")
    
    img = cv2.imread(chinese_img)
    
    found = False
    for i, (bbox, text, confidence) in enumerate(result, 1):
        print(f"\n{i}. 文本: {text}")
        print(f"   置信度: {confidence:.4f}")
        
        if target_text in text:
            print(f"   ✓ 找到目标文本！")
            found = True
            
            bbox = np.array(bbox).astype(np.int32)
            
            cv2.rectangle(img, 
                        tuple(bbox[0]), 
                        tuple(bbox[2]), 
                        (0, 255, 0), 
                        3)
            
            label = f"{text} ({confidence:.2f})"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            
            cv2.rectangle(img,
                        tuple(bbox[0]),
                        (bbox[0][0] + label_size[0] + 10, bbox[0][1] - label_size[1] - 10),
                        (0, 255, 0),
                        -1)
            
            cv2.putText(img, label, 
                      (bbox[0][0] + 5, bbox[0][1] - 5),
                      cv2.FONT_HERSHEY_SIMPLEX, 
                      0.5, 
                      (0, 0, 0), 
                      2)
    
    if found:
        output_path = os.path.join(os.path.dirname(__file__), 'output_with_green_box.jpg')
        cv2.imwrite(output_path, img)
        print(f"\n✓ 已保存标记后的图片: {output_path}")
        print(f"  图片大小: {img.shape}")
    else:
        print(f"\n✗ 未找到目标文本: {target_text}")
    
    print("\n" + "=" * 60)
    print("处理完成！")
    print("=" * 60)
    
    return output_path if found else None

if __name__ == '__main__':
    draw_green_box_for_text()