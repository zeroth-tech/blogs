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


def get_file_last_modified(file_path: Path, repo_path: Path = Path(".")) -> Optional[str]:
    """
    Get the last modified date of a file from Git history.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        ISO date string or None if not found
    """
    relative_path = file_path.relative_to(repo_path)
    
    # Get the most recent commit for this file
    output = run_git_command([
        "log", "-1",
        "--pretty=format:%aI",
        "--", str(relative_path)
    ], repo_path)
    
    if output:
        return output.strip()
    
    return None


def get_recent_commits(file_path: Path, repo_path: Path = Path("."), limit: int = 5) -> List[Dict[str, str]]:
    """
    Get recent Git commits for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        limit: Maximum number of commits to return
        
    Returns:
        List of commit dictionaries with keys: hash, author, date, message
    """
    relative_path = file_path.relative_to(repo_path)
    
    output = run_git_command([
        "log", f"-{limit}", "--follow",
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
                commits.append({
                    'hash': parts[0][:7],  # Short hash
                    'author': parts[1],
                    'date': parts[2][:10],  # YYYY-MM-DD format
                    'message': parts[3]
                })
    
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


def get_file_git_metadata(file_path: Path, repo_path: Path = Path(".")) -> Dict[str, Any]:
    """
    Get comprehensive Git metadata for a file.
    
    Args:
        file_path: Path to the file
        repo_path: Path to git repository root
        
    Returns:
        Dictionary containing all Git metadata
    """
    return {
        'file_hash': compute_file_hash(file_path),
        'github_url': get_github_url(file_path, repo_path),
        'created_date': get_file_creation_date(file_path, repo_path),
        'modified_date': get_file_last_modified(file_path, repo_path),
        'recent_commits': get_recent_commits(file_path, repo_path, limit=3),
        'total_commits': get_commit_count(file_path, repo_path),
        'file_path': str(file_path.relative_to(repo_path))
    }
