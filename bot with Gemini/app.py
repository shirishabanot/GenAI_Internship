import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB4tK6azgrb_-VQSgsNT2BW29ABjwaxJII")

llm = genai.GenerativeModel("models/gemini-1.5-flash")

chatbot = llm.start_chat(history=[])

st.title("Welcome to the Chatbot")

st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

human_prompt = st.chat_input("Say Something...")

if human_prompt:
    st.chat_message("human").write(human_prompt)
    response = chatbot.send_message(human_prompt)
    st.chat_message("ai").write(response.text)



# ---Virtual environments ctreating steps---
#  cd ..
# cd "F:\My Documents"
#  .\.env_jupyter\.\.env_jupyter\Scripts\Activate.bat
# .\.env_jupyter\Scripts\Activate.bat
#  cd siri
# Get-ChildItem "F:\My Documents\siri"
# cd "Building Chatbot with Gemini"
# streamlit run app.py
