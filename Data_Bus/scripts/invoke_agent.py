import argparse
import json
import os
import requests
import sys

def extract_json_from_text(text):
    """Attempt to extract JSON from markdown code blocks or raw text."""
    # Simplified extraction logic
    if "```json" in text:
        try:
            return text.split("```json")[1].split("```")[0].strip()
        except:
            pass
    elif "```" in text:
        try:
            # Maybe it just used ``` instead of ```json
            return text.split("```")[1].split("```")[0].strip()
        except:
            pass
    return text.strip()

def invoke_nvidia_nim(system_prompt, user_payload, model):
    api_key = os.environ.get("NVIDIA_NIM_API_KEY")
    if not api_key:
        print("WARNING: NVIDIA_NIM_API_KEY not found. Using a dummy successful response for testing.")
        return json.dumps({
            "priority": "HIGH",
            "objective": "Capitalize on emerging market trend identified in intel.",
            "rationale": "Empirical data shows a 20% spike in search volume. First-mover advantage is critical.",
            "target_divisions": ["CPO", "CMO"],
            "division_commands": {
                "CPO": "Generate PRD for rapid prototype.",
                "CMO": "Prepare go-to-market messaging and intercept ads."
            }
        })
        
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # We force the model into JSON mode if supported, or via prompt
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt + "\n\nCRITICAL CONSTRAINT: You MUST respond ONLY with valid JSON. No markdown wrappers, no conversational text."},
            {"role": "user", "content": f"Here is the daily intel payload:\n{user_payload}\n\nExecute your evaluation and output the Strategic Directive."}
        ],
        "temperature": 0.1,
        "max_tokens": 4096
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        result = response.json()
        content = result['choices'][0]['message']['content']
        return extract_json_from_text(content)
    except Exception as e:
        print(f"Error calling NVIDIA NIM: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent_profile", required=True)
    parser.add_argument("--input_payload", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--output_path", required=True)
    args = parser.parse_args()
    
    print(f"Loading Agent Profile: {args.agent_profile}")
    try:
        with open(args.agent_profile, 'r', encoding='utf-8') as f:
            system_prompt = f.read()
    except Exception as e:
        print(f"Failed to read agent profile: {e}")
        sys.exit(1)
        
    print(f"Loading Input Payload: {args.input_payload}")
    try:
        with open(args.input_payload, 'r', encoding='utf-8') as f:
            user_payload = f.read()
    except Exception as e:
        print(f"Failed to read input payload: {e}")
        sys.exit(1)
        
    print(f"Invoking {args.model} via Data Bus...")
    raw_response = invoke_nvidia_nim(system_prompt, user_payload, args.model)
    
    # Attempt to parse to ensure it's valid JSON before writing
    try:
        json_data = json.loads(raw_response)
    except json.JSONDecodeError:
        print("ERROR: Agent failed to output valid JSON.")
        print(f"Raw Output: {raw_response}")
        sys.exit(1)
        
    # Write the output
    os.makedirs(os.path.dirname(args.output_path), exist_ok=True)
    with open(args.output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2)
        
    print(f"Successfully wrote output to {args.output_path}")

if __name__ == "__main__":
    main()
