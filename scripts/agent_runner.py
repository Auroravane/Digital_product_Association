import os
import re
import json
import requests
from typing import Dict, Any

class AgentRunner:
    """The bridge between .md System Prompts and LLM API Endpoints."""
    
    def __init__(self, agent_path: str):
        self.agent_path = agent_path
        self.system_prompt = self._load_agent_prompt()

    def _load_agent_prompt(self) -> str:
        """Extracts the <system_instructions> block from the agent's markdown file."""
        with open(self.agent_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find the content inside <system_instructions> tags
        match = re.search(r'<system_instructions>(.*?)</system_instructions>', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            # Fallback to the whole file if tags are missing (though our Grandmaster spec includes them)
            return content

    def call_nvidia_nim(self, payload: str, model="meta/llama-3.3-70b-instruct") -> str:
        """Invokes the high-tier reasoning model via NVIDIA NIM."""
        api_key = os.getenv("NVIDIA_API_KEY")
        if not api_key:
            raise ValueError("NVIDIA_API_KEY not found in environment.")

        url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": payload}
            ],
            "temperature": 0.1,
            "top_p": 0.7,
            "max_tokens": 4096
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        raw_content = response.json()['choices'][0]['message']['content']
        cleaned_content = self._clean_json_response(raw_content)
        
        # Security Guard: Prevent Secret Leakage
        self._check_for_secret_leak(cleaned_content)
        
        return cleaned_content

    def _check_for_secret_leak(self, text: str):
        """Scans output for patterns that look like sensitive keys."""
        # Detect GitHub PATs and NVIDIA API Keys
        patterns = [
            r'ghp_[a-zA-Z0-9]{36}',
            r'nvapi-[a-zA-Z0-9-]{64}'
        ]
        for pattern in patterns:
            if re.search(pattern, text):
                raise SecurityException("CRITICAL: LLM attempted to leak a potential API secret. Execution blocked.")

class SecurityException(Exception):
    pass

    def _clean_json_response(self, text: str) -> str:
        """Removes markdown code block wrappers if present."""
        # Remove ```json ... ``` or ``` ... ```
        text = re.sub(r'```json\s*', '', text)
        text = re.sub(r'```\s*', '', text)
        return text.strip()

    def call_gemini(self, payload: str, model="gemini-2.0-flash-lite-preview-02-05") -> str:
        """Invokes the high-velocity worker model via Google Gemini API (Flash Lite)."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment.")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{
                "parts": [{
                    "text": f"SYSTEM INSTRUCTIONS:\n{self.system_prompt}\n\nUSER PAYLOAD:\n{payload}"
                }]
            }]
        }
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['candidates'][0]['content']['parts'][0]['text']

if __name__ == "__main__":
    # Example usage for testing
    print("Agent Runner initialized. Ready to execute .md agents via API.")
