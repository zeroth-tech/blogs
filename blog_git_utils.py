#!/usr/bin/env python3
"""
Git utilities for blog posts - provides functions for extracting Git metadata.
Simplified version of policy_utils adapted for blog use.
"""

import hashlib
import logging
import subprocess
from pathlib import Path
from typing import Dict, Optional, List, Any

# Configure logging
logger = logging.getLogger(__name__)


def setup_logging(level: str = "INFO") -> None:
    """Configure logging for blog scripts."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def compute_file_hash(file_path: Path) -> str:
    """
    Compute SHA-256 hash of file contents.
    
    Args:
        file_path: Path to the file
        
    Returns:
        SHA-256 hash as hex string
    """
    try:
        with open(file_path, 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        logger.error(f"File not found for hashing: {file_path}")
        return ""
    except Exception as e:
        logger.error(f"Error computing hash for {file_path}: {e}")
        return ""


def run_git_command(args: List[str], cwd: Path = Path(".")) -> Optional[str]:
    """
    Run a git command and return output.
    
    Args:
        args: Git command arguments (without 'git' prefix)
        cwd: Working directory for command
        
    Returns:
        Command output as string or None if failed
    """
    cmd = ["git"] + args
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.warning(f"Git command failed: {' '.join(cmd)}: {e.stderr}")
        return None
    except FileNotFoundError:
        logger.error("Git executable not found")
        return None


def get_github_url(file_path: Path, repo_path: Path = Path(".")) -> str:
    """
    Get GitHub blob URL for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        GitHub URL string or empty string if unavailable
    """
    try:
        # Get current commit hash
        result = run_git_command(["rev-parse", "HEAD"], repo_path)
        if not result:
            return ""
        current_commit = result.strip()
        
        # Get remote URL
        result = run_git_command(["config", "--get", "remote.origin.url"], repo_path)
        if not result:
            return ""
        remote_url = result.strip()
        
        # Convert SSH URL to HTTPS if needed
        if remote_url.startswith('git@github.com:'):
            remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
        
        # Remove .git suffix if present
        if remote_url.endswith('.git'):
            remote_url = remote_url[:-4]
        
        # Build blob URL
        relative_path = file_path.relative_to(repo_path)
        return f"{remote_url}/blob/{current_commit}/{relative_path}"
        
    except (ValueError, Exception) as e:
        logger.warning(f"Could not generate GitHub URL for {file_path}: {e}")
        return ""


def get_file_creation_date(file_path: Path, repo_path: Path = Path(".")) -> Optional[str]:
    """
    Get the creation date of a file from Git history.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        ISO date string or None if not found
    """
    relative_path = file_path.relative_to(repo_path)
    
    # Get the first commit that added this file
    output = run_git_command([
        "log", "--follow", "--reverse",
        "--pretty=format:%aI",
        "--", str(relative_path)
    ], repo_path)
    
    if output:
        lines = output.strip().split('\n')
        if lines and lines[0]:
            return lines[0]  # Return ISO format date
    
    return None


def is_frontmatter_only_change(commit_hash: str, file_path: Path, repo_path: Path = Path(".")) -> bool:
    """
    Check if a commit only changed the frontmatter (YAML header) of a file.
    
    Args:
        commit_hash: Git commit hash
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        True if only frontmatter was changed, False otherwise
    """
    relative_path = file_path.relative_to(repo_path)
    
    # Get the diff for this specific file in this commit
    output = run_git_command([
        "show", commit_hash,
        "--", str(relative_path)
    ], repo_path)
    
    if not output:
        return False
    
    lines = output.split('\n')
    in_diff = False
    
    # We need to track the line numbers to understand where we are in the file
    # Frontmatter is typically at the beginning of markdown files between --- markers
    
    for line in lines:
        # Look for the diff section with line numbers
        if line.startswith('@@'):
            in_diff = True
            continue
            
        if not in_diff:
            continue
            
        # Skip context lines (no + or - prefix)
        if not line.startswith(('+', '-')):
            continue
            
        # Skip the +++ and --- lines
        if line.startswith('+++') or line.startswith('---'):
            continue
            
        # Get the content without +/- prefix
        content = line[1:]
        
        # If there's any non-whitespace content and we can tell it's not in frontmatter,
        # then it's not frontmatter-only
        if content.strip():
            # Simple heuristic: if the line contains markdown content indicators
            # or is clearly not YAML frontmatter syntax, it's content
            stripped = content.strip()
            
            # Skip YAML frontmatter delimiters
            if stripped == '---':
                continue
                
            # Check if this looks like YAML frontmatter (key: value pairs, lists, etc.)
            # or markdown content
            if (
                # Markdown headers
                stripped.startswith('#') or
                # Markdown paragraphs (not indented YAML)
                (not stripped.startswith((' ', '-', 'categories:', 'tags:', 'date:', 'draft:', 'authors:', 'comments:')) and 
                 ':' not in stripped and
                 len(stripped) > 20)  # Likely prose, not YAML
            ):
                return False
    
    return True


def get_file_last_modified(file_path: Path, repo_path: Path = Path("."), exclude_frontmatter_only: bool = False) -> Optional[str]:
    """
    Get the last modified date of a file from Git history.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        exclude_frontmatter_only: If True, skip commits that only changed frontmatter
        
    Returns:
        ISO date string or None if not found
    """
    relative_path = file_path.relative_to(repo_path)
    
    if not exclude_frontmatter_only:
        # Original behavior - get the most recent commit
        output = run_git_command([
            "log", "-1",
            "--pretty=format:%aI",
            "--", str(relative_path)
        ], repo_path)
        
        if output:
            return output.strip()
        return None
    
    # Enhanced behavior - skip frontmatter-only changes
    # Get all commits for this file
    output = run_git_command([
        "log",
        "--pretty=format:%H|%aI",
        "--", str(relative_path)
    ], repo_path)
    
    if not output:
        return None
    
    for line in output.strip().split('\n'):
        if not line:
            continue
            
        parts = line.split('|', 1)
        if len(parts) != 2:
            continue
            
        commit_hash, date = parts
        
        # Check if this commit only changed frontmatter
        if not is_frontmatter_only_change(commit_hash, file_path, repo_path):
            return date
    
    # If all commits were frontmatter-only, return the first (creation) date
    first_line = output.strip().split('\n')[-1]
    if '|' in first_line:
        return first_line.split('|', 1)[1]
    
    return None


def get_recent_commits(file_path: Path, repo_path: Path = Path("."), limit: int = 5, exclude_frontmatter_only: bool = False) -> List[Dict[str, str]]:
    """
    Get recent Git commits for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        limit: Maximum number of commits to return
        exclude_frontmatter_only: If True, exclude commits that only changed frontmatter
        
    Returns:
        List of commit dictionaries with keys: hash, author, date, message
    """
    relative_path = file_path.relative_to(repo_path)
    
    # Get more commits than needed in case we need to filter out frontmatter-only ones
    fetch_limit = limit * 3 if exclude_frontmatter_only else limit
    
    output = run_git_command([
        "log", f"-{fetch_limit}", "--follow",
        "--pretty=format:%H|%an|%aI|%s",
        "--", str(relative_path)
    ], repo_path)
    
    if not output:
        return []
    
    commits = []
    for line in output.strip().split('\n'):
        if line:
            parts = line.split('|', 3)
            if len(parts) == 4:
                commit_hash = parts[0]
                
                # If excluding frontmatter-only changes, check if this commit qualifies
                if exclude_frontmatter_only and is_frontmatter_only_change(commit_hash, file_path, repo_path):
                    continue
                
                commits.append({
                    'hash': commit_hash[:7],  # Short hash
                    'author': parts[1],
                    'date': parts[2][:10],  # YYYY-MM-DD format
                    'message': parts[3]
                })
                
                # Stop once we have enough commits
                if len(commits) >= limit:
                    break
    
    return commits


def get_commit_count(file_path: Path, repo_path: Path = Path(".")) -> int:
    """
    Get the total number of commits for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        Number of commits
    """
    relative_path = file_path.relative_to(repo_path)
    
    output = run_git_command([
        "rev-list", "--count", "HEAD", "--", str(relative_path)
    ], repo_path)
    
    if output:
        try:
            return int(output.strip())
        except ValueError:
            pass
    
    return 0


def get_file_git_metadata(file_path: Path, repo_path: Path = Path("."), exclude_frontmatter_only: bool = False) -> Dict[str, Any]:
    """
    Get comprehensive Git metadata for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        exclude_frontmatter_only: If True, exclude frontmatter-only changes from last modified date and recent commits
        
    Returns:
        Dictionary containing all Git metadata
    """
    return {
        'file_hash': compute_file_hash(file_path),
        'github_url': get_github_url(file_path, repo_path),
        'created_date': get_file_creation_date(file_path, repo_path),
        'modified_date': get_file_last_modified(file_path, repo_path, exclude_frontmatter_only),
        'recent_commits': get_recent_commits(file_path, repo_path, limit=3, exclude_frontmatter_only=exclude_frontmatter_only),
        'total_commits': get_commit_count(file_path, repo_path),
        'file_path': str(file_path.relative_to(repo_path))
    }
