import requests

def run_critic(posts: list, groq_key: str) -> list:
    """Critic Agent - score deta hai"""
    if not groq_key:
        raise ValueError("GROQ_API_KEY missing")
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Critic Agent. Ruthless LinkedIn editor. Score Hook/Value/Virality 1-10. Give score + 1 line brutal fix. Short."
    scored = []
    for p in posts:
        user = f"Post: {p[:600]}\nScore and give 1-line feedback."
        data = {
            "model": "allam-2-7b",
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": 0.4,
            "max_tokens": 350
        }
        r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
        critique = r.json()['choices'][0]['message']['content'].strip() if r.status_code == 200 else "No critique"
        scored.append({"post": p, "critique": critique})
    return scored