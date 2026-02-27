import streamlit as st
from groq import Groq
from openai import OpenAI
import base64, json, sys
import PyPDF2

# ── PAGE CONFIG ───────────────────────────────────────────────
st.set_page_config(
    page_title="The Molecular Man AI Suite",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)
try:
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── FORCE DARK MODE — NUCLEAR EDITION ────────────────────────
# Injects CSS at <head> level AND a <style> tag at body root
# to capture BaseWeb portals rendered outside .stApp
st.markdown("""
<style>
/* ═══ 1. COLOR SCHEME — tells browser & BaseWeb to use dark ═══ */
:root {
  color-scheme: dark !important;
}
html {
  background: #000428 !important;
  color: #e2e8f0 !important;
}

/* ═══ 2. APP BACKGROUND ═══ */
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="block-container"],
section.main,
.main {
  background: linear-gradient(135deg,#004e92 0%,#000428 100%) !important;
  color: #e2e8f0 !important;
}

/* ═══ 3. PORTAL OVERLAYS (rendered at body root, NOT inside .stApp) ═══ */
/* These are the white dropdown popups */
body > div[class],
body > div[data-baseweb],
body > div > div[data-baseweb],
body > div[id] > div,
div[data-baseweb="popover"],
div[data-baseweb="popover"] > div,
div[data-baseweb="popover"] > div > div,
div[data-baseweb="popover"] > div > div > div,
div[data-baseweb="popover"] > div > div > div > div,
div[data-baseweb="popover"] ul,
div[data-baseweb="popover"] li {
  background-color: #031a3f !important;
  color: #e2e8f0 !important;
}

/* ═══ 4. MENU & LISTBOX inside portals ═══ */
[data-baseweb="menu"],
[data-baseweb="menu"] *,
ul[role="listbox"],
ul[role="listbox"] *,
div[role="listbox"],
div[role="listbox"] * {
  background-color: #031a3f !important;
  color: #e2e8f0 !important;
  border-color: rgba(0,255,255,.25) !important;
}

/* Individual options */
li[role="option"],
div[role="option"],
[data-baseweb="menu-item"],
[data-baseweb="menu-item"] * {
  background-color: #031a3f !important;
  color: #e2e8f0 !important;
}
li[role="option"]:hover,
div[role="option"]:hover,
li[role="option"][aria-selected="true"],
div[role="option"][aria-selected="true"],
[data-baseweb="menu-item"]:hover {
  background-color: rgba(0,255,255,.18) !important;
  color: #ffffff !important;
}

/* Popover box itself */
[data-baseweb="popover"] {
  background: #031a3f !important;
  border: 1px solid rgba(0,255,255,.28) !important;
  border-radius: 12px !important;
  box-shadow: 0 8px 40px rgba(0,0,0,.8) !important;
  overflow: hidden !important;
}

/* ═══ 5. SELECT TRIGGER ═══ */
[data-baseweb="select"],
[data-baseweb="select"] > div,
[data-baseweb="select"] > div > div {
  background-color: #00122e !important;
  color: #e2e8f0 !important;
  border-color: rgba(0,255,255,.4) !important;
  border-radius: 10px !important;
}
[data-baseweb="select"] span,
[data-baseweb="select"] [data-baseweb="icon"],
[data-baseweb="select"] svg {
  fill: #e2e8f0 !important;
  color: #e2e8f0 !important;
  background: transparent !important;
}

/* ═══ 6. ALL INPUTS ═══ */
input, textarea,
input[type="text"], input[type="number"],
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
.stTextInput input,
.stTextArea textarea,
[data-testid="stNumberInput"] input {
  background-color: #00122e !important;
  color: #ffffff !important;
  border: 1px solid rgba(0,255,255,.4) !important;
  border-radius: 10px !important;
  caret-color: #00ffff !important;
}
input::placeholder, textarea::placeholder {
  color: rgba(255,255,255,.4) !important;
}

/* Number input steppers */
[data-testid="stNumberInput"] button,
[data-baseweb="spinner"] button {
  background-color: #001a3f !important;
  color: #e2e8f0 !important;
  border-color: rgba(0,255,255,.3) !important;
}

/* ═══ 7. RADIO BUTTONS ═══ */
[data-testid="stRadio"] label,
[data-testid="stRadio"] p,
[data-testid="stRadio"] span,
.stRadio label p {
  color: #e2e8f0 !important;
}

/* ═══ 8. EXPANDERS ═══ */
[data-testid="stExpander"], details {
  background: #00122e !important;
  border: 1px solid rgba(255,255,255,.15) !important;
  border-radius: 14px !important;
}
details summary, details summary * {
  color: #e2e8f0 !important;
  font-weight: 700 !important;
}
details > div, details[open] > div {
  background: #00122e !important;
}

/* ═══ 9. CONTAINERS / CARDS ═══ */
div[data-testid="stVerticalBlockBorderWrapper"] {
  background: rgba(0,18,46,.75) !important;
  border: 1px solid rgba(255,255,255,.15) !important;
  border-radius: 16px !important;
}

/* ═══ 10. METRICS ═══ */
[data-testid="stMetric"] {
  background: rgba(0,18,46,.7) !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  border-radius: 14px !important;
  padding: 16px !important;
}
[data-testid="stMetricValue"] { color: #ffd700 !important; }
[data-testid="stMetricLabel"] p { color: #94a3b8 !important; }

/* ═══ 11. TABS ═══ */
[data-testid="stTabs"] [role="tablist"] {
  background: rgba(0,0,0,.3) !important;
  border-radius: 30px !important;
  padding: 4px !important;
  gap: 4px !important;
}
[data-testid="stTabs"] button[role="tab"] {
  border-radius: 25px !important;
  color: #94a3b8 !important;
  font-weight: 700 !important;
  letter-spacing: .5px !important;
  padding: 10px 24px !important;
  background: transparent !important;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
  background: linear-gradient(90deg,#6d28d9,#3b82f6) !important;
  color: #fff !important;
  box-shadow: 0 4px 16px rgba(109,40,217,.4) !important;
}

/* ═══ 12. CHAT ═══ */
[data-testid="stChatMessage"] {
  background: rgba(0,18,46,.7) !important;
  border: 1px solid rgba(255,255,255,.12) !important;
  border-radius: 14px !important;
}
[data-testid="stChatInput"] > div {
  background: #00122e !important;
  border: 1px solid rgba(0,255,255,.3) !important;
  border-radius: 30px !important;
}
[data-testid="stChatInput"] textarea {
  background: transparent !important;
  color: #fff !important;
}

/* ═══ 13. GOLD BUTTONS ═══ */
.stButton > button {
  background: linear-gradient(135deg,#ffd700,#ffb900) !important;
  color: #000 !important;
  border: none !important;
  border-radius: 50px !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  letter-spacing: .8px !important;
  box-shadow: 0 4px 16px rgba(255,215,0,.35) !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 24px rgba(255,215,0,.6) !important;
}
.stButton > button p, .stButton > button span, .stButton > button div {
  color: #000 !important;
}

/* ═══ 14. ALERTS ═══ */
[data-testid="stAlert"] { border-radius: 12px !important; }

/* ═══ 15. FILE UPLOADER ═══ */
[data-testid="stFileUploader"] {
  background: #00122e !important;
  border: 1px dashed rgba(0,255,255,.4) !important;
  border-radius: 12px !important;
}
[data-testid="stFileUploader"] * { color: #e2e8f0 !important; }

/* ═══ 16. MARKDOWN TEXT ═══ */
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] strong {
  color: #e2e8f0 !important;
}

/* ═══ 17. HIDE CHROME ═══ */
#MainMenu, footer, header, .stDeployButton,
[data-testid="stToolbar"],
section[data-testid="stSidebar"] { display: none !important; }

/* ═══ 18. SCROLLBAR ═══ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #000428; }
::-webkit-scrollbar-thumb { background: rgba(255,215,0,.4); border-radius: 4px; }
</style>

<script>
// JS fallback: force dark on any white-background portal divs injected after page load
const observer = new MutationObserver(() => {
  document.querySelectorAll('[data-baseweb="popover"], [data-baseweb="menu"], ul[role="listbox"], div[role="listbox"]').forEach(el => {
    el.style.setProperty('background-color', '#031a3f', 'important');
    el.style.setProperty('color', '#e2e8f0', 'important');
    el.querySelectorAll('*').forEach(child => {
      const bg = window.getComputedStyle(child).backgroundColor;
      if (bg === 'rgb(255, 255, 255)' || bg === 'rgba(255, 255, 255, 1)') {
        child.style.setProperty('background-color', '#031a3f', 'important');
        child.style.setProperty('color', '#e2e8f0', 'important');
      }
    });
  });
});
observer.observe(document.body, { childList: true, subtree: true });
</script>
""", unsafe_allow_html=True)

