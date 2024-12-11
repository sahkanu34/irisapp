import streamlit as st
import numpy as np
import pickle
import pandas as pd


import os

file_path = 'C:/Iris app/iris_logistic_regression_model (2).pkl'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
else:
    print(f"File not found at {file_path}. Please check the path and try again.")

st.image("iris.jpg" ,width=300)

def main():
# Streamlit app

    st.header("Iris Flower Classification")

   
# Input features
sepal_length = st.text_input("Sepal Length", "5.1")
sepal_width = st.text_input("Sepal Width", "3.5")
petal_length = st.text_input("Petal Length", "1.4")
petal_width = st.text_input("Petal Width", "0.2")

# Convert inputs to numeric values
try:
    features = np.array([[float(sepal_length), float(sepal_width), float(petal_length), float(petal_width)]])
except ValueError:
    st.error("Please enter valid numeric values for all features.")
    features = None

# Prediction
if features is not None:
    if st.button("Predict"):
        prediction = model.predict(features)
        iris_type = ['Setosa', 'Versicolor', 'Virginica'][prediction[0]]
        st.write(f"The predicted Iris flower type is **{iris_type}**")

if __name__ =='__main__':
    main()