# DEEPVISION-AI 👁️‍🗨️

A modern Streamlit web application powered by Google Gemini AI for multimodal vision, chatbot, and audio analysis tasks.

## 🚀 Features
- 📸 **Image Description**: Upload images and generate intelligent AI descriptions.
- 💬 **Gemini Chatbot**: Interactive conversational AI assistant.
- 🎵 **Audio Description**: Upload audio clips (`.mp3`) and extract AI insights.
- 🎨 **Modern Dark UI**: Sleek, responsive interface with easy API key configuration in the sidebar.

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/PalakThakur10/Deep-Vision-Ai.git
cd Deep-Vision-Ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key
Create a `.env` file in the project root (or use the sidebar in the app):
```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application
```bash
python -m streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.