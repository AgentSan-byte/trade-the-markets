import requests
import os
import re
import subprocess
import tempfile
import shutil
from typing import List, Dict

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional for CI, required for local

MY_USERNAME = os.environ.get("MY_USERNAME")
MY_TOKEN = os.environ.get("MY_TOKEN")
MY_REPO = os.environ.get("MY_REPO")  # e.g. "username/repo"

if not MY_USERNAME:
    raise EnvironmentError("MY_USERNAME environment variable not set.")
if not MY_TOKEN:
    raise EnvironmentError("MY_TOKEN environment variable not set.")
if not MY_REPO:
    raise EnvironmentError("MY_REPO environment variable not set.")

def fetch_gists(username: str) -> List[Dict]:
    """Fetch all Gists for the user."""
    url = f"https://api.github.com/users/{username}/gists"
    headers = {"Authorization": f"token {MY_TOKEN}"}
    gists = []
    page = 1
    while True:
        resp = requests.get(url + f"?per_page=100&page={page}", headers=headers)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        gists.extend(data)
        page += 1
    return gists

def fetch_gist_content(gist_id: str) -> str:
    """Fetch the README.md content for a given Gist ID."""
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {MY_TOKEN}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    gist = resp.json()
    return gist["files"].get("README.md", {}).get("content", "")

def parse_tasks_from_readme(readme: str) -> List[str]:
    """Extract unchecked tasks from the Gist README.md."""
    return re.findall(r"- \[ \] (.+)", readme)

def filter_active_gists(gists: List[Dict]) -> List[Dict]:
    """Filter Gists to only those not marked as done/complete."""
    status_pattern = re.compile(r"^\\*\\*Status:\\*\\*\\s*([^\\n]+)", re.MULTILINE | re.IGNORECASE)
    active_gists = []
    for gist in gists:
        files = gist.get("files", {})
        readme = files.get("README.md", {}).get("content")
        if readme is None:
            readme = fetch_gist_content(gist["id"])
        if readme:
            match = status_pattern.search(readme)
            status = match.group(1).strip().lower() if match else ""
            if status not in ["done", "complete"]:
                active_gists.append({"id": gist["id"], "content": readme})
    return active_gists

def write_context_file(gist_contexts: List[Dict], filename: str = ".copilot-context.md"):
    """Write the Copilot context file from active Gists."""
    with open(filename, "w", encoding="utf-8") as f:
        for context in gist_contexts:
            f.write(f"# Gist: {context['id']}\n")
            f.write(context['content'])
            f.write("\n\n---\n\n")

def run_copilot_agent(task: str, context: str, output_dir: str):
    """Run Copilot CLI or fallback to Copilot Chat for code generation."""
    copilot_cli = shutil.which("copilot")
    if copilot_cli:
        # Use Copilot CLI if available
        prompt = f"{task}\nContext:\n{context}"
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write(prompt)
            tmp.flush()
            subprocess.run([copilot_cli, "generate", "--input", tmp.name, "--output", output_dir], check=True)
    else:
        print(f"Copilot CLI not found. Please use Copilot Chat in VS Code and load .copilot-context.md as custom context.")
        # Optionally, print the prompt for manual use
        print(f"Prompt Copilot with: {task}\nContext:\n{context}")

def update_gist_status_to_complete(gist_id: str, readme: str):
    """Update the Gist README status to complete using GitHub API."""
    new_readme = re.sub(r"(\*\*Status:\*\*\s*)([^\n]+)", r"\1complete", readme, flags=re.IGNORECASE)
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {MY_TOKEN}"}
    data = {"files": {"README.md": {"content": new_readme}}}
    resp = requests.patch(url, headers=headers, json=data)
    resp.raise_for_status()
    print(f"Updated Gist {gist_id} status to complete.")

def commit_and_push(branch: str, message: str):
    subprocess.run(["git", "checkout", "-b", branch], check=True)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push", "-u", "origin", branch], check=True)

def open_pull_request(branch: str, gist_id: str):
    subprocess.run(["gh", "pr", "create", "--fill", "--head", branch, "--title", f"Auto: Complete Gist {gist_id}", "--body", f"Automated PR for Gist {gist_id}"], check=True)

def main():
    gists = fetch_gists(MY_USERNAME)
    active_gists = filter_active_gists(gists)
    write_context_file(active_gists)
    print(f"Fetched and wrote {len(active_gists)} active Gists to .copilot-context.md")
    for gist in active_gists:
        gist_id = gist["id"]
        readme = gist["content"]
        tasks = parse_tasks_from_readme(readme)
        if not tasks:
            # If no unchecked tasks, mark as complete
            update_gist_status_to_complete(gist_id, readme)
            continue
        branch = f"feature/gist-{gist_id}-auto"
        os.makedirs(branch, exist_ok=True)
        for task in tasks:
            print(f"Running Copilot agent for Gist {gist_id} task: {task}")
            run_copilot_agent(task, readme, branch)
        commit_and_push(branch, f"Auto: Complete Gist {gist_id} tasks")
        open_pull_request(branch, gist_id)
        # After PR, optionally update Gist status
        update_gist_status_to_complete(gist_id, readme)

if __name__ == "__main__":
    main()
