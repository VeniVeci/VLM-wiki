import os
import sys
import base64
from pathlib import Path
from openai import OpenAI


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def analyze_single_image(image_path, api_key):
    """分析单张图片"""
    
    print("=" * 60)
    print("Qwen 3.5 Omni Flash - 单张图片分析")
    print("=" * 60)
    
    image_path = Path(image_path)
    print(f"\n图片路径: {image_path}")
    
    if not image_path.exists():
        print(f"❌ 图片不存在: {image_path}")
        return None
    
    # 初始化客户端
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    
    # 编码图片
    print(f"\n正在编码图片...")
    image_base64 = encode_image_to_base64(image_path)
    print(f"✓ 编码完成")
    
    # 构造提示词
    prompt = """请详细分析这张图片，包括：
1. 场景识别（这是什么场景、什么时间、什么地点）
2. 视觉元素描述（图片中有什么物体、人物、建筑、自然景观等）
3. 内容详细描述（用自然语言描述你看到的内容）
4. 情绪/氛围分析
5. 建议的标签（至少5个）

请用中文回答，格式清晰。"""
    
    print(f"\n正在调用 qwen3.5-omni-flash 模型...")
    
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
    
    result = completion.choices[0].message.content
    
    # 输出结果
    print("\n" + "=" * 60)
    print("📊 分析结果")
    print("=" * 60)
    print(result)
    print("\n" + "=" * 60)
    
    # 保存结果
    output_file = image_path.parent / f"{image_path.stem}_qwen_analysis.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Qwen 3.5 Omni Flash 分析结果\n\n")
        f.write(f"**图片**: {image_path.name}\n")
        f.write(f"**分析时间**: {os.popen('date /t').read().strip()} {os.popen('time /t').read().strip()}\n\n")
        f.write("---\n\n")
        f.write(result)
    
    print(f"\n✓ 结果已保存到: {output_file}")
    
    return result


if __name__ == "__main__":
    # 默认图片
    default_image = r"D:\MyProject\VLM-wiki\VLM-wiki\raw\images\微信图片_20260503182120_190_41.jpg"
    
    print("\n请输入你的阿里云百炼 API Key")
    print("获取地址: https://www.alibabacloud.com/help/zh/model-studio/get-api-key")
    print("\n注意: API Key 只在此会话中使用，不会保存\n")
    
    api_key = input("请粘贴 API Key: ").strip()
    
    if not api_key:
        print("❌ 没有输入 API Key，无法继续")
        sys.exit(1)
    
    analyze_single_image(default_image, api_key)
