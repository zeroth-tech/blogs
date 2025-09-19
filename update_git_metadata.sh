#!/bin/bash
#
# Script to update Git metadata in blog posts
# This should be run before building/deploying the site
#

echo "📝 Updating Git metadata in blog posts..."

# Change to the script's directory
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    source .venv/bin/activate 2>/dev/null || true
fi

# Run the metadata injector
python3 mkdocs_blog_git_plugin.py "$@"

if [ $? -eq 0 ]; then
    echo "✅ Git metadata updated successfully!"
    echo ""
    echo "You can now:"
    echo "  1. Review the changes: git diff"
    echo "  2. Build the site: mkdocs build"
    echo "  3. Serve locally: mkdocs serve"
    echo "  4. Commit the changes: git add -A && git commit -m 'Update blog post metadata'"
else
    echo "❌ Failed to update Git metadata"
    exit 1
fi
