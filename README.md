# VLM Wiki

A full-modal personal knowledge base built on the Karpathy LLM Wiki concept.

## Core Philosophy

- **Multi-modal Intake**: Support comprehensive recording of images, videos, audio, and text
- **VLM + LLM**: Use Vision Language Models to understand images/videos, and Language Models to organize knowledge
- **Obsidian Display**: All content stored as Markdown, browseable directly in Obsidian
- **Continuous Compounding**: The wiki is a persistent, ever-compounding personal knowledge base

## Project Structure

```
.
├── raw/                    # Raw materials (read-only)
│   ├── images/            # Photos, screenshots
│   ├── videos/            # Videos + transcripts
│   ├── audio/             # Voice memos
│   ├── text/              # Text documents
│   └── diary/             # Daily diary
│
├── wiki/                   # Compiled knowledge articles
│   ├── index.md           # Global index
│   ├── log.md             # Operation log
│   ├── moments/           # Life moments
│   ├── people/            # People
│   ├── places/            # Places
│   ├── projects/          # Projects
│   ├── concepts/          # Concepts
│   ├── patterns/          # Discovered patterns
│   └── archives/          # Archives
│
├── .vlmwiki/              # Configuration
│   └── config.json        # Model configuration
│
├── references/            # Templates
│   ├── raw-template.md
│   ├── article-template.md
│   ├── archive-template.md
│   └── index-template.md
│
├── scripts/               # Analysis scripts
│   ├── video_extractor.py # Video frame extraction
│   ├── image_analyzer.py  # Image metadata analysis
│   ├── qwen_vlm_analyzer.py # Qwen multimodal analysis
│   └── run_analysis_now.py # Run analysis immediately
│
└── AGENTS.md              # Agent specifications (Chinese: AGENTS.zh.md)
```

## Quick Start

### 1. Configure Model

Edit `.vlmwiki/config.json` to choose your model provider:

```json
{
  "vlm": {
    "provider": "openai",      // openai | gemini | claude | ollama
    "model": "gpt-4o",
    "api_key_env": "OPENAI_API_KEY"
  }
}
```

Supports local models (Ollama) or cloud APIs (OpenAI, Gemini, Claude).

### 2. Add Materials

**Images**
```
Put photos in raw/images/YYYY-MM/
Then say: "analyze this image and update wiki"
```

**Videos**
```
Put videos in raw/videos/YYYY-MM/
VLM will extract keyframes, transcribe audio, generate descriptions
```

**Audio**
```
Put recordings in raw/audio/YYYY-MM/
Automatically transcribe and extract key information
```

**Diary/Text**
```
Write directly to raw/diary/ or raw/text/
```

### 3. Knowledge Organization

The Agent automatically:

1. **Analyze Materials**: Use VLM to understand image/video content
2. **Extract Information**: People, time, location, activities, emotions
3. **Update Wiki**: Create/update articles in appropriate categories
4. **Discover Patterns**: Identify recurring patterns (habits, relationships, places)

### 4. Browse with Obsidian

Open the project folder directly with Obsidian - all content is standard Markdown.

## Wiki Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| moments | Life milestones | Travel, parties, milestones |
| people | People in your life | Family, friends, colleagues |
| places | Places you've been | Cities, frequent visits |
| projects | Projects | Work projects, learning projects |
| concepts | Concepts & ideas | New knowledge, thoughts |
| patterns | Discovered patterns | Habits, mood cycles, time allocation |
| archives | Archives | Comprehensive analysis, memoirs |

## Trigger Commands

- `add image [path]` - Add image to wiki
- `add video [path]` - Add video to wiki
- `add audio [path]` - Add audio to wiki
- `what do I know about [topic]` - Query knowledge about a topic
- `analyze my patterns` - Analyze your life patterns
- `today in history` - Recall this day across years

## Differences from Karpathy LLM Wiki

| Feature | LLM Wiki | VLM Wiki |
|---------|----------|----------|
| Text processing | ✅ | ✅ |
| Image understanding | ❌ | ✅ |
| Video analysis | ❌ | ✅ |
| Audio processing | ❌ | ✅ |
| Multi-modal linking | ❌ | ✅ |
| Life pattern discovery | Basic | Deep |

## License

MIT
