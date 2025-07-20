import streamlit as st
import pandas as pd
import joblib

# Load the trained model and feature names
model_bundle = joblib.load("loan_acceptance_model.pkl")
model = model_bundle['model']
feature_names = model_bundle['feature_names']

st.set_page_config(page_title="Loan Acceptance Prediction", layout="centered")

st.title("📘 Personal Loan Acceptance Prediction")
st.markdown("Enter customer details below to predict if they are likely to accept a loan offer.")

# Input fields
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", [
    'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
    'retired', 'self-employed', 'services', 'student', 'technician',
    'unemployed', 'unknown'
])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced', 'unknown'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has Credit in Default?", ['yes', 'no', 'unknown'])
housing = st.selectbox("Has Housing Loan?", ['yes', 'no', 'unknown'])
loan = st.selectbox("Has Personal Loan?", ['yes', 'no', 'unknown'])
contact = st.selectbox("Contact Method", ['cellular', 'telephone', 'unknown'])
month = st.selectbox("Last Contact Month", [
    'jan', 'feb', 'mar', 'apr', 'may', 'jun',
    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
])
day_of_week = st.selectbox("Day of Week", ['mon', 'tue', 'wed', 'thu', 'fri'])
campaign = st.slider("Number of Contacts During Campaign", 1, 50, 1)
previous = st.slider("Number of Previous Contacts", 0, 10, 0)
poutcome = st.selectbox("Previous Campaign Outcome", ['success', 'failure', 'nonexistent'])

# Collect input in a DataFrame
input_dict = {
    'age': age,
    'job': job,
    'marital': marital,
    'education': education,
    'default': default,
    'housing': housing,
    'loan': loan,
    'contact': contact,
    'month': month,
    'day_of_week': day_of_week,
    'campaign': campaign,
    'previous': previous,
    'poutcome': poutcome
}

input_df = pd.DataFrame([input_dict])

# One-hot encode input to match training
input_encoded = pd.get_dummies(input_df)

# Align with training features
input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

# Make prediction
if st.button("🔮 Predict Loan Acceptance"):
    prediction = model.predict(input_encoded)[0]
    result = "✅ Likely to Accept the Loan Offer" if prediction == 1 else "❌ Not Likely to Accept the Loan Offer"
    st.subheader("Prediction Result:")
    st.success(result)
