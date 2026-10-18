import streamlit as st
from brain import app_graph
import json, datetime
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="CONTENT OS - Jiya", layout="wide", page_icon="⚡")

# --- ADVANCE UI CSS - NAYA LOOK ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&display=swap');

* { font-family: 'Space Grotesk', sans-serif; }

.stApp {
    background: #050507;
    background-image: 
        radial-gradient(at 20% 30%, #6D28D9 0px, transparent 50%),
        radial-gradient(at 80% 20%, #06B6D4 0px, transparent 50%),
        radial-gradient(at 40% 80%, #EC4899 0px, transparent 50%);
}

.glass-card {
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    transition: 0.3s;
}
.glass-card:hover {
    border: 1px solid rgba(124,58,237,0.5);
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(109,40,217,0.25);
}

.main-title {
    font-size: 64px;
    font-weight: 800;
    background: linear-gradient(90deg, #fff 0%, #A78BFA 30%, #06B6D4 70%, #EC4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -2px;
    line-height: 0.9;
    margin-bottom: 10px;
}

.sub-title {
    color: rgba(255,255,255,0.5);
    font-size: 18px;
    letter-spacing: 1px;
}

.platform-badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 8px;
    border: 1px solid;
}
.badge-linkedin { background: rgba(0,119,181,0.15); color: #0A66C2; border-color: rgba(0,119,181,0.3); }
.badge-twitter { background: rgba(255,255,255,0.08); color: #fff; border-color: rgba(255,255,255,0.2); }
.badge-insta { background: linear-gradient(45deg, rgba(225,48,108,0.15), rgba(255,220,128,0.15)); color: #E1306C; border-color: rgba(225,48,108,0.3); }
.badge-youtube { background: rgba(255,0,0,0.12); color: #FF0000; border-color: rgba(255,0,0,0.3); }

div.stButton > button {
    background: linear-gradient(90deg, #6D28D9, #06B6D4) !important;
    color: white !important;
    border: none !important;
    border-radius: 100px !important;
    padding: 16px 36px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    letter-spacing: 1px;
    box-shadow: 0 8px 20px rgba(109,40,217,0.4);
    transition: 0.3s !important;
}
div.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 12px 30px rgba(109,40,217,0.6);
}

.score-ring {
    width: 90px; height: 90px;
    border-radius: 50%;
    background: conic-gradient(#6D28D9 0% 88%, rgba(255,255,255,0.1) 88% 100%);
    display: flex; align-items: center; justify-content: center;
}
.score-inner {
    width: 70px; height: 70px;
    background: #0A0A0B;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 20px; color: white;
}

.stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.03); border-radius: 100px; padding: 6px; }
.stTabs [data-baseweb="tab"] { border-radius: 100px; color: rgba(255,255,255,0.5); }
.stTabs [aria-selected="true"] { background: white !important; color: black !important; }

</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-title">CONTENT OS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">BY JIYA BHARDWAJ • AGENTIC AI • 7 PLATFORMS • 1 CLICK • 100% FREE STACK</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

# --- SIDEBAR WITH GLASS ---
with st.sidebar:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color:white; margin:0;">⚡ Control Center</h3>
        <p style="color:rgba(255,255,255,0.4); font-size:12px;">GROQ FAST + DUCKDUCKGO FREE</p>
    </div>
    """, unsafe_allow_html=True)
    
    topic = st.text_input("Enter Viral Topic", "AI Agents for Startups", label_visibility="visible")
    st.markdown("<br>", unsafe_allow_html=True)
    run = st.button("GENERATE MAGIK →", use_container_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <p style="color:white; font-size:13px; margin:0;">🔮 System Status</p>
        <p style="color:#10B981; font-size:12px; margin-top:8px;">● Research Agent Active<br>● Brand Lock Active<br>● Writer Swarm Ready<br>● Critic Online</p>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN AREA ---
if run:
    with st.spinner(""):
        st.markdown("""
        <div class="glass-card" style="text-align:center; border-style:dashed;">
            <h3 style="color:white;">Agents are cooking content for 7 platforms...</h3>
            <p style="color:rgba(255,255,255,0.5);">Research → Brand Voice → Writing Swarm → Critic</p>
        </div>
        """, unsafe_allow_html=True)
        result = app_graph.invoke({"topic": topic})
    
    # SCORE + HEADER
    col1, col2, col3 = st.columns([1,2,2])
    with col1:
        st.markdown(f"""
        <div class="glass-card" style="display:flex; gap:16px; align-items:center;">
            <div class="score-ring"><div class="score-inner">{result.get('score',88)}</div></div>
            <div><p style="color:white; font-weight:700; margin:0;">Quality Score</p><p style="color:rgba(255,255,255,0.5); font-size:12px; margin:0;">Critic Agent Approved</p></div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="glass-card">
            <p style="color:rgba(255,255,255,0.4); font-size:12px; margin:0;">CURRENT TOPIC</p>
            <p style="color:white; font-size:20px; font-weight:600; margin:0;">{topic}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="glass-card">
            <p style="color:rgba(255,255,255,0.4); font-size:12px; margin:0;">GENERATED</p>
            <p style="color:white; font-size:20px; font-weight:600; margin:0;">{datetime.date.today()} • 7 Packs</p>
        </div>
        """, unsafe_allow_html=True)

    # TABS
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["💼 LINKEDIN", "🐦 TWITTER / FB", "📸 INSTAGRAM", "▶ YOUTUBE", "📝 BLOG + EMAIL"])
    
    with tab1:
        st.markdown('<div class="platform-badge badge-linkedin">LINKEDIN • VIRAL FORMAT</div><br><br>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card"><pre style="white-space:pre-wrap; color:white;">{result["linkedin"]}</pre></div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div class="platform-badge badge-twitter">X / TWITTER • THREAD</div><br><br>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card"><pre style="white-space:pre-wrap; color:white;">{result["twitter"]}</pre></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card" style="margin-top:20px;"><pre style="white-space:pre-wrap; color:rgba(255,255,255,0.8);">{result["facebook"]}</pre></div>', unsafe_allow_html=True)
    with tab3:
        st.markdown('<div class="platform-badge badge-insta">INSTAGRAM • CAPTION + REEL</div><br><br>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card"><pre style="white-space:pre-wrap; color:white;">{result["instagram"]}</pre></div>', unsafe_allow_html=True)
    with tab4:
        st.markdown('<div class="platform-badge badge-youtube">YOUTUBE • SEO PACK</div><br><br>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card"><pre style="white-space:pre-wrap; color:white;">{result["youtube"]}</pre></div>', unsafe_allow_html=True)
    with tab5:
        st.markdown(f'<div class="glass-card"><pre style="white-space:pre-wrap; color:white;">{result["blog"]}</pre></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="glass-card" style="margin-top:20px; border-color:rgba(236,72,153,0.3);"><pre style="white-space:pre-wrap; color:rgba(255,255,255,0.9);">{result["newsletter"]}</pre></div>', unsafe_allow_html=True)

    # Save
    with open("content_calendar.json", "a") as f:
        f.write(json.dumps({"date": str(datetime.date.today()), "topic": topic, "score": result.get('score')}) + "\n")

else:
    # EMPTY STATE - FUTURISTIC
    st.markdown("""
    <div class="glass-card" style="text-align:center; padding:60px 20px;">
        <h1 style="color:white; font-size:42px; font-weight:800; letter-spacing:-1px;">One Topic.<br>Seven Platforms.<br><span style="background: linear-gradient(90deg, #6D28D9, #06B6D4); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Ten Seconds.</span></h1>
        <p style="color:rgba(255,255,255,0.4); max-width:500px; margin:20px auto;">Enter a topic in sidebar. Our agentic swarm will research trends via DuckDuckGo, lock your brand voice via ChromaDB, and write platform-native content via Groq Llama 3.1 70B</p>
        <div style="margin-top:30px;">
            <span class="platform-badge badge-linkedin">LINKEDIN</span>
            <span class="platform-badge badge-twitter">TWITTER/X</span>
            <span class="platform-badge badge-insta">INSTAGRAM</span>
            <span class="platform-badge badge-youtube">YOUTUBE</span>
            <span class="platform-badge badge-linkedin">BLOG</span>
            <span class="platform-badge badge-twitter">NEWSLETTER</span>
        </div>
    </div>
    """, unsafe_allow_html=True)