import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
import cv2
import numpy as np
from PIL import Image
import io

# Load the acne detection model
model = load_model("facemodel.h5")

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        return weight / (height ** 2)
    except ZeroDivisionError:
        return None

# Function to classify BMI into categories
def bmi_category(bmi):
    if bmi is None:
        return "Invalid"
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    elif 30 <= bmi < 34.9:
        return "Obesity Class 1"
    elif 35 <= bmi < 39.9:
        return "Obesity Class 2"
    else:
        return "Obesity Class 3"

# Function to analyze PCOS risk based on BMI and image analysis
def pcos_risk_analysis(bmi, acne_detected, hair_growth_detected):
    if bmi and bmi > 25 and acne_detected and hair_growth_detected:
        return "High"
    else:
        return "Low"

# Function to predict acne using the model
def detect_acne(image):
    try:
        face = image.convert('RGB')
        face = face.resize((224, 224))
        face = img_to_array(face)
        face = preprocess_input(face)
        face = np.expand_dims(face, axis=0)

        # Make prediction
        (acne, withoutAcne) = model.predict(face)[0]
        return acne > withoutAcne, max(acne, withoutAcne) * 100  # Returns True if acne is detected, and the confidence score
    except Exception as e:
        st.error(f"Acne detection error: {str(e)}")
        return False, 0.0

# Placeholder function to detect excessive hair growth
def detect_hair_growth(image):
    # Hair growth detection logic can be added here
    return True

# Streamlit layout
st.title("PCOS Detection System")

# User inputs
weight = st.number_input("Weight (kg):", min_value=1.0, max_value=200.0)
height = st.number_input("Height (m):", min_value=0.5, max_value=2.5)
cycle_length = st.number_input("Menstrual Cycle Length (days):", min_value=1, max_value=60)
sleep_hours = st.number_input("Average Sleep Hours:", min_value=0, max_value=24)

acne_choice = st.selectbox("Do you have acne?", ("No", "Yes"))
hair_growth_choice = st.selectbox("Do you have excessive hair growth?", ("No", "Yes"))

# Image capture or upload
image_option = st.radio("Choose image source:", ("Upload Image", "Use Camera"))

if image_option == "Upload Image":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
else:
    uploaded_image = st.camera_input("Take a picture")

# Calculate and show PCOS risk
if st.button("Check PCOS Risk"):
    try:
        bmi = calculate_bmi(weight, height)
        bmi_cat = bmi_category(bmi)
        
        # Handle acne detection
        acne_detected = False
        hair_growth_detected = hair_growth_choice == "Yes"
        
        if uploaded_image is not None:
            # Open the image and convert for model processing
            img = Image.open(uploaded_image)
            acne_detected, acne_confidence = detect_acne(img)
            st.write(f"Acne detected: {'Yes' if acne_detected else 'No'} with confidence {acne_confidence:.2f}%")
        
        # Analyze PCOS risk
        pcos_risk = pcos_risk_analysis(bmi, acne_detected, hair_growth_detected)
        
        st.write(f"BMI: {bmi:.2f} ({bmi_cat})")
        st.write(f"PCOS Risk: {pcos_risk}")
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
