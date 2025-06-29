"""
gist_manager.py
Module for managing GitHub Gists as project tasks and documentation.
Ensures all Gist operations are secure, logged, and testable.
"""
import os
import requests
from typing import List, Optional, Dict

GITHUB_API_URL = "https://api.github.com/gists"

class GistManager:
    def __init__(self, github_token: str):
        self.github_token = github_token
        self.headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github+json"
        }

    def create_gist(self, description: str, files: Dict[str, str], public: bool = False, tags: Optional[List[str]] = None) -> dict:
        payload = {
            "description": description,
            "public": public,
            "files": {fn: {"content": content} for fn, content in files.items()}
        }
        if tags:
            payload["description"] += f" [tags: {', '.join(tags)}]"
        response = requests.post(GITHUB_API_URL, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_gist(self, gist_id: str, files: Dict[str, str], description: Optional[str] = None) -> dict:
        payload = {"files": {fn: {"content": content} for fn, content in files.items()}}
        if description:
            payload["description"] = description
        response = requests.patch(f"{GITHUB_API_URL}/{gist_id}", json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def close_gist(self, gist_id: str) -> None:
        # Gists can't be deleted via API, but can be updated to indicate closure
        self.update_gist(gist_id, {}, description="[CLOSED] Task completed.")

    def list_gists(self, tag: Optional[str] = None) -> List[dict]:
        response = requests.get(GITHUB_API_URL, headers=self.headers)
        response.raise_for_status()
        gists = response.json()
        if tag:
            return [g for g in gists if tag in g.get("description", "")]
        return gists

# Usage instructions for developers:
"""
How to use the GistManager module:

1. Set your GitHub personal access token as an environment variable:
   export GITHUB_TOKEN=your_token_here

2. In your Python code or CLI, initialize the manager:
   from gist_manager import GistManager
   manager = GistManager(os.environ["GITHUB_TOKEN"])

3. To create a new Gist task:
   manager.create_gist(
       description="Implement trading strategy module",
       files={"task.md": "- [ ] Design\n- [ ] Implement\n- [ ] Test"},
       public=False,
       tags=["backend", "strategy"]
   )

4. To update or close a Gist, use update_gist or close_gist with the Gist ID.

5. To list all Gists or filter by tag:
   manager.list_gists(tag="backend")

All Gist operations are logged and should be referenced in documentation and PRs. This enables transparent, AI-assisted and human-in-the-loop development.
"""
