from pathlib import Path


def add_disclaimer_to_vlm_docs():
    """给所有 VLM 分析文档添加免责声明"""
    vlm_dir = Path(__file__).parent / "../raw/vlm_analysis"
    
    disclaimer = """# ⚠️ 模拟分析（非真实 VLM 结果）

**注意**: 此文档内容是为了演示目的而创建的模拟分析，不是真实调用 qwen3.5-omni-flash 模型的结果。

真实分析请参考：[注意事项.md](注意事项.md)

---

"""
    
    # 处理所有图片和视频帧文档
    patterns = ["image_*.md", "video_frame_*.md"]
    
    for pattern in patterns:
        for doc_file in vlm_dir.glob(pattern):
            content = doc_file.read_text(encoding="utf-8")
            
            # 检查是否已经有免责声明
            if "⚠️ 模拟分析" in content:
                print(f"跳过（已有声明）: {doc_file.name}")
                continue
            
            # 添加免责声明
            # 同时修正一些格式问题
            new_content = disclaimer + content
            new_content = new_content.replace("文件名: `", "文件名**: `")
            new_content = new_content.replace("## 🤖 VLM 视觉分析", "## 🤖 模拟 VLM 视觉分析")
            
            doc_file.write_text(new_content, encoding="utf-8")
            print(f"已更新: {doc_file.name}")
    
    print("\n完成！")


if __name__ == "__main__":
    print("=" * 60)
    print("给 VLM 分析文档添加免责声明")
    print("=" * 60)
    add_disclaimer_to_vlm_docs()
