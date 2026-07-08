import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import streamlit as st
st.title("Customer Churn Prediction")
CS= st.number_input("Credit Score")
Age= st.number_input("Age")
Tenure= st.number_input("Tenure")
Balance= st.number_input("Balance")
NumOfProducts= st.number_input("Number of Products")
Geography= st.selectbox("Geography",("France","Germany","Spain"))
Gender= st.selectbox("Gender",("Male","Female"))
Has_credit_card= st.selectbox("Has Credit Card",("Yes","No"))
Is_active_member= st.selectbox("Is Active Member",("Yes","No"))
