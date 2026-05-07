import os
import re

def update_role_files():
    base_dir = r"d:\Zanime\Projects\Ruflo\Company"
    
    count = 0
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                    # Replacement logic
                    updated_content = content
                    updated_content = re.sub(r'Moonshot Kimi K2\.6', 'Meta Llama 3.3 70B', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'Kimi K2\.6', 'Llama 3.3 70B', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'Claude 3\.5 Sonnet', 'Meta Llama 3.3 70B', updated_content, flags=re.IGNORECASE)
                    
                    updated_content = re.sub(r'GPT-4o-mini', 'Gemini 2.5 Flash Lite', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'GPT-4o', 'Llama 3.3 70B', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'GPT-4', 'Kimi K2.6', updated_content, flags=re.IGNORECASE)
                    
                    updated_content = re.sub(r'OpenAI/Anthropic', 'NVIDIA NIM', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'Anthropic', 'NVIDIA', updated_content, flags=re.IGNORECASE)
                    updated_content = re.sub(r'OpenAI', 'NVIDIA', updated_content, flags=re.IGNORECASE)

                    if updated_content != content:
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(updated_content)
                        count += 1
                        print(f"Updated {file}")
                except Exception as e:
                    print(f"Skipping {file}: {e}")
                    
    print(f"\\nTotal files updated: {count}")

if __name__ == "__main__":
    update_role_files()
