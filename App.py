import streamlit as st
import os
import json
import base64
import datetime
import uuid
import requests
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

if "aya_messages" not in st.session_state:
    st.session_state.aya_messages = []

if 'mt_questions' not in st.session_state: st.session_state.mt_questions = None
if 'mt_answers' not in st.session_state: st.session_state.mt_answers = {}
if 'mt_feedback' not in st.session_state: st.session_state.mt_feedback = None

NOTIFICATIONS_FILE = "notifications.json"
LIVE_STATUS_FILE = "live_status.json"

def init_files():
    if not os.path.exists(NOTIFICATIONS_FILE):
        with open(NOTIFICATIONS_FILE, "w") as f:
            json.dump([], f)
    if not os.path.exists(LIVE_STATUS_FILE):
        with open(LIVE_STATUS_FILE, "w") as f:
            json.dump({"is_live": False, "topic": "", "link": ""}, f)

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

def get_notifications():
    try:
        with open(NOTIFICATIONS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def get_live_status():
    try:
        with open(LIVE_STATUS_FILE, "r") as f:
            return json.load(f)
    except:
        return {"is_live": False, "topic": "", "link": ""}

# -----------------------------------------------------------------------------
# 4. CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
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
    div.stButton > button {
        background: linear-gradient(90deg, #1e3a5f, #3b6b9e, #1e3a5f);
        color: white !important; border-radius: 25px !important; border: 1px solid rgba(255,255,255,0.2) !important;
    }
    div.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
    div[data-testid="stFormSubmitButton"] > button {
        background: #1e3a5f !important; color: #ffffff !important; border: 2px solid white !important;
    }
    div[data-testid="stFormSubmitButton"] > button p { color: #ffffff !important; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div {
        background-color: rgba(255, 255, 255, 0.1) !important; color: #ffffff !important; border-radius: 8px; border: 1px solid rgba(255,255,255,0.3) !important;
    }
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
    /* Founder Header */
    .founder-header-container {
        text-align: center; padding: 25px 15px; background: rgba(0, 0, 0, 0.2);
        border-radius: 20px; margin-bottom: 25px; border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .founder-headline { font-size: 2.2rem; font-weight: 900; color: #ffffff; margin-bottom: 12px; }
    .founder-subhead { font-size: 1.2rem; color: #e0f7fa; font-weight: 500; }
    .founder-tagline { color: #ffd700; font-style: italic; font-weight: 800; letter-spacing: 1.5px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. NAVIGATION
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

    # 2. FIXED DYNAMIC ADVERTISEMENT (No Indentation)
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
    
    status = get_live_status()
    if status["is_live"]:
        st.markdown(f"""
        <div style="background: rgba(255, 0, 0, 0.1); border: 2px solid red; padding: 30px; border-radius: 15px; text-align: center;">
            <h1 style="color: #ff4444 !important;">🔴 LIVE NOW</h1>
            <h2>Topic: {status['topic']}</h2>
            <br>
            <a href="{status['link']}" target="_blank" style="background:red;color:white;padding:10px 20px;border-radius:20px;text-decoration:none;">🎥 JOIN GOOGLE MEET</a>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### 💤 Class is offline")
    
    st.markdown("### 🔔 Notice Board")
    for n in get_notifications():
        st.markdown(f"**{n['date']}**: {n['message']}")
        st.markdown("---")

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
# PAGE: TESTIMONIALS
# ==========================================
elif st.session_state.page == "Testimonials":
    st.markdown("# 💬 Student Success Stories")
    t1, t2 = st.columns(2)
    def testimonial_card(text, author):
        st.markdown(f"""
        <div style="background:white; padding:20px; border-radius:10px; border-left:5px solid #2c5282; margin-bottom:20px;">
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

# ==========================================
# PAGE: CONTACT
# ==========================================
elif st.session_state.page == "Contact":
    st.markdown("# 📞 Get In Touch")
    c1, c2 = st.columns([1, 1])
    with c1:
        with st.container(border=True):
            st.markdown("### Contact Information")
            st.markdown("**📱 Phone:** +91 73393 15376")
            st.markdown("**✉️ Email:** the.molecularmanexpert@gmail.com")
            st.link_button("💬 WhatsApp Us", "https://wa.me/917339315376", use_container_width=True)
    with c2:
        with st.container(border=True):
            st.markdown("### Send us a Message")
            with st.form("contact_page_form"):
                name = st.text_input("Name")
                phone = st.text_input("Phone")
                msg = st.text_area("Message")
                if st.form_submit_button("Send Message", use_container_width=True):
                    if name and phone:
                        try:
                            url = "https://formsubmit.co/the.molecularmanexpert@gmail.com"
                            requests.post(url, data={"name": name, "phone": phone, "message": msg, "_captcha": "false"})
                            st.success("✅ Thank you! We'll contact you shortly.")
                        except: st.error("Connection Error")
                    else: st.warning("Please fill details")

# Footer
st.write("")
st.markdown("""
    <div style='text-align: center; color: rgba(255,255,255,0.5); padding: 20px;'>
        <p>© 2026 The Molecular Man Expert Tuition Solutions | Mohammed Salmaan M.</p>
    </div>
""", unsafe_allow_html=True)
