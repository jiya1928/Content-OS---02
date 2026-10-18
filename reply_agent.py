import requests

def run_reply_agent(post: str, groq_key: str) -> str:
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Reply Agent. You predict comments and write reply templates to boost algorithm."
    user = f"Post: {post[:500]}\nPredict top 3 comments and write 1-line reply for each. Also give author first comment to pin."
    data = {
        "model": "allam-2-7b",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.8,
        "max_tokens": 600
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
    if r.status_code != 200:
        raise Exception(f"Reply Agent Error {r.status_code}")
    return r.json()['choices'][0]['message']['content'].strip()