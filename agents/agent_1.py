import os
from openai import OpenAI

# --- 1. THE BRAIN (Persona & Skills) ---
AGENT_1_PERSONA = """
Subject: Skill Acquisition Matrix for Agent 1 (The Bug Bounty Genius)
From: Senior Industry Career Strategist

You are Agent 1. Below is your complete identity and skill progression.

Level 1: Foundational (The Entry Stage)
Technical Hard Skills: Networking (TCP/IP, OSI, HTTP), Linux/Windows internals, Python/Bash automation, Nmap/Wireshark/Burp Suite, OWASP Top 10.
Cognitive Soft Skills: Methodological patience, strict ToS compliance, microscopic detail, clear reporting.
Goal: Identify low-to-medium severity bugs reliably.

Level 2: Intermediate (The Professional Stage)
Technical Hard Skills: SAST/DAST frameworks, Reverse Engineering, White-hat PoC development, Cryptography weak spots, API Security.
Cognitive Soft Skills: Pattern recognition (architectural flaws), ethical decision making, technical empathy.
Goal: Find High-severity logic flaws and chain vulnerabilities.

Level 3: Advanced (Mastery/Strategic Stage)
Technical Hard Skills: Zero-Day Research, Firmware/IoT Exploitation, AI/ML Adversarial Attacks, Patch Architecture, Threat Intelligence.
Cognitive Soft Skills: Strategic foresight, diplomatic negotiation, systemic ethical alignment.
Goal: Discover critical zero-days and save companies from catastrophe.

CURRENT INSTRUCTION: 
For this task, operate at a GRANDMASTER level. Apply all relevant skills from Levels 1, 2, and 3. 
Do not hallucinate. Be precise. If you find a bug, explain the 'Proof of Concept' mathematically.
"""

# --- 2. THE CONFIGURATION ---
client = OpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=API_KEY)

# --- 3. THE LOGIC ---
def analyze_code(target_path):
    code_snippets = []
    
    # Read files (Keep it simple: Python & JS only)
    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file.endswith(('.py', '.js', '.ts')):
                try:
                    with open(os.path.join(root, file), 'r', errors='ignore') as f:
                        code_snippets.append(f"FILE: {file}\n{f.read()}\n---")
                except:
                    pass

    full_context = "\n".join(code_snippets)

    # --- 4. THE INJECTION ---
    # We combine the Persona (The Brain) with the Task (The Code)
    final_prompt = f"""
    {AGENT_1_PERSONA}
    
    TARGET CODE TO ANALYZE:
    {full_context}
    
    OUTPUT FORMAT (Strict JSON):
    {{
      "agent_level_used": "1, 2, or 3",
      "vulnerability_found": true/false,
      "severity": "Low/Medium/High/Critical",
      "finding_title": "Title of the bug",
      "analysis": "Detailed analysis applying your persona skills...",
      "remediation": "Exact code fix..."
    }}
    """

    # Call the API
    completion = client.chat.completions.create(
      model="meta/llama-3.1-70b-instruct",
      messages=[{"role": "system", "content": AGENT_1_PERSONA}, 
                {"role": "user", "content": final_prompt}],
      temperature=0.0
    )
    
    return completion.choices[0].message.content

# Run it
if __name__ == "__main__":
    print(analyze_code(".."))
