import os
import sys
import json

# Add the parent 'scripts' directory to sys.path so we can import agent_runner
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent_runner import AgentRunner

# Configuration
# Note: Using the exact em-dash '—' as found in the filesystem
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
INTEL_FILE = os.path.join(BASE_DIR, "intel_drops", "daily_intel.json")
CDO_PROMPT_PATH = os.path.join(BASE_DIR, "Chief Executive Officer (CEO)", "CDO — Data & Analytics Division", "Managing_Agent_CDO.md")
SCHEMA_PATH = os.path.join(BASE_DIR, "specs", "schemas", "Strategic_Directive_Schema.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "specs", "directives", "latest_directive.json")

def run_cdo_pipeline():
    print(f"--- Starting CDO Evaluation Pipeline ---")
    
    # 1. Load Intel
    if not os.path.exists(INTEL_FILE):
        print(f"Error: {INTEL_FILE} not found. Ingestion aborted.")
        return

    with open(INTEL_FILE, 'r') as f:
        intel_data = f.read()

    # 2. Initialize CDO Agent
    print(f"Loading CDO Agent from: {CDO_PROMPT_PATH}")
    cdo = AgentRunner(CDO_PROMPT_PATH)

    # 3. Call NVIDIA NIM (Llama 3.3) for strategic reasoning
    print(f"Invoking Llama 3.3 70B for strategic analysis...")
    
    # Load Schema for injection
    with open(SCHEMA_PATH, 'r') as s:
        schema_content = s.read()

    prompt_payload = f"""
INTEL PAYLOAD:
{intel_data}

### MANDATORY OUTPUT FORMAT:
You MUST output a valid JSON object matching this schema:
{schema_content}

DO NOT include any markdown formatting, headers, or conversational text.
ONLY return the raw JSON object.
"""

    try:
        directive_json = cdo.call_nvidia_nim(prompt_payload)
        
        # 4. Save Output
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, 'w') as f:
            f.write(directive_json)
        
        print(f"Success! Strategic Directive saved to {OUTPUT_PATH}")
        
    except Exception as e:
        print(f"Pipeline Failed: {str(e)}")

if __name__ == "__main__":
    run_cdo_pipeline()
