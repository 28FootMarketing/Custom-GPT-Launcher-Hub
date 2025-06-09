import streamlit as st
import datetime

def launch_gpt(url, user):
    timestamp = datetime.datetime.now().isoformat()
    st.session_state['last_launch'] = timestamp
    st.markdown(f"[Click here to open your GPT in a new tab]({url})")
    # Here you can also log the user and timestamp to a database or file
