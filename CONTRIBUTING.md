# Contributing to VLM Wiki

Thank you for your interest in contributing to VLM Wiki! This document provides guidelines and instructions for contributing.

## Ways to Contribute

### 1. Report Issues
- Search existing issues before creating a new one
- Use issue templates when available
- Include clear titles and detailed descriptions
- Add labels appropriately

### 2. Submit Pull Requests
- Fork the repository
- Create a feature branch: `git checkout -b feature/your-feature-name`
- Make your changes
- Write clear commit messages
- Submit a pull request to the `main` branch

### 3. Improve Documentation
- Fix typos or grammar errors
- Translate documentation to other languages
- Add examples or tutorials
- Improve clarity of existing docs

### 4. Code Contributions
- Follow the existing code style
- Add comments for complex logic
- Update relevant documentation
- Ensure tests pass (if applicable)

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/VLM-wiki.git
cd VLM-wiki

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r scripts/requirements.txt

# Set up environment variables
cp scripts/.env.example .env
# Edit .env with your API keys
```

## Project Structure

```
VLM-wiki/
├── raw/                    # Raw materials (read-only)
│   ├── images/            # Photos, screenshots
│   ├── videos/            # Videos
│   ├── audio/             # Voice memos
│   ├── text/              # Text documents
│   └── diary/             # Daily diary
│
├── wiki/                   # Compiled knowledge articles
│   ├── index.md           # Global index
│   ├── moments/           # Life moments
│   ├── people/            # People
│   ├── places/            # Places
│   └── ...
│
├── scripts/               # Analysis scripts
│   ├── video_extractor.py
│   ├── image_analyzer.py
│   └── qwen_vlm_analyzer.py
│
└── .vlmwiki/             # Configuration
```

## Code Style

- Use meaningful variable and function names
- Add docstrings for functions
- Keep functions focused and small
- Handle errors gracefully

## Testing

Before submitting:
```bash
# Run your changes locally
python scripts/run_analysis_now.py
```

## Questions?

- Open an issue for questions
- Join discussions in GitHub Issues

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
