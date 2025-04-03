import streamlit as st
import google.generativeai as genai
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key is missing. Please check the 'GEMINI_API_KEY' in your .env file!")
else:
    try:
        genai.configure(api_key=api_key)
        st.success("Gemini API successfully configured! ✅")
    except Exception as e:
        st.error(f"Failed to configure API key: {e}")

# Sidebar Navigation
with st.sidebar:
    selected = option_menu("ProfessorGPT", ["AI Professor", "Translator"],
                           icons=['🎓', '🌍'], menu_icon="📚", default_index=0)

# AI Professor Section
if selected == "AI Professor":
    st.title("🎓 ProfessorGPT - Your AI Professor")
    st.caption("Learn anything in a simple way!")
    st.divider()
    prompt = st.text_input("📚 What do you want to learn?")
    gptbutton = st.button("Ask Professor ✨")
    st.caption("Want more details? Click again!")
    st.divider()

    if gptbutton and prompt:
        with st.spinner("Professor is thinking... 🧠"):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")  # Use correct model name
                response = model.generate_content(f"Explain {prompt} in a simple way. Include sources if possible.")
                st.snow()
                st.write(response.text)  # Correct way to access response
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Translator Section
elif selected == "Translator":
    st.title("🌍 TranslatorGPT - AI Translator")
    st.caption("Translate anything instantly!")
    st.divider()
    prompt = st.text_input("📝 Enter text to translate:")
    gptbutton = st.button("Translate 🌎")
    st.caption("Click to translate!")
    st.divider()

    if gptbutton and prompt:
        with st.spinner("Translating... 🌐"):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(f"Translate this to English: {prompt}")
                st.snow()
                st.write(response.text)  # Correct way to access response
            except Exception as e:
                st.error(f"An error occurred: {e}")