# ── HELPERS ───────────────────────────────────────────────────
def get_img_b64(path):
    try:
        with open(path,"rb") as f: return base64.b64encode(f.read()).decode()
    except: return None

def groq_openai(api_key):
    return OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

BEST_MODELS = ["llama-3.3-70b-versatile","llama-3.1-70b-versatile","mixtral-8x7b-32768"]

# ── SESSION STATE ─────────────────────────────────────────────
for k,v in {
    "aya_msgs":[],"aya_key":0,
    "mt_qs":None,"mt_answers":{},"mt_feedback":None,
    "mt_score":0,"mt_total":0,"mt_qtype":"MCQ","mt_cfg":{},
}.items():
    if k not in st.session_state: st.session_state[k]=v

# ── API KEY ───────────────────────────────────────────────────
try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except:
    st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets.")
    st.stop()

# ── SYSTEM PROMPT ─────────────────────────────────────────────
AYA_PROMPT = """# IDENTITY & MISSION
You are AyA, the Lead AI Tutor at "The Molecular Man Expert Tuition Solutions," Madurai. You were architected by Mohammed Salmaan to provide elite, concept-first education. Your mission: transform students from **Zero to Hero**.

# CRITICAL RULE 1: THE INTAKE GUARDRAIL (PRIORITY #1)
You are STRICTLY FORBIDDEN from providing any academic content (Concept, Solution, or Answer) until you know the student's context.

1. **Check:** Does the student's message include their **Board** and **Class**?
2. **Action (If NO):** You must ignore the academic query for now and respond ONLY with:
   "I'd love to help you master this! To provide the most accurate explanation for your syllabus, could you please tell me which **Board** (CBSE, ICSE, IB, or State Board) and **Class/Exam** (Class 6-12, NEET, or JEE) you are preparing for?"
3. **Action (If YES):** Proceed to the structured explanation in Rule 2.

# CRITICAL RULE 2: THE TEACHING STRUCTURE (WHY BEFORE HOW)
Once (and only once) the context is established, provide your response using this 5-point format:

1. 🧠 **CONCEPT:** Explain the "Why" and the fundamental principle simply.
2. 🌍 **REAL-WORLD CONTEXT:** Relate it to daily life or industrial precision (e.g., manufacturing/labs).
3. ✍️ **SOLUTION:** Step-by-step breakdown using LaTeX for equations. **Bold** keywords.
4. ✅ **ANSWER:** A clear final result with correct units.
5. 🚀 **HERO TIP:** An exam shortcut, mnemonic, or pro-tip to avoid common errors.

# TONE & STYLE
- **Professional & Encouraging:** You are a mentor who focuses on "Why" and "How" rather than rote memorization.
- **No Fluff:** You are pure teaching intelligence.
- **Technical Rigor:** Use LaTeX for all math/science (e.g., $HA \rightleftharpoons H^+ + A^-$).

# CONSTRAINTS
- Never mention you are an AI. You are AyA.
- Do not repeat the intake question once the student has answered it."""

