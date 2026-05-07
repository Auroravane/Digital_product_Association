import json
import argparse
from jsonschema import validate, ValidationError

def validate_json(schema_path, target_path):
    print(f"Validating {target_path} against {schema_path}...")
    
    try:
        with open(schema_path, 'r') as s:
            schema = json.load(s)
        
        with open(target_path, 'r') as t:
            target = json.load(t)
            
        validate(instance=target, schema=schema)
        print("Validation Successful: JSON matches schema.")
        return True
        
    except ValidationError as e:
        print(f"Validation Failed: {e.message}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON against a Schema")
    parser.add_argument("--schema", required=True, help="Path to JSON Schema")
    parser.add_argument("--target", required=True, help="Path to JSON file to validate")
    
    args = parser.parse_args()
    
    if not validate_json(args.schema, args.target):
        exit(1) # Fail the CI/CD pipeline
