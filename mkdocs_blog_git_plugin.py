#!/usr/bin/env python3
"""
MkDocs Blog Git Metadata Plugin
Injects Git metadata into blog posts between special markers.
"""

import argparse
import logging
import re
from pathlib import Path
from typing import List, Optional, Dict, Any

from blog_git_utils import (
    setup_logging,
    get_file_git_metadata,
)

# Configure logger
logger = logging.getLogger(__name__)


class BlogGitInjector:
    def __init__(self, docs_dir: str = "docs", repo_path: str = ".", exclude_frontmatter_only: bool = True):
        """
        Initialize the blog git metadata injector.
        
        Args:
            docs_dir: Documentation directory path
            repo_path: Git repository root path
            exclude_frontmatter_only: If True, exclude frontmatter-only changes from last modified date
        """
        self.docs_dir = Path(docs_dir)
        self.repo_path = Path(repo_path)
        self.exclude_frontmatter_only = exclude_frontmatter_only
        self.metadata_start = "<!-- BLOG_GIT_METADATA START -->"
        self.metadata_end = "<!-- BLOG_GIT_METADATA END -->"
        
    def format_metadata_html(self, metadata: Dict[str, Any]) -> str:
        """
        Format Git metadata as expandable HTML.
        
        Args:
            metadata: Dictionary containing git metadata
            
        Returns:
            Formatted HTML string
        """
        if not metadata.get('recent_commits'):
            return "No Git history available for this post."
        
        # Format creation and modification dates
        created = metadata.get('created_date', '').split('T')[0] if metadata.get('created_date') else 'Unknown'
        modified = metadata.get('modified_date', '').split('T')[0] if metadata.get('modified_date') else 'Unknown'
        
        # Build the HTML content
        html = f"""
<div class="blog-git-metadata" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--md-default-fg-color--lightest);">
  <details style="background: var(--md-code-bg-color); padding: 0.5rem 1rem; border-radius: 0.2rem;">
    <summary style="cursor: pointer; font-weight: 500; color: var(--md-default-fg-color--light);">
      📝 Content Provenance
    </summary>
    <div style="margin-top: 1rem; font-size: 0.9em;">
      <p style="margin: 0.5rem 0;"><strong>Created:</strong> {created}</p>
      <p style="margin: 0.5rem 0;"><strong>Last Modified:</strong> {modified}</p>
      <p style="margin: 0.5rem 0;"><strong>Total Revisions:</strong> {metadata.get('total_commits', 0)}</p>
      <p style="margin: 0.5rem 0;"><strong>File SHA-256:</strong> <code style="font-size: 0.85em;">{metadata.get('file_hash', '')[:16]}...</code></p>
      
      <div style="margin-top: 1rem;">
        <p style="margin: 0.5rem 0; font-weight: 500;">Recent Changes:</p>
        <table style="width: 100%; font-size: 0.85em; margin-top: 0.5rem;">
          <thead>
            <tr style="border-bottom: 1px solid var(--md-default-fg-color--lightest);">
              <th style="text-align: left; padding: 0.25rem;">Date</th>
              <th style="text-align: left; padding: 0.25rem;">Author</th>
              <th style="text-align: left; padding: 0.25rem;">Change</th>
            </tr>
          </thead>
          <tbody>
"""
        
        # Add recent commits
        for commit in metadata.get('recent_commits', []):
            message = commit['message'].replace('|', '\\|')
            # Truncate long messages
            if len(message) > 50:
                message = message[:47] + '...'
            html += f"""            <tr>
              <td style="padding: 0.25rem;">{commit['date']}</td>
              <td style="padding: 0.25rem;">{commit['author']}</td>
              <td style="padding: 0.25rem;">{message}</td>
            </tr>
"""
        
        html += """          </tbody>
        </table>
      </div>
"""
        
        # Add GitHub link if available
        if metadata.get('github_url'):
            html += f"""      
      <p style="margin-top: 1rem; margin-bottom: 0;">
        <a href="{metadata['github_url']}" target="_blank" style="color: var(--md-primary-fg-color); text-decoration: none;">
          View Full History on GitHub →
        </a>
      </p>
"""
        
        html += """    </div>
  </details>
  
  <div style="margin-top: 0.5rem; font-size: 0.8em; color: var(--md-default-fg-color--lighter);">
    <p style="margin: 0;">
      <em>This metadata provides cryptographic proof of this document's creation and modification history. 
      The SHA-256 hash can be used to verify the document's integrity, while the Git history shows its evolution over time.</em>
    </p>
  </div>
</div>
"""
        
        return html
    
    def inject_metadata(self, file_path: Path) -> tuple[bool, str]:
        """
        Inject Git metadata into a blog post.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Tuple of (success, message)
        """
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if markers exist
            has_markers = self.metadata_start in content and self.metadata_end in content
            
            # Get file metadata
            metadata = get_file_git_metadata(file_path, self.repo_path, self.exclude_frontmatter_only)
            
            # Format metadata
            metadata_html = self.format_metadata_html(metadata)
            
            if has_markers:
                # Replace content between markers
                pattern = re.compile(
                    f"{re.escape(self.metadata_start)}.*?{re.escape(self.metadata_end)}",
                    re.DOTALL
                )
                
                new_content = pattern.sub(
                    f"{self.metadata_start}\n{metadata_html}\n{self.metadata_end}",
                    content
                )
            else:
                # Add markers before comments section if it exists
                # Look for the comments: true frontmatter to know this is a blog post
                if 'comments: true' not in content:
                    return False, "not a blog post (no comments: true)"
                
                # Find where to insert - ideally just before any existing comment markers
                # or at the end of the content
                lines = content.split('\n')
                insert_position = len(lines)
                
                # Look for common end-of-content patterns
                for i in range(len(lines) - 1, -1, -1):
                    line = lines[i].strip()
                    # Look for giscus/comment scripts or end of content
                    if 'giscus' in line.lower() or '{% if page.meta.comments %}' in line:
                        insert_position = i
                        break
                    # Also check for the end of actual content (before trailing newlines)
                    if line and not line.startswith('<!--') and not line.startswith('<script'):
                        insert_position = i + 1
                        break
                
                # Insert the metadata section
                metadata_section = f"\n{self.metadata_start}\n{metadata_html}\n{self.metadata_end}\n"
                lines.insert(insert_position, metadata_section)
                new_content = '\n'.join(lines)
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            commits = len(metadata.get('recent_commits', []))
            return True, f"{commits} commits, hash: {metadata.get('file_hash', '')[:8]}"
            
        except Exception as e:
            logger.error(f"Error processing {file_path}: {e}")
            return False, f"error: {e}"
    
    def process_blog_posts(self) -> tuple[int, int, int]:
        """
        Process all blog posts in the posts directory.
        
        Returns:
            Tuple of (updated_count, skipped_count, error_count)
        """
        updated_count = 0
        skipped_count = 0
        error_count = 0
        
        # Find all markdown files in the posts directory
        posts_dir = self.docs_dir / "posts"
        if not posts_dir.exists():
            logger.error(f"Posts directory not found: {posts_dir}")
            return 0, 0, 1
        
        md_files = list(posts_dir.glob("*.md"))
        
        logger.info(f"Found {len(md_files)} blog posts")
        
        for md_file in md_files:
            logger.debug(f"Processing: {md_file}")
            
            success, message = self.inject_metadata(md_file)
            
            if success:
                logger.info(f"✅ Updated: {md_file.name} ({message})")
                updated_count += 1
            elif "error" in message:
                logger.error(f"❌ Error: {md_file.name} - {message}")
                error_count += 1
            else:
                logger.debug(f"⏭️  Skipped: {md_file.name} ({message})")
                skipped_count += 1
        
        return updated_count, skipped_count, error_count


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Inject Git metadata into blog posts'
    )
    parser.add_argument(
        '--docs-dir',
        default='docs',
        help='Documentation directory (default: docs)'
    )
    parser.add_argument(
        '--repo-path',
        default='.',
        help='Git repository path (default: current directory)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--file',
        help='Process a single file instead of all posts'
    )
    parser.add_argument(
        '--remove',
        action='store_true',
        help='Remove metadata sections instead of adding them'
    )
    parser.add_argument(
        '--include-frontmatter',
        action='store_true',
        help='Include frontmatter-only changes in last modified date (default: exclude them)'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging("DEBUG" if args.verbose else "INFO")
    
    # Create injector
    injector = BlogGitInjector(
        docs_dir=args.docs_dir,
        repo_path=args.repo_path,
        exclude_frontmatter_only=not args.include_frontmatter
    )
    
    # Process files
    if args.file:
        # Single file mode
        file_path = Path(args.file)
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            return 1
            
        success, message = injector.inject_metadata(file_path)
        if success:
            print(f"✅ Updated: {file_path} ({message})")
            return 0
        else:
            print(f"❌ Failed: {file_path} - {message}")
            return 1
    else:
        # Process all blog posts
        print("📝 Injecting Git metadata into blog posts...")
        updated, skipped, errors = injector.process_blog_posts()
        
        # Summary
        print(f"\n📊 Summary:")
        print(f"  ✅ Updated: {updated} posts")
        print(f"  ⏭️  Skipped: {skipped} posts")
        if errors > 0:
            print(f"  ❌ Errors: {errors} posts")
            return 1
        
        return 0


if __name__ == "__main__":
    try:
        exit(main())
    except KeyboardInterrupt:
        print("\n⚠️  Operation interrupted by user")
        exit(130)
    except Exception as e:
        logger.exception("Unexpected error")
        print(f"\n❌ Failed with unexpected error: {type(e).__name__}: {e}")
        exit(1)
