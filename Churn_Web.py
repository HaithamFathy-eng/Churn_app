import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import joblib 
import base64


# Function to add offline background
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call background function
set_background("backgound.png")  


# Title
st.title(" Customer Churn Prediction ")

st.write("Enter customer details to predict if they will churn")

# Load dataset and model
df = pd.read_excel("churn_dataset.xlsx")
model = joblib.load("Churn_Model.pkl")

target = {1: "churn", 0: "not churn"}

# Inputs
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
tenure = st.sidebar.slider("Tenure (Months)", min_value=0, max_value=100, value=12)

gender_encoded = 1 if gender == "Male" else 0
input_data = np.array([[age, gender_encoded, tenure]])

# Predictions
prediction = model.predict(input_data)[0]
prediction_prob = model.predict_proba(input_data)[0]

# Results
st.subheader("Prediction Result")
st.write(f"Customer is {target[prediction]}")

st.subheader("Prediction Probability Result")
st.write(f"Probability of churn: {prediction_prob[1]:.2f}")
st.write(f"Probability of no churn: {prediction_prob[0]:.2f}")

if prediction == 1:
    st.error("⚠️ Customer is likely to churn!")
else:
    st.success("✅ Customer is not likely to churn.")
