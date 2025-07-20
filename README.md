# 📘 DeveloperHub Task 5 – Personal Loan Acceptance Prediction using ML

## 📌 Task Objective  
This task focuses on building a classification-based machine learning model that predicts whether a customer is likely to accept a personal loan offer based on demographic and account-related features.

---

## 📁 Dataset  
**Name:** Bank Marketing Dataset  
**Source:** UCI Machine Learning Repository

---

## 📊 Features:

- Age  
- Job  
- Marital Status  
- Education  
- Default  
- Balance  
- Housing Loan  
- Personal Loan  
- Contact  
- Day  
- Month  
- Duration  
- Campaign  
- Pdays  
- Previous  
- Poutcome

---

## 🎯 Target:
- **Loan Acceptance** (Yes/No)

---

## 🛠️ Tools & Libraries Used

- **Pandas** – Data loading and preprocessing  
- **Matplotlib & Seaborn** – Data visualization and EDA  
- **Scikit-learn** – Model training and classification  
- **Joblib** – Saving and loading the trained model  
- **Streamlit** – Web app development and deployment  

---

## 🚀 Approach

### 1. Dataset Loading & Understanding  
- Loaded dataset using `pandas.read_csv()`  
- Reviewed structure with `.head()`, `.info()`, `.describe()`, and `.shape()`

### 2. Data Preprocessing  
- Handled categorical variables using one-hot encoding (e.g., job, marital, education)  
- Converted data into numeric format suitable for model input  
- No missing values required imputation

### 3. Exploratory Data Analysis (EDA)  
- Visualized distribution of loan acceptance based on age, balance, and job type  
- Analyzed feature relationships with heatmaps and count plots  
- Identified trends between customer demographics and loan acceptance

### 4. Model Training & Testing  
- Split the data into 80% training and 20% testing  
- Trained classification models including:
  - Logistic Regression  
  - Decision Tree Classifier  
- Selected the best-performing model and saved it using `joblib`

### 5. Evaluation Metrics  
- Accuracy Score  
- Confusion Matrix  
- Classification Report  

---

## 📊 Results & Insights

- **Decision Tree Classifier** gave the best performance for this classification task  
- Key factors influencing loan acceptance include:
  - Age  
  - Job type  
  - Balance  
  - Marital status  
- Customers aged under 35 are more likely to accept a loan offer

---

## ✅ Conclusion

This task completed the end-to-end machine learning pipeline:

- Data preprocessing  
- Exploratory Data Analysis  
- Model training and evaluation  
- Deployment via Streamlit  

The deployed app allows users to check loan acceptance predictions based on dynamic input.

---

## 🖥️ Streamlit Web App  
Try out the deployed model here:  
🔗 [Loan Acceptance Predictor App](https://loan-acceptance-prediction-pc9ecejr8je7huty9hbpnt.streamlit.app/)

---

## 🔗 Useful Links  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [Streamlit Docs](https://docs.streamlit.io/)  
- [Matplotlib Docs](https://matplotlib.org/stable/index.html)  
- [Seaborn Docs](https://seaborn.pydata.org/)

---

> 🔖 Submitted as part of the **DeveloperHub Internship Program**
