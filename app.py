from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
import PIL.Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gemini AI Web App", layout="centered")

# --- CUSTOM CSS FOR THEMING ---
def load_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stApp {
            background-color: #0e1117;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stButton>button {
            background-color: #4F8BF9;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1f6feb;
        }
        .stTextInput>div>div>input {
            background-color: #1e222d;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

load_custom_css()

# --- SIDEBAR ---
with st.sidebar:
    st.image("Deep VISION.png", width=120)
    st.title("✨ Gemini AI")
    st.markdown("Powered by Google Generative AI")
    st.markdown("---")
    
    env_api_key = os.getenv("GOOGLE_API_KEY", "")
    api_key = st.text_input(
        "🔑 Gemini API Key",
        value=env_api_key,
        type="password",
        help="Enter your Google Gemini API key or set it in .env"
    )
    
    st.markdown("---")
    st.markdown("🔹 Describe images\n🔹 Chat with AI\n🔹 Understand audio clips")
    st.markdown("---")
    st.markdown("📍 Made with ❤️ using Streamlit")

# --- CONFIGURE GOOGLE GEN AI ---
model = None
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    st.warning("⚠️ Please provide a Gemini API Key in the sidebar or via `.env` to use the AI features.")

# --- MAIN TITLE ---
st.title("🤖 Gemini AI Interface")
st.markdown("Welcome! Use this app to describe images, audio, and chat with Gemini.")
st.markdown("---")

# --- IMAGE DESCRIPTION ---
st.header("📸 Describe an Image")
img_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if img_file is not None:
    image = PIL.Image.open(img_file)
    st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

    col1, _ = st.columns([1, 3])
    with col1:
        if st.button("🧠 Generate Image Description"):
            if not model:
                st.error("❌ Please enter a valid Gemini API Key first.")
            else:
                with st.spinner("Analyzing image..."):
                    try:
                        response = model.generate_content(["Tell me about this image", image])
                        st.success("✅ Done!")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error generating description: {e}")

st.markdown("---")

# --- CHATBOT SECTION ---
st.header("💬 Gemini Chatbot")

if model and "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

user_input = st.text_input("📝 Ask a question to Gemini")
if st.button("📨 Send Message"):
    if not model:
        st.error("❌ Please enter a valid Gemini API Key first.")
    elif user_input:
        try:
            if "chat" not in st.session_state:
                st.session_state.chat = model.start_chat(
                    history=[
                        {"role": "user", "parts": "Hello"},
                        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
                    ]
                )
            response = st.session_state.chat.send_message(user_input)
            st.markdown("**Gemini:** " + response.text)
        except Exception as e:
            st.error(f"Error sending message: {e}")

st.markdown("---")

# --- AUDIO DESCRIPTION ---
st.header("🎵 Describe an Audio Clip")
audio_file = st.file_uploader("Upload an audio file (.mp3)", type=["mp3"])

if audio_file is not None:
    with open("temp_audio.mp3", "wb") as f:
        f.write(audio_file.read())

    col2, _ = st.columns([1, 3])
    with col2:
        if st.button("🎧 Generate Audio Description"):
            if not model:
                st.error("❌ Please enter a valid Gemini API Key first.")
            else:
                with st.spinner("Processing audio..."):
                    try:
                        myfile = genai.upload_file("temp_audio.mp3")
                        result = model.generate_content([myfile, "Describe this audio clip"])
                        st.success("✅ Done!")
                        st.write(result.text)
                    except Exception as e:
                        st.error(f"Error processing audio: {e}")
                    finally:
                        if os.path.exists("temp_audio.mp3"):
                            os.remove("temp_audio.mp3")

