import easyocr
import cv2
import numpy as np
import os
import sys
import time

def draw_boxes_for_text(target_text="愚园路", color=(0, 255, 0), line_thickness=3):
    print("=" * 60)
    print("EasyOCR 示例 - 用指定颜色框标记文本")
    print("=" * 60)
    
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    
    print(f"\n模型目录: {model_dir}")
    print(f"目标文本: {target_text}")
    print(f"框颜色: RGB({color[0]}, {color[1]}, {color[2]})")
    print(f"框粗细: {line_thickness}")
    
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
        return None
    
    print("正在识别图片...")
    result = reader.readtext(chinese_img)
    
    img = cv2.imread(chinese_img)
    
    found_count = 0
    for i, (bbox, text, confidence) in enumerate(result, 1):
        print(f"\n{i}. 文本: {text}")
        print(f"   置信度: {confidence:.4f}")
        
        if target_text in text:
            print(f"   ✓ 找到目标文本！")
            found_count += 1
            
            bbox = np.array(bbox).astype(np.int32)
            
            x1, y1 = bbox[0]
            x3, y3 = bbox[2]
            width = x3 - x1
            height = y3 - y1
            
            print(f"   绿框坐标: ({x1}, {y1}) -> ({x3}, {y3})")
            print(f"   绿框宽高: 宽度={width}px, 高度={height}px")
            print(f"   四个角点: {bbox.tolist()}")
            
            cv2.rectangle(img, 
                        tuple(bbox[0]), 
                        tuple(bbox[2]), 
                        color, 
                        line_thickness)
            
            label = f"{text} ({confidence:.2f})"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
            
            cv2.rectangle(img,
                        tuple(bbox[0]),
                        (bbox[0][0] + label_size[0] + 10, bbox[0][1] - label_size[1] - 10),
                        color,
                        -1)
            
            cv2.putText(img, label, 
                      (bbox[0][0] + 5, bbox[0][1] - 5),
                      cv2.FONT_HERSHEY_SIMPLEX, 
                      0.5, 
                      (0, 0, 0), 
                      2)
    
    if found_count > 0:
        timestamp = int(time.time())
        output_path = os.path.join(os.path.dirname(__file__), f'output_box_{timestamp}.jpg')
        cv2.imwrite(output_path, img)
        print(f"\n✓ 找到 {found_count} 个匹配项")
        print(f"✓ 已保存标记后的图片: {output_path}")
        print(f"  目标文本: {target_text}")
        print(f"  图片大小: {img.shape}")
        return output_path
    else:
        print(f"\n✗ 未找到目标文本: {target_text}")
        return None

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target_text = sys.argv[1]
    else:
        target_text = "愚园路"
    
    draw_boxes_for_text(target_text)