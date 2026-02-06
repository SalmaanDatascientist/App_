import streamlit as st
import os
import json
import base64
import datetime
import uuid
import requests
import hashlib
from PIL import Image
from groq import Groq
from openai import OpenAI
import PyPDF2

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
try:
    im = Image.open("logo.png")
except:
    im = "🧪"

st.set_page_config(
    page_title="The Molecular Man | Expert Tuition Solutions",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. SESSION STATE & FILE SETUP
# -----------------------------------------------------------------------------
if 'page' not in st.session_state:
    st.session_state.page = "Home"

if "username" not in st.session_state:
    st.session_state.username = "Student"

# Auth State for Live Class
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

# AI Tutor State
if "aya_messages" not in st.session_state:
    st.session_state.aya_messages = []

# Mock Test State
if 'mt_questions' not in st.session_state: st.session_state.mt_questions = None
if 'mt_answers' not in st.session_state: st.session_state.mt_answers = {}
if 'mt_feedback' not in st.session_state: st.session_state.mt_feedback = None

# Files
USERS_FILE = "users_database.json"
NOTIFICATIONS_FILE = "notifications.json"
LIVE_STATUS_FILE = "live_status.json"

def create_users_db():
    if not os.path.exists(USERS_FILE):
        default_users = {
            "Mohammed": hashlib.sha256("Molsalmaan@9292".encode()).hexdigest(),
            "Muskan": hashlib.sha256("mus1234kan".encode()).hexdigest(),
            "Prithwin": hashlib.sha256("prithwin".encode()).hexdigest()
        }
        with open(USERS_FILE, "w") as f:
            json.dump(default_users, f)

def init_files():
    if not os.path.exists(NOTIFICATIONS_FILE):
        with open(NOTIFICATIONS_FILE, "w") as f:
            json.dump([], f)
    if not os.path.exists(LIVE_STATUS_FILE):
        with open(LIVE_STATUS_FILE, "w") as f:
            json.dump({"is_live": False, "topic": "", "link": ""}, f)

create_users_db()
init_files()

# -----------------------------------------------------------------------------
# 3. HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def get_image_path(filename_base):
    extensions = [".png", ".jpg", ".jpeg", ".webp", ".gif"]
    paths = [f"images/{filename_base}", f"assets/{filename_base}", filename_base, f"./{filename_base}"]
    for path in paths:
        for ext in extensions:
            full_path = path + ext
            if os.path.exists(full_path):
                return full_path
    return None

def render_image(filename, caption=None, width=None, use_column_width=False):
    img_path = get_image_path(filename)
    try:
        if img_path:
            if use_column_width:
                st.image(img_path, caption=caption, use_container_width=True)
            else:
                st.image(img_path, caption=caption, width=width)
            return True
        return False
    except:
        return False

# Auth Helpers
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    try:
        with open(USERS_FILE, "r") as f:
            all_users = json.load(f)
        if username in all_users and all_users[username] == hash_password(password):
            return True
        return False
    except:
        return False

# Data Helpers
def get_notifications():
    try:
        with open(NOTIFICATIONS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def add_notification(message):
    notifs = get_notifications()
    new_notif = {"date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "message": message}
    notifs.insert(0, new_notif)
    with open(NOTIFICATIONS_FILE, "w") as f:
        json.dump(notifs, f)

def get_live_status():
    try:
        with open(LIVE_STATUS_FILE, "r") as f:
            return json.load(f)
    except:
        return {"is_live": False, "topic": "", "link": ""}

def set_live_status(is_live, topic="", link=""):
    status = {"is_live": is_live, "topic": topic, "link": link}
    with open(LIVE_STATUS_FILE, "w") as f:
        json.dump(status, f)

# -----------------------------------------------------------------------------
# 4. CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* GLOBAL STYLES */
    .stApp {
        background: linear-gradient(135deg, #004e92 0%, #000428 100%) !important;
        background-attachment: fixed;
    }
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }
    h1, h2, h3, h4, h5, h6, p, div, span, li, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    /* BUTTONS */
    div.stButton > button {
        background: linear-gradient(90deg, #1e3a5f, #3b6b9e, #1e3a5f);
        color: white !important; border-radius: 25px !important; border: 1px solid rgba(255,255,255,0.2) !important;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
    div[data-testid="stFormSubmitButton"] > button {
        background: #1e3a5f !important; color: #ffffff !important; border: 2px solid white !important;
    }
    div[data-testid="stFormSubmitButton"] > button p { color: #ffffff !important; }
    
    /* INPUTS */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div {
        background-color: rgba(255, 255, 255, 0.1) !important; color: #ffffff !important; border-radius: 8px; border: 1px solid rgba(255,255,255,0.3) !important;
    }
    
    /* UTILS */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* --- HERO AD BANNER --- */
    @keyframes neon-pulse {
        0% { box-shadow: 0 0 5px #ffd700, 0 0 15px #ffd700 inset; border-color: #ffd700; }
        50% { box-shadow: 0 0 20px #00ffff, 0 0 10px #00ffff inset; border-color: #00ffff; }
        100% { box-shadow: 0 0 5px #ffd700, 0 0 15px #ffd700 inset; border-color: #ffd700; }
    }
    .hero-ad-box {
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(12px);
        border: 2px solid #ffd700;
        border-radius: 20px;
        padding: 40px 20px;
        margin: 30px 0;
        text-align: center;
        animation: neon-pulse 4s infinite alternate;
    }
    .hero-headline {
        font-size: 32px; font-weight: 900; text-transform: uppercase; letter-spacing: 1px;
        background: linear-gradient(to right, #ffffff, #ffd700); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
    }
    .hero-subhead { font-size: 18px; color: #e0e0e0; margin-bottom: 25px; font-weight: 300; }
    .hero-suite-title {
        font-size: 22px; color: #00ffff; font-weight: 800; text-transform: uppercase; margin-bottom: 20px;
        text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
    }
    .hero-feature-grid { display: flex; justify-content: center; gap: 30px; margin-bottom: 30px; flex-wrap: wrap; }
    .hero-feature-item {
        background: rgba(255, 255, 255, 0.05); padding: 15px 25px; border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1); text-align: left; max-width: 400px;
    }
    .hero-footer {
        font-size: 14px; font-weight: 800; color: #ff4d4d; letter-spacing: 1.5px;
        border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 15px; margin-top: 10px;
    }

    /* --- ANIMATED FOUNDER HEADER --- */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translate3d(0, 30px, 0); }
        to { opacity: 1; transform: translate3d(0, 0, 0); }
    }
    @keyframes border-flow {
        0% { border-color: rgba(255, 215, 0, 0.3); box-shadow: 0 0 15px rgba(255, 215, 0, 0.1); }
        50% { border-color: rgba(0, 255, 255, 0.5); box-shadow: 0 0 25px rgba(0, 255, 255, 0.2); }
        100% { border-color: rgba(255, 215, 0, 0.3); box-shadow: 0 0 15px rgba(255, 215, 0, 0.1); }
    }
    
    .founder-header-container {
        text-align: center;
        padding: 35px 20px;
        background: linear-gradient(135deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.2) 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 30px;
        animation: border-flow 4s infinite alternate;
        overflow: hidden;
        position: relative;
    }
    
    .founder-headline {
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        background: linear-gradient(to right, #ffffff 0%, #a1c4fd 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 15px;
        opacity: 0;
        animation: fadeInUp 0.8s ease-out forwards;
    }
    
    .founder-subhead {
        font-size: 1.2rem;
        color: #e2e8f0;
        font-weight: 400;
        margin-bottom: 15px;
        opacity: 0;
        animation: fadeInUp 0.8s ease-out 0.3s forwards;
    }
    
    .founder-tagline {
        font-size: 1rem;
        color: #ffd700;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        opacity: 0;
        animation: fadeInUp 0.8s ease-out 0.6s forwards;
    }

    /* Live Class Specifics */
    .notif-card {
        background: rgba(255, 215, 0, 0.1);
        border-left: 4px solid #ffd700;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    @keyframes pulse-btn {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .live-button-container {
        text-align: center;
        margin-top: 20px;
        animation: pulse-btn 2s infinite;
    }

    /* --- CRITICAL FIX FOR TESTIMONIALS --- */
    /* This forces black text inside white cards, overriding global white text */
    .white-card-fix {
        background-color: white !important;
        color: black !important;
        padding: 20px !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
        margin-bottom: 20px !important;
    }
    /* Target ALL children elements to ensure they are black */
    .white-card-fix *, .white-card-fix p, .white-card-fix span, .white-card-fix div, .white-card-fix h1, .white-card-fix h2, .white-card-fix h3 {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. NAVIGATION (With Animated Header)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="founder-header-container">
<div class="founder-headline">Other Apps Were Coded by Engineers. This One Was Coded by Your Master Tutor - Mohammed Salmaan.</div>
<div class="founder-subhead">The only online tuition service in the world running on a proprietary engine built by the Founder.</div>
<div class="founder-tagline">Pure Teaching Intelligence. Zero Corporate Noise.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🧭 Main Menu")
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"; st.rerun()
with col2:
    if st.button("📚 Services", use_container_width=True): st.session_state.page = "Services"; st.rerun()
with col3:
    if st.button("🔴 Live Class", use_container_width=True): st.session_state.page = "Live Class"; st.rerun()
with col4:
    if st.button("💬 Stories", use_container_width=True): st.session_state.page = "Testimonials"; st.rerun()
with col5:
    if st.button("🐍 Bootcamp", use_container_width=True): st.session_state.page = "Bootcamp"; st.rerun()
with col6:
    if st.button("📞 Contact", use_container_width=True): st.session_state.page = "Contact"; st.rerun()

st.write("")
st.markdown("### 🤖 AI Power Tools (Free)")
ai_col1, ai_col2 = st.columns(2)
with ai_col1:
    if st.button("🧠 Chat with AyA (AI Tutor)", use_container_width=True, type="primary"): 
        st.session_state.page = "AyA_AI"
        st.rerun()
with ai_col2:
    if st.button("📝 Generate Mock Test", use_container_width=True, type="primary"): 
        st.session_state.page = "Mock_Test"
        st.rerun()

st.divider()

# -----------------------------------------------------------------------------
# 6. PAGE LOGIC
# -----------------------------------------------------------------------------

# ==========================================
# PAGE: HOME
# ==========================================
if st.session_state.page == "Home":
    
    # 1. Logo and Intro
    logo_col1, logo_col2 = st.columns([1, 2])
    with logo_col1:
        with st.container(border=True):
            if not render_image("logo", use_column_width=True):
                st.markdown("# 🧪")
                st.markdown("### The Molecular Man")
    with logo_col2:
        with st.container(border=True):
            st.markdown("# Expert Tuition for Excellence 🎓")
            st.markdown("### Personalized coaching in Mathematics, Physics, Chemistry & Biology")
            st.write("For Classes 6-12 & Competitive Exams (NEET/JEE/Boards)")
            st.write("")
            st.link_button("📱 Book Free Trial", "https://wa.me/917339315376", use_container_width=True)

    # 2. DYNAMIC ADVERTISEMENT
    st.markdown("""
<div class="hero-ad-box">
<div class="hero-headline">🚨 The Education System Just Got a Reality Check</div>
<div class="hero-subhead">
Stop paying for "premium" test series. The corporate coaching giants are scared.
</div>
<div class="hero-suite-title">INTRODUCING: THE MOLECULAR MAN AI SUITE</div>
<div class="hero-feature-grid">
<div class="hero-feature-item">
<span style="font-size: 20px; color: #ffd700;">1. 🧠 AyA (AI Tutor)</span><br>
<span style="font-size: 16px; color: #e0e0e0;">She doesn't sleep. She solves PDFs & problems instantly.</span>
</div>
<div class="hero-feature-item">
<span style="font-size: 20px; color: #ffd700;">2. 📝 Infinite Mock Tests</span><br>
<span style="font-size: 16px; color: #e0e0e0;">Generate unlimited tests for ANY Board/Subject for ₹0.</span>
</div>
</div>
<div class="hero-footer">
🚫 NO SUBSCRIPTIONS. NO HIDDEN FEES. PURE TEACHING INTELLIGENCE.
</div>
</div>
""", unsafe_allow_html=True)

    # 3. Stats
    st.markdown("## 📊 Our Impact")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Students Taught", "500+")
    with m2: st.metric("Success Rate", "100%")
    with m3: st.metric("Support", "24/7")
    with m4: st.metric("Experience", "5+ Years")

    st.markdown("## 🎯 What We Offer")
    s1, s2, s3 = st.columns(3)
    with s1:
        with st.container(border=True):
            st.markdown("#### 👨‍🏫 Expert Tutoring")
            st.write("One-on-one and small group classes for Classes 6-12.")
    with s2:
        with st.container(border=True):
            st.markdown("#### 📚 Comprehensive Material")
            st.write("Access to curated notes, practice problems, and revision guides.")
    with s3:
        with st.container(border=True):
            st.markdown("#### 🐍 Python Bootcamp")
            st.write("Weekend intensive courses in Data Science & AI.")

# ==========================================
# PAGE: AyA AI TUTOR
# ==========================================
elif st.session_state.page == "AyA_AI":
    st.markdown("## 🧠 AyA - The Molecular Man AI")
    st.caption("Your personal AI Tutor for Math, Science, and Coding.")

    try:
        groq_api_key = st.secrets["GROQ_API_KEY"]
        groq_client = Groq(api_key=groq_api_key)
    except Exception:
        st.error("⚠️ GROQ_API_KEY not found in Secrets!")
        st.stop()

    SYSTEM_PROMPT = """You are **Aya**, the Lead AI Tutor at **The Molecular Man Expert Tuition Solutions**. 
    Your Mission: Guide students from "Zero" to "Hero".
    Tone: Encouraging, clear, patient, and intellectually rigorous.
    Structure: 🧠 CONCEPT -> 🌍 CONTEXT -> ✍️ SOLUTION -> ✅ ANSWER -> 🚀 HERO TIP.
    """

    with st.expander("📝 New Problem Input", expanded=(len(st.session_state.aya_messages) == 0)):
        input_type = st.radio("Input Method:", ["📄 Text Problem", "📕 Upload PDF"], horizontal=True)
        
        if input_type == "📄 Text Problem":
            user_text = st.text_area("Paste question:", height=100)
            if st.button("Ask AyA 🚀", use_container_width=True):
                if user_text:
                    st.session_state.aya_messages = [] 
                    st.session_state.aya_messages.append({"role": "user", "content": f"PROBLEM:\n{user_text}"})
                    st.rerun()

        elif input_type == "📕 Upload PDF":
            uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
            if st.button("Analyze PDF 🚀", use_container_width=True):
                if uploaded_file:
                    try:
                        pdf_reader = PyPDF2.PdfReader(uploaded_file)
                        pdf_text = ""
                        for page_num in range(min(2, len(pdf_reader.pages))):
                            pdf_text += pdf_reader.pages[page_num].extract_text()[:3000]
                        st.session_state.aya_messages = [] 
                        st.session_state.aya_messages.append({"role": "user", "content": f"PROBLEM from PDF:\n{pdf_text}"})
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    for msg in st.session_state.aya_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if st.session_state.aya_messages and st.session_state.aya_messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("🤖 AyA is thinking..."):
                try:
                    msgs = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.aya_messages
                    chat_completion = groq_client.chat.completions.create(
                        messages=msgs,
                        model="llama-3.3-70b-versatile",
                        temperature=0.5,
                        max_tokens=6000,
                    )
                    response_text = chat_completion.choices[0].message.content
                    st.markdown(response_text)
                    st.session_state.aya_messages.append({"role": "assistant", "content": response_text})
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    if st.session_state.aya_messages:
        if user_input := st.chat_input("Ask a follow-up..."):
            st.session_state.aya_messages.append({"role": "user", "content": user_input})
            st.rerun()

# ==========================================
# PAGE: MOCK TEST
# ==========================================
elif st.session_state.page == "Mock_Test":
    st.markdown("## 📝 AI Mock Test Generator")
    st.caption("Generate unlimited tests for any Board, Subject, or Difficulty.")
    
    api_key = st.secrets.get("GROQ_API_KEY")
    if not api_key:
        st.error("Missing API Key"); st.stop()
    
    client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

    def get_questions_json(board, cls, sub, chap, num, diff, q_type):
        safe_sub = sub.encode('ascii', 'ignore').decode('ascii').strip()
        if q_type == "MCQ":
            prompt = f"""
            You are a strict Examiner for {board} Board. Subject: {safe_sub}, Class: {cls}, Chapter: {chap}.
            Create a valid JSON list of {num} {diff} MCQs.
            Format: [{{"id": 1, "question": "...", "options": ["A","B","C","D"], "correct_answer": "A"}}]
            """
        else:
            prompt = f"""
            You are a strict Examiner for {board} Board. Subject: {safe_sub}, Class: {cls}, Chapter: {chap}.
            Create a valid JSON list of {num} {diff} Descriptive Questions with marks.
            Format: [{{"id": 1, "question": "...", "marks": 5}}]
            """
        try:
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt + " Return ONLY JSON."}],
                temperature=0.1
            )
            content = res.choices[0].message.content.replace("```json", "").replace("```", "").strip()
            return json.loads(content)
        except: return None

    if not st.session_state.mt_questions:
        with st.container(border=True):
            c1, c2 = st.columns(2)
            with c1:
                board = st.selectbox("Board", ["CBSE", "ICSE", "State", "Other"])
                cls = st.selectbox("Class", ["9", "10", "11", "12"])
                diff = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
            with c2:
                sub = st.text_input("Subject", "Physics")
                chap = st.text_input("Chapter", "Thermodynamics")
                q_type = st.radio("Format", ["MCQ", "Descriptive"], horizontal=True)
                num = st.slider("Questions", 3, 20, 5)

        if st.button("🚀 Generate Test", type="primary"):
            if sub and chap:
                with st.spinner("Generating Paper..."):
                    st.session_state.mt_q_type = q_type
                    st.session_state.mt_questions = get_questions_json(board, cls, sub, chap, num, diff, q_type)
                    st.session_state.mt_answers = {}
                    st.session_state.mt_feedback = None
                    st.rerun()

    else:
        if st.session_state.mt_feedback:
            st.success("Test Analysis Complete")
            st.markdown(st.session_state.mt_feedback)
            if st.button("🔄 Start New Test"):
                st.session_state.mt_questions = None
                st.rerun()
        else:
            with st.form("mock_test_form"):
                for q in st.session_state.mt_questions:
                    st.markdown(f"**Q{q['id']}. {q['question']}**")
                    if st.session_state.mt_q_type == "MCQ":
                        st.radio("Choose:", q['options'], key=f"q_{q['id']}", label_visibility="collapsed", index=None)
                    else:
                        st.text_area("Answer:", key=f"q_{q['id']}")
                    st.markdown("---")
                
                submitted = st.form_submit_button("✅ Submit Exam")
            
            if submitted:
                answers = {}
                all_answered = True
                for q in st.session_state.mt_questions:
                    val = st.session_state.get(f"q_{q['id']}")
                    if not val: all_answered = False
                    answers[str(q['id'])] = val
                
                if not all_answered and st.session_state.mt_q_type == "MCQ":
                    st.error("Please answer all questions.")
                else:
                    prompt = f"Grade this student. Questions: {json.dumps(st.session_state.mt_questions)}. Answers: {json.dumps(answers)}."
                    with st.spinner("Grading..."):
                        res = client.chat.completions.create(
                            model="llama-3.3-70b-versatile",
                            messages=[{"role": "user", "content": prompt}],
                            temperature=0.3
                        )
                        st.session_state.mt_feedback = res.choices[0].message.content
                        st.rerun()

# ==========================================
# PAGE: LIVE CLASS
# ==========================================
elif st.session_state.page == "Live Class":
    st.markdown("# 🔴 Molecular Man Live Classroom")
    
    if not st.session_state.logged_in:
        # LOGIN VIEW
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown('<div style="font-size: 24px; text-align: center; margin-bottom: 20px;">Restricted Access</div>', unsafe_allow_html=True)
            with st.container(border=True):
                username = st.text_input("👤 Username")
                password = st.text_input("🔐 Password", type="password")
                
                if st.button("Login to Classroom 🚀", use_container_width=True):
                    if login_user(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.is_admin = (username == "Mohammed")
                        st.rerun()
                    else:
                        st.error("❌ Invalid Credentials")
    else:
        # LOGGED IN DASHBOARD
        col1, col2 = st.columns([3, 1])
        with col1: 
            st.write(f"Logged in as: **{st.session_state.username}**")
        with col2:
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = "Student"
                st.rerun()
        st.divider()

        if st.session_state.is_admin:
            # --- TEACHER DASHBOARD ---
            st.markdown("## 👨‍🏫 Teacher Command Center")
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### 🔴 Live Class Controls")
                with st.container(border=True):
                    status = get_live_status()
                    
                    if status["is_live"]:
                        st.success(f"✅ Class is LIVE: {status['topic']}")
                        st.markdown(f"**Current Link:** {status['link']}")
                        
                        # Direct Link Button
                        st.markdown(f"""
                            <div style="text-align:center; margin: 20px;">
                                <a href="{status['link']}" target="_blank" style="text-decoration:none;">
                                    <button style="background: linear-gradient(45deg, #00c853, #b2ff59); color: black; padding: 15px 30px; border: none; border-radius: 50px; font-weight: bold; font-size: 18px; cursor: pointer;">
                                        🎥 Enter Meeting
                                    </button>
                                </a>
                            </div>
                        """, unsafe_allow_html=True)

                        if st.button("End Class ⏹️", type="primary"):
                            set_live_status(False)
                            st.rerun()
                    else:
                        st.info("Start a new session")
                        with st.form("start_live"):
                            topic = st.text_input("Class Topic", placeholder="e.g., Thermodynamics Part 2")
                            # Flexible meeting link input
                            meet_link = st.text_input("Meeting Link", placeholder="Paste Google Meet / Teams / Zoom link here...")
                            
                            if st.form_submit_button("Go Live 📡"):
                                if topic and meet_link:
                                    set_live_status(True, topic, meet_link)
                                    add_notification(f"🔴 Live Class Started: {topic}. Join now!")
                                    st.rerun()
                                else:
                                    st.warning("Please enter both Topic and Meeting Link")

            with col2:
                st.markdown("### 📢 Send Notification")
                with st.form("notif_form"):
                    msg = st.text_area("Announcement Message")
                    submitted = st.form_submit_button("Send Blast 🚀", use_container_width=True)
                    if submitted and msg:
                        add_notification(msg)
                        st.success("Notification Sent!")
                
                st.markdown("### 📜 History")
                with st.container(border=True):
                    for n in get_notifications()[:5]:
                        st.markdown(f"<small>{n['date']}</small><br>{n['message']}<hr>", unsafe_allow_html=True)

        else:
            # --- STUDENT DASHBOARD ---
            st.write("")
            status = get_live_status()
            
            if status["is_live"]:
                # Direct link button for Students
                st.markdown(f"""
                <div style="background: rgba(255, 0, 0, 0.1); border: 2px solid red; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 20px;">
                    <h1 style="color: #ff4444 !important; margin:0; font-size: 40px;">🔴 LIVE NOW</h1>
                    <h2 style="color: white !important; margin-top: 10px;">Topic: {status['topic']}</h2>
                    <br>
                    <div class="live-button-container">
                        <a href="{status['link']}" target="_blank" style="text-decoration:none;">
                            <button style="background: linear-gradient(45deg, #ff0000, #ff5252); color: white; padding: 20px 40px; border: none; border-radius: 50px; font-weight: bold; font-size: 24px; cursor: pointer; box-shadow: 0 0 20px rgba(255, 0, 0, 0.5);">
                                👉 CLICK TO JOIN CLASS
                            </button>
                        </a>
                    </div>
                    <p style="margin-top: 15px; color: #aaa;">(Opens Google Meet / Teams in new tab)</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 40px; text-align: center; border: 2px dashed #ffd700; border-radius: 15px; margin-bottom: 20px;">
                    <h2 style="color: #888 !important;">💤 No live class right now</h2>
                    <p>Check notifications below for schedule.</p>
                </div>
                """, unsafe_allow_html=True)

            # Notifications
            st.markdown("### 🔔 Notice Board")
            notifs = get_notifications()
            if notifs:
                for n in notifs:
                    st.markdown(f"""
                    <div class="notif-card">
                        <div style="color: #ffd700; font-size: 12px; font-weight: bold;">📅 {n['date']}</div>
                        <div style="color: white; font-size: 16px;">{n['message']}</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No new announcements.")

# ==========================================
# PAGE: SERVICES
# ==========================================
elif st.session_state.page == "Services":
    st.markdown("# 📚 Our Services")
    st.markdown("## 🎓 Subjects We Teach")
    sub1, sub2 = st.columns(2)
    with sub1:
        with st.container(border=True):
            st.markdown("### 📐 Mathematics")
            st.write("Classes 6-12 (CBSE/State/Commerce/Science)")
        st.write("")
        with st.container(border=True):
            st.markdown("### ⚗️ Chemistry")
            st.write("NEET/JEE Chemistry, Organic & Inorganic")
    with sub2:
        with st.container(border=True):
            st.markdown("### ⚡ Physics")
            st.write("Conceptual clarity & Numerical problem solving")
        st.write("")
        with st.container(border=True):
            st.markdown("### 🧬 Biology")
            st.write("Botany, Zoology & NEET Prep")

# ==========================================
# PAGE: TESTIMONIALS (FIXED FOR READABILITY)
# ==========================================
elif st.session_state.page == "Testimonials":
    st.markdown("# 💬 Student Success Stories")
    t1, t2 = st.columns(2)
    
    def testimonial_card(text, author):
        # NOTE: Using the .white-card-fix class defined in CSS
        st.markdown(f"""
        <div class="white-card-fix">
            <div style="color:#333; font-style:italic;">"{text}"</div>
            <div style="color:#2c5282; font-weight:bold; margin-top:10px; text-align:right;">- {author}</div>
        </div>
        """, unsafe_allow_html=True)

    with t1:
        testimonial_card("Sir's organic chemistry teaching helped me a lot!", "Pranav.S, Class 12")
        testimonial_card("Math grades improved from 60% to 95%.", "Mrs. Lakshmi, Parent")
    with t2:
        testimonial_card("Physics numericals used to scare me. Now I solve them confidently.", "Rahul M., JEE Aspirant")
        testimonial_card("The Python bootcamp was amazing!", "Divya S., College Student")

    st.write("")
    st.markdown("## 🏆 Our Results")
    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.markdown('<div class="white-card-fix" style="text-align:center;"><div style="color:#555;font-weight:bold;">Board Exams</div><div style="font-size:28px;color:black;font-weight:bold;">80%</div><div style="font-size:12px;color:#666;">Average Score</div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="white-card-fix" style="text-align:center;"><div style="color:#555;font-weight:bold;">Improvement</div><div style="font-size:28px;color:black;font-weight:bold;">60%</div><div style="font-size:12px;color:#666;">vs. Baseline</div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="white-card-fix" style="text-align:center;"><div style="color:#555;font-weight:bold;">Doubt Support</div><div style="font-size:28px;color:black;font-weight:bold;">&lt; 2 Hrs</div><div style="font-size:12px;color:#666;">Resolution Time</div></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("## 💡 Why Parents Trust Us")
    w1, w2, w3 = st.columns(3)
    
    with w1:
        st.markdown('<div class="white-card-fix"><h3 style="color:#2c5282;margin:0;">🎓 Expert Educator</h3><p style="color:#333;margin-top:10px;">One-on-one mentoring that identifies specific learning gaps.</p></div>', unsafe_allow_html=True)
    with w2:
        st.markdown('<div class="white-card-fix"><h3 style="color:#2c5282;margin:0;">🧠 Conceptual</h3><p style="color:#333;margin-top:10px;">No rote memorization. We focus on "Why" and "How".</p></div>', unsafe_allow_html=True)
    with w3:
        st.markdown('<div class="white-card-fix"><h3 style="color:#2c5282;margin:0;">💰 Fair Pricing</h3><p style="color:#333;margin-top:10px;">No hidden fees. Quality education for every family.</p></div>', unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.link_button("📱 Book Free Trial", "https://wa.me/917339315376", use_container_width=True)

# ==========================================
# PAGE: BOOTCAMP
# ==========================================
elif st.session_state.page == "Bootcamp":
    st.markdown("# 🐍 Python for Data Science & AI")
    boot1, boot2 = st.columns([1, 1.5])
    with boot1:
        if not render_image("poster", use_column_width=True):
            st.markdown("# 🐍")
    with boot2:
        with st.container(border=True):
            st.markdown("### Weekend Intensive Program")
            st.write("Master the most in-demand programming language")
            st.markdown("👨‍🏫 **Instructor:** Mohammed Salmaan M")
            st.markdown("📅 **Schedule:** Saturdays & Sundays")
            st.link_button("📱 Enroll Now", "https://wa.me/917339315376", use_container_width=True)

==========================================
# PAGE: CONTACT
# ==========================================
elif st.session_state.page == "Contact":
    st.markdown("# 📞 Get In Touch")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        with st.container(border=True):
            st.markdown("### Contact Information")
            st.write("")
            
            st.markdown("**📱 Phone**")
            st.write("+91 73393 15376")
            st.write("")
            
            st.markdown("**✉️ Email**")
            st.markdown(
                """
                <div style="
                    display: inline-block;
                    background-color: #ffffff;
                    padding: 10px 20px;
                    border-radius: 25px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    border: 1px solid #e0e0e0;
                ">
                    <a href="mailto:the.molecularmanexpert@gmail.com" style="text-decoration: none; display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 20px;">✉️</span>
                        <span style="
                            color: #333333 !important;
                            font-weight: bold;
                            font-size: 16px;
                            font-family: sans-serif;
                        ">
                            the.molecularmanexpert@gmail.com
                        </span>
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("")
            
            st.markdown("**🕒 Operating Hours**")
            st.write("Monday - Saturday: 9:00 AM - 9:00 PM")
            st.write("Sunday: Closed (AI Support Available 24/7)")
            st.write("")
            
            st.link_button("💬 WhatsApp Us", "[https://wa.me/917339315376](https://wa.me/917339315376)", use_container_width=True)
    
    with c2:
        with st.container(border=True):
            st.markdown("### Send us a Message")
            
            # UNIQUE KEY for this form to prevent duplicate key errors
            with st.form("contact_page_form_unique"):
                name = st.text_input("Your Name")
                phone = st.text_input("Phone Number")
                email = st.text_input("Email (Optional)")
                grade = st.selectbox("Student's Grade", 
                    ["6-8", "9-10", "11-12 (Science)", "11-12 (Commerce)", "College/Other"])
                message = st.text_area("Message", height=120)
                
                # CORRECTED INDENTATION: Button inside the form
                submitted = st.form_submit_button("Send Message", use_container_width=True)

                if submitted:
                    if name and phone:
                        try:
                            # 1. Prepare data
                            form_data = {
                                "name": name,
                                "phone": phone,
                                "email": email,
                                "grade": grade,
                                "message": message,
                                "_subject": f"New Inquiry from {name}",
                                "_captcha": "false"
                            }

                            # 2. Send to FormSubmit
                            # URL is constructed safely by joining strings to guarantee no hidden spaces
                            url = "https://" + "formsubmit.co/the.molecularmanexpert@gmail.com"
                            response = requests.post(url, data=form_data)

                            # 3. Success Message
                            if response.status_code == 200:
                                st.markdown(
                                    """
                                    <div style="
                                        background-color: #a7e4d8; 
                                        padding: 15px; 
                                        border-radius: 10px; 
                                        color: black; 
                                        font-weight: bold; 
                                        border: 1px solid #6ccec0;
                                        margin-top: 10px;
                                    ">
                                        ✅ Thank you! We'll contact you within 24 hours.
                                    </div>
                                    """,
                                    unsafe_allow_html=True
                                )
                                st.balloons()
                            else:
                                st.error("⚠️ Connection error. Please try again.")
                        
                        except Exception as e:
                            st.error(f"⚠️ Error: {e}")

                    else:
                        st.warning("⚠️ Please fill in your name and phone number.")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.write("")
st.write("")
with st.container(border=True):
    # 1. CSS Animation Logic
    st.markdown("""
        <style>
        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .animated-footer-text {
            font-weight: 800;
            font-size: 24px;
            text-transform: uppercase;
            text-align: center;
            letter-spacing: 2px;
            /* The Color Gradient: Add more colors here if you want */
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 300%;
            
            /* Clip the background to the text */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent; 
            background-clip: text;
            color: transparent;
            
            /* The Animation Speed */
            animation: gradient-animation 10s ease infinite;
        }
        </style>
        
        <div class="animated-footer-text">
            PRECISE • PASSIONATE • PROFESSIONAL
        </div>
    """, unsafe_allow_html=True)
    
    # The Copyright Caption
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 12px; margin-top: 10px;'>"
        "© 2026 The Molecular Man Expert Tuition Solutions | Mohammed Salmaan M. All Rights Reserved."
        "</div>", 
        unsafe_allow_html=True
    )
