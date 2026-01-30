import streamlit as st
from groq_llm import query_llama
from prompt import build_prompt
from image_utils import analyze_image
from PIL import Image

st.set_page_config(page_title="StyleSense", layout="centered")

st.title("👗 StyleSense – AI Fashion Recommendation System")

gender = st.selectbox("Select Gender", ["Male", "Female", "Unisex"])
occasion = st.selectbox(
    "Select Occasion",
    ["Casual", "Formal", "Party", "Interview", "Wedding"]
)

budget = st.slider("Budget (₹)", 1000, 10000, 3000)
colors = st.text_input("Preferred Colors (optional)")
image_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if st.button("Get AI Recommendation"):
    image_info = "No image uploaded"

    if image_file:
        img = Image.open(image_file)
        image_info = analyze_image(img)

    prompt = build_prompt(gender, occasion, budget, colors, image_info)
    response = query_llama(prompt)

    st.subheader("🧠 AI Styling Advice")
    st.write(response)
