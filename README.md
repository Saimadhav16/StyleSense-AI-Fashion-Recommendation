# StyleSense – AI Fashion Recommendation System 👗🤖

StyleSense is an AI-powered fashion recommendation system that suggests outfit ideas based on user preferences such as gender, occasion, budget, colors, and uploaded images.  
The system uses **Groq LLaMA 3.3 (70B)** for intelligent fashion reasoning.

---

## 🚀 Features
- Gender-based outfit recommendations
- Occasion-aware styling (Casual, Formal, Party, Interview, Wedding)
- Budget-based suggestions
- Optional color preferences
- Image-based fashion understanding
- Fast AI responses using Groq API

---

## 🛠️ Tech Stack
- Python
- Streamlit
- Groq LLaMA 3.3 70B
- Pillow (Image Processing)
- dotenv

---

## 📂 Project Structure
```text
StyleSense-AI-Fashion-Recommendation/
│
├── app.py               # Streamlit application entry point
├── groq_llm.py          # Groq LLaMA 3.3 API logic
├── prompt.py            # Prompt generation logic
├── image_utils.py       # Image analysis utilities
├── requirements.txt     # Project dependencies
├── .gitignore           # Ignored files
└── README.md            # Project documentation
```
---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Saimadhav16/StyleSense-AI-Fashion-Recommendation.git
cd StyleSense-AI-Fashion-Recommendation
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File
Create a `.env` file in the project root and add:
```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ Do NOT upload `.env` to GitHub.

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

The app will open at:
```
http://localhost:8501
```
---

## 🧠 How It Works
1. User selects gender, occasion, budget, and preferred colors
2. User optionally uploads an image
3. Image is analyzed for fashion context
4. A structured prompt is generated
5. Groq LLaMA 3.3 (70B) processes the prompt
6. AI generates outfit recommendations
7. Results are displayed in real-time
## 👥 Team Members

| Name | Role |
|-----|-----|
| Pavani | Team Lead & Backend |
| Sathwika | Frontend Development |
| Manohar | Image Processing |
| Madhav | Prompt Engineering |
| Sharanya | Documentation & Testing |
---

## 📌 Project Type
Team Project (5 Members)  
Academic / Hackathon Ready

