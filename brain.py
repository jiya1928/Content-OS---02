import requests

def run_brain(topic: str, trends: str, style: str, length: int, elements: list, groq_key: str, name: str) -> list:
    """Brain Agent - 3 posts likhta hai"""
    if not groq_key:
        raise ValueError("GROQ_API_KEY missing")
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = f"You are Brain Agent. Ghostwriter for {name}. Style: {style}, Must include: {', '.join(elements)}. Trends: {trends}"
    posts = []
    for i in range(3):
        user = f"Write LinkedIn post variant {i+1} on '{topic}'. Length {length} words. Strong hook first line. Personal story. End with question. ONLY post content."
        data = {
            "model": "allam-2-7b",
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": 0.85,
            "max_tokens": 800
        }
        r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
        if r.status_code != 200:
            raise Exception(f"Brain Error {r.status_code}: {r.text[:400]}")
        posts.append(r.json()['choices'][0]['message']['content'].strip())
    return posts