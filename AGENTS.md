# VLM Wiki Agent

Build and maintain a personal full-modal knowledge base using VLMs (Vision Language Models) and LLMs. Manage multiple directories for different media types, compile them into unified wiki articles. The wiki compounds over time.

**Trigger keywords**: `vlmwiki`, `add media`, `add image`, `add video`, `add audio`, `multimodal wiki`, `全模态`, `记忆库`

> **Model Note**: If multi-modal models are not configured in `.vlmwiki/config.json`, the agent will automatically use the built-in models from the current AI IDE (e.g., Trae IDE's MiniMax-M2).

## Core Philosophy

"The VLM wiki is a persistent, compounding artifact of your life."
"The wiki writes and maintains itself with VLM/LLM; the human reads and reflects."

## Architecture

Three layers, all under the user's project root:

```
project/
├── raw/                    # Immutable source material (read-only)
│   ├── images/            # Photos, screenshots, images
│   ├── videos/            # Video files with transcripts
│   ├── audio/             # Voice memos, recordings
│   ├── text/              # Text documents, notes
│   └── diary/             # Daily diary entries
│
├── wiki/                  # Compiled knowledge articles (VLM/LLM maintained)
│   ├── index.md          # Global index
│   ├── log.md            # Append-only operation log
│   ├── moments/           # Life moments & milestones
│   ├── people/            # People in your life
│   ├── places/            # Places you've been
│   ├── projects/          # Projects you're working on
│   ├── concepts/          # Topics, ideas, concepts
│   ├── patterns/          # Discovered patterns
│   └── archives/          # Archived syntheses
│
├── .vlmwiki/             # Configuration
│   └── config.json       # Model and settings config
│
└── AGENTS.md             # This file
```

### Special Files

- **wiki/index.md** — Global index with one row per article, grouped by category
- **wiki/log.md** — Append-only operation log
- **.vlmwiki/config.json** — Model configuration (VLM, LLM, storage paths)

## Model Configuration

`.vlmwiki/config.json` defines which models to use. If not configured, AI IDE's built-in models will be used.

```json
{
  "vlm": {
    "provider": "openai|gemini|claude|ollama|local|ide",
    "model": "gpt-4o|gemini-pro-vision|claude-3-sonnet|llava|mini-max",
    "api_key_env": "OPENAI_API_KEY|GEMINI_API_KEY|ANTHROPIC_API_KEY",
    "base_url": "http://localhost:11434 (for ollama)"
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

## Initialization

Run on first use. Check for raw/ and wiki/ structure, create missing directories:

```
raw/images/, raw/videos/, raw/audio/, raw/text/, raw/diary/
wiki/moments/, wiki/people/, wiki/places/, wiki/projects/, wiki/concepts/, wiki/patterns/, wiki/archives/
.vlmwiki/config.json
wiki/index.md, wiki/log.md
```

## Media Ingest

### Image Ingest

1. **Read image**: Use VLM to analyze the image
2. **Extract metadata**: Date from filename/exif, location if available, people, activities
3. **Generate description**: Detailed caption of what's in the image
4. **Store raw**: Save to `raw/images/YYYY-MM/`
5. **Update wiki**:
   - Add to `wiki/moments/` if it's a life moment
   - Add to relevant `wiki/people/` if people are identified
   - Add to relevant `wiki/places/` if location identified
   - Update `wiki/patterns/` if new pattern discovered

### Video Ingest

1. **Extract frames**: Sample key frames (beginning, middle, end, scene changes)
2. **Transcribe**: If audio present, transcribe speech
3. **Analyze with VLM**: Describe key visual moments
4. **Store raw**: Save frames + transcript to `raw/videos/YYYY-MM/`
5. **Generate summary**: VLM summarizes the video content
6. **Update wiki**: Create moment entry, link to related people/places

### Audio Ingest

1. **Transcribe**: Convert speech to text
2. **Analyze content**: Identify topic, sentiment, key points
3. **Store raw**: Save audio + transcript to `raw/audio/YYYY-MM/`
4. **Generate summary**: Extract key information
5. **Update wiki**: Create entry in relevant category

### Text/Diary Ingest

1. **Parse content**: Extract date, activities, people mentioned, places, topics
2. **Store raw**: Save to `raw/text/` or `raw/diary/`
3. **Update wiki**: Follow the LLM Wiki workflow for text

## Wiki Article Format

```yaml
---
title: Article Title
type: moment | person | place | project | concept | pattern | archive
date: 2025-05-01
media:
  - type: image|video|audio
    src: ../../raw/images/2025-05/photo.jpg
    caption: Description
tags:
  - tag1
  - tag2
related:
  - "[[People/John]]"
  - "[[Places/Tokyo]]"
last_updated: 2025-05-01
summary: One-sentence description
---

# Article Title

Content...
```

## Query

Search the wiki and answer questions:

1. Read `wiki/index.md` to locate relevant articles
2. Read those articles and synthesize an answer
3. Prefer wiki content over training knowledge
4. Cite sources with Obsidian links: `[[Category/Article]]`

## Pattern Discovery

Automatically detect:
- **Time patterns** (recurring activities)
- **People patterns** (who you interact with often)
- **Location patterns** (places visited frequently)
- **Mood patterns** (emotional trends over time)
- **Learning patterns** (topics revisited)

## Archive

When user asks to archive a synthesis:

1. Write to `wiki/archives/YYYY-MM-DD-topic.md`
2. Update `wiki/index.md` with [Archived] prefix
3. Append to `wiki/log.md`

## Log Format

```markdown
## [YYYY-MM-DD] ingest | media type | article title
- Media: image/video/audio
- Created: new article
- Updated: cascaded articles
```

## Conventions

- All timestamps in ISO format (YYYY-MM-DD)
- Media paths relative from wiki/ to raw/
- Internal links use Obsidian `[[]]` syntax
- Chinese content in Chinese, English content in English
- Raw files are immutable (never modify)
- All articles have frontmatter with required fields
