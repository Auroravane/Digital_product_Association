import os
import sys
import json
import base64
import requests

# Add the parent 'scripts' directory to sys.path so we can import agent_runner
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent_runner import AgentRunner

# Configuration
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Repo 1 (Agent 1 / Archilles) configuration
REPO_1_OWNER = "Auroravane"
REPO_1_NAME = "Authority-Blueprint"
REPORT_PATH = "reports/latest.md"

CEO_PROMPT_PATH = os.path.join(BASE_DIR, "Chief Executive Officer (CEO)", "Managing_Agent_CEO.md")
SCHEMA_PATH = os.path.join(BASE_DIR, "specs", "schemas", "Strategic_Directive_Schema.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "specs", "directives", "latest_directive.json")

def fetch_agent1_report(pat):
    """Fetch the latest report from Agent 1 via GitHub API."""
    url = f"https://api.github.com/repos/{REPO_1_OWNER}/{REPO_1_NAME}/contents/{REPORT_PATH}"
    headers = {"Authorization": f"token {pat}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch report from Agent 1: {response.status_code} - {response.text}")
    
    content = response.json()
    report_text = base64.b64decode(content['content']).decode('utf-8')
    return report_text

def run_ceo_pipeline():
    print(f"--- Starting CEO Ingestion Pipeline ---")
    
    pat = os.getenv("GH_PAT")
    if not pat:
        print("Error: GH_PAT environment variable not set. Cannot fetch from Agent 1.")
        return

    # 1. Load Intel from Agent 1 (GitHub)
    print("Fetching raw daily report from Agent 1 (Archilles)...")
    try:
        intel_data = fetch_agent1_report(pat)
        print("Successfully retrieved Agent 1 report.")
    except Exception as e:
        print(f"Ingestion aborted: {e}")
        return

    # 2. Initialize CEO Agent
    print(f"Loading CEO Agent from: {CEO_PROMPT_PATH}")
    ceo = AgentRunner(CEO_PROMPT_PATH)

    # 3. Call NVIDIA NIM (Llama 3.3 70B) for executive decision making
    print(f"Invoking Llama 3.3 70B for Executive Strategy...")
    
    # Load Schema for injection
    with open(SCHEMA_PATH, 'r') as s:
        schema_content = s.read()

    prompt_payload = f"""
AGENT 1 (ARCHILLES) DAILY REPORT:
{intel_data}

### MANDATORY OUTPUT FORMAT:
You MUST output a valid JSON object matching this schema:
{schema_content}

DO NOT include any markdown formatting, headers, or conversational text.
ONLY return the raw JSON object.
"""

    try:
        directive_json = ceo.call_nvidia_nim(prompt_payload)
        
        # 4. Save Output
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, 'w') as f:
            f.write(directive_json)
        
        print(f"Success! Executive Strategic Directive saved to {OUTPUT_PATH}")
        
    except Exception as e:
        print(f"CEO Pipeline Failed: {str(e)}")

if __name__ == "__main__":
    run_ceo_pipeline()
