import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import io

def remove_bg_ui():
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Original Image")
        
        with st.spinner("Removing background..."):
            output = remove(image)

        st.image(output, caption="Image without Background")

        # Convert image to byte stream
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button("📥 Download", data=byte_im, file_name="no_bg.png", mime="image/png")


def edit_image_ui():
    st.subheader("🎨 Edit Your Image")
    uploaded_file = st.file_uploader("Upload an Image to Edit", type=["png", "jpg", "jpeg"], key="edit")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image")

        option = st.selectbox("Select Edit Option", ["Crop", "Rotate", "Flip", "Resize"])

        if option == "Crop":
            st.markdown("#### Set Crop Dimensions:")
            left = st.number_input("Left", 0, image.width - 1)
            top = st.number_input("Top", 0, image.height - 1)
            right = st.number_input("Right", left + 1, image.width)
            bottom = st.number_input("Bottom", top + 1, image.height)
            if st.button("✂️ Apply Crop"):
                cropped = image.crop((left, top, right, bottom))
                st.image(cropped, caption="Cropped Image")

        elif option == "Rotate":
            angle = st.slider("Rotate Angle (°)", -180, 180, 0)
            if st.button("🔄 Rotate"):
                rotated = image.rotate(angle)
                st.image(rotated, caption=f"Rotated by {angle}°")

        elif option == "Flip":
            flip = st.radio("Flip Mode", ["Horizontal", "Vertical"])
            if st.button("↔️ Flip"):
                flipped = ImageOps.mirror(image) if flip == "Horizontal" else ImageOps.flip(image)
                st.image(flipped, caption=f"{flip} Flipped Image")

        elif option == "Resize":
            st.markdown("#### Enter New Dimensions:")
            width = st.number_input("Width", 1, 2000, value=image.width)
            height = st.number_input("Height", 1, 2000, value=image.height)
            if st.button("📐 Resize"):
                resized = image.resize((int(width), int(height)))
                st.image(resized, caption=f"Resized to {width}x{height}")
