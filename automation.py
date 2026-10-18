from hunter import run_hunter
from brain import run_brain
from critic import run_critic
from publisher import run_publisher
from tag_agent import run_tag_agent
from design_agent import run_design_agent
from reply_agent import run_reply_agent

def run_all_agents(topic, style, length, elements, groq_key, name):
    """7-Agent Manager"""
    
    # Agent 1: Hunter - Research
    print("🕵️ Agent 1: Hunter running...")
    trends = run_hunter(topic, groq_key)
    
    # Agent 2: Brain - Writer
    print("✍️ Agent 2: Brain running...")
    posts = run_brain(topic, trends, style, length, elements, groq_key, name)
    
    # Agent 3: Critic - Scoring
    print("🧐 Agent 3: Critic running...")
    scored = run_critic(posts, groq_key)
    best = scored[0]['post'] if scored else posts[0]
    
    # Agent 4: Publisher - Strategy
    print("🚀 Agent 4: Publisher running...")
    plan = run_publisher(best, topic, groq_key)
    
    # Agent 5: Tag - Hashtag Optimizer
    print("#️⃣ Agent 5: Tag running...")
    tags = run_tag_agent(best, topic, groq_key)
    
    # Agent 6: Design - Visual Prompt
    print("🎨 Agent 6: Design running...")
    design = run_design_agent(best, groq_key)
    
    # Agent 7: Reply - Engagement
    print("💬 Agent 7: Reply running...")
    reply = run_reply_agent(best, groq_key)

    print("✅ All 7 Agents Done")

    return {
        "trends": trends,
        "scored": scored,
        "plan": plan,
        "tags": tags,
        "design": design,
        "reply": reply
    }