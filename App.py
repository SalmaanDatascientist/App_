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
    .founder-subhead { font-size: 1.2rem; color: #e
