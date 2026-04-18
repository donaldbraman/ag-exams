# Write Assist User Guide

This guide explains how to use **Write Assist** to draft, research, and edit legal academic writing.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following environment variables set (e.g., in a `.env` file):

```bash
# Required for Drafting/Editing
ANTHROPIC_API_KEY=sk-...    # For Claude
GOOGLE_API_KEY=AIza...      # For Gemini & Search
OPENAI_API_KEY=sk-...       # For ChatGPT

# Required for Web Research
GOOGLE_CSE_ID=0123...       # Google Custom Search Engine ID
```

### Installation

```bash
uv sync
```

---

## ✍️ Creating a New Draft

Use the `run` command to start the drafting pipeline.

### Basic Usage

```bash
uv run write-assist run \
  --topic "The intersection of AI and Copyright Law" \
  --type article
```

### With Research 🔍

Enable the autonomous research loop to have the agent verify facts and find new sources *before* writing.

```bash
uv run write-assist run \
  --topic "Recent circuit court splits on fair use" \
  --type article \
  --research-steps 5  # Allow up to 5 web search iterations
```

The agent will:
1.  Analyze the topic.
2.  Query Google Search for authoritative sources.
3.  Read snippets and findings.
4.  Integrate these "Research Findings" into the final draft.

### Using Local Sources (Cite-Assist) 📚

If you have a local Zotero database indexed with `cite-assist`, the tool will automatically query it.

```bash
uv run write-assist run \
  --topic "Originalism in constitutional interpretation" \
  --type article \
  --use-cite-assist
```

---

## 🛠️ Configuration options

| Option | Description | Default |
|--------|-------------|---------|
| `--model-claude` | Specific Claude model to use | `claude-opus-4-5-20251101` |
| `--model-gemini` | Specific Gemini model to use | `gemini-2.5-flash` |
| `--target-length` | Target word count | Appropriate for section |
| `--audience` | Target audience | Legal academics |

## 📊 Outputs

Artifacts are saved to the `runs/` directory, organized by date and topic.

- `drafts/`: Initial drafts from all 3 models.
- `edits/`: Refined versions.
- `judgments/`: Final rankings and score explanations.
- `final_result.md`: The recommended best version.
