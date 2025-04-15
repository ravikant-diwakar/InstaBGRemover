import streamlit as st
from auth import login, signup
from image_processing import remove_background, edit_image
from gallery import view_gallery

# Streamlit app
st.set_page_config(page_title="InstaBGRemover", layout="wide")
st.title('InstaBGRemover')

# Sidebar options
app_option = st.sidebar.selectbox('Choose an option', ['Remove Background', 'Edit Image', 'View Gallery'])

if app_option == 'Remove Background':
    remove_background()
else:
    # User authentication
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False

    if not st.session_state['authenticated']:
        auth_option = st.sidebar.selectbox('Login or Sign Up', ['Login', 'Sign Up'])
        if auth_option == 'Login':
            login()
        else:
            signup()
    else:
        st.sidebar.success("Logged in as {}".format(st.session_state['username']))
        if app_option == 'Edit Image':
            edit_image()
        elif app_option == 'View Gallery':
            view_gallery()