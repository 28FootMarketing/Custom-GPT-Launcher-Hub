def login_user():
    import streamlit as st
    email = st.text_input("Enter your email to continue:")
    if email:
        st.session_state['user_email'] = email
        return email
    return None
