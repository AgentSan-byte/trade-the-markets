# Gist Management Usage Guide

## Purpose
This guide explains how developers and AI agents can use the Gist management module to track, update, and close project tasks, ensuring transparent and collaborative development.

## Getting Started
1. **Set your GitHub personal access token:**
   - Store your token securely as an environment variable: `export GITHUB_TOKEN=your_token_here` (Linux/macOS) or `set GITHUB_TOKEN=your_token_here` (Windows).
2. **Initialize the GistManager in your code:**
   ```python
   from gist_management.gist_manager import GistManager
   import os
   manager = GistManager(os.environ["GITHUB_TOKEN"])
   ```

## Common Operations
- **Create a new Gist task:**
  ```python
  manager.create_gist(
      description="Implement trading strategy module",
      files={"task.md": "- [ ] Design\n- [ ] Implement\n- [ ] Test"},
      public=False,
      tags=["backend", "strategy"]
  )
  ```
- **Update a Gist:**
  ```python
  manager.update_gist(gist_id, files={"task.md": "- [x] Design\n- [ ] Implement\n- [ ] Test"})
  ```
- **Close a Gist:**
  ```python
  manager.close_gist(gist_id)
  ```
- **List Gists (optionally by tag):**
  ```python
  manager.list_gists(tag="backend")
  ```

## Human-in-the-Loop Development
- Developers can intervene at any time by creating, updating, or closing Gists to:
  - Add new tasks or design notes
  - Mark tasks as complete or update progress
  - Reference Gist IDs in code comments, PRs, and documentation
- All Gist operations are logged for audit and traceability.

## Best Practices
- Always keep Gist tasks up to date with project progress.
- Reference relevant Gist IDs in code and documentation for transparency.
- Never hardcode your GitHub token; use environment variables.

---
For more details, see `gist_management/gist_manager.py` and project documentation.
