import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import io

def remove_background():
    st.header('Remove Background')
    uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_container_width=True)
        with st.spinner('Removing background...'):
            output_image = remove(image)
        st.image(output_image, caption='Processed Image', use_container_width=True)
        buf = io.BytesIO()
        output_image.save(buf, format='PNG')
        byte_im = buf.getvalue()
        st.download_button(
            label="Download Processed Image",
            data=byte_im,
            file_name="processed_image.png",
            mime="image/png"
        )

def edit_image():
    st.header('Edit Image')
    uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Image', use_container_width=True)
        edit_option = st.selectbox('Choose an edit option', ['Crop', 'Resize', 'Rotate', 'Flip'])
        if edit_option == 'Crop':
            left = st.slider('Left', 0, image.width, 0)
            top = st.slider('Top', 0, image.height, 0)
            right = st.slider('Right', 0, image.width, image.width)
            bottom = st.slider('Bottom', 0, image.height, image.height)
            cropped_image = image.crop((left, top, right, bottom))
            st.image(cropped_image, caption='Cropped Image', use_container_width=True)
        elif edit_option == 'Resize':
            width = st.slider('Width', 1, image.width, image.width)
            height = st.slider('Height', 1, image.height, image.height)
            resized_image = image.resize((width, height))
            st.image(resized_image, caption='Resized Image', use_container_width=True)
        elif edit_option == 'Rotate':
            angle = st.slider('Angle', 0, 360, 0)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption='Rotated Image', use_container_width=True)
        elif edit_option == 'Flip':
            flip_option = st.selectbox('Flip Option', ['Horizontal', 'Vertical'])
            if flip_option == 'Horizontal':
                flipped_image = ImageOps.mirror(image)
            else:
                flipped_image = ImageOps.flip(image)
            st.image(flipped_image, caption='Flipped Image', use_container_width=True)