import streamlit as st
from utils.auth import login_user
from utils.launcher import launch_gpt

st.set_page_config(page_title="🚀 Custom GPT Launcher", layout="wide")
st.title("🚀 Welcome to Your Custom GPT Hub")

user = login_user()

role = st.selectbox("What best describes you?", ["Student-Athlete", "Coach", "Parent", "Recruiter", "Business Owner"])

gpts = {
    "DIY Recruiting GPT": "https://chatgpt.com/g/g-680164288ea88191b5579446ecf1f2fd-diy-athletic-recruiting",
    "Credit Repair GPT": "https://chatgpt.com/g/g-32c95f3c609c4906ba6a1ea1246c1f28-credit-repair-pro-assistant",
    "Leadership GPT": "https://chatgpt.com/g/g-2d45021ccf9f476294d832812449e50e-code-switching-in-leadership"
}

if role == "Student-Athlete":
    st.subheader("🎯 Recruiting Tools")
    if st.button("Launch DIY Recruiting GPT"):
        launch_gpt(gpts["DIY Recruiting GPT"], user)

if role == "Parent":
    st.subheader("💰 Financial Support Tools")
    if st.button("Launch Credit Repair GPT"):
        launch_gpt(gpts["Credit Repair GPT"], user)

if role in ["Coach", "Recruiter", "Business Owner"]:
    st.subheader("🧠 Leadership & Mentorship Tools")
    if st.button("Launch Leadership GPT"):
        launch_gpt(gpts["Leadership GPT"], user)

st.markdown("💡 *Tip: Review each GPT’s starter prompt before launching for best results.*")

