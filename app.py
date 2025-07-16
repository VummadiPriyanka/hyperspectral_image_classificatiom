import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(page_title="Hyperspectral Image Classifier")

st.title("🌈 Hyperspectral Image Classification")
st.write("Upload a hyperspectral image slice (or sample input) and the model will predict its class.")

uploaded_file = st.file_uploader("Choose a spectral image (RGB or composite)...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Placeholder for prediction
    if st.button("Predict"):
        # TODO: Replace with your model's actual prediction
        st.success("Predicted Class: Corn Field (Demo)")  # Change this
