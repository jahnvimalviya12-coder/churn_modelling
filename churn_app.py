import streamlit as st
import numpy as np
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model("churn_class.h5")

st.title("Customer Churn Prediction")

# Input fields
CS = st.number_input("Credit Score")
Age = st.number_input("Age")
Tenure = st.number_input("Tenure")
Balance = st.number_input("Balance")
NumOfProducts = st.number_input("Number of Products")
EstimatedSalary = st.number_input("Estimated Salary")

Geography = st.selectbox(
    "Geography",
    ("France", "Germany", "Spain")
)

Gender = st.selectbox(
    "Gender",
    ("Male", "Female")
)

Has_credit_card = st.selectbox(
    "Has Credit Card",
    ("Yes", "No")
)

Is_active_member = st.selectbox(
    "Is Active Member",
    ("Yes", "No")
)


# Prediction button
if st.button("Predict"):

    # Convert categorical values to numbers
    gender = 1 if Gender == "Male" else 0

    has_card = 1 if Has_credit_card == "Yes" else 0

    active_member = 1 if Is_active_member == "Yes" else 0

    geography_germany = 1 if Geography == "Germany" else 0

    geography_spain = 1 if Geography == "Spain" else 0


    # Same order as training X.columns
    input_data = np.array([[
        CS,
        gender,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        has_card,
        active_member,
        EstimatedSalary,
        geography_germany,
        geography_spain
    ]])


    # Prediction
    prediction = model.predict(input_data)


    if prediction[0][0] > 0.5:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is likely to stay")
