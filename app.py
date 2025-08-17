import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 1. Load your trained MNIST model
model = load_model('mnist_cnn_model.h5')  # Ensure this file exists (tumhara saved model)

# 2. Streamlit UI
st.title("MNIST Digit Recognizer 🔢")
st.write("Upload a handwritten digit (0-9) image, and I'll predict it!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read and preprocess the image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)  # Grayscale
    img = cv2.resize(img, (28, 28))  # Resize to 28x28
    img = img.reshape(1, 28, 28, 1).astype('float32') / 255  # Normalize

    # Display the uploaded image
    st.image(img.reshape(28, 28), caption="Uploaded Image", width=100)

    # Predict
    prediction = model.predict(img)
    predicted_digit = np.argmax(prediction)

    st.success(f"Predicted Digit: **{predicted_digit}**")
    st.write(f"Confidence: {np.max(prediction) * 100:.2f}%")