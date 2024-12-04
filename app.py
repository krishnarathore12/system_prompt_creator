import streamlit as st
import os
from openai import OpenAI

st.title("System Prompt Creator")
st.subheader("Assume if Foundational Models were to be humans")

why = st.text_input("Why would they do it?", "You are ")
how = st.text_input("How would they do it?", "By doing ")
what = st.text_input("What will it achieve?", "Will give ")

openai_api_key = st.text_input("OPENAI-API-KEY", type="password")

client = OpenAI(
    api_key=openai_api_key,  
)

if st.button("Generate"):
   
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Create a system prompt for a Large Language Model (LLM) to guide its behavior. 
                    The prompt should be structured as follows:
                    - **Why**: {why}
                    - **How**: {how}
                    - **What**: {what}

                    Ensure the system prompt is clear, concise, and provides enough guidance for the model to understand its role, the process, and the expected outcome in first person and paragraph only.
                    """,
                }
            ],
            model="gpt-4o-mini",
        )
        
        st.write(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occurred: {e}")
