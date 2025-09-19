# Git Metadata for Blog Posts

This feature adds content provenance information to blog posts, providing readers with cryptographic proof of creation and modification dates through Git commit history.

## What It Does

Each blog post now includes an expandable section at the bottom (just before the comments area) that displays:
- Creation date (from first Git commit)
- Last modified date
- Total number of revisions
- SHA-256 hash of the file content
- Recent commit history (last 3 changes)
- Direct link to the file's history on GitHub

## How It Works

The system consists of two Python modules:
1. `blog_git_utils.py` - Core utilities for extracting Git metadata
2. `mkdocs_blog_git_plugin.py` - Plugin that injects metadata into blog posts

The metadata is inserted between special HTML comment markers:
```html
<!-- BLOG_GIT_METADATA START -->
... metadata content ...
<!-- BLOG_GIT_METADATA END -->
```

## Usage

### Automatic Update
Run the provided shell script before building or deploying:
```bash
./update_git_metadata.sh
```

### Manual Update
Update all blog posts:
```bash
python3 mkdocs_blog_git_plugin.py
```

Update a specific post:
```bash
python3 mkdocs_blog_git_plugin.py --file docs/posts/your_post.md
```

### Options
- `--verbose` or `-v`: Enable detailed logging
- `--docs-dir`: Specify documentation directory (default: docs)
- `--repo-path`: Specify Git repository path (default: current directory)

## User Experience

The metadata section:
- Is subtle and non-intrusive (collapsed by default)
- Uses an expandable `<details>` element so users can view it if interested
- Includes explanatory text for casual users
- Matches the site's color scheme and styling
- Provides cryptographic proof (SHA-256 hash) for verification
- Links directly to GitHub for full history

## Why This Matters

1. **Transparency**: Readers can verify when content was created and last modified
2. **Trust**: Cryptographic hashes provide proof of document integrity
3. **Attribution**: Shows who contributed to the content
4. **Accountability**: Creates an audit trail of changes
5. **Historical Context**: Helps readers understand the evolution of ideas

## Workflow Integration

Recommended workflow:
1. Write/edit your blog post
2. Commit your changes to Git
3. Run `./update_git_metadata.sh` to update metadata
4. Build and deploy the site

The metadata will automatically reflect the Git history, ensuring accuracy and preventing manual date manipulation.

## Technical Notes

- Uses SHA-256 for file hashing (more secure than SHA-1)
- Fetches only recent commits (last 3) for performance
- Handles edge cases (no Git history, new files)
- Works with MkDocs Material theme
- Compatible with existing git-revision-date-localized plugin
