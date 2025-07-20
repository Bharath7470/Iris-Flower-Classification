import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("iris_model.pkl")

# App title
st.title("🌸 Iris Flower Classification")
st.write("Enter the flower measurements to predict the species:")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    
    species_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    st.success(f"🌼 Predicted Iris Species: **{species_map[prediction]}**")