import streamlit as st
import os
from groq import Groq

key="put your api key here"
st.title("Chat with Groq Llama bot")

client=Groq(api_key=key)

st.sidebar.title("Model options for Llama")

selected=st.sidebar.selectbox("Chooose the llama model", ["llama3-8b-8192", "llama3-70b-8192"])
user_input=st.text_input("Enter your query: ")
if st.button("Submit"):
    chat=client.chat.completions.create(messages=[
        {
            "role":"user",
            "content":user_input
        }
        
        
    ], model=selected
                                  )
    actual_output=chat.choices[0].message.content
    st.write(actual_output)
    

