import streamlit as st
import random
import time
from financial_analysis_automation import perform_rag

st.title("Stock chatbot 🤖")
st.write("I can help you with stock related queries.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input('Stock inquiry')
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    with st.chat_message("assistant"):
        response = perform_rag(prompt)
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})