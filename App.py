import streamlit as st
from groq import Groq
from openai import OpenAI
import base64
import json
import sys
import PyPDF2

# ─────────────────────────────────────────────────────────────
# 1. PAGE CONFIG
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="The Molecular Man AI Suite",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fix encoding
try:
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ─────────────────────────────────────────────────────────────
# 2. GLOBAL CSS  — matches website palette exactly
#    --bg-from: #004e92  --bg-to: #000428
#    --gold:    #ffd700  --cyan: #00ffff
# ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ══════════════════════════════════════════════════════════════
   MOLECULAR MAN AI SUITE — DARK THEME (aggressive overrides)
   Palette: bg #004e92→#000428 | gold #ffd700 | cyan #00ffff
   All rules use !important to beat Streamlit's injected styles
══════════════════════════════════════════════════════════════ */

/* ── GLOBAL RESET ───────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; }

/* Force dark background everywhere */
html, body,
.stApp,
.stApp > div,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="block-container"],
.main, .main > div,
section.main, section.main > div {
    background: linear-gradient(135deg, #004e92 0%, #000428 100%) !important;
    background-color: transparent !important;
    color: #ffffff !important;
}

/* ── HIDE CHROME ────────────────────────────────────────────── */
#MainMenu, footer, header,
.stDeployButton,
[data-testid="stToolbar"],
[data-testid="manage-app-button"],
section[data-testid="stSidebar"] { display: none !important; }

/* ── UNIVERSAL TEXT WHITE ───────────────────────────────────── */
h1, h2, h3, h4, h5, h6,
p, span, div, li, a,
label, small, strong, em,
.stMarkdown *, .stText *,
[data-testid="stMarkdownContainer"] *,
[data-testid="stCaptionContainer"] * {
    color: #ffffff !important;
}

/* ── EXPANDER — dark background, white text ─────────────────── */
[data-testid="stExpander"],
[data-testid="stExpander"] > div,
[data-testid="stExpander"] details,
[data-testid="stExpander"] details > div,
[data-testid="stExpander"] details summary,
details, details > div, details > summary {
    background: rgba(0, 10, 40, 0.85) !important;
    background-color: rgba(0, 10, 40, 0.85) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;
}
[data-testid="stExpander"] summary,
details summary {
    color: #e2e8f0 !important;
    font-weight: 700 !important;
    font-size: .95rem !important;
    padding: 14px 18px !important;
    background: transparent !important;
    border-radius: 14px !important;
    list-style: none !important;
}
[data-testid="stExpander"] summary::-webkit-details-marker,
details summary::-webkit-details-marker { display: none; }
[data-testid="stExpander"] details > div > div,
[data-testid="stExpander"] > details > div {
    background: transparent !important;
    padding: 0 18px 14px !important;
}

/* ── CONTAINER / BORDER WRAPPER ─────────────────────────────── */
div[data-testid="stVerticalBlockBorderWrapper"],
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: rgba(0, 15, 50, 0.7) !important;
    background-color: rgba(0, 15, 50, 0.7) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 16px !important;
    color: #ffffff !important;
}

/* ── FORM CONTAINER ─────────────────────────────────────────── */
[data-testid="stForm"],
[data-testid="stForm"] > div {
    background: rgba(0, 15, 50, 0.7) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 16px !important;
}

/* ── TEXT INPUT ─────────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextInput > div > div,
input[type="text"], input[type="number"], input[type="email"] {
    background: rgba(0, 20, 60, 0.9) !important;
    background-color: rgba(0, 20, 60, 0.9) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,255,255,0.3) !important;
    border-radius: 10px !important;
    font-size: .95rem !important;
    caret-color: #00ffff !important;
}
.stTextInput > div > div > input::placeholder { color: rgba(255,255,255,0.4) !important; }
.stTextInput > div > div > input:focus {
    border-color: #00ffff !important;
    box-shadow: 0 0 0 2px rgba(0,255,255,0.15) !important;
    outline: none !important;
}

/* ── TEXT AREA ──────────────────────────────────────────────── */
.stTextArea > div,
.stTextArea > div > div,
.stTextArea > div > div > textarea,
textarea {
    background: rgba(0, 20, 60, 0.9) !important;
    background-color: rgba(0, 20, 60, 0.9) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,255,255,0.3) !important;
    border-radius: 10px !important;
    font-size: .95rem !important;
    caret-color: #00ffff !important;
}
textarea::placeholder { color: rgba(255,255,255,0.4) !important; }
textarea:focus {
    border-color: #00ffff !important;
    box-shadow: 0 0 0 2px rgba(0,255,255,0.15) !important;
    outline: none !important;
}

/* ── NUMBER INPUT ───────────────────────────────────────────── */
.stNumberInput > div > div,
.stNumberInput input {
    background: rgba(0, 20, 60, 0.9) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,255,255,0.3) !important;
    border-radius: 10px !important;
}
.stNumberInput button {
    background: rgba(0,255,255,0.1) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,255,255,0.25) !important;
    border-radius: 8px !important;
}

