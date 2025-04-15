import streamlit as st

users = {}

def login():
    st.sidebar.header('Login')
    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')
    if st.sidebar.button('Login'):
        if username in users and users[username] == password:
            st.session_state['authenticated'] = True
            st.session_state['username'] = username
            st.sidebar.success('Login successful')
        else:
            st.sidebar.error('Invalid username or password')

def signup():
    st.sidebar.header('Sign Up')
    username = st.sidebar.text_input('Choose a Username')
    password = st.sidebar.text_input('Choose a Password', type='password')
    if st.sidebar.button('Sign Up'):
        if username in users:
            st.sidebar.error('Username already exists')
        else:
            users[username] = password
            st.sidebar.success('Sign up successful. Please log in.')