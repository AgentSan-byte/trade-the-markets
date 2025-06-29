import os
from gist_management.gist_manager import GistManager
import re

GIST_FOLDER = os.path.join(os.path.dirname(__file__), 'gists')
MODULES = [
    'backend', 'frontend', 'wallet_integration', 'ai_agents',
    'trading_strategies', 'journaling', 'dashboard', 'gist_management', 'docs'
]

def get_module_from_description(description):
    # Look for [tags: ...] in the description
    match = re.search(r'\[tags: ([^\]]+)\]', description)
    if match:
        tags = [tag.strip() for tag in match.group(1).split(',')]
        for tag in tags:
            if tag in MODULES:
                return tag
    return 'docs'  # Default if no module tag found

def sync_gists_to_folders(github_token):
    manager = GistManager(github_token)
    gists = manager.list_gists()
    for gist in gists:
        module = get_module_from_description(gist.get('description', ''))
        folder = os.path.join(GIST_FOLDER, module)
        os.makedirs(folder, exist_ok=True)
        for filename, fileinfo in gist['files'].items():
            local_path = os.path.join(folder, f"{gist['id']}_{filename}")
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(fileinfo['content'])
    print(f"Synced {len(gists)} gists into organized folders.")

if __name__ == "__main__":
    import sys
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("Set GITHUB_TOKEN environment variable.")
        sys.exit(1)
    sync_gists_to_folders(token)
