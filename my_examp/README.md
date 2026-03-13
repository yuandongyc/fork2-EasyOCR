# EasyOCR 示例脚本

本目录包含 EasyOCR 的使用示例脚本。

## 文件说明

- `check_env.py` - 环境检查脚本
- `example.py` - OCR 识别示例脚本
- `draw_green_box.py` - 用绿框标记特定文本（"愚园路"）
- `draw_box_advanced.py` - 用指定颜色框标记任意文本（高级版本）

## 使用步骤

### 1. 激活虚拟环境

```bash
cd D:\MyProjects\c_projects\fork2-EasyOCR
venv\Scripts\activate
```

### 2. 运行环境检查

```bash
cd my_examp
python check_env.py
```

这个脚本会检查：
- Python 环境
- EasyOCR 安装状态
- PyTorch 安装状态
- 模型文件是否存在
- 示例图片是否存在

### 3. 运行 OCR 示例

```bash
python example.py
```

这个脚本会演示：
- 识别中文图片
- 识别英文图片
- 简化输出（只返回文本）

### 4. 运行文本标记示例

#### 基础版本（固定标记"愚园路"）

```bash
python draw_green_box.py
```

这个脚本会：
- 识别中文图片
- 找到"愚园路"文本
- 用绿框标记该文本
- 保存标记后的图片到 `output_with_green_box.jpg`

#### 高级版本（标记任意文本）

```bash
# 标记"愚园路"
python draw_box_advanced.py "愚园路"

# 标记"315"
python draw_box_advanced.py "315"

# 标记"东"
python draw_box_advanced.py "东"
```

这个脚本会：
- 识别中文图片
- 找到指定文本
- 用绿框标记该文本
- 显示置信度
- 保存标记后的图片到 `output_{文本}_box.jpg`

## 配置说明

示例脚本使用以下配置：

- **语言**: 中文简体 + 英文
- **GPU**: 禁用（使用 CPU）
- **模型路径**: `../models` 目录
- **自动下载**: 禁用（使用本地模型）

## 模型文件

确保以下模型文件存在于 `models` 目录：

- `models/cn/chinese_sim.pth` - 中文简体模型
- `models/latin/latin.pth` - 英文/拉丁语模型

## 示例图片

确保以下示例图片存在于 `examples` 目录：

- `examples/chinese.jpg` - 中文示例图片
- `examples/english.png` - 英文示例图片

## 自定义使用

你可以在 `example.py` 中修改以下参数：

```python
reader = easyocr.Reader(
    ['ch_sim', 'en'],  # 语言列表
    gpu=False,          # 是否使用 GPU
    model_storage_directory=model_dir,  # 模型目录
    download_enabled=False  # 是否允许自动下载
)
```

## 常见问题

### 1. 模型文件不存在

运行环境检查脚本，确认模型文件已下载。

### 2. 识别速度慢

这是正常的，因为使用的是 CPU 模式。如果有 GPU，可以设置 `gpu=True`。

### 3. 识别结果不准确

可以尝试：
- 使用更高分辨率的图片
- 调整识别参数
- 使用更合适的语言模型

## 更多信息

- EasyOCR 官方文档: https://www.jaided.ai/easyocr
- EasyOCR GitHub: https://github.com/JaidedAI/EasyOCR