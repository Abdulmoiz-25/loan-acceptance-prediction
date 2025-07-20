# app.py

import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("loan_acceptance_model.pkl")

st.set_page_config(page_title="Loan Acceptance Prediction", layout="centered")
st.title("💳 Personal Loan Acceptance Prediction")

st.write("Enter customer details below to predict loan acceptance:")

# Define form inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
                           'retired', 'self-employed', 'services', 'student', 'technician',
                           'unemployed'])
marital = st.selectbox("Marital Status", ['divorced', 'married', 'single'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has Credit in Default?", ['no', 'yes'])
housing = st.selectbox("Has Housing Loan?", ['no', 'yes'])
loan = st.selectbox("Has Personal Loan?", ['no', 'yes'])
contact = st.selectbox("Contact Method", ['cellular', 'telephone'])
month = st.selectbox("Last Contact Month", ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'])
day_of_week = st.selectbox("Day of Week", ['mon','tue','wed','thu','fri'])
campaign = st.slider("Number of Contacts During Campaign", 1, 50, 1)
previous = st.slider("Number of Previous Contacts", 0, 10, 0)
poutcome = st.selectbox("Previous Campaign Outcome", ['failure', 'nonexistent', 'success'])

# Preprocess input
def preprocess_input():
    # Create DataFrame with one row
    data = {
        'age': age,
        'campaign': campaign,
        'previous': previous,
        # Encode categorical vars
        f'job_{job}': 1,
        f'marital_{marital}': 1,
        f'education_{education}': 1,
        f'default_{default}': 1,
        f'housing_{housing}': 1,
        f'loan_{loan}': 1,
        f'contact_{contact}': 1,
        f'month_{month}': 1,
        f'day_of_week_{day_of_week}': 1,
        f'poutcome_{poutcome}': 1
    }

    # All possible encoded columns (same as training)
    columns = model.feature_names_in_
    row = {col: 0 for col in columns}
    row.update(data)

    return pd.DataFrame([row])

# Predict
if st.button("Predict"):
    input_df = preprocess_input()
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ The customer is likely to accept the loan offer.")
    else:
        st.warning("❌ The customer is unlikely to accept the loan offer.")
