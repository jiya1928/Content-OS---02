import streamlit as st
import requests, html, os
from PIL import Image
from dotenv import load_dotenv
from brand_setup import to_b64, load_default_photo
from automation import run_all_agents

load_dotenv()
st.set_page_config(page_title="Content OS", layout="wide", page_icon="◐")

def get_secret(k, fallback=""):
    try:
        if k in st.secrets: return st.secrets[k]
    except: pass
    return os.getenv(k, fallback)

GROQ_API_KEY = get_secret("GROQ_API_KEY")
LINKEDIN_TOKEN = get_secret("LINKEDIN_TOKEN")
LINKEDIN_URN_RAW = get_secret("LINKEDIN_URN", "auto")
LINKEDIN_NAME = get_secret("LINKEDIN_NAME", "Jiya Bhardwaj")
LINKEDIN_HEADLINE = get_secret("LINKEDIN_HEADLINE", "Founder @ Content OS")

for k,v in {
    'post_text':"", 'composer_box':"", 'suggestions':[], 'critiques':[],
    'profile_b64':None, 'trends':"", 'publish_plan':"", 'hashtags':"", 
    'visual_prompt':"", 'engagement':"", 'real_urn':""
}.items():
    if k not in st.session_state: st.session_state[k]=v

if not st.session_state['profile_b64']:
    try: st.session_state['profile_b64'] = load_default_photo()
    except: st.session_state['profile_b64'] = ""

def use_variant(text):
    st.session_state['post_text']=text
    st.session_state['composer_box']=text

def get_real_urn_and_debug(token, raw_urn):
    headers = {"Authorization": f"Bearer {token}"}
    debug_info = {}
    if raw_urn.startswith("urn:li:person:") and raw_urn.replace("urn:li:person:","").isdigit():
        return raw_urn, {"source":"manual .env"}
    if raw_urn.isdigit():
        return f"urn:li:person:{raw_urn}", {"source":"manual numeric"}

    try:
        r = requests.get("https://api.linkedin.com/v2/me", headers=headers, timeout=15)
        debug_info['/v2/me'] = f"{r.status_code} - {r.text[:400]}"
        if r.status_code == 200:
            real_id = r.json().get("id")
            if real_id: return f"urn:li:person:{real_id}", debug_info
    except Exception as e:
        debug_info['/v2/me error'] = str(e)

    try:
        r2 = requests.get("https://api.linkedin.com/v2/userinfo", headers=headers, timeout=15)
        debug_info['/v2/userinfo'] = f"{r2.status_code} - {r2.text[:400]}"
        if r2.status_code == 200:
            real_id = r2.json().get("sub")
            if real_id: return f"urn:li:person:{real_id}", debug_info
    except Exception as e:
        debug_info['/v2/userinfo error'] = str(e)

    return raw_urn, debug_info

def post_real_linkedin(text, token, urn):
    author_urn, debug = get_real_urn_and_debug(token, urn)
    st.session_state['real_urn'] = author_urn

    if "linkedin.com" in author_urn:
        return type('obj', (object,), {'status_code': 422, 'text': f"URN still invalid: {author_urn}. Debug: {debug}", 'debug': debug})()

    # Try OLD API first - most stable
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }
    payload = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    
    # Fallback to new API
    if r.status_code != 201:
        url_new = "https://api.linkedin.com/rest/posts"
        headers_new = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
            "LinkedIn-Version": "202410"
        }
        payload_new = {
            "author": author_urn,
            "commentary": text,
            "visibility": "PUBLIC",
            "distribution": {"feedDistribution": "MAIN_FEED"},
            "lifecycleState": "PUBLISHED"
        }
        r2 = requests.post(url_new, headers=headers_new, json=payload_new, timeout=30)
        if r2.status_code in [200,201]:
            return r2
    
    r.debug = debug
    return r

