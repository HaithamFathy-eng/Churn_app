import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import joblib 

# Title

st.title(" Customer Churn Prediction ")

st.write("Enter customer details to predict if they will churn")

df = pd.read_excel(r"C:\Users\PC\OneDrive\Desktop\churn_dataset.xlsx")

model = joblib.load("Churn_Model.pkl")

target={1:"churn",0:"not churn"}


age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.slider("Tenure (Months)", min_value=0, max_value=100, value=12)

gender_encoded = 1 if gender == "Male" else 0

input_data = np.array([[age,gender_encoded,tenure]])

predicition = model.predict(input_data)[0]

predicition_prob = model.predict_proba(input_data)[0]



st.subheader("predection result")
st.write(f"Customer is {target[predicition]}")


st.subheader("predection probabilty result")
st.write(f"Probability of churn: {predicition_prob[1]:.2f}")
st.write(f"Probability of no churn: {predicition_prob[0]:.2f}")