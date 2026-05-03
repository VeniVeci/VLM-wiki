# Qwen 多模态分析使用说明

## 📋 前置准备

### 1. 获取 API Key

访问：https://www.alibabacloud.com/help/zh/model-studio/get-api-key

步骤：
1. 前往阿里云百炼控制台
2. 选择地域（推荐华北2-北京或新加坡）
3. 在左侧导航栏选择 API Key
4. 点击创建 API Key
5. 复制并保存 API Key（只显示一次！

### 2. 安装依赖

```bash
cd scripts
pip install openai
```

---

## 🚀 使用方法

### 方式一：环境变量（推荐）

```bash
# 设置环境变量
set DASHSCOPE_API_KEY=你的-api-key

# 运行分析
python qwen_vlm_analyzer.py
```

### 方式二：在代码中配置

复制 `.env.example` 为 `.env`，填入你的 API Key，然后修改脚本读取。

---

## 📊 输出结果

分析结果将保存在：`raw/qwen_vlm_results/`

- 每张图片对应一个 `.md` 文件
- 包含完整的模型分析结果
- 包含汇总 `summary.json`

---

## 🔧 脚本功能

`qwen_vlm_analyzer.py` 会：
1. 扫描 `raw/images/` 目录下所有图片
2. 使用 qwen3.5-omni-flash 模型分析
3. 保存分析结果（场景识别、视觉元素、内容描述、标签
4. 结果保存为 Markdown 文档

---

## 💡 提示

**注意**：实际调用需要 API 会消耗 token，请注意控制调用前请确认。
