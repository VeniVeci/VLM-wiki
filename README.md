# VLM Wiki

基于 Karpathy LLM Wiki 思想的全模态个人记忆库。

## 核心理念

- **多模态摄入**: 支持图片、视频、音频、文本的全方位记录
- **VLM + LLM**: 用视觉语言模型理解图像视频，用语言模型整理知识
- **Obsidian 展示**: 所有内容以 Markdown 格式存储，直接用 Obsidian 浏览
- **持续积累**: Wiki 是一个持久的、不断复合的个人知识库

## 项目结构

```
.
├── raw/                    # 原始素材（只读）
│   ├── images/            # 照片、截图
│   ├── videos/            # 视频 + 字幕
│   ├── audio/             # 语音备忘
│   ├── text/              # 文本文档
│   └── diary/             # 日记
│
├── wiki/                   # 编译后的知识文章
│   ├── index.md           # 总索引
│   ├── log.md             # 操作日志
│   ├── moments/           # 人生时刻
│   ├── people/            # 人物
│   ├── places/            # 地点
│   ├── projects/          # 项目
│   ├── concepts/          # 概念
│   ├── patterns/          # 模式发现
│   └── archives/          # 归档
│
├── .vlmwiki/              # 配置
│   └── config.json        # 模型配置
│
├── references/            # 模板
│   ├── raw-template.md
│   ├── article-template.md
│   ├── archive-template.md
│   └── index-template.md
│
├── scripts/               # 分析脚本
│   ├── video_extractor.py # 视频抽帧
│   ├── image_analyzer.py  # 图片元数据分析
│   ├── qwen_vlm_analyzer.py # Qwen多模态分析
│   └── run_analysis_now.py # 立即分析脚本
│
└── AGENTS.md              # Agent 操作规范（中文版为 AGENTS.zh.md）
```

## 快速开始

### 1. 配置模型

编辑 `.vlmwiki/config.json`，选择你的模型 provider：

```json
{
  "vlm": {
    "provider": "openai",      // openai | gemini | claude | ollama
    "model": "gpt-4o",
    "api_key_env": "OPENAI_API_KEY"
  }
}
```

支持本地模型 (Ollama) 或云端 API (OpenAI, Gemini, Claude)。

### 2. 添加素材

**图片**
```
将照片放入 raw/images/YYYY-MM/
然后描述："帮我分析这张照片，更新 wiki"
```

**视频**
```
将视频放入 raw/videos/YYYY-MM/
VLM 会提取关键帧、转录音频、生成描述
```

**音频**
```
将录音放入 raw/audio/YYYY-MM/
自动转录并提取关键信息
```

**日记/文本**
```
直接写入 raw/diary/ 或 raw/text/
```

### 3. 知识整理

Agent 会自动：

1. **分析素材**: 用 VLM 理解图片/视频内容
2. **提取信息**: 人物、时间、地点、活动、情绪
3. **更新 Wiki**: 在对应分类下创建/更新文章
4. **发现模式**: 识别重复模式（习惯、人际、地点）

### 4. Obsidian 浏览

直接用 Obsidian 打开项目文件夹，所有内容都是标准 Markdown。

## Wiki 分类说明

| 分类 | 用途 | 示例 |
|------|------|------|
| moments | 人生重要时刻 | 旅行、聚会、里程碑 |
| people | 人物 | 家人、朋友、同事 |
| places | 地点 | 去过的城市、常去的地方 |
| projects | 项目 | 工作项目、学习项目 |
| concepts | 概念 | 学到的新知识、想法 |
| patterns | 模式发现 | 习惯、情绪周期、时间分配 |
| archives | 归档 | 综合分析、回忆录 |

## 触发指令

- `add image [path]` - 添加图片到 wiki
- `add video [path]` - 添加视频到 wiki
- `add audio [path]` - 添加音频到 wiki
- `what do I know about [topic]` - 查询关于某主题的知识
- `analyze my patterns` - 分析你的生活模式
- `today in history` - 回忆每年今日

## 与 Karpathy LLM Wiki 的区别

| 特性 | LLM Wiki | VLM Wiki |
|------|---------|----------|
| 文本处理 | ✅ | ✅ |
| 图片理解 | ❌ | ✅ |
| 视频分析 | ❌ | ✅ |
| 音频处理 | ❌ | ✅ |
| 多模态关联 | ❌ | ✅ |
| 生活模式发现 | 基础 | 深度 |

## License

MIT
