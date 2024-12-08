import streamlit as st
import numpy as np
import pickle
import pandas as pd


# Load the saved model
with open('C:/Iris app/iris_logistic_regression_model (2).pkl', 'rb') as file:
    model = pickle.load(file)

    # Loadinf the datasets
    # df=pd.read_csv("C:\Iris app\Iris.csv")
    # df.sample(5)
    # st.write(df.sample(5))

def main():
# Streamlit app

    st.title("Iris Flower Classification")

   
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