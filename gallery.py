import streamlit as st
from PIL import Image
import os

def view_gallery():
    st.header('Image Gallery')
    gallery_path = 'gallery'
    if not os.path.exists(gallery_path):
        os.makedirs(gallery_path)
    images = os.listdir(gallery_path)
    if images:
        for image_file in images:
            image = Image.open(os.path.join(gallery_path, image_file))
            st.image(image, caption=image_file, use_container_width=True)
    else:
        st.write('No images in the gallery.')