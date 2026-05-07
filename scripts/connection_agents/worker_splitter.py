import os
import sys
import json
import glob

# Add the parent 'scripts' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent_runner import AgentRunner

# Configuration
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PRD_FILE = os.path.join(BASE_DIR, "specs", "directives", "latest_prd.json")
BUILD_DIR = os.path.join(BASE_DIR, "build")

def find_role_file(worker_name):
    """Searches for the worker markdown file recursively in the Company directory."""
    # Worker names are typically like "Worker_SEO_Manager", but files might be "SEO_Manager.md"
    # or "Worker_SEO_Manager.md". We'll do a loose search.
    clean_name = worker_name.replace("Worker_", "")
    
    # Search in Roles first
    roles_dir = os.path.join(BASE_DIR, "Roles")
    if os.path.exists(roles_dir):
        for root, dirs, files in os.walk(roles_dir):
            for file in files:
                if clean_name.lower() in file.lower() and file.endswith(".md"):
                    return os.path.join(root, file)
                    
    # Search in CEO divisions
    ceo_dir = os.path.join(BASE_DIR, "Chief Executive Officer (CEO)")
    if os.path.exists(ceo_dir):
        for root, dirs, files in os.walk(ceo_dir):
            for file in files:
                if clean_name.lower() in file.lower() and file.endswith(".md"):
                    return os.path.join(root, file)
                    
    return None

def run_worker_splitter():
    print(f"--- Starting Worker Splitter Pipeline ---")
    
    if not os.path.exists(PRD_FILE):
        print(f"Error: PRD {PRD_FILE} not found.")
        return

    with open(PRD_FILE, 'r') as f:
        try:
            prd_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse PRD JSON - {str(e)}")
            return

    assignments = prd_data.get("worker_assignments", {})
    if not assignments:
        print("No worker assignments found in the PRD.")
        return
        
    os.makedirs(BUILD_DIR, exist_ok=True)
    print(f"Found {len(assignments)} worker assignments. Spawning agents...")

    for worker_name, task_details in assignments.items():
        print(f"\\n[{worker_name}] Locating role file...")
        role_path = find_role_file(worker_name)
        
        if not role_path:
            print(f"[{worker_name}] ERROR: Could not find a matching .md role file. Skipping.")
            continue
            
        print(f"[{worker_name}] Loaded identity from: {role_path}")
        
        # Prepare the execution payload with PRODUCTION MANDATE
        worker_payload = f"""
### PRODUCTION MANDATE — READ CAREFULLY ###
YOU ARE IN INDUSTRIAL PRODUCTION MODE. 
1. DO NOT PROVIDE INTRODUCTIONS, EXPLANATIONS, OR CONVERSATIONAL FILLER.
2. DO NOT TALK ABOUT THE WORK.
3. ONLY OUTPUT THE FINAL, RAW CONTENT OF THE PRODUCT ASSET.
4. IF THE TASK IS CODE, ONLY OUTPUT THE CODE BLOCKS.
5. IF THE TASK IS CONTENT, ONLY OUTPUT THE FINAL COPY.

PRODUCT NAME: {prd_data.get('product_name', 'Unknown')}
TASK DISPATCH FOR: {worker_name}

YOUR SPECIFIC INSTRUCTIONS:
{task_details.get('task_description', 'No description provided')}

CONTEXT:
{json.dumps(task_details.get('context_payload', {}), indent=2)}

REQUIRED OUTPUT FORMAT:
{task_details.get('required_output_format', 'Standard output')}
"""
        
        # Initialize and run
        runner = AgentRunner(role_path)
        print(f"[{worker_name}] Invoking Llama 3.3 for execution...")
        
        try:
            # We use Llama 3.3 70B for standard worker execution, which is the default in call_nvidia_nim
            # but wait, we changed the default to Kimi! We should specify llama here.
            output_content = runner.call_nvidia_nim(worker_payload, model="meta/llama-3.3-70b-instruct")
            
            # --- SMART EXTRACTION LOGIC ---
            file_ext = ".md"
            final_output = output_content
            
            # If the AI wrapped code in blocks, extract it and change extension
            if "```python" in output_content:
                final_output = output_content.split("```python")[1].split("```")[0].strip()
                file_ext = ".py"
            elif "```html" in output_content:
                final_output = output_content.split("```html")[1].split("```")[0].strip()
                file_ext = ".html"
            elif "```css" in output_content:
                final_output = output_content.split("```css")[1].split("```")[0].strip()
                file_ext = ".css"
            elif "```json" in output_content:
                final_output = output_content.split("```json")[1].split("```")[0].strip()
                file_ext = ".json"
            
            output_file = os.path.join(BUILD_DIR, f"{worker_name}_product{file_ext}")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_output)
                
            print(f"[{worker_name}] Success! PRODUCT ASSET saved to {output_file}")
            
        except Exception as e:
            print(f"[{worker_name}] Execution Failed: {str(e)}")

    print(f"\\n--- Worker Pipeline Complete ---")

if __name__ == "__main__":
    run_worker_splitter()
