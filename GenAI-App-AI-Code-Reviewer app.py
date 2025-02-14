import streamlit as st
import google.generativeai as genai

# Configure the Google Generative AI API
genai.configure(api_key="PATH")  # Replace with your actual API key

# Set up the app layout
st.title("An AI Code Reviewer")
st.write("Enter your Python code below for review:")

# Text area for code input
user_code = st.text_area("Enter your Python code here...", height=200)

# Button to trigger code review
if st.button("Generate"):
    if user_code:
        # Initialize the generative model
        llm = genai.GenerativeModel("models/gemini-1.5-flash")
        
        # Send the user code for review
        chatbot = llm.start_chat(history=[])
        response = chatbot.send_message(f"Review the following Python code and identify any bugs:\n{user_code}")
        
        # Display the AI-generated response
        st.subheader("Code Review")
        st.write("Bug Report:")
        st.write(response.text)  # Display AI response




# cd
# PS F:\My Documents\siri> python -m venv .env_jupyter
# >> 
# PS F:\My Documents\siri> 
# PS F:\My Documents\siri> .\.env_jupyter\Scripts\activate.bat
# >> 
# PS F:\My Documents\siri> .\.env_jupyter\Scripts\Activate.ps1
#     (.env_jupyter) PS F:\My Documents\siri> .\.env_jupyter\Scripts\Activate.ps1
# >>
# (.env_jupyter) PS F:\My Documents\siri> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# >>
# (.env_jupyter) PS F:\My Documents\siri> .\.env_jupyter\Scripts\Activate.ps1
# >>
# (.env_jupyter) PS F:\My Documents\siri> .\.env_jupyter\Scripts\activate.bat
# >>
# (.env_jupyter) PS F:\My Documents\siri> cd "Building Chatbot with Gemini\GenAI-App-AI-Code-Reviewer"
# >>
# (.env_jupyter) PS F:\My Documents\siri\Building Chatbot with Gemini\GenAI-App-AI-Code-Reviewer> streamlit run app.py

#   You can now view your Streamlit app in your browser.

#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.5:8501
APIKEY___PATH__AIzaSyBq7czKCO8KjjOFrmvDOd8qbIt-CZwYDHk




