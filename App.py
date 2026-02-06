import streamlit as st
import os
import json
import hashlib
import uuid
import datetime
import requests
from PIL import Image
import base64
import io
import sys
from groq import Groq
from openai import OpenAI
import PyPDF2

# Fix console encoding for Mock Test
try:
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

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
# Navigation State
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Auth State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False
if "device_id" not in st.session_state:
    st.session_state.device_id = str(uuid.uuid4())

# Mock Test State
if 'questions' not in st.session_state:
    st.session_state.questions = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'feedback' not in st.session_state:
    st.session_state.feedback = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_marks' not in st.session_state:
    st.session_state.total_marks = 0
if 'q_type' not in st.session_state:
    st.session_state.q_type = "MCQ"

# Files
USERS_FILE = "users_database.json"
SESSIONS_FILE = "active_sessions.json"
NOTIFICATIONS_FILE = "notifications.json"
LIVE_STATUS_FILE = "live_status.json"

# Database Init Functions
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
    if not os.path.exists(SESSIONS_FILE):
        with open(SESSIONS_FILE, "w") as f:
            json.dump({}, f)

create_users_db()
init_files()

# -----------------------------------------------------------------------------
# 3. HELPER FUNCTIONS
# -----------------------------------------------------------------------------

# --- Image Handling ---
def get_image_path(filename_base):
    extensions = [".png", ".jpg", ".jpeg", ".webp", ".gif"]
    paths = [f"images/{filename_base}", f"assets/{filename_base}", filename_base, f"./{filename_base}"]
    for path in paths:
        for ext in extensions:
            full_path = path + ext
            if os.path.exists(full_path):
                return full_path
            if os.path.exists(full_path.upper()):
                return full_path.upper()
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

def get_img_as_base64(file_path):
    """Converts image to base64 for embedding in HTML"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# --- Authentication & Data ---
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

# --- AyA AI Functions ---
def solve_problem(groq_client, question_text, uploaded_file, file_type):
    try:
        base_prompt = """You are 'Aya', a highly intelligent AI teaching assistant developed by Mohammed Salmaan M for The Molecular Man Expert Tuition Solutions.

Your expertise covers: Mathematics, Physics, Chemistry, and Biology for Classes 6-12 (CBSE/ISC/IGCSE/IB), NEET, and JEE preparation.

INSTRUCTIONS:
1. Analyze the problem carefully
2. Provide step-by-step explanations
3. Show ALL calculation steps
4. Explain the concepts involved
5. Highlight common mistakes to avoid
6. Format your answer clearly using markdown

If the problem contains an image, describe what you see first, then solve it."""

        if file_type == "image":
            image = Image.open(uploaded_file)
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_b64 = base64.b64encode(buffered.getvalue()).decode()
            
            for model in ["llama-3.2-90b-vision-preview", "llama-3.2-11b-vision-preview"]:
                try:
                    message = groq_client.chat.completions.create(
                        model=model,
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": base_prompt + "\n\nAnalyze this image and solve the problem:"},
                                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}}
                                ]
                            }
                        ],
                        max_tokens=2048,
                        temperature=0.5
                    )
                    break
                except:
                    continue
        
        elif file_type == "pdf":
            try:
                pdf_reader = PyPDF2.PdfReader(uploaded_file)
                pdf_text = ""
                for page in pdf_reader.pages:
                    pdf_text += page.extract_text()
                
                prompt = base_prompt + f"\n\nPROBLEM FROM PDF:\n{pdf_text}"
                for model in ["llama-3.1-70b-versatile", "llama-3.1-8b-instant"]:
                    try:
                        message = groq_client.chat.completions.create(
                            model=model,
                            messages=[{"role": "user", "content": prompt}],
                            max_tokens=1024,
                            temperature=0.5
                        )
                        break
                    except:
                        continue
            except Exception as e:
                return f"Error reading PDF: {str(e)}"
        
        else:
            prompt = base_prompt + f"\n\nPROBLEM:\n{question_text}"
            for model in ["llama-3.1-70b-versatile", "llama-3.1-8b-instant"]:
                try:
                    message = groq_client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=1024,
                        temperature=0.5
                    )
                    break
                except:
                    continue
        
        if 'message' in locals():
            response_text = message.choices[0].message.content
            return response_text
        else:
            return "❌ Error: Could not connect to AI services. Please try again."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Mock Test Functions ---
def get_groq_client(api_key):
    return OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )

def clean_input(text):
    if not text: return ""
    return text.encode('ascii', 'ignore').decode('ascii').strip()

def generate_questions_groq(api_key, model, board, cls, sub, chap, num, diff, q_type):
    client = get_groq_client(api_key)
    safe_sub = clean_input(sub)
    safe_chap = clean_input(chap)
    
    context = (
        f"You are a strict Textbook Author and Examiner for the {board} Board. "
        f"Subject: {safe_sub}, Class: {cls}, Chapter: '{safe_chap}'.\n"
        f"CRITICAL RULES:\n"
        f"1. Questions must be factually 100% correct according to standard {board} textbooks.\n"
        f"2. Avoid ambiguous questions. There must be exactly one indisputable correct answer.\n"
        f"3. Use questions from Past Year Papers where possible.\n"
    )

    if q_type == "MCQ":
        prompt = f"""
        {context}
        Create a strictly valid JSON list of {num} {diff}-level Multiple Choice Questions (MCQs).
        
        JSON Format:
        [
            {{
                "id": 1, 
                "question": "Question text?", 
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": "Option A"
            }}
        ]
        VERIFICATION STEP: Before outputting, check that 'correct_answer' matches one of the 'options' exactly and is factually true.
        Return ONLY raw JSON.
        """
    else:
        prompt = f"""
        {context}
        Create a strictly valid JSON list of {num} {diff}-level Descriptive Questions.
        Include 'marks' (e.g., 2, 3, 5).
        
        JSON Format:
        [
            {{
                "id": 1, 
                "question": "Question text?", 
                "marks": 3
            }}
        ]
        Return ONLY raw JSON.
        """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a precise academic assistant. You do not hallucinate facts. You output strictly valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1 
        )
        content = response.choices[0].message.content.strip()
        if "```" in content:
            content = content.replace("```json", "").replace("```", "")
        return json.loads(content)
    except Exception as e:
        st.error(f"Error generating questions: {str(e)}")
        return None

def grade_mcq(api_key, model, questions, user_answers, board, cls, sub):
    client = get_groq_client(api_key)
    score = 0
    incorrect_log = ""
    
    for q in questions:
        q_id = str(q['id'])
        u_ans = user_answers.get(q_id)
        c_ans = q['correct_answer']
        if u_ans == c_ans:
            score += 1
        else:
            incorrect_log += f"Q: {q['question']}\nStudent Answer: {u_ans}\nCorrect Answer: {c_ans}\n\n"
            
    st.session_state.score = score
    st.session_state.total_marks = len(questions)

    if score == len(questions):
        return "### Excellent! Perfect Score. \nYou have mastered this topic based on Board standards."
        
    prompt = f"""
    The student scored {score}/{len(questions)} in a {board} Class {cls} {sub} MCQ test.
    Mistakes:
    {incorrect_log}
    
    Provide a "Scope for Improvement" analysis. 
    Explain clearly WHY the student's answer was wrong and why the correct answer is correct.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error analyzing performance: {str(e)}"