# ── MOCK TEST FUNCTIONS ───────────────────────────────────────
def generate_questions(model, board, cls, subject, chapter, num, difficulty, q_type):
    client = groq_openai(API_KEY)
    ctx = (f"Strict {board} Board Examiner. Subject:{subject}, Class:{cls}, Chapter:'{chapter}'. "
           f"Questions must be 100% factually correct per {board} textbooks. One indisputable correct answer.")
    if q_type == "MCQ":
        prompt = f"""{ctx}
Generate exactly {num} {difficulty}-level MCQs. Return ONLY this JSON, no other text:
[{{"id":1,"question":"...","options":["A","B","C","D"],"correct_answer":"A"}}]
Verify correct_answer matches one option exactly."""
    else:
        prompt = f"""{ctx}
Generate exactly {num} {difficulty}-level Descriptive questions. Return ONLY this JSON:
[{{"id":1,"question":"...","marks":3}}]"""
    try:
        r = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"Output strictly valid JSON only. No markdown fences. No explanation."},
                {"role":"user","content":prompt}
            ], temperature=0.1)
        c = r.choices[0].message.content.strip().replace("```json","").replace("```","").strip()
        return json.loads(c)
    except Exception as e:
        st.error(f"Generation failed: {e}")
        return None

def grade_mcq(questions, answers, board, cls, subject, model):
    client = groq_openai(API_KEY)
    score, wrong = 0, ""
    for q in questions:
        u = answers.get(str(q["id"])); c = q["correct_answer"]
        if u == c: score += 1
        else: wrong += f"Q:{q['question']}\nStudent:{u}\nCorrect:{c}\n\n"
    st.session_state.mt_score = score
    st.session_state.mt_total = len(questions)
    if score == len(questions):
        return "### 🏆 Perfect Score!\nComplete mastery of this topic. Outstanding work."
    try:
        r = client.chat.completions.create(model=model, temperature=0.3,
            messages=[{"role":"user","content":
                f"Student scored {score}/{len(questions)} in {board} Cl.{cls} {subject}.\nMistakes:\n{wrong}\n"
                "Provide Scope for Improvement: explain WHY each answer was wrong and WHY correct answer is right. Use Markdown."}])
        return r.choices[0].message.content
    except Exception as e: return f"Grading error: {e}"

