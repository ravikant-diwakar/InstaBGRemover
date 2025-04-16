import streamlit as st

users = {}

def login_ui():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state.authenticated = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

def signup_ui():
    st.subheader("Sign Up")
    new_user = st.text_input("Username", key="signup_user")
    new_pass = st.text_input("Password", type="password", key="signup_pass")
    if st.button("Sign Up"):
        if new_user in users:
            st.warning("User already exists.")
        else:
            users[new_user] = new_pass
            st.success("Account created! Please login.")

def check_auth():
    return st.session_state.get("authenticated", False)