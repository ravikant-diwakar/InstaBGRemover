import streamlit as st
from auth import check_auth, login_ui, signup_ui
from image_processing import remove_bg_ui, edit_image_ui
from gallery import show_gallery

st.set_page_config(page_title="InstaBGRemover", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.markdown("<style>" + open("assets/styles/style.css").read() + "</style>", unsafe_allow_html=True)

st.title("📸 InstaBGRemover")

menu = ["Home", "Login", "Sign Up", "Gallery"] if not st.session_state.authenticated else ["Home", "Gallery", "Logout"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Login":
    login_ui()
elif choice == "Sign Up":
    signup_ui()
elif choice == "Logout":
    st.session_state.authenticated = False
    st.experimental_rerun()
elif choice == "Gallery":
    if st.session_state.authenticated:
        show_gallery()
    else:
        st.warning("Please login to view your gallery.")
else:
    st.subheader("Remove Background from Image")
    remove_bg_ui()
    if st.session_state.authenticated:
        st.subheader("Edit Your Image")
        edit_image_ui()