import json
from pathlib import Path
from PIL import Image

def analyze_image(image_path):
    image_path = Path(image_path)
    
    try:
        img = Image.open(image_path)
        width, height = img.size
        format = img.format
        mode = img.mode
        
        return {
            "filename": image_path.name,
            "path": str(image_path),
            "size": (width, height),
            "format": format,
            "mode": mode,
            "filesize": image_path.stat().st_size
        }
    except Exception as e:
        return {
            "filename": image_path.name,
            "error": str(e)
        }

def analyze_all_images(images_dir):
    images_dir = Path(images_dir)
    results = []
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    
    for file_path in images_dir.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            result = analyze_image(file_path)
            results.append(result)
    
    return results

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    
    print("=" * 60)
    print("VLM Wiki - 图片分析工具")
    print("=" * 60)
    
    # 分析原始图片
    print("\n[1/3] 分析原始图片...")
    images_dir = script_dir / "../raw/images"
    image_results = analyze_all_images(images_dir)
    
    print(f"\n找到 {len(image_results)} 张图片:")
    for r in image_results:
        if "error" not in r:
            print(f"  - {r['filename']}: {r['size'][0]}x{r['size'][1]}, {r['format']}")
        else:
            print(f"  - {r['filename']}: 错误 - {r['error']}")
    
    # 分析视频帧
    print("\n[2/3] 分析视频提取帧...")
    frames_dir = script_dir / "../raw/videos/2023-05-frames"
    if frames_dir.exists():
        frame_results = analyze_all_images(frames_dir)
        print(f"\n找到 {len(frame_results)} 个视频帧:")
        for r in frame_results:
            if "error" not in r:
                print(f"  - {r['filename']}: {r['size'][0]}x{r['size'][1]}")
    else:
        print("  视频帧目录不存在，请先运行 video_extractor.py")
    
    # 保存分析结果
    print("\n[3/3] 保存分析结果...")
    output_file = script_dir / "../raw/analysis_results.json"
    
    analysis_data = {
        "timestamp": "2026-05-03",
        "images": image_results,
        "frames": frame_results if 'frame_results' in locals() else []
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n分析结果已保存到: {output_file.resolve()}")
    print("\n" + "=" * 60)
    print("图片分析完成！")
    print("=" * 60)