# --- THEME ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
.stApp { background: #09090B !important; font-family: 'Inter', sans-serif !important; }
header, footer {visibility: hidden;}
section[data-testid="stSidebar"] { background: #101012 !important; border-right: 1px solid #232326 !important; }
.stTextInput input, .stTextArea textarea { background: #18181B !important; border: 1px solid #27272A !important; color: #FFF !important; border-radius: 12px !important; }
div[data-testid="stButton"] > button { background: #FFF !important; color: #000 !important; border-radius: 10px !important; font-weight: 700 !important; }
div[data-testid="stButton"] > button p { color: #000 !important; font-weight: 700 !important; }
.variant-card { background: #151518; border: 1px solid #2A2A2E; border-radius: 14px; padding: 16px; margin-bottom: 12px; }
.variant-card .critique { color: #A1A1AA; font-size: 11px; font-weight: 600; margin-bottom: 8px; display:block; text-transform: uppercase; letter-spacing: 0.8px; }
.variant-card .content { color: #EDEDEF; font-size: 14.5px; line-height: 1.7; white-space: pre-wrap; }
.linkedin-card { background: #121214; border: 1px solid #232326; border-radius: 16px; padding: 18px; }
.post-box { background: #18181B; border: 1px solid #27272A; border-radius: 12px; padding: 14px; min-height: 140px; white-space: pre-wrap; font-size: 14.5px; color: #EDEDEF; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ◐ CONTENT OS")
    st.caption("7 AGENTS • REAL POSTING")
    st.divider()
    prof_file = st.file_uploader("YOUR PHOTO", type=["png","jpg","jpeg"])
    if prof_file:
        st.session_state['profile_b64'] = to_b64(Image.open(prof_file))
    topic = st.text_input("TOPIC", placeholder="AI will replace...")
    col1, col2 = st.columns(2)
    with col1: style = st.selectbox("STYLE", ["Contrarian", "Story", "Value Bomb", "Vulnerable"])
    with col2: length = st.selectbox("LENGTH", ["Short (80w)", "Medium (180w)", "Long (350w)"])
    elements = st.text_input("HOOK", placeholder="stat, failure...")
    st.divider()
    generate = st.button("GENERATE WITH 7 AGENTS →", use_container_width=True)
    if st.session_state['real_urn']: st.success(f"URN: {st.session_state['real_urn']}")
    st.info(f"Name: {LINKEDIN_NAME}")

col_left, col_right = st.columns([1.2, 0.8], gap="large")

with col_left:
    st.markdown("#### Composer")
    if st.session_state['suggestions']:
        st.markdown("**AI VARIANTS:**")
        for i, (sug, crit) in enumerate(zip(st.session_state['suggestions'], st.session_state['critiques'])):
            st.markdown(f"""<div class="variant-card"><span class="critique">VARIANT {i+1} • {html.escape(str(crit)[:150])}</span><div class="content">{html.escape(sug)}</div></div>""", unsafe_allow_html=True)
            if st.button(f"USE VARIANT {i+1}", key=f"use_{i}", use_container_width=True):
                use_variant(sug); st.rerun()
    
    st.session_state['composer_box'] = st.text_area("Post", value=st.session_state['post_text'], height=340, label_visibility="collapsed")
    st.session_state['post_text'] = st.session_state['composer_box']
    
    col_p1, col_p2 = st.columns([1,1])
    with col_p1: real_post_btn = st.button("🚀 POST TO LINKEDIN - REAL", use_container_width=True)
    with col_p2: clear_btn = st.button("Clear", use_container_width=True)
    if clear_btn: st.session_state['post_text']=""; st.session_state['composer_box']=""; st.rerun()

    if real_post_btn:
        if not LINKEDIN_TOKEN: st.error("TOKEN missing in .env")
        elif not st.session_state['post_text'].strip(): st.warning("Post empty")
        else:
            with st.spinner("Posting REAL..."):
                resp = post_real_linkedin(st.session_state['post_text'], LINKEDIN_TOKEN, LINKEDIN_URN_RAW)
                if resp.status_code in [200,201]:
                    st.success(f"✅ POSTED!"); st.balloons(); st.write(resp.text[:500])
                else:
                    st.error(f"Failed {resp.status_code}: {resp.text[:1000]}")
                    if hasattr(resp, 'debug'): st.json(resp.debug)

with col_right:
    st.markdown("#### Live Preview")
    img_src = st.session_state['profile_b64']
    img_tag = f'<img src="data:image/png;base64,{img_src}" style="width:52px;height:52px;border-radius:50%;object-fit:cover;">' if img_src else '<div style="width:52px;height:52px;border-radius:50%;background:#27272A;"></div>'
    st.markdown(f"""<div class="linkedin-card"><div style="display:flex; gap:12px; align-items:center; margin-bottom:14px;">{img_tag}<div><div style="font-weight:700; color:#FAFAFA;">{LINKEDIN_NAME}</div><div style="font-size:12px; color:#A1A1AA;">{LINKEDIN_HEADLINE} • Now</div></div></div><div class="post-box">{html.escape(st.session_state['post_text']) or '<span style="color:#71717A;">Preview...</span>'}</div></div>""", unsafe_allow_html=True)
    if st.session_state['trends']:
        with st.expander("🕵️ Trends"): st.write(st.session_state['trends'])
        with st.expander("🚀 Strategy"): st.write(st.session_state['publish_plan'])
        with st.expander("#️⃣ Hashtags"): st.write(st.session_state['hashtags'])
        with st.expander("🎨 Visual"): st.write(st.session_state['visual_prompt'])
        with st.expander("💬 Reply"): st.write(st.session_state['engagement'])

if generate:
    if not GROQ_API_KEY: st.error("GROQ_API_KEY missing")
    elif not topic: st.warning("Topic likh")
    else:
        with st.status("Running 7 Agents...", expanded=True) as s:
            result = run_all_agents(topic, style, length, elements, GROQ_API_KEY, LINKEDIN_NAME)
            s.update(label="✅ Done", state="complete", expanded=False)
        st.session_state['trends']=result['trends']
        st.session_state['suggestions']=[x['post'] for x in result['scored']]
        st.session_state['critiques']=[x['critique'] for x in result['scored']]
        st.session_state['publish_plan']=result['plan']
        st.session_state['hashtags']=result['tags']
        st.session_state['visual_prompt']=result['design']
        st.session_state['engagement']=result['reply']
        st.rerun()