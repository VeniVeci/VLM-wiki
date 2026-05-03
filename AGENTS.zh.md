# VLM Wiki Agent

使用 VLM（视觉语言模型）和 LLM 构建和维护个人全模态知识库。管理不同媒体类型的目录，将它们编译成统一的 Wiki 文章。Wiki 随着时间不断积累。

**触发关键词**: `vlmwiki`, `添加素材`, `添加图片`, `添加视频`, `添加音频`, `多模态 wiki`, `全模态`, `记忆库`

> **模型说明**: 如果 `.vlmwiki/config.json` 中未配置多模态模型，将自动使用当前 AI IDE 内置的模型（如 Trae IDE 内置的 MiniMax-M2 等）。

## 核心理念

"VLM Wiki 是你生活的持久复合产物。"
"Wiki 由 VLM/LLM 编写和维护；人类阅读和反思。"

## 架构

三层结构，都在用户项目根目录下：

```
project/
├── raw/                    # 原始素材（只读）
│   ├── images/            # 照片、截图、图片
│   ├── videos/            # 视频文件（含字幕）
│   ├── audio/             # 语音备忘、录音
│   ├── text/              # 文本文档、笔记
│   └── diary/             # 日记
│
├── wiki/                  # 编译后的知识文章（VLM/LLM 维护）
│   ├── index.md          # 全局索引
│   ├── log.md            # 追加式操作日志
│   ├── moments/           # 人生时刻 & 里程碑
│   ├── people/            # 人物
│   ├── places/            # 地点
│   ├── projects/          # 项目
│   ├── concepts/         # 主题、想法、概念
│   ├── patterns/          # 发现的模式
│   └── archives/          # 归档
│
├── .vlmwiki/             # 配置
│   └── config.json       # 模型和设置配置
│
└── AGENTS.md             # 本文件
```

### 特殊文件

- **wiki/index.md** — 全局索引，每篇文章一行，按分类分组
- **wiki/log.md** — 追加式操作日志
- **.vlmwiki/config.json** — 模型配置（VLM、LLM、存储路径）

## 模型配置

`.vlmwiki/config.json` 定义使用的模型。如果未配置，将使用 AI IDE 内置模型。

```json
{
  "vlm": {
    "provider": "openai|gemini|claude|ollama|local|ide",
    "model": "gpt-4o|gemini-pro-vision|claude-3-sonnet|llava|mini-max",
    "api_key_env": "OPENAI_API_KEY|GEMINI_API_KEY|ANTHROPIC_API_KEY",
    "base_url": "http://localhost:11434 (用于 ollama)"
  },
  "llm": {
    "provider": "openai|anthropic|ollama|local|ide",
    "model": "gpt-4o|claude-3-sonnet|qwen2|mini-max",
    "api_key_env": "OPENAI_API_KEY|ANTHROPIC_API_KEY"
  },
  "storage": {
    "raw_base": "raw",
    "wiki_base": "wiki"
  }
}
```

## 初始化

首次使用时运行。检查 raw/ 和 wiki/ 结构，创建缺失的目录：

```
raw/images/, raw/videos/, raw/audio/, raw/text/, raw/diary/
wiki/moments/, wiki/people/, wiki/places/, wiki/projects/, wiki/concepts/, wiki/patterns/, wiki/archives/
.vlmwiki/config.json
wiki/index.md, wiki/log.md
```

## 素材摄入

### 图片摄入

1. **读取图片**: 使用 VLM 分析图片
2. **提取元数据**: 从文件名/EXIF 获取日期、位置（如果有）、人物、活动
3. **生成描述**: 图片内容的详细说明
4. **存储原始文件**: 保存到 `raw/images/YYYY-MM/`
5. **更新 wiki**:
   - 如果是人生重要时刻，添加到 `wiki/moments/`
   - 如果识别出人物，添加到相应的 `wiki/people/`
   - 如果有位置，添加到相应的 `wiki/places/`
   - 如果发现新模式，更新 `wiki/patterns/`

### 视频摄入

1. **提取帧**: 采样关键帧（开头、中间、结尾、场景切换处）
2. **转录**: 如果有音频，转录语音
3. **VLM 分析**: 描述关键视觉时刻
4. **存储原始文件**: 将帧 + 字幕保存到 `raw/videos/YYYY-MM/`
5. **生成摘要**: VLM 总结视频内容
6. **更新 wiki**: 创建时刻条目，关联相关人物/地点

### 音频摄入

1. **转录**: 将语音转换为文字
2. **分析内容**: 识别主题、情感、关键点
3. **存储原始文件**: 将音频 + 字幕保存到 `raw/audio/YYYY-MM/`
4. **生成摘要**: 提取关键信息
5. **更新 wiki**: 在相应分类中创建条目

### 文本/日记摄入

1. **解析内容**: 提取日期、活动、提到的人物、地点、主题
2. **存储原始文件**: 保存到 `raw/text/` 或 `raw/diary/`
3. **更新 wiki**: 按照 LLM Wiki 工作流程处理文本

## Wiki 文章格式

```yaml
---
title: 文章标题
type: moment | person | place | project | concept | pattern | archive
date: 2025-05-01
media:
  - type: image|video|audio
    src: ../../raw/images/2025-05/photo.jpg
    caption: 描述
tags:
  - 标签1
  - 标签2
related:
  - "[[人物/张三]]"
  - "[[地点/北京]]"
last_updated: 2025-05-01
summary: 一句话描述
---

# 文章标题

内容...
```

## 查询

搜索 wiki 并回答问题：

1. 读取 `wiki/index.md` 定位相关文章
2. 阅读这些文章并综合答案
3. 优先使用 wiki 内容而非训练知识
4. 使用 Obsidian 链接引用来源: `[[分类/文章]]`

## 模式发现

自动检测：
- **时间模式**（重复活动）
- **人物模式**（经常互动的人）
- **地点模式**（常去的地点）
- **情绪模式**（情绪趋势）
- **学习模式**（反复回顾的主题）

## 归档

当用户要求归档一个综合分析时：

1. 写入 `wiki/archives/YYYY-MM-DD-topic.md`
2. 在 `wiki/index.md` 中添加 [Archived] 前缀
3. 追加到 `wiki/log.md`

## 日志格式

```markdown
## [YYYY-MM-DD] ingest | 媒体类型 | 文章标题
- Media: image/video/audio
- Created: 新文章
- Updated: 级联更新的文章
```

## 约定

- 所有时间戳使用 ISO 格式 (YYYY-MM-DD)
- 媒体路径相对于 wiki/ 到 raw/
- 内部链接使用 Obsidian `[[]]` 语法
- 中文内容使用中文，英文内容使用英文
- 原始文件不可变（永不修改）
- 所有文章都有带必需字段的 frontmatter
