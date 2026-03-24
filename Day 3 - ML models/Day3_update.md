# 📅 Day 3: Loan Prediction Project (Classification)

## 🚀 Overview  
On Day 3, I built a **Loan Approval Prediction System**, applying an end-to-end machine learning workflow on a real-world financial dataset.

This project focuses on predicting whether a loan will be approved based on applicant details such as income, credit history, and demographics.

---

## 🎯 Objective  
To predict **Loan_Status (Approved / Not Approved)** using machine learning techniques.

---

## 📊 Dataset Features  

- **Demographics:** Gender, Married, Dependents  
- **Financial Info:** ApplicantIncome, CoapplicantIncome, LoanAmount  
- **Loan Details:** Loan_Amount_Term, Credit_History  
- **Property Info:** Property_Area  
- **Target:** Loan_Status  

---

## 🧠 Key Steps Performed  

### 1️⃣ Data Understanding  
- Explored dataset structure using `.info()` and `.describe()`  
- Checked class distribution of target variable  

---

### 2️⃣ Data Cleaning  
- Handled missing values:
  - Numerical → Median  
  - Categorical → Mode  
- Removed unnecessary column (`Loan_ID`)  

---

### 3️⃣ Feature Engineering  
- Created new feature:
  - **Total_Income = ApplicantIncome + CoapplicantIncome**  
- Converted categorical variables into numerical format  

---

### 4️⃣ Data Preprocessing  
- Applied encoding using `pd.get_dummies()`  
- Split dataset into training and testing sets  

---

### 5️⃣ Model Building  

- **Logistic Regression** (Baseline Model)  
- **Decision Tree Classifier** (Non-linear model)  

---

### 6️⃣ Model Evaluation  

- Accuracy Score  
- Confusion Matrix  

---

## 📈 Results  

- Logistic Regression Accuracy: ~XX%  
- Decision Tree Accuracy: ~XX%  

*(Update with your actual results)*

---

## 💡 Key Learnings  

- Importance of handling missing values correctly  
- Understanding when to use encoding techniques  
- Feature engineering improves model performance  
- Difference between linear and tree-based models  
- Importance of baseline models  

---

## 🧠 Interview Takeaways  

- Always start with a **baseline model (Logistic Regression)**  
- Use **tree-based models** for capturing complex patterns  
- Feature engineering should reflect **real-world logic**  

---

## 📌 Next Steps  

- Try Random Forest / XGBoost  
- Perform Hyperparameter Tuning  
- Deploy the model using Flask/Streamlit