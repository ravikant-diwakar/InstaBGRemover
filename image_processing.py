import streamlit as st
from rembg import remove
from PIL import Image, ImageOps

def remove_bg_ui():
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        output = remove(image)
        st.image(output, caption="Image without background", use_container_width=True)
        st.download_button("Download", data=output.tobytes(), file_name="no_bg.png")

def edit_image_ui():
    uploaded_file = st.file_uploader("Upload an Image to Edit", type=["png", "jpg", "jpeg"], key="edit")
    if uploaded_file:
        image = Image.open(uploaded_file)

        st.image(image, caption="Original", use_container_width=True)

        option = st.selectbox("Edit Option", ["Crop", "Rotate", "Flip", "Resize"])

        if option == "Crop":
            left = st.number_input("Left", 0, image.width)
            top = st.number_input("Top", 0, image.height)
            right = st.number_input("Right", left, image.width)
            bottom = st.number_input("Bottom", top, image.height)
            if st.button("Apply Crop"):
                cropped = image.crop((left, top, right, bottom))
                st.image(cropped, caption="Cropped Image", use_container_width=True)

        elif option == "Rotate":
            angle = st.slider("Rotate Angle", -180, 180)
            if st.button("Rotate"):
                rotated = image.rotate(angle)
                st.image(rotated, caption="Rotated Image", use_container_width=True)

        elif option == "Flip":
            flip = st.radio("Flip Mode", ["Horizontal", "Vertical"])
            if st.button("Flip"):
                if flip == "Horizontal":
                    flipped = ImageOps.mirror(image)
                else:
                    flipped = ImageOps.flip(image)
                st.image(flipped, caption="Flipped Image", use_container_width=True)

        elif option == "Resize":
            width = st.number_input("Width", 1, 1000, value=image.width)
            height = st.number_input("Height", 1, 1000, value=image.height)
            if st.button("Resize"):
                resized = image.resize((int(width), int(height)))
                st.image(resized, caption="Resized Image", use_container_width=True)