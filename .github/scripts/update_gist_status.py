import os
import re
import requests
from github import Github

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ.get("GITHUB_REPOSITORY", "")
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO)

def update_gist_status(gist_id, status):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    gist = requests.get(url, headers=headers).json()
    desc = gist.get("description", "")
    new_desc = re.sub(r"\[status:.*?\]", f"[status: {status}]", desc)
    if "[status:" not in new_desc:
        new_desc += f" [status: {status}]"
    requests.patch(url, headers=headers, json={"description": new_desc})

def main():
    # Scan last 10 commits for GistID and status
    for commit in repo.get_commits()[:10]:
        msg = commit.commit.message
        match = re.search(r"GistID:([a-f0-9]+).*\bstatus: (in progress|done)\b", msg, re.I)
        if match:
            gist_id = match.group(1)
            status = match.group(2)
            update_gist_status(gist_id, status)

if __name__ == "__main__":
    main()
