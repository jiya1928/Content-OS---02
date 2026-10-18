import requests

def run_publisher(best_post: str, topic: str, groq_key: str) -> str:
    """Publisher Agent - image idea + hashtags + time"""
    if not groq_key:
        raise ValueError("GROQ_API_KEY missing")
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Publisher Agent. You optimize for LinkedIn algorithm Oct 2026. Short, actionable."
    user = f"Topic: {topic}\nBest Post: {best_post[:500]}\nGive: 1) Image/Carousel idea (1 line) 2) 3 hashtags 3) Best IST time to post today (Sunday). Short."
    data = {
        "model": "allam-2-7b",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.7,
        "max_tokens": 500
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
    if r.status_code != 200:
        raise Exception(f"Publisher Error {r.status_code}: {r.text[:400]}")
    return r.json()['choices'][0]['message']['content'].strip()