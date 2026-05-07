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
ROLES_DIR = os.path.join(BASE_DIR, "Roles")

def get_available_roles():
    """Reads the Roles directory and returns a list of available role IDs."""
    if not os.path.exists(ROLES_DIR):
        return []
    # Convert "SEO_Manager.md" to "Worker_SEO_Manager" for the CPO to use
    roles = []
    for f in os.listdir(ROLES_DIR):
        if f.endswith(".md"):
            role_id = f"Worker_{f[:-3]}"
            roles.append(role_id)
    return roles

def run_cpo_pipeline():
    print(f"--- Starting CPO Planning Pipeline ---")
    
    # 1. Load available roles
    worker_registry = get_available_roles()
    registry_text = "\n".join([f"- {r}" for r in worker_registry])
    
    if not os.path.exists(DIRECTIVE_FILE):
        print(f"Error: Directive {DIRECTIVE_FILE} not found.")
        return

    with open(DIRECTIVE_FILE, 'r') as f:
        directive_data = f.read()

    print(f"Loading CPO Agent from: {CPO_PROMPT_PATH}")
    cpo = AgentRunner(CPO_PROMPT_PATH)

    print(f"Invoking Llama 3.3 70B for industrial product planning...")
    
    # Load Schema for injection
    with open(SCHEMA_PATH, 'r') as s:
        schema_content = s.read()

    prompt_payload = f"""
[CONTEXT]: You are the Chief Product Officer (CPO). Your task is to break down the CEO's Strategic Directive into a high-fidelity PRODUCTION PRD.

[AVAILABLE WORKFORCE REGISTRY]:
You MUST hire workers ONLY from this list. Use the EXACT ID shown:
{registry_text}

[STRICT PRODUCTION RULES]:
1. DO NOT assign tasks to "Managers" (CMO, CTO, COO) if an "Execution Worker" (Engineer, Writer, Designer) is available.
2. Every 'task_description' MUST be a command to build a RAW ASSET (e.g., "Write the Meta Tags", "Develop the API endpoint", "Write the Waitlist Copy").
3. Every 'required_output_format' MUST be a file extension (e.g., ".py", ".md", ".html").
4. WE DO NOT WANT REPORTS. WE WANT SHIPPABLE PRODUCTS.

[CEO DIRECTIVE]:
{directive_data}

[JSON SCHEMA FOR YOUR OUTPUT]:
{schema_content}

ONLY return the raw JSON object. NO CONVERSATIONAL FILLER.
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
