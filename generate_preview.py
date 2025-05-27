#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
生成 Typora 主题预览图占位图
"""

import os
from PIL import Image, ImageDraw, ImageFont

def ensure_directory(directory):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_preview_image(filename, title, is_dark=False):
    """创建预览图片占位符"""
    # 设置图片大小和背景色
    width, height = 800, 600
    bg_color = (31, 31, 31) if is_dark else (255, 255, 255)
    text_color = (224, 224, 224) if is_dark else (51, 51, 51)
    
    # 创建一个新的图像，设置背景色
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # 尝试加载字体，如果失败则使用默认字体
    try:
        # 尝试加载不同的字体，根据系统可用性
        font_paths = [
            'C:/Windows/Fonts/Arial.ttf',  # Windows
            '/Library/Fonts/Arial.ttf',     # macOS
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',  # Linux
            None  # 默认字体
        ]
        
        font = None
        for path in font_paths:
            try:
                if path:
                    font = ImageFont.truetype(path, 36)
                    break
            except Exception:
                continue
        
        if font is None:
            font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
    
    # 在图像中心绘制文本
    text = f"{title} 预览图"
    text_width = draw.textlength(text, font=font) if hasattr(draw, 'textlength') else font.getsize(text)[0]
    text_position = ((width - text_width) // 2, height // 2 - 20)
    draw.text(text_position, text, fill=text_color, font=font)
    
    # 添加说明文字
    note = "这是一个预览图占位符。请使用真实截图替换。"
    note_font = font if font.size <= 24 else ImageFont.truetype(font.path, 24) if hasattr(font, 'path') else font
    note_width = draw.textlength(note, font=note_font) if hasattr(draw, 'textlength') else note_font.getsize(note)[0]
    note_position = ((width - note_width) // 2, height // 2 + 30)
    draw.text(note_position, note, fill=text_color, font=note_font)
    
    # 保存图像
    image.save(filename)
    print(f"已生成预览图: {filename}")

def main():
    """主函数"""
    # 确保img目录存在
    ensure_directory('img')
    
    # 生成明亮主题预览图
    create_preview_image('img/light-preview.png', '明亮主题', is_dark=False)
    
    # 生成暗色主题预览图
    create_preview_image('img/dark-preview.png', '暗色主题', is_dark=True)

if __name__ == "__main__":
    main() 