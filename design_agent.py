import requests

def run_design_agent(post: str, groq_key: str) -> str:
    headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
    system = "You are Design Agent. You create image prompts for DALL-E/Midjourney for LinkedIn. Detailed, 3D, professional, no text."
    user = f"Post: {post[:500]}\nCreate 1 detailed image prompt. Style: 3D global enterprise, clean, Stripe/Linear style."
    data = {
        "model": "allam-2-7b",
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
        "temperature": 0.9,
        "max_tokens": 500
    }
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=40)
    if r.status_code != 200:
        raise Exception(f"Design Agent Error {r.status_code}")
    return r.json()['choices'][0]['message']['content'].strip()