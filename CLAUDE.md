# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A personal knowledge-base website (ZhongPei's notes) built with **MkDocs + Material theme**, deployed to GitHub Pages at `https://zp1008611.github.io/`. Content covers operations research, machine learning, deep learning, reinforcement learning, LLMs, and LeetCode.

## Common Commands

```bash
# Install dependencies (use a Python virtual environment)
pip install -r requirements.txt

# Local development server (hot-reload at http://127.0.0.1:8000/)
mkdocs serve

# Build static site into site/
mkdocs build

# Deploy to GitHub Pages manually
mkdocs gh-deploy --force
```

> Deployment is also triggered automatically by GitHub Actions on every push to `main`.

## Adding New Content

1. Create a Markdown file under `docs/` in the appropriate section folder.
2. Register the file in the `nav:` section of `mkdocs.yml`.

If a page is not listed in `nav:`, it won't appear in the sidebar but is still accessible by direct URL.

## Architecture

```
mkdocs.yml          # Site config: nav, theme, plugins, markdown extensions
requirements.txt    # Python dependencies
docs/
  index.md          # Homepage
  stylesheets/
    extra.css       # Custom CSS (font: LXGW WenKai Screen, grid width, admonition sizing)
  javascripts/
    mathjax.js      # MathJax config (LaTeX support via $...$ and $$...$$)
    tablesort.js    # Sortable tables
    extra.js        # Misc JS
  <section>/        # Each content area (OROPT, ML, DL, RL, LLMs_RECORDS, LEETCODE, …)
    index.md        # Section landing page
    <topic>/
      README.md     # Topic page
```

**Content sections:**
- `OROPT/` — Operations research: exact methods (LP, IP, decomposition), metaheuristics, VRP/FJSP projects
- `ML/` — Machine learning: supervised learning, ensemble methods
- `DL/` — Deep learning: basics, GNN, NLP/forecasting projects
- `RL/` — Reinforcement learning: MDPs, policy/value methods, projects
- `LLMs_RECORDS/` — LLM technology notes: Agentic-RL, RAG, Agent
- `LEETCODE/` — Algorithm notes and problem solutions
- `MATH/` — Mathematics (graph theory, etc.)

## Key MkDocs Plugins

- `git-revision-date-localized` + `git-authors` — show last-modified date and commit authors per page (requires git history)
- `statistics` — page-count statistics
- `search` — Chinese-aware search via `jieba`

## Math Rendering

Both **KaTeX** (CSS only, for fast rendering) and **MathJax** (full JS) are loaded. Use standard LaTeX syntax: inline `$...$` or display `$$...$$`. The `pymdownx.arithmatex` extension with `generic: true` handles the Markdown side.

## Git Notes

On Windows, run this once to avoid case-sensitivity issues with file paths:

```bash
git config core.ignorecase false
```
