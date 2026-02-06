import streamlit as st
from groq import Groq
import os
from PIL import Image
import base64
import io
import PyPDF2

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="The Molecular Man AI",
    page_icon="logo.png",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 2. HELPER FUNCTIONS & SETUP
# -----------------------------------------------------------------------------
def get_img_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
# Dynamic Key to fix uploader error
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0
# Set default username since auth is removed
if "username" not in st.session_state:
    st.session_state.username = "Student"

# -----------------------------------------------------------------------------
# 3. CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #004e92 0%, #000428 100%) !important;
        background-attachment: fixed;
    }
    h1, h2, h3, h4, h5, h6, p, div, span, li, label, .stMarkdown {
        color: #ffffff !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"], .login-container {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
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
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea, 
    .stSelectbox > div > div > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    /* Chat Message Styling */
    .stChatMessage {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. SYSTEM PROMPT
# -----------------------------------------------------------------------------
SYSTEM_PROMPT = """You are **Aya**, the Lead AI Tutor at **The Molecular Man Expert Tuition Solutions**. 
Your Mission: Guide students on a journey from "Zero" (absolute beginner) to "Hero" (advanced mastery).
Your Tone: Encouraging, clear, patient, and intellectually rigorous.

### RESPONSE GUIDELINES
1. **Be Conversational:** If the user asks a follow-up (e.g., "Explain step 2"), answer that specific question directly.
2. **Structure:** For main problems, use:
   - 🧠 CONCEPT
   - 🌍 REAL-WORLD CONTEXT
   - ✍️ SOLUTION (Step-by-Step)
   - ✅ ANSWER
   - 🚀 HERO TIP
3. **Format:** Use Bold for keywords and LaTeX for math.
"""

# -----------------------------------------------------------------------------
# 5. MAIN APP FUNCTION
# -----------------------------------------------------------------------------
def show_main_app():
    # Header
    col1, col2 = st.columns([3, 1], vertical_alignment="center")
    with col1:
        logo_b64 = get_img_as_base64("logo.png")
        if logo_b64:
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 20px;">
                    <img src="data:image/png;base64,{logo_b64}" style="height: 80px; width: 80px; border-radius: 50%; border: 3px solid #ffd700; box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);">
                    <div>
                        <h1 style="margin: 0; font-size: 34px; color: white; text-shadow: 0 2px 4px rgba(0,0,0,0.5);">The Molecular Man</h1>
                        <p style="margin: 0; color: #ffd700; font-size: 16px; font-weight: 500;">Expert Tuition Solutions AI</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="display: flex; align-items: center; gap: 15px;">
                    <div>
                        <h1 style="margin: 0; font-size: 34px; color: white;">The Molecular Man</h1>
                        <p style="margin: 0; color: #ffd700; font-size: 16px;">Expert Tuition Solutions AI</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.markdown(f"<div style='text-align: right; color: white; padding-top: 10px;'>👤 {st.session_state.username}</div>", unsafe_allow_html=True)
    
    st.write("")
    
    # API Setup
    try:
        groq_api_key = st.secrets["GROQ_API_KEY"]
        groq_client = Groq(api_key=groq_api_key)
    except Exception:
        st.error("⚠️ GROQ_API_KEY not found in Streamlit Secrets!")
        st.stop()

    # --- PROBLEM INPUT SECTION ---
    with st.expander("📝 New Problem Input", expanded=(len(st.session_state.messages) == 0)):
        st.markdown("### Upload or Type Problem")
        input_type = st.radio("Input Method:", ["📄 Text Problem", "🖼️ Upload Image", "📕 Upload PDF"], horizontal=True)
        
        prompt_content = None
        
        if input_type == "📄 Text Problem":
            user_text = st.text_area("Paste question:", height=100)
            if st.button("Start New Chat 🚀", use_container_width=True):
                if user_text:
                    st.session_state.messages = [] 
                    prompt_content = f"PROBLEM:\n{user_text}"
                    st.session_state.messages.append({"role": "user", "content": prompt_content})
                    st.rerun()
                else:
                    st.warning("Please enter text.")

        elif input_type == "🖼️ Upload Image":
            # Dynamic Key Fix
            key_str = f"img_uploader_{st.session_state.uploader_key}"
            uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png", "webp"], key=key_str)
            
            if st.button("Analyze Image 🚀", use_container_width=True):
                if uploaded_file:
                    try:
                        st.session_state.messages = [] 
                        image = Image.open(uploaded_file)
                        if image.mode in ("RGBA", "P"): image = image.convert("RGB")
                        buffered = io.BytesIO()
                        image.save(buffered, format="JPEG", quality=85)
                        img_base64 = base64.standard_b64encode(buffered.getvalue()).decode("utf-8")
                        
                        msg_content = [
                            {"type": "text", "text": "SOLVE THE PROBLEM IN THIS IMAGE:"},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}}
                        ]
                        st.session_state.messages.append({"role": "user", "content": msg_content})
                        
                        st.session_state.uploader_key += 1 # Reset Uploader
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error processing image: {e}")
                else:
                    st.warning("Please upload an image.")

        elif input_type == "📕 Upload PDF":
            # Dynamic Key Fix
            key_str = f"pdf_uploader_{st.session_state.uploader_key}"
            uploaded_file = st.file_uploader("Upload PDF", type=["pdf"], key=key_str)
            
            if st.button("Analyze PDF 🚀", use_container_width=True):
                if uploaded_file:
                    try:
                        st.session_state.messages = [] 
                        pdf_reader = PyPDF2.PdfReader(uploaded_file)
                        pdf_text = ""
                        for page_num in range(min(2, len(pdf_reader.pages))):
                            pdf_text += pdf_reader.pages[page_num].extract_text()[:3000]
                        
                        prompt_content = f"PROBLEM from PDF:\n{pdf_text}"
                        st.session_state.messages.append({"role": "user", "content": prompt_content})
                        
                        st.session_state.uploader_key += 1 # Reset Uploader
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error reading PDF: {e}")
                else:
                    st.warning("Please upload a PDF.")

    # --- CHAT INTERFACE ---
    st.markdown("---")
    st.markdown("### 💬 Chat with Aya")
    
    # Display Chat History (With Text Hiding)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            if isinstance(msg["content"], list):
                st.write(msg["content"][0]["text"])
                st.caption("🖼️ [Image Uploaded]")
            else:
                # Hide large prompts (PDF/Problems)
                if msg["role"] == "user" and (msg["content"].startswith("PROBLEM from PDF:") or msg["content"].startswith("PROBLEM:")):
                    with st.expander("📄 View Uploaded Problem Content (Click to Expand)", expanded=False):
                        st.markdown(msg["content"])
                else:
                    st.markdown(msg["content"])

    # Trigger AI Response
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        with st.chat_message("assistant"):
            with st.spinner("🤖 Aya is thinking..."):
                try:
                    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
                    
                    last_msg = st.session_state.messages[-1]["content"]
                    is_vision = isinstance(last_msg, list)
                    
                    if is_vision:
                        models = ["llama-3.2-11b-vision-preview", "llama-3.2-90b-vision-preview"]
                        response_text = None
                        for m in models:
                            try:
                                chat_completion = groq_client.chat.completions.create(
                                    messages=api_messages,
                                    model=m,
                                    temperature=0.5,
                                    max_tokens=2048,
                                )
                                response_text = chat_completion.choices[0].message.content
                                break
                            except:
                                continue
                        if not response_text:
                            response_text = "⚠️ **System Update:** Vision models unavailable."
                    
                    else:
                        models = ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile"]
                        response_text = None
                        for m in models:
                            try:
                                chat_completion = groq_client.chat.completions.create(
                                    messages=api_messages,
                                    model=m,
                                    temperature=0.5,
                                    max_tokens=6000,
                                )
                                response_text = chat_completion.choices[0].message.content
                                break
                            except:
                                continue
                        if not response_text:
                            response_text = "❌ Error: Could not connect to AI."

                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                
                except Exception as e:
                    st.error(f"System Error: {str(e)}")

    # Follow-up Input
    if st.session_state.messages:
        if user_input := st.chat_input("Ask a follow-up question..."):
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.rerun()

    # Footer
    st.write("")
    st.markdown("""
        <div style='text-align: center; color: rgba(255,255,255,0.5); padding: 20px;'>
            <p>The Molecular Man Expert Tuition Solutions | Madurai, Tamil Nadu</p>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. EXECUTION LOGIC
# -----------------------------------------------------------------------------
# Directly show the main app
show_main_app()
