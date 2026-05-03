import os
import base64
from pathlib import Path
from openai import OpenAI


def encode_image_to_base64(image_path):
    """将图片编码为 base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_image_with_qwen(image_path, api_key=None, base_url=None):
    """
    使用 qwen3.5-omni-flash 模型分析图片
    
    Args:
        image_path: 图片路径
        api_key: DASHSCOPE_API_KEY，如果为 None 则从环境变量获取
        base_url: API Base URL，如果为 None 则使用默认值
    
    Returns:
        模型的分析结果
    """
    image_path = Path(image_path)
    
    if not image_path.exists():
        raise FileNotFoundError(f"图片文件不存在: {image_path}")
    
    # 配置 API
    api_key = api_key or os.getenv("DASHSCOPE_API_KEY")
    base_url = base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"
    
    if not api_key:
        raise ValueError("请设置 DASHSCOPE_API_KEY 环境变量或传入 api_key 参数")
    
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )
    
    # 编码图片
    image_base64 = encode_image_to_base64(image_path)
    
    # 构造提示词
    prompt = """请详细分析这张图片，包括：
1. 场景识别（这是什么场景、什么时间、什么地点）
2. 视觉元素描述（图片中有什么物体、人物、建筑、自然景观等）
3. 内容详细描述（用自然语言描述你看到的内容）
4. 情绪/氛围分析
5. 建议的标签（至少5个）

请用中文回答，格式清晰。"""
    
    # 调用模型
    completion = client.chat.completions.create(
        model="qwen3.5-omni-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        modalities=["text"],
    )
    
    return completion.choices[0].message.content


def analyze_all_images(images_dir, output_dir, api_key=None):
    """
    批量分析图片并保存结果
    
    Args:
        images_dir: 图片目录
        output_dir: 输出目录
        api_key: API Key
    """
    images_dir = Path(images_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 支持的图片格式
    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
    
    # 获取所有图片
    image_files = []
    for ext in image_extensions:
        image_files.extend(images_dir.glob(f"*{ext}"))
        image_files.extend(images_dir.glob(f"*{ext.upper()}"))
    
    print(f"找到 {len(image_files)} 张图片")
    
    # 分析每张图片
    results = []
    for i, image_path in enumerate(image_files, 1):
        print(f"\n[{i}/{len(image_files)}] 正在分析: {image_path.name}")
        
        try:
            analysis = analyze_image_with_qwen(image_path, api_key=api_key)
            
            # 保存结果
            output_file = output_dir / f"vlm_result_{image_path.stem}.md"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"# VLM 分析结果 - {image_path.name}\n\n")
                f.write(f"**原始图片**: {image_path}\n\n")
                f.write(f"**分析时间**: {os.popen('date /t').read().strip()} {os.popen('time /t').read().strip()}\n\n")
                f.write("---\n\n")
                f.write(analysis)
            
            print(f"分析完成，结果已保存到: {output_file}")
            results.append({
                "image": str(image_path),
                "output": str(output_file),
                "status": "success"
            })
            
        except Exception as e:
            print(f"分析失败: {e}")
            results.append({
                "image": str(image_path),
                "error": str(e),
                "status": "failed"
            })
    
    # 保存汇总
    summary_file = output_dir / "summary.json"
    import json
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n分析汇总已保存到: {summary_file}")
    return results


if __name__ == "__main__":
    import sys
    
    print("=" * 60)
    print("Qwen 3.5 Omni Flash 多模态图片分析工具")
    print("=" * 60)
    
    # 获取 API Key
    api_key = os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        print("\n⚠️  未设置 DASHSCOPE_API_KEY 环境变量")
        print("请获取 API Key: https://www.alibabacloud.com/help/zh/model-studio/get-api-key")
        print("\n设置方式:")
        print("  set DASHSCOPE_API_KEY=你的-api-key")
        print("  或者在脚本中直接传入 api_key 参数\n")
        api_key_input = input("请输入 API Key（直接回车跳过）: ").strip()
        if api_key_input:
            api_key = api_key_input
        else:
            print("\n没有 API Key，无法进行真实分析。")
            print("此脚本已创建，待配置 API Key 后可运行。")
            sys.exit(1)
    
    # 分析图片
    script_dir = Path(__file__).parent
    images_dir = script_dir / "../raw/images"
    output_dir = script_dir / "../raw/qwen_vlm_results"
    
    print(f"\n图片目录: {images_dir}")
    print(f"输出目录: {output_dir}\n")
    
    confirm = input("开始分析？(y/n): ").strip().lower()
    if confirm == "y":
        results = analyze_all_images(images_dir, output_dir, api_key=api_key)
        
        success_count = sum(1 for r in results if r["status"] == "success")
        print(f"\n分析完成！成功: {success_count}/{len(results)}")
    else:
        print("已取消")
