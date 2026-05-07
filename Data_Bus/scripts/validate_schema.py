import argparse
import json
import os
import sys

def validate_schema(target_file, schema_file):
    try:
        from jsonschema import validate, ValidationError
    except ImportError:
        print("jsonschema not installed. Install via: pip install jsonschema")
        sys.exit(1)

    print(f"Validating {target_file} against {schema_file}...")
    
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            target_data = json.load(f)
    except Exception as e:
        print(f"Error loading target JSON: {e}")
        sys.exit(1)
        
    try:
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema_data = json.load(f)
    except Exception as e:
        print(f"Error loading schema JSON: {e}")
        sys.exit(1)

    try:
        validate(instance=target_data, schema=schema_data)
        print("✅ Strict Schema Validation Passed.")
        
        # If the priority is DROP, we might want to exit cleanly but signal no further action
        if target_data.get("priority") == "DROP":
            print("Priority is DROP. The CDO chose to ignore the intel.")
            
    except ValidationError as e:
        print(f"❌ Schema Validation Failed: {e.message}")
        print("This prevents hallucinated LLM data from poisoning the downstream pipeline.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="Path to the JSON output from the LLM")
    parser.add_argument("--schema", required=True, help="Path to the JSON Schema definition")
    args = parser.parse_args()
    
    validate_schema(args.target, args.schema)