/* ── SELECTBOX ──────────────────────────────────────────────── */
.stSelectbox > div > div,
.stSelectbox > div > div > div,
[data-baseweb="select"],
[data-baseweb="select"] > div {
    background: rgba(0, 20, 60, 0.9) !important;
    background-color: rgba(0, 20, 60, 0.9) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,255,255,0.3) !important;
    border-radius: 10px !important;
}
[data-baseweb="select"] span { color: #ffffff !important; }

/* Dropdown menu */
[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="menu"],
ul[role="listbox"] {
    background: #031a3f !important;
    background-color: #031a3f !important;
    border: 1px solid rgba(0,255,255,0.2) !important;
    border-radius: 12px !important;
}
li[role="option"], div[role="option"] {
    color: #e2e8f0 !important;
    background: transparent !important;
    padding: 10px 14px !important;
}
li[role="option"]:hover, div[role="option"]:hover,
li[role="option"][aria-selected="true"],
div[role="option"][aria-selected="true"] {
    background: rgba(0,255,255,0.1) !important;
    color: #00ffff !important;
}

/* ── RADIO BUTTONS ──────────────────────────────────────────── */
.stRadio > div,
.stRadio > label,
[data-testid="stRadio"] > div,
[data-testid="stRadio"] label {
    color: #e2e8f0 !important;
    background: transparent !important;
}
.stRadio label p,
[data-testid="stRadio"] label p { color: #e2e8f0 !important; }

/* ── FILE UPLOADER ──────────────────────────────────────────── */
[data-testid="stFileUploader"],
[data-testid="stFileUploaderDropzone"],
[data-testid="stFileUploader"] > div {
    background: rgba(0, 20, 60, 0.8) !important;
    background-color: rgba(0, 20, 60, 0.8) !important;
    border: 1px dashed rgba(0,255,255,0.35) !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stFileUploaderDropzone"] span { color: #a0aec0 !important; }

/* ── BUTTONS ────────────────────────────────────────────────── */
.stButton > button,
.stButton > button > div,
.stButton > button > div > p {
    background: linear-gradient(135deg, #ffd700 0%, #ffb900 100%) !important;
    color: #000000 !important;
    border-radius: 50px !important;
    border: none !important;
    font-weight: 800 !important;
    font-size: .92rem !important;
    padding: 13px 28px !important;
    letter-spacing: .8px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 20px rgba(255,215,0,0.35) !important;
    transition: all .25s !important;
    width: 100%;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 28px rgba(255,215,0,0.6) !important;
    background: linear-gradient(135deg, #ffe44d 0%, #ffd000 100%) !important;
}
.stButton > button p { color: #000000 !important; }

/* Form submit button */
div[data-testid="stFormSubmitButton"] > button,
div[data-testid="stFormSubmitButton"] > button > div,
div[data-testid="stFormSubmitButton"] > button p {
    background: linear-gradient(135deg, #004e92 0%, #3b6b9e 100%) !important;
    color: #ffffff !important;
    border: 2px solid rgba(0,255,255,0.5) !important;
    border-radius: 50px !important;
    font-weight: 800 !important;
    font-size: .92rem !important;
    padding: 13px 28px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 20px rgba(0,200,255,0.25) !important;
}
div[data-testid="stFormSubmitButton"] > button p { color: #ffffff !important; }
div[data-testid="stFormSubmitButton"] > button:hover {
    box-shadow: 0 6px 28px rgba(0,255,255,0.45) !important;
    border-color: #00ffff !important;
    transform: translateY(-2px) !important;
}

/* ── CHAT ───────────────────────────────────────────────────── */
.stChatMessage,
[data-testid="stChatMessage"],
[data-testid="stChatMessage"] > div {
    background: rgba(0, 20, 60, 0.75) !important;
    background-color: rgba(0, 20, 60, 0.75) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    margin-bottom: 10px !important;
    color: #e2e8f0 !important;
}
[data-testid="stChatMessageContent"] p,
[data-testid="stChatMessageContent"] * { color: #e2e8f0 !important; }

[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] > div > div,
[data-testid="stChatInputTextArea"],
[data-testid="stChatInput"] textarea {
    background: rgba(0, 20, 60, 0.9) !important;
    background-color: rgba(0, 20, 60, 0.9) !important;
    border: 1px solid rgba(0,255,255,0.3) !important;
    border-radius: 30px !important;
    color: #ffffff !important;
}

/* ── METRIC ─────────────────────────────────────────────────── */
[data-testid="stMetric"],
[data-testid="stMetric"] > div {
    background: rgba(0, 20, 60, 0.7) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    padding: 16px !important;
}
[data-testid="stMetricValue"] { color: #ffd700 !important; }
[data-testid="stMetricLabel"] { color: #a0aec0 !important; }
[data-testid="stMetricDelta"] { color: #48ff00 !important; }

/* ── ALERTS ─────────────────────────────────────────────────── */
[data-testid="stAlert"],
.stSuccess, .element-container .stSuccess { background: rgba(72,255,0,0.08) !important; border: 1px solid rgba(72,255,0,0.3) !important; border-radius: 10px !important; }
.stWarning, .element-container .stWarning { background: rgba(255,215,0,0.08) !important; border: 1px solid rgba(255,215,0,0.35) !important; border-radius: 10px !important; }
.stError,   .element-container .stError   { background: rgba(255,70,70,0.08) !important;  border: 1px solid rgba(255,70,70,0.35) !important; border-radius: 10px !important; }
.stInfo,    .element-container .stInfo    { background: rgba(0,255,255,0.06) !important;  border: 1px solid rgba(0,255,255,0.25) !important; border-radius: 10px !important; }
[data-testid="stAlert"] p { color: #ffffff !important; }

/* ── SPINNER ────────────────────────────────────────────────── */
.stSpinner > div { border-top-color: #ffd700 !important; }
[data-testid="stSpinner"] p { color: #e2e8f0 !important; }

/* ── DIVIDER ────────────────────────────────────────────────── */
hr { border-color: rgba(255,255,255,0.1) !important; margin: 20px 0 !important; }

/* ── SCROLLBAR ──────────────────────────────────────────────── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(0,0,0,0.3); }
::-webkit-scrollbar-thumb { background: rgba(255,215,0,0.4); border-radius: 4px; }

/* ── CUSTOM CLASSES ─────────────────────────────────────────── */
.mm-nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 24px;
    background: rgba(0,0,0,0.45);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin: -1rem -1rem 0 -1rem;
    position: sticky; top: 0; z-index: 999;
    flex-wrap: wrap; gap: 10px;
}
.mm-brand { display: flex; align-items: center; gap: 12px; }
.mm-brand-name  { font-size: 1.05rem; font-weight: 800; color: #ffffff !important; line-height: 1.2; }
.mm-brand-sub   { font-size: .72rem; color: #ffd700 !important; letter-spacing: 1px; }
.mm-tab-row     { display: flex; gap: 8px; flex-wrap: wrap; }
.mm-tab {
    padding: 8px 18px; border-radius: 25px; cursor: pointer;
    font-size: .82rem; font-weight: 700; letter-spacing: .5px;
    border: 1px solid rgba(255,255,255,0.2);
    background: rgba(255,255,255,0.06);
    color: #ffffff !important; transition: all .2s;
    text-transform: uppercase;
}
.mm-tab:hover { border-color: rgba(0,255,255,0.5); background: rgba(0,255,255,0.08); }
.mm-tab.active-aya {
    background: linear-gradient(90deg,#1a0533,#6d28d9,#1a0533) !important;
    border-color: rgba(167,139,250,0.55) !important;
    box-shadow: 0 4px 18px rgba(109,40,217,0.45);
}
.mm-tab.active-mt {
    background: linear-gradient(90deg,#1e3a5f,#3b6b9e,#1e3a5f) !important;
    border-color: rgba(0,255,255,0.55) !important;
    box-shadow: 0 4px 18px rgba(0,200,255,0.3);
}
.glass-card  { background: rgba(0,20,60,0.6); border: 1px solid rgba(255,255,255,0.13); border-radius: 18px; padding: 24px; margin-bottom: 20px; }
.gold-card   { background: rgba(255,215,0,0.05); border: 1px solid rgba(255,215,0,0.25); border-radius: 18px; padding: 24px; margin-bottom: 20px; }
.cyan-card   { background: rgba(0,255,255,0.04); border: 1px solid rgba(0,255,255,0.22); border-radius: 18px; padding: 24px; margin-bottom: 20px; }
.purple-card { background: rgba(109,40,217,0.1); border: 1px solid rgba(167,139,250,0.28); border-radius: 18px; padding: 24px; margin-bottom: 20px; }
.section-label { font-size: .68rem; font-weight: 800; letter-spacing: 2.5px; text-transform: uppercase; padding: 4px 12px; border-radius: 20px; display: inline-block; margin-bottom: 10px; }
.lbl-gold   { background: rgba(255,215,0,0.1);   border: 1px solid rgba(255,215,0,0.4);   color: #ffd700 !important; }
.lbl-cyan   { background: rgba(0,255,255,0.08);   border: 1px solid rgba(0,255,255,0.35);  color: #00ffff !important; }
.lbl-purple { background: rgba(167,139,250,0.1);  border: 1px solid rgba(167,139,250,0.4); color: #c4b5fd !important; }
.stat-box { text-align: center; padding: 16px 8px; }
.stat-num { font-size: 2rem; font-weight: 900; background: linear-gradient(to right,#ffd700,#00ffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.stat-lbl { font-size: .72rem; color: #a0aec0 !important; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
.score-badge { display: inline-block; padding: 10px 28px; border-radius: 30px; font-weight: 900; font-size: 1.6rem; background: linear-gradient(135deg,rgba(255,215,0,0.15),rgba(0,255,255,0.1)); border: 2px solid rgba(255,215,0,0.45); color: #ffd700 !important; }
.ans-correct { color: #48ff00 !important; font-weight: 700; }
.ans-wrong   { color: #ff6b6b !important; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 3. HELPERS
# ─────────────────────────────────────────────────────────────
def get_img_b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return None

def clean_input(text):
    if not text: return ""
    return text.encode("ascii", "ignore").decode("ascii").strip()

def get_groq_openai_client(api_key):
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

def fetch_available_models(api_key):
    try:
        client = get_groq_openai_client(api_key)
        models = client.models.list()
        return sorted([m.id for m in models.data])
    except Exception:
        return ["llama-3.3-70b-versatile"]

# ─────────────────────────────────────────────────────────────
# 4. SESSION STATE
# ─────────────────────────────────────────────────────────────
defaults = {
    "active_tab":      "aya",          # "aya" | "mock"
    "aya_messages":    [],
    "aya_uploader_key": 0,
    "mt_questions":    None,
    "mt_user_answers": {},
    "mt_feedback":     None,
    "mt_score":        0,
    "mt_total_marks":  0,
    "mt_q_type":       "MCQ",
    "mt_config":       {},             # saves last config for results header
    "mt_models":       [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─────────────────────────────────────────────────────────────
# 5. API KEY
# ─────────────────────────────────────────────────────────────
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets. Please add it in Settings → Secrets.")
    st.stop()

if not st.session_state.mt_models:
    st.session_state.mt_models = fetch_available_models(GROQ_API_KEY)

# ─────────────────────────────────────────────────────────────
# 6. SYSTEM PROMPT  (AyA)
# ─────────────────────────────────────────────────────────────
AYA_SYSTEM_PROMPT = """You are **AyA**, the Lead AI Tutor at **The Molecular Man Expert Tuition Solutions**, Madurai.
Your mission: guide students from "Zero" (absolute beginner) to "Hero" (advanced mastery).
Your tone: encouraging, clear, patient, and intellectually rigorous.

### RESPONSE GUIDELINES
1. **Conversational Follow-ups:** Answer follow-up questions directly without repeating the full structure.
2. **Main Problem Structure:**
   - 🧠 **CONCEPT** — What principle is at play?
   - 🌍 **REAL-WORLD CONTEXT** — Where do we see this in life?
   - ✍️ **SOLUTION** — Step-by-step working.
   - ✅ **ANSWER** — Clear final answer.
   - 🚀 **HERO TIP** — An insight that turns good students into great ones.
3. **Formatting:** Bold for keywords, LaTeX for all equations.
4. **Scope:** Chemistry, Physics, Maths, Biology (Classes 6–12, NEET, JEE, Boards).
"""

# ─────────────────────────────────────────────────────────────
# 7. MOCK TEST FUNCTIONS
# ─────────────────────────────────────────────────────────────
def generate_questions(api_key, model, board, cls, subject, chapter, num, difficulty, q_type):
    client = get_groq_openai_client(api_key)
    safe_sub  = clean_input(subject)
    safe_chap = clean_input(chapter)

    context = (
        f"You are a strict Textbook Author and Examiner for the {board} Board. "
        f"Subject: {safe_sub}, Class: {cls}, Chapter: '{safe_chap}'.\n"
        f"RULES: Questions must be factually 100% correct per standard {board} textbooks. "
        f"No ambiguous questions. Exactly one indisputable correct answer."
    )

    if q_type == "MCQ":
        prompt = f"""{context}
Create a valid JSON list of exactly {num} {difficulty}-level Multiple Choice Questions.

Format:
[
  {{"id": 1, "question": "...", "options": ["A", "B", "C", "D"], "correct_answer": "A"}}
]
Verify: correct_answer must match one option exactly and be factually correct.
Return ONLY raw JSON. No explanation. No markdown fences."""
    else:
        prompt = f"""{context}
Create a valid JSON list of exactly {num} {difficulty}-level Descriptive Questions with marks.

Format:
[
  {{"id": 1, "question": "...", "marks": 3}}
]
Return ONLY raw JSON. No explanation. No markdown fences."""

    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a precise academic assistant. Output strictly valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        content = resp.choices[0].message.content.strip()
        content = content.replace("```json", "").replace("```", "").strip()
        return json.loads(content)
    except Exception as e:
        st.error(f"❌ Question generation failed: {str(e)}")
        return None


def grade_mcq(api_key, model, questions, user_answers, board, cls, subject):
    client = get_groq_openai_client(api_key)
    score = 0
    incorrect_log = ""

    for q in questions:
        q_id    = str(q["id"])
        u_ans   = user_answers.get(q_id)
        c_ans   = q["correct_answer"]
        if u_ans == c_ans:
            score += 1
        else:
            incorrect_log += f"Q: {q['question']}\nStudent: {u_ans}\nCorrect: {c_ans}\n\n"

    st.session_state.mt_score       = score
    st.session_state.mt_total_marks = len(questions)

    if score == len(questions):
        return "### 🏆 Perfect Score!\nYou have completely mastered this topic. Outstanding work."

    prompt = f"""
The student scored {score}/{len(questions)} in a {board} Class {cls} {subject} MCQ test.
Mistakes:
{incorrect_log}

Provide a "Scope for Improvement" analysis.
For each wrong answer, clearly explain WHY it was wrong and WHY the correct answer is right.
Format in clean Markdown with headers per question.
"""
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Error analysing performance: {str(e)}"


def grade_descriptive(api_key, model, questions, user_answers, board, cls, subject):
    client = get_groq_openai_client(api_key)
    qa_data = ""
    total_possible = 0

    for q in questions:
        q_id  = str(q["id"])
        u_ans = user_answers.get(q_id, "No Answer Provided")
        marks = q.get("marks", 1)
        total_possible += marks
        qa_data += f"Q ({marks} marks): {q['question']}\nStudent Answer: {u_ans}\n\n"

    st.session_state.mt_total_marks = total_possible

    prompt = f"""
You are a strict examiner for {board} Class {cls} {subject}.
Evaluate these descriptive answers per standard Board marking schemes.

{qa_data}

Requirements:
1. Award marks for EACH question with justification.
2. State Total Score obtained out of {total_possible}.
3. Provide "Scope for Improvement" noting missing keywords or concepts.
Format clearly in Markdown.
"""
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"Error grading descriptive answers: {str(e)}"

# ─────────────────────────────────────────────────────────────
# 8. NAV BAR
# ─────────────────────────────────────────────────────────────
logo_b64 = get_img_b64("logo.png")
logo_html = (
    f'<img src="data:image/png;base64,{logo_b64}" '
    f'style="height:44px;width:44px;border-radius:50%;border:2px solid #ffd700;'
    f'box-shadow:0 0 12px rgba(255,215,0,0.35);object-fit:cover;">'
    if logo_b64 else "🧬"
)

aya_active = "active-aya" if st.session_state.active_tab == "aya" else ""
mt_active  = "active-mt"  if st.session_state.active_tab == "mock" else ""

st.markdown(f"""
<div class="mm-nav">
  <div class="mm-brand">
    {logo_html}
    <div>
      <div class="mm-brand-name">The Molecular Man</div>
      <div class="mm-brand-sub">AI Suite — Powered by AyA</div>
    </div>
  </div>
  <div class="mm-tab-row">
    <button class="mm-tab {aya_active}" onclick="document.getElementById('btn-aya').click()">🤖 AyA Tutor</button>
    <button class="mm-tab {mt_active}"  onclick="document.getElementById('btn-mt').click()">📝 Mock Tests</button>
  </div>
</div>
""", unsafe_allow_html=True)

# Hidden Streamlit buttons the nav calls
col_nav1, col_nav2, *_ = st.columns([1, 1, 6])
with col_nav1:
    if st.button("AyA Tutor", key="btn-aya"):
        st.session_state.active_tab = "aya"
        st.rerun()
with col_nav2:
    if st.button("Mock Tests", key="btn-mt"):
        st.session_state.active_tab = "mock"
        st.rerun()

st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 9. AyA TUTOR TAB
# ─────────────────────────────────────────────────────────────
if st.session_state.active_tab == "aya":

    # ── Hero header ──────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:32px 16px 20px;">
      <div style="display:inline-flex;align-items:center;gap:8px;padding:5px 16px;
                  border-radius:20px;background:rgba(109,40,217,.18);
                  border:1px solid rgba(167,139,250,.4);margin-bottom:16px;">
        <span style="width:8px;height:8px;border-radius:50%;background:#a78bfa;display:inline-block;
                     box-shadow:0 0 8px #a78bfa;"></span>
        <span style="font-size:.72rem;font-weight:800;letter-spacing:2px;color:#c4b5fd !important;">LIVE · 24 / 7</span>
      </div>
      <h1 style="font-size:clamp(2rem,6vw,3.5rem);font-weight:900;margin:0;
                 background:linear-gradient(135deg,#fff 0%,#c4b5fd 35%,#00ffff 70%,#ffd700 100%);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
        Meet AyA
      </h1>
      <p style="color:#94a3b8 !important;font-size:1rem;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;line-height:1.7;">
        Your 24/7 AI Tutor. Ask any doubt — Chemistry, Physics, Maths, Biology.<br>
        She doesn't sleep. She doesn't judge. She simply teaches.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Stats row ─────────────────────────────────────────────
    sc1, sc2, sc3, sc4 = st.columns(4)
    for col, num, lbl in [
        (sc1, "24/7", "Always Online"),
        (sc2, "₹0",  "Cost Forever"),
        (sc3, "6+",  "Boards Covered"),
        (sc4, "∞",   "Questions Answered"),
    ]:
        with col:
            st.markdown(f"""
            <div class="glass-card stat-box">
              <div class="stat-num">{num}</div>
              <div class="stat-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")

    # ── Problem input ─────────────────────────────────────────
    with st.expander("📝 Start a New Problem", expanded=(len(st.session_state.aya_messages) == 0)):
        st.markdown('<span class="section-label lbl-purple">Input Method</span>', unsafe_allow_html=True)
        input_type = st.radio("", ["📄 Type / Paste Problem", "📕 Upload PDF"], horizontal=True, label_visibility="collapsed")

        if input_type == "📄 Type / Paste Problem":
            user_text = st.text_area("Paste your question here…", height=120, placeholder="e.g. Explain the mechanism of SN2 reaction with an example.")
            if st.button("🚀 Send to AyA", key="aya_send_text"):
                if user_text.strip():
                    st.session_state.aya_messages = []
                    st.session_state.aya_messages.append({"role": "user", "content": f"PROBLEM:\n{user_text}"})
                    st.rerun()
                else:
                    st.warning("Please enter a question first.")

        else:
            uploader_key = f"pdf_{st.session_state.aya_uploader_key}"
            pdf_file = st.file_uploader("Upload a PDF (first 2 pages will be read)", type=["pdf"], key=uploader_key)
            if st.button("🚀 Analyse PDF", key="aya_send_pdf"):
                if pdf_file:
                    try:
                        st.session_state.aya_messages = []
                        reader   = PyPDF2.PdfReader(pdf_file)
                        pdf_text = ""
                        for i in range(min(2, len(reader.pages))):
                            pdf_text += reader.pages[i].extract_text()[:3000]
                        st.session_state.aya_messages.append({"role": "user", "content": f"PROBLEM from PDF:\n{pdf_text}"})
                        st.session_state.aya_uploader_key += 1
                        st.rerun()
                    except Exception as e:
                        st.error(f"Could not read PDF: {e}")
                else:
                    st.warning("Please upload a PDF first.")

    # ── Chat history ──────────────────────────────────────────
    if st.session_state.aya_messages:
        st.markdown('<span class="section-label lbl-purple">💬 Chat with AyA</span>', unsafe_allow_html=True)

    for msg in st.session_state.aya_messages:
        with st.chat_message(msg["role"]):
            content = msg["content"]
            if msg["role"] == "user" and (content.startswith("PROBLEM from PDF:") or content.startswith("PROBLEM:")):
                with st.expander("📄 Uploaded Problem (click to expand)", expanded=False):
                    st.markdown(content)
            else:
                st.markdown(content)

    # ── Trigger AI ────────────────────────────────────────────
    if st.session_state.aya_messages and st.session_state.aya_messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("🤖 AyA is thinking…"):
                try:
                    groq_client = Groq(api_key=GROQ_API_KEY)
                    api_msgs    = [{"role": "system", "content": AYA_SYSTEM_PROMPT}] + st.session_state.aya_messages
                    response_text = None

                    for model_id in ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"]:
                        try:
                            resp = groq_client.chat.completions.create(
                                messages=api_msgs,
                                model=model_id,
                                temperature=0.5,
                                max_tokens=6000,
                            )
                            response_text = resp.choices[0].message.content
                            break
                        except Exception:
                            continue

                    if not response_text:
                        response_text = "❌ Could not connect to AI. Please try again in a moment."

                    st.markdown(response_text)
                    st.session_state.aya_messages.append({"role": "assistant", "content": response_text})
                except Exception as e:
                    st.error(f"System error: {e}")

    # ── Follow-up input ───────────────────────────────────────
    if st.session_state.aya_messages:
        if follow_up := st.chat_input("Ask AyA a follow-up question…"):
            st.session_state.aya_messages.append({"role": "user", "content": follow_up})
            st.rerun()

# ─────────────────────────────────────────────────────────────
# 10. MOCK TEST TAB
# ─────────────────────────────────────────────────────────────
elif st.session_state.active_tab == "mock":

    # ── Hero header ──────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding:32px 16px 20px;">
      <div style="display:inline-flex;align-items:center;gap:8px;padding:5px 16px;
                  border-radius:20px;background:rgba(0,255,255,.08);
                  border:1px solid rgba(0,255,255,.3);margin-bottom:16px;">
        <span style="font-size:.72rem;font-weight:800;letter-spacing:2px;color:#00ffff !important;">∞ INFINITE MOCK TEST ENGINE</span>
      </div>
      <h1 style="font-size:clamp(2rem,6vw,3.5rem);font-weight:900;margin:0;
                 background:linear-gradient(135deg,#fff 0%,#ffd700 50%,#00ffff 100%);
                 -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
        Generate. Practice. Master.
      </h1>
      <p style="color:#94a3b8 !important;font-size:1rem;margin-top:8px;max-width:520px;margin-left:auto;margin-right:auto;line-height:1.7;">
        Unique, AI-generated test papers for CBSE, ICSE, IB, State Boards, NEET &amp; JEE.<br>
        Every paper is fresh. Every paper costs ₹0.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Model — hardcoded internally, never shown to students ─
    model_choice = "llama-3.3-70b-versatile"
    if st.session_state.mt_models and model_choice not in st.session_state.mt_models:
        for fallback in ["llama-3.1-70b-versatile", "mixtral-8x7b-32768"]:
            if fallback in st.session_state.mt_models:
                model_choice = fallback
                break

    # ══════════════════════════════════════════════════════════
    # VIEW A: CONFIGURATION (no questions yet)
    # ══════════════════════════════════════════════════════════
    if not st.session_state.mt_questions:
        st.markdown('<span class="section-label lbl-gold">⚙️ Configure Your Test</span>', unsafe_allow_html=True)
        st.markdown("")

        with st.container(border=True):
            left, right = st.columns(2, gap="large")

            with left:
                st.markdown("**📋 Exam Details**")
                board      = st.selectbox("Board", ["CBSE", "ICSE", "IGCSE", "IB", "Tamil Nadu State Board", "Maharashtra Board", "Other"])
                cls        = st.selectbox("Class", [str(i) for i in range(6, 13)] + ["NEET", "JEE", "Other"])
                difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

            with right:
                st.markdown("**📚 Topic Details**")
                subject = st.text_input("Subject", placeholder="e.g. Chemistry")
                chapter = st.text_input("Chapter", placeholder="e.g. Electrochemistry")
                qtype_col, qcount_col = st.columns(2)
                with qtype_col:
                    q_type = st.radio("Question Type", ["MCQ", "Descriptive"])
                with qcount_col:
                    num_q  = st.number_input("Count", min_value=1, max_value=20, value=5)

        st.markdown("")
        if st.button("⚡ GENERATE MOCK TEST", type="primary"):
            if not subject.strip() or not chapter.strip():
                st.warning("⚠️ Please fill in the Subject and Chapter fields.")
            else:
                with st.spinner(f"🧠 Generating {board} pattern {q_type}s for {chapter}…"):
                    st.session_state.mt_user_answers = {}
                    st.session_state.mt_feedback     = None
                    st.session_state.mt_score        = 0
                    st.session_state.mt_q_type       = q_type
                    st.session_state.mt_config       = {
                        "board": board, "class": cls, "subject": subject,
                        "chapter": chapter, "difficulty": difficulty,
                    }
                    qs = generate_questions(
                        GROQ_API_KEY, model_choice,
                        board, cls, subject, chapter, num_q, difficulty, q_type
                    )
                    if qs:
                        st.session_state.mt_questions = qs
                        st.rerun()

    # ══════════════════════════════════════════════════════════
    # VIEW B: RESULTS
    # ══════════════════════════════════════════════════════════
    elif st.session_state.mt_feedback:
        cfg   = st.session_state.mt_config
        score = st.session_state.mt_score
        total = st.session_state.mt_total_marks

        st.markdown(f"""
        <div class="gold-card" style="text-align:center;">
          <div class="section-label lbl-gold">📊 Result Analysis</div>
          <p style="color:#94a3b8 !important;margin:4px 0 12px;">
            {cfg.get('board','')} · Class {cfg.get('class','')} · {cfg.get('subject','')} · {cfg.get('chapter','')}
          </p>
          {'<div class="score-badge">' + str(score) + ' / ' + str(total) + '</div>' if st.session_state.mt_q_type == "MCQ" else ''}
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.mt_q_type == "MCQ":
            pct = round((score / total) * 100) if total else 0
            m1, m2, m3 = st.columns(3)
            m1.metric("Score",      f"{score}/{total}")
            m2.metric("Percentage", f"{pct}%")
            m3.metric("Status",     "✅ Pass" if pct >= 40 else "❌ Needs Work")

        st.markdown('<div class="purple-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Examiner's Feedback")
        st.markdown(st.session_state.mt_feedback)
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.mt_q_type == "MCQ":
            with st.expander("📋 Full Answer Key"):
                for q in st.session_state.mt_questions:
                    q_id  = str(q["id"])
                    u_ans = st.session_state.mt_user_answers.get(q_id)
                    c_ans = q["correct_answer"]
                    is_ok = u_ans == c_ans
                    st.markdown(f"**Q{q['id']}.** {q['question']}")
                    if is_ok:
                        st.markdown(f'<span class="ans-correct">✅ {u_ans}</span>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<span class="ans-wrong">❌ Your answer: {u_ans}</span>', unsafe_allow_html=True)
                        st.markdown(f'<span class="ans-correct">✅ Correct: {c_ans}</span>', unsafe_allow_html=True)
                    st.markdown("---")

        st.markdown("")
        if st.button("🔄 New Test"):
            st.session_state.mt_questions    = None
            st.session_state.mt_feedback     = None
            st.session_state.mt_user_answers = {}
            st.session_state.mt_score        = 0
            st.rerun()

    # ══════════════════════════════════════════════════════════
    # VIEW C: EXAM INTERFACE
    # ══════════════════════════════════════════════════════════
    else:
        cfg = st.session_state.mt_config
        st.markdown(f"""
        <div class="cyan-card">
          <div class="section-label lbl-cyan">📝 Exam in Progress</div>
          <p style="color:#e2e8f0 !important;margin-top:8px;font-size:.95rem;">
            <strong>{cfg.get('board','')} · Class {cfg.get('class','')} · {cfg.get('subject','')} · {cfg.get('chapter','')}</strong>
            &nbsp;|&nbsp; {cfg.get('difficulty','')} · {st.session_state.mt_q_type}
          </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("exam_form"):
            for q in st.session_state.mt_questions:
                marks_txt = f" *({q.get('marks', 1)} Marks)*" if st.session_state.mt_q_type == "Descriptive" else ""
                st.markdown(f"**Q{q['id']}.** {q['question']}{marks_txt}")

                if st.session_state.mt_q_type == "MCQ":
                    st.radio(
                        "Select your answer:",
                        q["options"],
                        key=f"ans_{q['id']}",
                        index=None,
                        label_visibility="collapsed"
                    )
                else:
                    st.text_area(
                        "Write your answer:",
                        key=f"ans_{q['id']}",
                        height=110,
                        label_visibility="collapsed",
                        placeholder="Type your answer here…"
                    )
                st.markdown("---")

            submitted = st.form_submit_button("✅ Submit Exam")

        if submitted:
            all_answered = True
            for q in st.session_state.mt_questions:
                val = st.session_state.get(f"ans_{q['id']}")
                if (val is None or val == "") and st.session_state.mt_q_type == "MCQ":
                    all_answered = False
                st.session_state.mt_user_answers[str(q["id"])] = val

            if not all_answered:
                st.error("⚠️ Please answer all questions before submitting.")
            else:
                with st.spinner("🧠 Evaluating your performance…"):
                    cfg = st.session_state.mt_config
                    if st.session_state.mt_q_type == "MCQ":
                        fb = grade_mcq(
                            GROQ_API_KEY, model_choice,
                            st.session_state.mt_questions,
                            st.session_state.mt_user_answers,
                            cfg.get("board","Board"), cfg.get("class","Class"), cfg.get("subject","Subject")
                        )
                    else:
                        fb = grade_descriptive(
                            GROQ_API_KEY, model_choice,
                            st.session_state.mt_questions,
                            st.session_state.mt_user_answers,
                            cfg.get("board","Board"), cfg.get("class","Class"), cfg.get("subject","Subject")
                        )
                    st.session_state.mt_feedback = fb
                    st.rerun()

# ─────────────────────────────────────────────────────────────
# 11. FOOTER
# ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:48px;border-top:1px solid rgba(255,255,255,0.08);">

  <!-- Parent website banner -->
  <div style="
    background: linear-gradient(135deg, rgba(0,0,0,0.5) 0%, rgba(0,20,50,0.6) 100%);
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 18px;
    padding: 28px 32px;
    margin: 32px 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    animation: none;
  ">
    <div>
      <div style="font-size:.7rem;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;
                  color:#ffd700 !important;margin-bottom:6px;">🏠 Our Parent Website</div>
      <div style="font-size:1.15rem;font-weight:800;color:#ffffff !important;margin-bottom:4px;">
        The Molecular Man Expert Tuition Solutions
      </div>
      <div style="font-size:.85rem;color:#94a3b8 !important;line-height:1.6;">
        Live Classes · Study Notes · Student Portal · Downloads · Contact
      </div>
    </div>
    <a href="https://themolecularmanexpert.gitlab.io/AyA/"
       target="_blank"
       style="
         display: inline-block;
         padding: 12px 28px;
         background: linear-gradient(135deg, #ffd700 0%, #ffb900 100%);
         color: #000000 !important;
         border-radius: 50px;
         font-weight: 800;
         font-size: .9rem;
         text-decoration: none;
         letter-spacing: .8px;
         text-transform: uppercase;
         box-shadow: 0 4px 18px rgba(255,215,0,0.35);
         white-space: nowrap;
         transition: all .2s;
       ">
      🌐 Visit Website →
    </a>
  </div>

  <!-- Small footer line -->
  <div style="text-align:center;padding:0 0 24px;color:rgba(255,255,255,0.25) !important;font-size:.78rem;">
    <strong style="color:rgba(255,215,0,0.45) !important;">The Molecular Man Expert Tuition Solutions</strong>
    &nbsp;·&nbsp; Madurai, Tamil Nadu &nbsp;·&nbsp; Built by Mohammed Salmaan M. &nbsp;·&nbsp; Pure Teaching Intelligence
  </div>

</div>
""", unsafe_allow_html=True)
