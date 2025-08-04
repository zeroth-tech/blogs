# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a technical blog built with MkDocs Material, hosted on GitHub Pages. The blog focuses on blockchain, cryptography, digital identity, and distributed systems topics.

## Essential Commands

### Local Development
```bash
# Install dependencies (only needed once)
pip install mkdocs-material

# Serve locally with hot reload
mkdocs serve

# Build static site
mkdocs build
```

### Deployment
```bash
# Deploy to GitHub Pages (CI/CD handles this automatically on push to main)
mkdocs gh-deploy --force
```

## Architecture & Key Files

### Content Structure
- **Blog posts**: `/docs/posts/` - All blog articles in Markdown format
- **Main config**: `mkdocs.yml` - Site configuration, navigation, plugins
- **Homepage**: `/docs/index.md` - Simple landing page
- **Built site**: `/site/` - Generated static files (git-ignored)

### Customizations
- **Templates**: `/overrides/` - Custom HTML templates for git revision dates
- **Styling**: `/docs/stylesheets/` - Custom CSS for code wrapping and branding
- **JavaScript**: `/docs/javascripts/mathjax.js` - LaTeX math rendering support

### CI/CD
- **GitHub Actions**: `.github/workflows/ci.yml` - Automated build and deploy pipeline
- Triggers on push to main branch
- Caches dependencies for faster builds
- Deploys to GitHub Pages automatically

## Writing Blog Posts

Blog posts require YAML frontmatter:
```yaml
---
authors:
  - author_name
date: YYYY-MM-DD
categories:
  - Category Name
tags:
  - tag1
  - tag2
comments: true  # Enable Giscus comments
---
```

### Supported Features
- Mermaid diagrams
- LaTeX math via MathJax
- Code syntax highlighting
- Custom admonitions
- DrawIO diagrams (save as .drawio.svg)

## Important Notes

1. **No test suite** - This is a documentation site, not an application
2. **Automated deployment** - Changes to main branch auto-deploy via GitHub Actions
3. **Git revision dates** - Automatically tracked and displayed on posts
4. **Comments** - Giscus integration requires `comments: true` in frontmatter
5. **License** - GNU GPL v3.0 - ensure compatibility when adding content