def grade_descriptive(questions, answers, board, cls, subject, model):
    client = groq_openai(API_KEY)
    qa, total = "", 0
    for q in questions:
        m = q.get("marks",1); total += m
        qa += f"Q({m}m): {q['question']}\nAnswer: {answers.get(str(q['id']),'—')}\n\n"
    st.session_state.mt_total = total
    try:
        r = client.chat.completions.create(model=model, temperature=0.2,
            messages=[{"role":"user","content":
                f"Strict {board} Cl.{cls} {subject} examiner.\n{qa}\n"
                f"Award marks per question, state total/{total}, give Scope for Improvement. Markdown format."}])
        return r.choices[0].message.content
    except Exception as e: return f"Grading error: {e}"

def best_model():
    return BEST_MODELS[0]

# ── HEADER ────────────────────────────────────────────────────
logo = get_img_b64("logo.png")
logo_tag = (f'<img src="data:image/png;base64,{logo}" '
            'style="height:48px;width:48px;border-radius:50%;'
            'border:2px solid #ffd700;object-fit:cover;box-shadow:0 0 12px rgba(255,215,0,.4);">'
            if logo else "🧬")

st.markdown(f"""
<div style="display:flex;align-items:center;gap:14px;padding:20px 4px 8px;">
  {logo_tag}
  <div>
    <div style="font-size:1.2rem;font-weight:900;color:#fff;">The Molecular Man</div>
    <div style="font-size:.75rem;color:#ffd700;letter-spacing:1.5px;text-transform:uppercase;">AI Suite · Powered by AyA</div>
  </div>
</div>
""", unsafe_allow_html=True)

tab_aya, tab_mt = st.tabs(["🤖  AyA Tutor", "📝  Mock Tests"])