def grade_descriptive(api_key, model, questions, user_answers, board, cls, sub):
    client = get_groq_client(api_key)
    qa_data = ""
    total_possible_marks = 0
    
    for q in questions:
        q_id = str(q['id'])
        u_ans = user_answers.get(q_id, "No Answer")
        marks = q.get('marks', 1)
        total_possible_marks += marks
        qa_data += f"Q ({marks} marks): {q['question']}\nStudent Answer: {u_ans}\n\n"
    
    st.session_state.total_marks = total_possible_marks

    prompt = f"""
    You are a strict examiner for {board} Class {cls} {sub}.
    Evaluate these descriptive answers based on standard Board marking schemes.
    
    Data:
    {qa_data}
    
    Output Requirements:
    1. Award marks for EACH question.
    2. Calculate Total Score obtained out of {total_possible_marks}.
    3. Provide "Scope for Improvement" pointing out missing keywords or concepts.
    4. Format clearly in Markdown.
    """

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error grading descriptive answers: {str(e)}"

# -----------------------------------------------------------------------------
# 4. CSS STYLING & FOUNDER HEADER
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* 1. Reduce Top Padding */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }

    /* 2. Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #4a90a4 0%, #6bb5c7 50%, #8fd4e3 100%) !important;
    }
    
    /* 3. FOUNDER HEADER STYLES */
    @keyframes flash-pulse {
        0% { opacity: 1; transform: scale(1); text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        50% { opacity: 0.85; transform: scale(1.01); text-shadow: 0 0 15px rgba(255, 255, 255, 0.8), 0 0 25px rgba(255, 255, 255, 0.5); }
        100% { opacity: 1; transform: scale(1); text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    }
    
    .founder-header-container {
        text-align: center;
        padding: 25px 15px;
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(5px);
    }
    
    .founder-headline {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 2.2rem;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 12px;
        line-height: 1.2;
        animation: flash-pulse 2.5s infinite ease-in-out;
    }
    
    .founder-subhead {
        font-size: 1.2rem;
        color: #e0f7fa;
        margin-bottom: 10px;
        font-weight: 500;
    }
    
    .founder-tagline {
        font-size: 1.0rem;
        color: #ffd700;
        font-style: italic;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 5px;
    }

    /* --- ANIMATED BUTTONS --- */
    div.stButton > button {
        background: linear-gradient(90deg, #1e3a5f, #3b6b9e, #1e3a5f);
        background-size: 200% auto;
        color: white !important;
        border-radius: 25px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        animation: gradient-move 3s linear infinite;
    }
    @keyframes gradient-move {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }
    div.stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 10px 20px rgba(30, 58, 95, 0.5), 0 0 15px rgba(255, 255, 255, 0.4) !important;
        border-color: #ffffff !important;
    }
    div.stButton > button:active {
        transform: scale(0.95) !important;
    }
    
    /* Live Class Pulse */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .live-join-btn {
        background: linear-gradient(45deg, #00897b, #00bfa5);
        color: white;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        animation: pulse 2s infinite;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    .live-join-btn:hover {
        color: white;
        background: linear-gradient(45deg, #00695c, #00897b);
    }

    /* Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div, .stNumberInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #333 !important;
        border-radius: 8px;
        border: 1px solid rgba(0,0,0,0.1);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.2);
        border-radius: 10px 10px 0 0;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffd700 !important;
        color: black !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* AI Corner Highlight */
    @keyframes rainbow-glow {
        0% { box-shadow: 0 0 10px #ff0080, 0 0 20px #ff0080; }
        25% { box-shadow: 0 0 10px #00ff80, 0 0 20px #00ff80; }
        50% { box-shadow: 0 0 10px #0080ff, 0 0 20px #0080ff; }
        75% { box-shadow: 0 0 10px #ff8000, 0 0 20px #ff8000; }
        100% { box-shadow: 0 0 10px #ff0080, 0 0 20px #ff0080; }
    }
    
    .ai-promo-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        animation: rainbow-glow 3s infinite;
        margin: 20px 0;
    }
    
    /* Radio buttons visibility fix */
    .stRadio label {
        color: #000000 !important;
        font-weight: 500 !important;
        background-color: rgba(255,255,255,0.8);
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. HEADER & NAVIGATION MENU
# -----------------------------------------------------------------------------

st.markdown("""
<div class="founder-header-container">
    <div class="founder-headline">Other Apps Were Coded by Engineers. This One Was Coded by Your Master Tutor - Mohammed Salmaan.</div>
    <div class="founder-subhead">The only online tuition service in the world running on a proprietary engine built by the Founder.</div>
    <div class="founder-tagline">Pure Teaching Intelligence. Zero Corporate Noise.</div>
</div>
""", unsafe_allow_html=True)

# Updated to 7 Columns (Added AI Corner)
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("🏠 Home", use_container_width=True): st.session_state.page = "Home"; st.rerun()
with col2:
    if st.button("📚 Services", use_container_width=True): st.session_state.page = "Services"; st.rerun()
with col3:
    if st.button("🔴 Live Class", use_container_width=True): st.session_state.page = "Live Class"; st.rerun()
with col4:
    if st.button("🤖 AI Corner", use_container_width=True): st.session_state.page = "AI Corner"; st.rerun()
with col5:
    if st.button("💬 Testimonials", use_container_width=True): st.session_state.page = "Testimonials"; st.rerun()
with col6:
    if st.button("🐍 Bootcamp", use_container_width=True): st.session_state.page = "Bootcamp"; st.rerun()
with col7:
    if st.button("📞 Contact", use_container_width=True): st.session_state.page = "Contact"; st.rerun()

st.write("")

# -----------------------------------------------------------------------------
# 6. PAGE LOGIC
# -----------------------------------------------------------------------------

# ==========================================
# PAGE: HOME
# ==========================================
if st.session_state.page == "Home":
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

    # ⭐ AI CORNER MEGA PROMOTION ⭐
    st.markdown("""
    <div class="ai-promo-box">
        <h1 style="margin: 0; font-size: 2.5rem;">🤖 INTRODUCING AI CORNER</h1>
        <h2 style="margin: 10px 0; font-weight: 600;">Your 24/7 AI-Powered Study Assistants!</h2>
        <p style="font-size: 1.2rem; margin: 15px 0;">
            ✨ <strong>AyA - The Molecular Man AI:</strong> Upload chemistry, physics, math, or biology problems and get instant expert solutions!<br>
            ✨ <strong>MolecularMan Mock Test:</strong> Generate custom practice tests for any subject, chapter, and difficulty level!
        </p>
        <p style="font-size: 1.4rem; font-weight: bold; margin-top: 20px; color: #ffd700;">
            🚀 FREE FOR ALL STUDENTS - AVAILABLE NOW!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Access to AI Tools
    ai1, ai2 = st.columns(2)
    with ai1:
        with st.container(border=True):
            st.markdown("### 🧪 AyA - The Molecular Man AI")
            st.write("Upload problems from any subject (Math, Physics, Chemistry, Biology) and get instant step-by-step solutions with detailed explanations!")
            if st.button("Launch AyA →", use_container_width=True, key="home_aya"):
                st.session_state.page = "AI Corner"
                st.rerun()
    
    with ai2:
        with st.container(border=True):
            st.markdown("### 🎯 MolecularMan Mock Test")
            st.write("Generate custom practice tests for any board, class, subject, and chapter. Get instant grading and personalized feedback!")
            if st.button("Launch Mock Test →", use_container_width=True, key="home_mt"):
                st.session_state.page = "AI Corner"
                st.rerun()

    st.markdown("## 📊 Our Impact")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Students Taught", "500+")
    with m2: st.metric("Success Rate", "100%")
    with m3: st.metric("AI Support", "24/7")
    with m4: st.metric("Experience", "5+ Years")

    st.markdown("## 🎯 What We Offer")
    s1, s2, s3 = st.columns(3)
    with s1:
        with st.container(border=True):
            st.markdown("#### 👨‍🏫 Expert Tutoring")
            st.write("One-on-one and small group classes for Classes 6-12.")
    with s2:
        with st.container(border=True):
            st.markdown("#### 🤖 AI-Powered Learning")
            st.write("24/7 AI tutors for instant homework help and mock test generation.")
    with s3:
        with st.container(border=True):
            st.markdown("#### 🐍 Python Bootcamp")
            st.write("Weekend intensive courses in Data Science & AI with hands-on projects.")

# ==========================================
# PAGE: AI CORNER
# ==========================================
elif st.session_state.page == "AI Corner":
    st.markdown("# 🤖 AI Corner - Your Digital Study Assistants")
    
    st.markdown("""
    <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; text-align: center; color: white; margin-bottom: 30px;">
        <h2 style="margin: 0;">Welcome to the Future of Learning!</h2>
        <p style="margin: 10px 0; font-size: 1.1rem;">Choose your AI assistant below and get instant help with your studies 24/7</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for the two AI tools
    tab1, tab2 = st.tabs([" AyA - The Molecular Man AI", " MolecularMan Mock Test"])
    
    with tab1:
        st.markdown("### AyA: The Universal Problem Solver")
        st.markdown("""
        **What AyA Can Do:**
        - ✅ Solve complex problems in Math, Physics, Chemistry, and Biology
        - ✅ Analyze images, diagrams, and handwritten problems
        - ✅ Provide step-by-step explanations with detailed concepts
        - ✅ Extract and solve problems from PDF documents
        - ✅ Perfect for NEET/JEE/Board exam preparation
        - ✅ Available 24/7 for instant homework help
        """)
        
        st.divider()
        
        # AyA AI Implementation
        t.set_page_config(
    page_title="The Molecular Man AI",
    page_icon="logo.jpg",  # Using the logo as the browser tab icon
    layout="wide"
)

# -----------------------------------------------------------------------------
# HELPER: IMAGE TO BASE64 (For HTML Styling)
# -----------------------------------------------------------------------------
def get_img_as_base64(file_path):
    """Converts image to base64 for embedding in HTML"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# -----------------------------------------------------------------------------
# REDESIGNED CSS - DEEP BLUE & GOLD THEME
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* 1. Main Background - Deep Scientific Blue Gradient */
    .stApp {
        background: linear-gradient(135deg, #004e92 0%, #000428 100%) !important;
        background-attachment: fixed;
    }
    
    /* 2. Text Coloring - Force White for readability */
    h1, h2, h3, h4, h5, h6, p, div, span, li, label, .stMarkdown {
        color: #ffffff !important;
    }
    
    /* 3. Streamlit Containers (Cards) Styling */
    div[data-testid="stVerticalBlockBorderWrapper"], .login-container {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* 4. Buttons - Gold Gradient */
    .stButton > button {
        background: linear-gradient(to bottom, #ffd700 0%, #ffb900 100%) !important;
        color: #000000 !important;
        border-radius: 50px !important;
        border: none !important;
        font-weight: 800 !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(to bottom, #ffed4a 0%, #ffca00 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6) !important;
        color: #000000 !important;
    }
    
    /* 5. Inputs - Semi-transparent white */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea, 
    .stSelectbox > div > div > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    /* 6. Tabs styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255,255,255,0.1);
        border-radius: 10px 10px 0 0;
        color: white;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffd700 !important;
        color: black !important;
    }

    /* 7. Logo Styling */
    .logo-img {
        border-radius: 50%;
        border: 3px solid #ffd700;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
    }

    /* Hide Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# AUTHENTICATION & DATABASE
# -----------------------------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None
if "device_id" not in st.session_state:
    st.session_state.device_id = str(uuid.uuid4())

USERS_FILE = "users_database.json"
SESSIONS_FILE = "active_sessions.json"

def create_empty_database():
    # REMEMBER: Delete users_database.json manually to apply new passwords
    if not os.path.exists(USERS_FILE):
        default_user = {
            "Mohammed": hashlib.sha256("Molsalmaan@9292".encode()).hexdigest(),
            "Muskan": hashlib.sha256("mus1234kan".encode()).hexdigest(),
            "Prithwin": hashlib.sha256("prithwin".encode()).hexdigest()
        }
        with open(USERS_FILE, "w") as f:
            json.dump(default_user, f)

def create_empty_sessions():
    if not os.path.exists(SESSIONS_FILE):
        with open(SESSIONS_FILE, "w") as f:
            json.dump({}, f)

create_empty_database()
create_empty_sessions()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    try:
        with open(USERS_FILE, "r") as f:
            all_users = json.load(f)
        if username not in all_users:
            return False
        return all_users[username] == hash_password(password)
    except:
        return False

def is_user_logged_elsewhere(username, current_device_id):
    try:
        with open(SESSIONS_FILE, "r") as f:
            sessions = json.load(f)
        if username in sessions:
            if sessions[username] != current_device_id:
                return True
        return False
    except:
        return False

def save_session(username, device_id):
    try:
        with open(SESSIONS_FILE, "r") as f:
            sessions = json.load(f)
    except:
        sessions = {}
    sessions[username] = device_id
    with open(SESSIONS_FILE, "w") as f:
        json.dump(sessions, f)

def remove_session(username):
    try:
        with open(SESSIONS_FILE, "r") as f:
            sessions = json.load(f)
        if username in sessions:
            del sessions[username]
        with open(SESSIONS_FILE, "w") as f:
            json.dump(sessions, f)
    except:
        pass

def add_new_user(username, password):
    try:
        with open(USERS_FILE, "r") as f:
            all_users = json.load(f)
    except:
        all_users = {}
        
    if username in all_users:
        return False, "Username already exists!"
    all_users[username] = hash_password(password)
    with open(USERS_FILE, "w") as f:
        json.dump(all_users, f)
    return True, "User created successfully!"

# -----------------------------------------------------------------------------
# AI SOLVER LOGIC
# -----------------------------------------------------------------------------
def solve_problem(groq_client, question_text, file_obj=None, file_type=None):
    try:
        base_prompt = """### ROLE DEFINITION
You are **Aya**, the Lead AI Tutor at **The Molecular Man Expert Tuition Solutions**. 
Your Mission: Guide students on a journey from "Zero" (absolute beginner) to "Hero" (advanced mastery) in any subject. 
Your Tone: Encouraging, clear, patient, and intellectually rigorous when required.

### THE "ZERO TO HERO" FRAMEWORK
Before answering, assess the complexity of the user's query and the likely proficiency level. Adapt your response using one of these three modes:

**MODE A: THE BUILDER (Level: Zero/Beginner)**
* **Trigger:** Simple questions, confusion, or new topics.
* **Strategy:** Use analogies, real-world metaphors, and plain language. Avoid dense jargon.
* **Goal:** Build intuition. Help them understand "Why does this exist?"

**MODE B: THE SCHOLAR (Level: Intermediate)**
* **Trigger:** Homework problems, specific questions, or exam preparation.
* **Strategy:** Use standard academic terminology, step-by-step logic, and structured problem-solving.
* **Goal:** Build competence. Help them understand "How do I solve this?"

**MODE C: THE EXPERT (Level: Hero/Advanced)**
* **Trigger:** Complex theoretical questions, edge cases, or requests for deep analysis.
* **Strategy:** Use strict international standards (ISO, IUPAC, SI), technical nuance, and formal notation. 
* **Goal:** Build mastery. Help them understand "What are the deeper implications?"

### UNIVERSAL RESPONSE STRUCTURE
Regardless of the subject, structure your response as follows to ensure clarity:

1.  **🧠 CONCEPT (The "What"):** * Briefly define the core concept. 
    * *If Mode A:* Use an analogy (e.g., "Think of voltage like water pressure...").
    * *If Mode C:* Use the formal definition.

2.  **🌍 REAL-WORLD CONTEXT (The "Why"):** * One sentence on where this is used in real life (e.g., in nature, industry, or daily life).

3.  **✍️ SOLUTION / ANALYSIS (The "How"):** * **For Math/Science:** Provide a Step-by-Step calculation. State the formula first.
    * **For Humanities/Arts:** Provide a structured argument, timeline, or grammatical breakdown.
    * **Visual Aid:** Use simple text diagrams or tables if they clarify the point.

4.  **✅ ANSWER:** * The final result, clearly boxed or bolded. 
    * Include units and significant figures where applicable.

5.  **🚀 HERO TIP (The "Edge"):** * A "Pro Tip" to move them toward mastery. This could be a common trap to avoid, a shortcut, or a connection to a more advanced topic.

### GUIDELINES
* **Formatting:** Use Bold for keywords. Use bullet points for readability. Use LaTeX for math equations.
* **Safety:** Do not do the homework *for* them if they ask for an essay; provide the outline and key points. For math, show the full working.
* **Verification:** If the topic involves facts (History, Science), verify against standard academic consensus."""

        if file_type == "image" and file_obj:
            try:
                image = Image.open(file_obj)
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                img_base64 = base64.standard_b64encode(buffered.getvalue()).decode("utf-8")
                
                prompt = base_prompt + "\n\nSOLVE THE PROBLEM IN THIS IMAGE:"
                
                # Model selection strategy for vision
                for model in ["llama-3.2-11b-vision-preview", "llama-3.2-90b-vision-preview"]:
                    try:
                        message = groq_client.chat.completions.create(
                            model=model,
                            messages=[{
                                "role": "user", 
                                "content": [
                                    {"type": "text", "text": prompt},
                                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}}
                                ]
                            }],
                            max_tokens=1024,
                            temperature=0.5
                        )
                        break
                    except Exception as e:
                        continue
            except Exception as e:
                return f"Error processing image: {str(e)}"
        
        elif file_type == "pdf" and file_obj:
            try:
                pdf_reader = PyPDF2.PdfReader(file_obj)
                pdf_text = ""
                for page_num in range(min(2, len(pdf_reader.pages))):
                    page = pdf_reader.pages[page_num]
                    pdf_text += page.extract_text()[:1000]
                
                prompt = base_prompt + f"\n\nPROBLEM from PDF:\n{pdf_text}"
                
                for model in ["llama-3.1-70b-versatile", "llama-3.1-8b-instant", "gemma-7b-it"]:
                    try:
                        message = groq_client.chat.completions.create(
                            model=model,
                            messages=[{"role": "user", "content": prompt}],
                            max_tokens=1024,
                            temperature=0.5
                        )
                        break
                    except:
                        continue
            except Exception as e:
                return f"Error reading PDF: {str(e)}"
        
        else:
            prompt = base_prompt + f"\n\nPROBLEM:\n{question_text}"
            for model in ["llama-3.1-70b-versatile", "llama-3.1-8b-instant", "gemma-7b-it"]:
                try:
                    message = groq_client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=1024,
                        temperature=0.5
                    )
                    break
                except:
                    continue
        
        if 'message' in locals():
            response_text = message.choices[0].message.content
            return response_text
        else:
            return "❌ Error: Could not connect to AI services. Please try again."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# -----------------------------------------------------------------------------
# LOGIN PAGE
# -----------------------------------------------------------------------------
def show_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Display Logo Centered
        try:
            # We use columns here to perfectly center the image
            c_l, c_c, c_r = st.columns([1, 2, 1])
            with c_c:
                st.image("logo.jpg", use_container_width=True)
        except:
            st.markdown('<div class="login-header">🧪</div>', unsafe_allow_html=True)
            
        st.markdown('<div class="login-header" style="font-size: 32px; text-align: center; color: #ffd700; font-weight: bold; margin-bottom: 20px; margin-top: 10px; text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);">The Molecular Man AI</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            tab1, tab2 = st.tabs(["🔓 Login", "🆕 Create Account"])
            
            with tab1:
                st.markdown("### Access Your Account")
                username = st.text_input("👤 Username", key="login_user")
                password = st.text_input("🔐 Password", type="password", key="login_pass")
                st.write("")
                
                if st.button("Login 🚀", use_container_width=True):
                    if not username or not password:
                        st.error("❌ Please enter both username and password")
                    elif login_user(username, password):
                        if is_user_logged_elsewhere(username, st.session_state.device_id):
                            st.warning("⚠️ You were logged out from another device.")
                        save_session(username, st.session_state.device_id)
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.success("✅ Login Successful!")
                        st.rerun()
                    else:
                        st.error("❌ Invalid username or password")
            
            with tab2:
                st.markdown("### Create New Account")
                st.info("📌 Ask Admin (Mohammed) for the secret key")
                
                secret_key = st.text_input("🔑 Admin Secret Key", type="password", key="create_secret")
                new_username = st.text_input("👤 New Username", key="create_user")
                new_password = st.text_input("🔐 New Password", type="password", key="create_pass")
                confirm_password = st.text_input("🔐 Confirm Password", type="password", key="confirm_pass")
                st.write("")
                
                if st.button("Create Account ⚡", use_container_width=True):
                    if secret_key != "Ayasalmaan@9292":
                        st.error("❌ Invalid admin secret key")
                    elif not new_username or not new_password:
                        st.error("❌ Please fill all fields")
                    elif new_password != confirm_password:
                        st.error("❌ Passwords don't match")
                    elif len(new_password) < 4:
                        st.error("❌ Password too short (min 4 chars)")
                    else:
                        success, message = add_new_user(new_username, new_password)
                        if success:
                            st.success(f"✅ {message} Please Login.")
                        else:
                            st.error(f"❌ {message}")

# -----------------------------------------------------------------------------
# MAIN APP
# -----------------------------------------------------------------------------
def show_main_app():
    # Header Section with Flexbox for professional Logo alignment
    col1, col2 = st.columns([3, 1], vertical_alignment="center")
    
    with col1:
        # Prepare logo in Base64 for HTML embedding
        logo_b64 = get_img_as_base64("logo.jpg")
        
        if logo_b64:
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 20px;">
                    <img src="data:image/jpg;base64,{logo_b64}" width="100" class="logo-img">
                    <div>
                        <h1 style="margin: 0; font-size: 32px; color: white;">The Molecular Man</h1>
                        <p style="margin: 0; color: #ffd700; font-size: 16px;">Expert Tuition Solutions AI</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Fallback if image not found
            st.markdown("""
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div style="font-size: 40px;">🧪</div>
                    <div>
                        <h1 style="margin: 0; font-size: 32px; color: white;">The Molecular Man</h1>
                        <p style="margin: 0; color: #ffd700; font-size: 16px;">Expert Tuition Solutions AI</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<div style='text-align: right; color: white; margin-bottom: 5px;'>👤 {st.session_state.username}</div>", unsafe_allow_html=True)
        if st.button("Logout 🚪", use_container_width=True):
            remove_session(st.session_state.username)
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
    
    st.write("")
    
    # API Setup
    try:
        groq_api_key = st.secrets["GROQ_API_KEY"]
        groq_client = Groq(api_key=groq_api_key)
    except Exception:
        st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets!")
        st.stop()
    
    # Main Content
    with st.container(border=True):
        st.markdown("### 🤖 Aya - Universal Problem Solver")
        st.markdown("Upload a photo or paste text for Algebra, Physics, Chemistry, or Biology problems.")
        
        input_type = st.radio("Select Input Method:", 
                            ["📄 Text Problem", "🖼️ Upload Image", "📕 Upload PDF"], 
                            horizontal=True)
        
        user_question = None
        uploaded_file = None
        file_type = None
        
        if input_type == "📄 Text Problem":
            user_question = st.text_area("Paste your question here:", height=150)
        elif input_type == "🖼️ Upload Image":
            uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "webp"])
            if uploaded_file:
                st.image(uploaded_file, caption="Preview", width=300)
                file_type = "image"
        elif input_type == "📕 Upload PDF":
            uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
            if uploaded_file:
                st.info(f"📄 File: {uploaded_file.name}")
                file_type = "pdf"
        
        st.write("")
        if st.button("Solve Problem 🚀", use_container_width=True):
            if input_type == "📄 Text Problem" and not user_question:
                st.warning("⚠️ Please enter a question.")
            elif (input_type != "📄 Text Problem") and not uploaded_file:
                st.warning("⚠️ Please upload a file.")
            else:
                with st.spinner("🤖 Aya is analyzing... (This may take a moment)"):
                    solution = solve_problem(groq_client, user_question, uploaded_file, file_type)
                    
                    st.write("")
                    st.markdown("### 💡 Solution")
                    with st.container(border=True):
                        st.markdown(solution)
                        st.markdown("---")
                        st.caption("Generated by Aya AI Model | The Molecular Man")

    st.write("")
    st.markdown("""
        <div style='text-align: center; color: rgba(255,255,255,0.5); padding: 20px;'>
            <p>Developed by Mohammed Salmaan M | The Molecular Man Expert Tuition Solutions<br>
            Madurai, Tamil Nadu</p>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# RUN
# -----------------------------------------------------------------------------
if st.session_state.logged_in:
    show_main_app()
else:
    show_login_page()
        # Mock Test Implementation
        try:
            groq_api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets!")
            st.stop()
        
        # Sidebar Configuration
        with st.sidebar:
            st.markdown("## 🎯 Test Configuration")
            
            board = st.selectbox("Board", ["CBSE", "ISC", "IGCSE", "IB", "State Board"], key="mt_board")
            cls = st.selectbox("Class", [f"Class {i}" for i in range(6, 13)], key="mt_class")
            sub = st.text_input("Subject", placeholder="e.g., Physics, Chemistry", key="mt_sub")
            chap = st.text_input("Chapter Name", placeholder="e.g., Thermodynamics", key="mt_chap")
            
            st.divider()
            
            num_q = st.number_input("Number of Questions", min_value=1, max_value=20, value=5, key="mt_num")
            diff = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"], key="mt_diff")
            q_type = st.radio("Question Type", ["MCQ", "Descriptive"], key="mt_qtype")
            st.session_state.q_type = q_type
            
            model = st.selectbox("AI Model", 
                               ["llama-3.1-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
                               key="mt_model")
            
            st.divider()
            
            if st.button("🚀 Generate Test", use_container_width=True, key="mt_generate"):
                if not sub or not chap:
                    st.error("Please enter Subject and Chapter!")
                else:
                    with st.spinner("🤖 Generating your test..."):
                        st.session_state.questions = generate_questions_groq(
                            groq_api_key, model, board, cls, sub, chap, num_q, diff, q_type
                        )
                        st.session_state.user_answers = {}
                        st.session_state.feedback = None
                        if st.session_state.questions:
                            st.success(f"✅ {num_q} questions generated!")
                        else:
                            st.error("Failed to generate questions. Try again.")
            
            if st.session_state.questions and st.button("🔄 Reset Test", use_container_width=True, key="mt_reset"):
                st.session_state.questions = None
                st.session_state.user_answers = {}
                st.session_state.feedback = None
                st.rerun()
        
        # Main Test Area
        if st.session_state.questions:
            st.markdown(f"### 📝 {q_type} Test: {chap} ({board} - {cls})")
            
            with st.form("test_form"):
                for idx, q in enumerate(st.session_state.questions, 1):
                    st.markdown(f"**Q{idx}.** {q['question']}")
                    
                    if q_type == "MCQ":
                        answer = st.radio(
                            f"Select Answer for Q{idx}:",
                            options=q['options'],
                            key=f"q_{q['id']}",
                            index=None
                        )
                        if answer:
                            st.session_state.user_answers[str(q['id'])] = answer
                    else:
                        answer = st.text_area(
                            f"Your Answer ({q.get('marks', 1)} marks):",
                            key=f"q_{q['id']}",
                            height=100
                        )
                        if answer:
                            st.session_state.user_answers[str(q['id'])] = answer
                    
                    st.divider()
                
                submitted = st.form_submit_button("📊 Submit Test", use_container_width=True)
                
                if submitted:
                    if len(st.session_state.user_answers) != len(st.session_state.questions):
                        st.warning("⚠️ Please answer all questions before submitting!")
                    else:
                        with st.spinner("🤖 Grading your test..."):
                            if q_type == "MCQ":
                                st.session_state.feedback = grade_mcq(
                                    groq_api_key, model, st.session_state.questions,
                                    st.session_state.user_answers, board, cls, sub
                                )
                            else:
                                st.session_state.feedback = grade_descriptive(
                                    groq_api_key, model, st.session_state.questions,
                                    st.session_state.user_answers, board, cls, sub
                                )
            
            # Display Results
            if st.session_state.feedback:
                st.success("✅ Test Graded!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Your Score", f"{st.session_state.score}/{st.session_state.total_marks}")
                with col2:
                    percentage = (st.session_state.score / st.session_state.total_marks * 100) if st.session_state.total_marks > 0 else 0
                    st.metric("Percentage", f"{percentage:.1f}%")
                
                st.markdown("### 📈 Detailed Feedback")
                with st.container(border=True):
                    st.markdown(st.session_state.feedback)
        
        else:
            st.info("👈 Configure your test settings in the sidebar and click 'Generate Test' to begin!")


# ==========================================
# PAGE: LIVE CLASS
# ==========================================
elif st.session_state.page == "Live Class":
    st.markdown("# 🔴 Molecular Man Live Classroom")
    
    if not st.session_state.logged_in:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            with st.container(border=True):
                st.markdown("### Student/Teacher Login")
                username = st.text_input("Username", placeholder="Enter your ID")
                password = st.text_input("Password", type="password")
                if st.button("Login to Classroom ➜", use_container_width=True):
                    if login_user(username, password):
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.is_admin = (username == "Mohammed")
                        st.rerun()
                    else:
                        st.error("❌ Invalid Credentials")
    else:
        col1, col2 = st.columns([3, 1])
        with col1: st.write(f"Logged in as: **{st.session_state.username}**")
        with col2:
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.rerun()
        st.divider()

        if st.session_state.is_admin:
            st.markdown("## 👨‍🏫 Teacher Controls")
            status = get_live_status()
            
            col_a, col_b = st.columns([2, 1])
            with col_a:
                with st.container(border=True):
                    if status["is_live"]:
                        st.success(f"✅ YOU ARE LIVE: {status['topic']}")
                        st.markdown(f"**Meeting Link:** {status['link']}")
                        
                        if st.button("End Class ⏹️", type="primary"):
                            set_live_status(False)
                            st.rerun()
                    else:
                        st.info("Start a new session")
                        with st.form("start_live"):
                            topic = st.text_input("Topic")
                            meet_link = st.text_input("Google Meet Link", placeholder="https://meet.google.com/...")
                            
                            if st.form_submit_button("GO LIVE 🔴"):
                                if topic and meet_link:
                                    set_live_status(True, topic, meet_link)
                                    add_notification(f"🔴 Live Class Started: {topic}")
                                    st.rerun()
                                else:
                                    st.warning("Please enter both Topic and Link.")
            with col_b:
                with st.form("notif"):
                    msg = st.text_area("Announcement")
                    if st.form_submit_button("Send"):
                        add_notification(msg)
                        st.success("Sent")

        else:
            status = get_live_status()
            if status["is_live"]:
                st.markdown(f"""
                <div style="background: rgba(255, 0, 0, 0.1); border: 2px solid red; padding: 30px; border-radius: 15px; text-align: center;">
                    <h1 style="color: #ff4444 !important;">🔴 LIVE NOW</h1>
                    <h2>Topic: {status['topic']}</h2>
                    <br>
                    <a href="{status['link']}" target="_blank" class="live-join-btn">
                        🎥 JOIN GOOGLE MEET
                    </a>
                    <p style="margin-top:10px; color:#ccc;">(Opens in new tab)</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="padding: 40px; text-align: center; border: 2px dashed rgba(255,255,255,0.5); border-radius: 15px;">
                    <h2>💤 Class is offline</h2>
                    <p>Check back later for the next session.</p>
                </div>
                """, unsafe_allow_html=True)
            
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
            st.markdown("**Classes 6-8:** Foundation building with number systems, geometry, algebra basics")
            st.markdown("**Classes 9-10 (CBSE/State):** Algebra, Trigonometry, Coordinate Geometry, Statistics")
            st.markdown("**Classes 11-12 (Science):** Calculus, Vectors, 3D Geometry, Probability")
            st.markdown("**Classes 11-12 (Commerce):** Business Math, Statistics for Economics")
        
        st.write("")
        with st.container(border=True):
            st.markdown("### ⚗️ Chemistry")
            st.markdown("**Classes 6-10:** Basic concepts, Periodic Table, Chemical Reactions")
            st.markdown("**Classes 11-12:** Physical, Organic & Inorganic Chemistry")
            st.markdown("**Specialization:** NEET/JEE Chemistry Problem-Solving")
    
    with sub2:
        with st.container(border=True):
            st.markdown("### ⚡ Physics")
            st.markdown("**Classes 6-10:** Mechanics, Light, Sound, Electricity basics")
            st.markdown("**Classes 11-12:** Mechanics, Thermodynamics, Electromagnetism, Modern Physics")
            st.markdown("**Focus:** Numerical problem-solving & conceptual clarity")
        
        st.write("")
        with st.container(border=True):
            st.markdown("### 🧬 Biology")
            st.markdown("**Classes 6-10:** Cell biology, Human body systems, Ecology")
            st.markdown("**Classes 11-12:** Botany, Zoology, Genetics, Evolution")
            st.markdown("**NEET Prep:** High-yield topics with diagram practice")
    
    st.write("")
    st.markdown("## 🏆 Competitive Exam Preparation")
    
    e1, e2, e3 = st.columns(3)
    
    with e1:
        with st.container(border=True):
            st.markdown("#### 🎯 NEET (Medical)")
            st.markdown("**Focus Areas:**")
            st.write("• Biology: High-yield topics & diagrams")
            st.write("• Chemistry: Organic reactions & mechanisms")
            st.write("• Physics: Numerical shortcuts")
    
    with e2:
        with st.container(border=True):
            st.markdown("#### 🔬 JEE (Engineering)")
            st.markdown("**Focus Areas:**")
            st.write("• Mathematics: Advanced problem-solving")
            st.write("• Physics: Conceptual depth")
            st.write("• Chemistry: Simplified ")
    
    with e3:
        with st.container(border=True):
            st.markdown("#### 📝 Board Exams")
            st.markdown("**Preparation Strategy:**")
            st.write("• IGCSE/ISC/IB/ICSE/CBSE/State syllabus mastery")
            st.write("• Previous year papers")
            st.write("• Writing practice for theory")
    
    st.write("")
    st.markdown("## 💡 Our Teaching Approach")
    
    t1, t2 = st.columns(2)
    
    with t1:
        with st.container(border=True):
            st.markdown("### 📋 Personalized Learning Plans")
            st.write("Every student receives a custom curriculum based on:")
            st.write("• Initial assessment of strengths & weaknesses")
            st.write("• Target exam (Board/NEET/JEE)")
            st.write("• Learning pace & preferred style")
            st.write("• Regular progress tracking")
        
        st.write("")
        with st.container(border=True):
            st.markdown("### 🎨 Interactive Teaching Methods")
            st.write("• Visual aids & animations for complex topics")
            st.write("• Real-world applications of concepts")
            st.write("• Hands-on problem-solving sessions")
            st.write("• Doubt-clearing after every class")
    
    with t2:
        with st.container(border=True):
            st.markdown("### 📊 Continuous Assessment")
            st.write("• Weekly quizzes & mock tests")
            st.write("• Chapter-wise assignments")
            st.write("• Monthly performance reports")
            st.write("• Parent-teacher meetings")
        
        st.write("")
        with st.container(border=True):
            st.markdown("### 🤖 Technology Integration")
            st.write("• AI tutors available 24/7 for homework help")
            st.write("• Digital study materials & notes")
            st.write("• Online doubt sessions")
            st.write("• Recorded lectures for revision")
    
    st.write("")
    st.markdown("## 👥 Batch Options")
    
    b1, b2, b3 = st.columns(3)
    
    with b1:
        with st.container(border=True):
            st.markdown("#### 🎯 One-on-One")
            st.markdown("**Best for:** Personalized attention")
            st.write("• Fully customized pace")
            st.write("• Flexible timing")
            st.write("• Focus on specific weak areas")
    
    with b2:
        with st.container(border=True):
            st.markdown("#### 👫 Small Group (3-5)")
            st.markdown("**Best for:** Peer learning")
            st.write("• Interactive discussions")
            st.write("• Competitive environment")
            st.write("• Affordable pricing")
    
    with b3:
        with st.container(border=True):
            st.markdown("#### 💻 Online Classes")
            st.markdown("**Best for:** Flexibility")
            st.write("• Learn from anywhere")
            st.write("• Recorded sessions")
            st.write("• Digital whiteboard")


# ==========================================
# PAGE: TESTIMONIALS
# ==========================================
elif st.session_state.page == "Testimonials":
    st.markdown("""
    <style>
        .review-card {
            background-color: #ffffff !important;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            border-left: 5px solid #2c5282;
            color: #000000 !important;
        }
        .review-text {
            font-size: 16px;
            font-style: italic;
            color: #333333 !important;
            line-height: 1.5;
        }
        .review-author {
            margin-top: 10px;
            font-weight: bold;
            color: #2c5282 !important;
            text-align: right;
        }
        .metric-card {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            color: black !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .metric-value { font-size: 28px; font-weight: bold; color: black; }
        .metric-label { font-size: 14px; color: #555; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("# 💬 Student Success Stories")
    
    t1, t2 = st.columns(2)
    
    def testimonial_card(text, author):
        st.markdown(f"""
        <div class="review-card">
            <div class="review-text">"{text}"</div>
            <div class="review-author">- {author}</div>
        </div>
        """, unsafe_allow_html=True)

    with t1:
        testimonial_card("Sir's organic chemistry teaching helped me a lot. His mechanism approach made everything so clear!", "Pranav.S, Class 12 - IGCSE")
        testimonial_card("The AI tools are amazing! AyA helped me solve a tricky physics problem at 11 PM when I was stuck on homework.", "Arjun K., Class 12 CBSE")
        testimonial_card("My daughter's math grades improved from 60% to 95% in one semester. The personalized attention really works!", "Mrs. Lakshmi, Parent")
    
    with t2:
        testimonial_card("Physics numerical problems used to scare me. Now I solve them confidently thanks to sir's shortcut techniques.", "Rahul M., JEE Aspirant")
        testimonial_card("The Python bootcamp was amazing! Learned data science basics in 8 weekends and built my own project.", "Divya S., College Student")
        testimonial_card("The Mock Test generator is perfect for practice. I can make unlimited tests for any chapter!", "Sneha P., Class 12 ISC")
    
    st.write("")
    st.markdown("## 🏆 Our Results")
    
    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.markdown('<div class="metric-card"><div class="metric-label">Board Exams (All Boards)</div><div class="metric-value">80%</div><div class="metric-label">Average Score</div></div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="metric-card"><div class="metric-label">Improvement</div><div class="metric-value">60%</div><div class="metric-label">vs. Baseline</div></div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="metric-card"><div class="metric-label">AI Support</div><div class="metric-value">&lt; 2 Min</div><div class="metric-label">Response Time</div></div>', unsafe_allow_html=True)
    
    st.write("")
    st.markdown("## 💡 Why Parents Trust Us")
    
    w1, w2, w3 = st.columns(3)
    
    with w1:
        st.markdown('<div class="review-card"><h3>🎓 Expert Educator</h3><p style="color:#333;">One-on-one mentoring that identifies specific learning gaps.</p></div>', unsafe_allow_html=True)
    with w2:
        st.markdown('<div class="review-card"><h3>🧠 Conceptual</h3><p style="color:#333;">No rote memorization. We focus on "Why" and "How".</p></div>', unsafe_allow_html=True)
    with w3:
        st.markdown('<div class="review-card"><h3>💰 Fair Pricing</h3><p style="color:#333;">No hidden fees. Quality education for every family.</p></div>', unsafe_allow_html=True)

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
            if not render_image("python_bootcamp", use_column_width=True):
                with st.container(border=True):
                    st.markdown("# 🐍")
                    st.markdown("## Python")
                    st.markdown("### Weekend Intensive Program")
    
    with boot2:
        with st.container(border=True):
            st.markdown("### Weekend Intensive Program")
            st.write("Master the most in-demand programming language")
            st.write("")
            
            st.markdown("👨‍🏫 **Instructor:** Mohammed Salmaan M")
            st.caption("Data Science & AI Expert | Created Ed-Tech Platform - The Molecular Man Expert Tuition Solutions")
            st.write("")
            
            st.markdown("📅 **Schedule:** Saturdays & Sundays")
            st.caption("1 hour per session | Morning & Evening batches")
            st.write("")
            
            st.markdown("💻 **Requirements:** Laptop with internet")
            st.caption("We'll help you setup Jupyter Notebook & VS Code")
            st.write("")
            
            with st.expander("📚 Curriculum Highlights"):
                st.write("• Python Basics & Data Structures")
                st.write("• NumPy & Pandas for Data Analysis")
                st.write("• Data Visualization with Matplotlib")
                st.write("• Introduction to Machine Learning")
                st.write("• Real-world Project: Build your first AI model")
        
        st.write("")
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
            st.write("Sunday: AI Support Available 24/7")
            st.write("")
            
            st.link_button("💬 WhatsApp Us", "https://wa.me/917339315376", use_container_width=True)
    
    with c2:
        with st.container(border=True):
            st.markdown("### Send us a Message")
            
            with st.form("contact_page_form_unique"):
                name = st.text_input("Your Name")
                phone = st.text_input("Phone Number")
                email = st.text_input("Email (Optional)")
                grade = st.selectbox("Student's Grade", 
                    ["6-8", "9-10", "11-12 (Science)", "11-12 (Commerce)", "College/Other"])
                message = st.text_area("Message", height=120)
                
                submitted = st.form_submit_button("Send Message", use_container_width=True)

                if submitted:
                    if name and phone:
                        try:
                            form_data = {
                                "name": name,
                                "phone": phone,
                                "email": email,
                                "grade": grade,
                                "message": message,
                                "_subject": f"New Inquiry from {name}",
                                "_captcha": "false"
                            }

                            url = "https://formsubmit.co/the.molecularmanexpert@gmail.com"
                            response = requests.post(url, data=form_data)

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
            background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
            background-size: 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent; 
            background-clip: text;
            color: transparent;
            animation: gradient-animation 10s ease infinite;
        }
        </style>
        
        <div class="animated-footer-text">
            PRECISE • PASSIONATE • PROFESSIONAL
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 12px; margin-top: 10px;'>"
        "© 2026 The Molecular Man Expert Tuition Solutions | Mohammed Salmaan M. All Rights Reserved."
        "</div>", 
        unsafe_allow_html=True
    )
