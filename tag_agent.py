import requests

def run_tag_agent(post: str, topic: str, groq_key: str) -> str:
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Tag Agent. You find viral LinkedIn hashtags Oct 2026."
    user = f"Topic: {topic}\nPost: {post[:400]}\nGive: 5 hashtags with High/Med reach + 1 banned to avoid. Short."
    data = {
        "model": "allam-2-7b",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.6,
        "max_tokens": 400
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
    if r.status_code != 200:
        raise Exception(f"Tag Agent Error {r.status_code}")
    return r.json()['choices'][0]['message']['content'].strip()