# ══════════════════════════════════════════════════════════════
# TAB 1 — AyA TUTOR
# ══════════════════════════════════════════════════════════════
with tab_aya:
    st.markdown("""
    <div style="text-align:center;padding:28px 0 20px;">
      <div style="display:inline-block;padding:4px 16px;border-radius:20px;margin-bottom:14px;
          background:rgba(109,40,217,.2);border:1px solid rgba(167,139,250,.4);">
        <span style="font-size:.7rem;font-weight:800;letter-spacing:2px;color:#c4b5fd;">⚡ LIVE · 24/7 · FREE</span>
      </div>
      <h2 style="font-size:clamp(1.8rem,5vw,3rem);font-weight:900;color:#fff;margin:0 0 8px;">
        Meet <span style="color:#ffd700;">AyA</span>
      </h2>
      <p style="color:#94a3b8;font-size:.95rem;max-width:480px;margin:0 auto;line-height:1.7;">
        Your tireless AI tutor. Ask any question — Chemistry, Physics, Maths, Biology.<br>
        She never sleeps. She never judges. She simply teaches.
      </p>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    for col,num,lbl in [(c1,"24/7","Always Online"),(c2,"₹0","Cost Forever"),
                         (c3,"6+","Boards"),(c4,"∞","Questions")]:
        col.metric(lbl, num)

    st.divider()

    with st.expander("📝 New Problem", expanded=(len(st.session_state.aya_msgs)==0)):
        mode = st.radio("Input:", ["✏️ Type Problem","📄 Upload PDF"], horizontal=True)
        if "✏️" in mode:
            txt = st.text_area("Your question:", height=110, placeholder="e.g. Explain SN2 reaction mechanism with an example.")
            if st.button("🚀 Ask AyA", key="aya_txt_btn"):
                if txt.strip():
                    st.session_state.aya_msgs = [{"role":"user","content":f"PROBLEM:\n{txt}"}]
                    st.rerun()
                else: st.warning("Please type a question first.")
        else:
            pdf = st.file_uploader("Upload PDF (first 2 pages)", type=["pdf"], key=f"pdf_{st.session_state.aya_key}")
            if st.button("🚀 Analyse PDF", key="aya_pdf_btn"):
                if pdf:
                    try:
                        reader = PyPDF2.PdfReader(pdf)
                        text = "".join(reader.pages[i].extract_text()[:3000] for i in range(min(2,len(reader.pages))))
                        st.session_state.aya_msgs = [{"role":"user","content":f"PROBLEM from PDF:\n{text}"}]
                        st.session_state.aya_key += 1
                        st.rerun()
                    except Exception as e: st.error(f"PDF read error: {e}")
                else: st.warning("Please upload a PDF first.")

    for msg in st.session_state.aya_msgs:
        with st.chat_message(msg["role"]):
            c = msg["content"]
            if msg["role"]=="user" and (c.startswith("PROBLEM:") or c.startswith("PROBLEM from PDF:")):
                with st.expander("📄 Uploaded Problem", expanded=False): st.markdown(c)
            else: st.markdown(c)

    if st.session_state.aya_msgs and st.session_state.aya_msgs[-1]["role"]=="user":
        with st.chat_message("assistant"):
            with st.spinner("AyA is thinking…"):
                try:
                    gc = Groq(api_key=API_KEY)
                    msgs = [{"role":"system","content":AYA_PROMPT}] + st.session_state.aya_msgs
                    resp = None
                    for m in BEST_MODELS:
                        try:
                            resp = gc.chat.completions.create(
                                messages=msgs, model=m, temperature=0.5, max_tokens=5000
                            ).choices[0].message.content
                            break
                        except: continue
                    resp = resp or "❌ Could not connect. Please try again."
                    st.markdown(resp)
                    st.session_state.aya_msgs.append({"role":"assistant","content":resp})
                except Exception as e: st.error(f"Error: {e}")

    if st.session_state.aya_msgs:
        if fu := st.chat_input("Ask AyA a follow-up…"):
            st.session_state.aya_msgs.append({"role":"user","content":fu})
            st.rerun()

# ══════════════════════════════════════════════════════════════
# TAB 2 — MOCK TESTS
# ══════════════════════════════════════════════════════════════
with tab_mt:
    st.markdown("""
    <div style="text-align:center;padding:28px 0 20px;">
      <div style="display:inline-block;padding:4px 16px;border-radius:20px;margin-bottom:14px;
          background:rgba(0,255,255,.08);border:1px solid rgba(0,255,255,.35);">
        <span style="font-size:.7rem;font-weight:800;letter-spacing:2px;color:#00ffff;">∞ INFINITE MOCK TEST ENGINE</span>
      </div>
      <h2 style="font-size:clamp(1.8rem,5vw,3rem);font-weight:900;color:#fff;margin:0 0 8px;">
        Generate. Practice. <span style="color:#ffd700;">Master.</span>
      </h2>
      <p style="color:#94a3b8;font-size:.95rem;max-width:480px;margin:0 auto;line-height:1.7;">
        Fresh AI-generated test papers for CBSE, ICSE, IB, State Boards, NEET &amp; JEE.<br>
        Every paper unique. Every paper ₹0.
      </p>
    </div>
    """, unsafe_allow_html=True)

    MODEL = best_model()

    if not st.session_state.mt_qs:
        st.markdown("#### ⚙️ Configure Your Test")
        with st.container(border=True):
            L, R = st.columns(2, gap="large")
            with L:
                st.markdown("**📋 Exam Details**")
                board  = st.selectbox("Board", ["CBSE","ICSE","IGCSE","IB","Tamil Nadu State Board","Maharashtra Board","Other"])
                cls    = st.selectbox("Class", [str(i) for i in range(6,13)] + ["NEET","JEE","Other"])
                diff   = st.selectbox("Difficulty", ["Easy","Medium","Hard"])
            with R:
                st.markdown("**📚 Topic Details**")
                subj   = st.text_input("Subject", placeholder="e.g. Physics")
                chap   = st.text_input("Chapter", placeholder="e.g. Laws of Motion")
                qc1,qc2 = st.columns(2)
                with qc1: qtype = st.radio("Type", ["MCQ","Descriptive"])
                with qc2: num   = st.number_input("Count", 1, 20, 5)

        st.markdown("")
        if st.button("⚡ GENERATE MOCK TEST"):
            if not subj.strip() or not chap.strip():
                st.warning("⚠️ Please fill in Subject and Chapter.")
            else:
                with st.spinner(f"Generating {board} {qtype}s for {chap}…"):
                    st.session_state.mt_answers  = {}
                    st.session_state.mt_feedback = None
                    st.session_state.mt_score    = 0
                    st.session_state.mt_qtype    = qtype
                    st.session_state.mt_cfg      = {"board":board,"class":cls,"subject":subj,"chapter":chap,"diff":diff}
                    qs = generate_questions(MODEL, board, cls, subj, chap, num, diff, qtype)
                    if qs:
                        st.session_state.mt_qs = qs
                        st.rerun()

    elif st.session_state.mt_feedback:
        cfg   = st.session_state.mt_cfg
        score = st.session_state.mt_score
        total = st.session_state.mt_total

        st.markdown(f"""
        <div style="background:rgba(255,215,0,.06);border:1px solid rgba(255,215,0,.25);
             border-radius:18px;padding:24px;text-align:center;margin-bottom:20px;">
          <div style="font-size:.68rem;font-weight:800;letter-spacing:2px;text-transform:uppercase;
               color:#ffd700;margin-bottom:6px;">📊 Result Analysis</div>
          <p style="color:#94a3b8;margin:0 0 12px;font-size:.9rem;">
            {cfg.get('board','')} · Class {cfg.get('class','')} · {cfg.get('subject','')} · {cfg.get('chapter','')}
          </p>
          {'<div style="font-size:2rem;font-weight:900;color:#ffd700;border:2px solid rgba(255,215,0,.4);display:inline-block;padding:10px 32px;border-radius:30px;">' + str(score) + ' / ' + str(total) + '</div>' if st.session_state.mt_qtype=="MCQ" else ''}
        </div>
        """, unsafe_allow_html=True)

        if st.session_state.mt_qtype == "MCQ":
            pct = round((score/total)*100) if total else 0
            m1,m2,m3 = st.columns(3)
            m1.metric("Score",      f"{score}/{total}")
            m2.metric("Percentage", f"{pct}%")
            m3.metric("Status",     "✅ Pass" if pct >= 40 else "❌ Revise")

        with st.container(border=True):
            st.markdown("### 🧠 Examiner's Feedback")
            st.markdown(st.session_state.mt_feedback)

        if st.session_state.mt_qtype == "MCQ":
            with st.expander("📋 Full Answer Key"):
                for q in st.session_state.mt_qs:
                    u = st.session_state.mt_answers.get(str(q["id"]))
                    c = q["correct_answer"]
                    ok = u == c
                    st.markdown(f"**Q{q['id']}.** {q['question']}")
                    if ok: st.success(f"✅ {u}")
                    else:
                        st.error(f"❌ Your answer: {u}")
                        st.success(f"✅ Correct: {c}")
                    st.divider()

        st.markdown("")
        if st.button("🔄 New Test", key="new_test"):
            st.session_state.mt_qs       = None
            st.session_state.mt_feedback = None
            st.session_state.mt_answers  = {}
            st.session_state.mt_score    = 0
            st.rerun()

    else:
        cfg = st.session_state.mt_cfg
        st.markdown(f"""
        <div style="background:rgba(0,255,255,.04);border:1px solid rgba(0,255,255,.22);
             border-radius:16px;padding:18px 22px;margin-bottom:20px;">
          <span style="font-size:.68rem;font-weight:800;letter-spacing:2px;
                color:#00ffff;text-transform:uppercase;">📝 Exam in Progress</span>
          <p style="color:#e2e8f0;margin:6px 0 0;font-size:.9rem;">
            <strong>{cfg.get('board','')} · Class {cfg.get('class','')} · 
            {cfg.get('subject','')} · {cfg.get('chapter','')}</strong>
            &nbsp;|&nbsp;{cfg.get('diff','')} · {st.session_state.mt_qtype}
          </p>
        </div>
        """, unsafe_allow_html=True)

        for q in st.session_state.mt_qs:
            qid = str(q["id"])
            m_txt = f" *({q.get('marks',1)} marks)*" if st.session_state.mt_qtype=="Descriptive" else ""
            st.markdown(f"**Q{q['id']}.** {q['question']}{m_txt}")
            if st.session_state.mt_qtype == "MCQ":
                cur = st.session_state.mt_answers.get(qid)
                opts = q["options"]
                idx  = opts.index(cur) if cur in opts else None
                chosen = st.radio("", opts, index=idx, key=f"q_{qid}", label_visibility="collapsed")
                st.session_state.mt_answers[qid] = chosen
            else:
                cur = st.session_state.mt_answers.get(qid,"")
                ans = st.text_area("", value=cur, height=100, key=f"q_{qid}",
                                    placeholder="Write your answer…", label_visibility="collapsed")
                st.session_state.mt_answers[qid] = ans
            st.divider()

        if st.button("✅ SUBMIT EXAM", key="submit_exam"):
            qtype = st.session_state.mt_qtype
            if qtype == "MCQ":
                unanswered = [q for q in st.session_state.mt_qs
                              if not st.session_state.mt_answers.get(str(q["id"]))]
                if unanswered:
                    st.error(f"⚠️ Please answer all questions ({len(unanswered)} remaining).")
                    st.stop()
            cfg = st.session_state.mt_cfg
            with st.spinner("Evaluating your performance…"):
                if qtype == "MCQ":
                    fb = grade_mcq(st.session_state.mt_qs, st.session_state.mt_answers,
                                   cfg.get("board"), cfg.get("class"), cfg.get("subject"), MODEL)
                else:
                    fb = grade_descriptive(st.session_state.mt_qs, st.session_state.mt_answers,
                                           cfg.get("board"), cfg.get("class"), cfg.get("subject"), MODEL)
                st.session_state.mt_feedback = fb
                st.rerun()

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top:48px;border-top:1px solid rgba(255,255,255,.08);padding-top:24px;">
  <div style="background:rgba(0,0,0,.35);border:1px solid rgba(255,215,0,.2);border-radius:18px;
       padding:22px 28px;display:flex;align-items:center;justify-content:space-between;
       flex-wrap:wrap;gap:14px;margin-bottom:20px;">
    <div>
      <div style="font-size:.68rem;font-weight:800;letter-spacing:2px;color:#ffd700;
           text-transform:uppercase;margin-bottom:4px;">🏠 Our Main Website</div>
      <div style="font-size:1rem;font-weight:800;color:#fff;">The Molecular Man Expert Tuition Solutions</div>
      <div style="font-size:.82rem;color:#94a3b8;margin-top:2px;">Live Classes · Notes · Student Portal · Contact</div>
    </div>
    <a href="https://themolecularmanexpert.gitlab.io/AyA/" target="_blank"
       style="display:inline-block;padding:11px 26px;background:linear-gradient(135deg,#ffd700,#ffb900);
              color:#000;border-radius:50px;font-weight:800;font-size:.88rem;text-decoration:none;
              letter-spacing:.8px;text-transform:uppercase;box-shadow:0 4px 16px rgba(255,215,0,.35);
              white-space:nowrap;">
      🌐 Visit Website →
    </a>
  </div>
  <div style="text-align:center;color:rgba(255,255,255,.2);font-size:.75rem;padding-bottom:20px;">
    The Molecular Man Expert Tuition Solutions · Madurai, Tamil Nadu · Built by Mohammed Salmaan M.
  </div>
</div>
""", unsafe_allow_html=True)

