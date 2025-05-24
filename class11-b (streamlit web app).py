import streamlit as st
import numpy as np
import pickle
st.title("Iris Prediction App")

st.write("Please enter the data of flowers and I will predict the specie for you...")
sepal_l=st.number_input("Enter sepal length: ", min_value=0.0)
petal_l=st.number_input("Enter petal length: ", min_value=0.0)
sepal_w=st.number_input("Enter sepal width: ", min_value=0.0)
petal_w=st.number_input("Enter petal width: ", min_value=0.0)

user_data=np.array([[sepal_l,sepal_w,petal_l,petal_w]])

#opening the model with the help of pickle
with open("best_model.pkl", "rb") as file:
    model=pickle.load(file)

if st.button("Predict"): #is condition is true only when button is pressed
    pred=model.predict(user_data)
    st.write("the predicted specie is: ", pred[0])
    