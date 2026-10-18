import requests

def run_hunter(topic: str, groq_key: str) -> str:
    """Trend Hunter Agent - viral angles nikalta hai"""
    if not groq_key:
        raise ValueError("GROQ_API_KEY missing")
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Hunter Agent. Find viral LinkedIn angles for Oct 2026. Bullet points only, sharp, real."
    user = f"Topic: {topic}\nGive: 3 viral hooks, 1 contrarian take, 1 stat. Bullet list."
    data = {
        "model": "allam-2-7b",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.9,
        "max_tokens": 600
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
    if r.status_code != 200:
        raise Exception(f"Hunter Error {r.status_code}: {r.text[:400]}")
    return r.json()['choices'][0]['message']['content'].strip()