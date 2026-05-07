import os
import base64
import requests
from github_IMPORTANT import GH_PAT

# --- CONFIGURATION ---
REPO_OWNER = "Auroravane"
REPO_NAME = "Digital_product_Association"
SOURCE_DIR = "."

def upload_file(local_path, repo_path):
    """Uploads a single file to GitHub via API."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{repo_path}"
    headers = {
        "Authorization": f"token {GH_PAT}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Read and encode file content
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf-8")

    # Check if file exists to get SHA (for updates)
    res = requests.get(url, headers=headers)
    sha = res.json().get("sha") if res.status_code == 200 else None

    data = {
        "message": f"autobot: Uploading {repo_path}",
        "content": content,
        "branch": "main"
    }
    if sha:
        data["sha"] = sha

    response = requests.put(url, headers=headers, json=data)
    if response.status_code in [200, 201]:
        print(f"✅ Uploaded: {repo_path}")
    else:
        print(f"❌ Failed {repo_path}: {response.status_code} - {response.text}")

def main():
    print(f"🚀 Starting Upload to {REPO_OWNER}/{REPO_NAME}...")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory {SOURCE_DIR} not found.")
        return

    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file in ["github_IMPORTANT.py", "uploader.py", ".env"]:
                continue
            local_path = os.path.join(root, file)
            # Create the path relative to the SOURCE_DIR for GitHub
            repo_path = os.path.relpath(local_path, SOURCE_DIR).replace("\\", "/")
            upload_file(local_path, repo_path)

    print("\n🏁 Upload process complete.")

if __name__ == "__main__":
    main()
