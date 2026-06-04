"""小红书封面图生成器"""
import sys
import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1080, 1440

def create_cover(title, subtitle="", output="cover.png"):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#FFF5F5")
    draw = ImageDraw.Draw(img)
    
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]
    font_path = None
    for p in font_paths:
        if os.path.exists(p):
            font_path = p
            break
    
    title_font = ImageFont.truetype(font_path, 72) if font_path else ImageFont.load_default()
    subtitle_font = ImageFont.truetype(font_path, 40) if font_path else ImageFont.load_default()
    
    lines = title.split("\n")
    y_start = HEIGHT // 3
    
    for i, line in enumerate(lines):
        shadow_color = "#FFD0D0"
        for dx, dy in [(3, 3), (2, 2), (1, 1)]:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            tw = bbox[2] - bbox[0]
            x = (WIDTH - tw) // 2 + dx
            y = y_start + i * 100 + dy
            draw.text((x, y), line, fill=shadow_color, font=title_font)
        
        bbox = draw.textbbox((0, 0), line, font=title_font)
        tw = bbox[2] - bbox[0]
        x = (WIDTH - tw) // 2
        y = y_start + i * 100
        draw.text((x, y), line, fill="#D4380D", font=title_font)
    
    if subtitle:
        sy = y_start + len(lines) * 100 + 60
        bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        sw = bbox[2] - bbox[0]
        draw.text(((WIDTH - sw) // 2, sy), subtitle, fill="#888888", font=subtitle_font)
    
    draw.rectangle([200, HEIGHT - 200, WIDTH - 200, HEIGHT - 195], fill="#FFD0D0")
    img.save(output, "PNG")
    print(f"✅ 封面图已生成: {output}")
    size = os.path.getsize(output) / 1024
    print(f"   尺寸: {WIDTH}x{HEIGHT} | 大小: {size:.0f}KB")

def main():
    if len(sys.argv) < 2:
        print("用法: xiaohongshu-cover <标题> [副标题] [输出文件名]")
        print("示例: xiaohongshu-cover '一篇笔记憋3小时' 'AI工具' mycover.png")
        sys.exit(1)
    
    title = sys.argv[1].replace("\\n", "\n")
    subtitle = sys.argv[2] if len(sys.argv) > 2 else ""
    output = sys.argv[3] if len(sys.argv) > 3 else "cover.png"
    create_cover(title, subtitle, output)

if __name__ == "__main__":
    main()
