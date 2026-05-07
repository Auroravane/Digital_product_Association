import os
import sys
import json

# Add the parent 'scripts' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent_runner import AgentRunner

# Configuration
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DIRECTIVE_FILE = os.path.join(BASE_DIR, "specs", "directives", "latest_directive.json")
CPO_PROMPT_PATH = os.path.join(BASE_DIR, "Chief Executive Officer (CEO)", "CPO — Product Division", "Managing_Agent_CPO.md")
SCHEMA_PATH = os.path.join(BASE_DIR, "specs", "schemas", "PRD_Schema.json")
OUTPUT_PATH = os.path.join(BASE_DIR, "specs", "directives", "latest_prd.json")

def run_cpo_pipeline():
    print(f"--- Starting CPO Planning Pipeline ---")
    
    if not os.path.exists(DIRECTIVE_FILE):
        print(f"Error: Directive {DIRECTIVE_FILE} not found.")
        return

    with open(DIRECTIVE_FILE, 'r') as f:
        directive_data = f.read()

    print(f"Loading CPO Agent from: {CPO_PROMPT_PATH}")
    cpo = AgentRunner(CPO_PROMPT_PATH)

    print(f"Invoking Llama 3.3 70B for product planning...")
    
    # Load Schema for injection
    with open(SCHEMA_PATH, 'r') as s:
        schema_content = s.read()

    prompt_payload = f"""
STRATEGIC DIRECTIVE FROM CDO:
{directive_data}

### MANDATORY OUTPUT FORMAT:
You MUST output a valid JSON object matching this schema:
{schema_content}

Specify exact worker IDs from the company registry (e.g., Worker_SEO_Manager, Worker_Copywriter) inside the 'worker_assignments' object.
DO NOT include any conversational text. ONLY return the raw JSON object.
"""

    try:
        prd_json = cpo.call_nvidia_nim(prompt_payload)
        
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, 'w') as f:
            f.write(prd_json)
        
        print(f"Success! Technical PRD saved to {OUTPUT_PATH}")
        
    except Exception as e:
        print(f"CPO Pipeline Failed: {str(e)}")
        import sys
        sys.exit(1)

if __name__ == "__main__":
    run_cpo_pipeline()
