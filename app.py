import streamlit as st
import joblib
import pandas as pd

model = joblib.load("final_model.pkl")   # <-- full pipeline

st.title("Early Disease Risk Prediction Dashboard")

General_Health = st.selectbox("General Health",
    ["Excellent", "Very Good", "Good", "Fair", "Poor"])

Checkup = st.selectbox("Routine Checkup",
    ["Within past year", "1–2 years", "2–5 years", "5+ years"])

Exercise = st.selectbox("Exercise", ["Yes", "No"])
Skin_Cancer = st.selectbox("Skin Cancer", ["Yes", "No"])
Other_Cancer = st.selectbox("Other Cancer", ["Yes", "No"])
Depression = st.selectbox("Depression", ["Yes", "No"])
Diabetes = st.selectbox("Diabetes", ["Yes", "No"])
Arthritis = st.selectbox("Arthritis", ["Yes", "No"])
Sex = st.selectbox("Sex", ["Male", "Female"])

Age_Category = st.selectbox("Age Category",
    ["18-24","25-29","30-34","35-39","40-44",
     "45-49","50-54","55-59","60-64","65-69",
     "70-74","75-79","80+"] )

Height = st.number_input("Height (cm)", 120, 220, 165)
Weight = st.number_input("Weight (kg)", 30, 180, 70)
BMI = st.number_input("BMI", 10.0, 60.0, 25.0)

Smoking = st.selectbox("Smoking History", ["Yes", "No"])

Alcohol = st.slider("Alcohol Consumption (drinks/week)", 0, 30, 1)
Fruit = st.slider("Fruit Servings per Week", 0, 50, 5)
Vegetables = st.slider("Vegetable Servings per Week", 0, 50, 5)
FriedPotatoes = st.slider("Fried Potatoes per Week", 0, 20, 1)

df = pd.DataFrame({
    "General_Health": [General_Health],
    "Checkup": [Checkup],
    "Exercise": [Exercise],
    "Skin_Cancer": [Skin_Cancer],
    "Other_Cancer": [Other_Cancer],
    "Depression": [Depression],
    "Diabetes": [Diabetes],
    "Arthritis": [Arthritis],
    "Sex": [Sex],
    "Age_Category": [Age_Category],
    "Height_(cm)": [Height],
    "Weight_(kg)": [Weight],
    "BMI": [BMI],
    "Smoking_History": [Smoking],
    "Alcohol_Consumption": [Alcohol],
    "Fruit_Consumption": [Fruit],
    "Green_Vegetables_Consumption": [Vegetables],
    "FriedPotato_Consumption": [FriedPotatoes],
})

if st.button("Predict"):
    pred = model.predict(df)[0]   # <-- NO PREPROCESSOR

    if pred == 1:
        st.error("⚠️ High Disease Risk")
    else:
        st.success("✅ Low Disease Risk")
