"""
Reusable script to use Copilot agent for task breakdown on a single active (not done/complete) Gist.
- Fetches all Gists for the user.
- Selects the first Gist that is not marked as done/complete.
- Uses Copilot agent (CLI or manual prompt) to generate a task breakdown for that Gist's README.
"""
import os
import requests
import re
import tempfile
import shutil
import subprocess
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("MY_TOKEN")
GITHUB_USER = os.getenv("MY_USERNAME")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}


def get_active_gist():
    url = f"https://api.github.com/users/{GITHUB_USER}/gists"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        gists = resp.json()
    except Exception as e:
        print(f"Error fetching gists: {e}")
        return None
    for gist in gists:
        desc = gist.get("description", "")
        # Check for [status: done] or [status: complete] in description
        if not re.search(r"\[status:\s*(done|complete)\]", desc, re.I):
            return gist
    return None


def get_gist_readme(gist):
    files = gist.get("files", {})
    readme = files.get("README.md", {}).get("content")
    if readme:
        return readme
    # Fallback: fetch full gist content
    url = f"https://api.github.com/gists/{gist['id']}"
    try:
        resp = requests.get(url, headers=HEADERS)
        resp.raise_for_status()
        gist_data = resp.json()
        return gist_data["files"].get("README.md", {}).get("content", "")
    except Exception as e:
        print(f"Error fetching README.md for gist {gist['id']}: {e}")
        return ""


def run_copilot_task_breakdown(gist_id, readme):
    if not readme:
        print(f"No README.md found for Gist {gist_id}. Cannot generate task breakdown.")
        return
    prompt = f"""
You are an expert project manager. Break down the following Gist into actionable development tasks, using a checklist format. Only include tasks that are not yet completed. Gist ID: {gist_id}\n\nREADME:\n{readme}\n"""
    copilot_cli = shutil.which("copilot")
    if copilot_cli:
        with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
            tmp.write(prompt)
            tmp.flush()
            try:
                subprocess.run([copilot_cli, "generate", "--input", tmp.name], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Copilot CLI failed: {e}")
    else:
        print("Copilot CLI not found. Use the following prompt in Copilot Chat:")
        print(prompt)


def main():
    gist = get_active_gist()
    if not gist:
        print("No active (not done/complete) Gist found.")
        return
    readme = get_gist_readme(gist)
    print(f"Using Gist: {gist['id']} - {gist.get('description', '')}")
    run_copilot_task_breakdown(gist['id'], readme)

if __name__ == "__main__":
    main()
