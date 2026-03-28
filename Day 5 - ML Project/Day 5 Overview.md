# 🏠 Day 5 - House Price Prediction (Regression Project)

## 📌 Overview

On Day 5, I built my first end-to-end Machine Learning regression model to predict house prices. This project includes data preprocessing, feature engineering, model training, and evaluation.

---

## 🚀 Workflow

### 1. Data Loading

* Loaded dataset using pandas
* Inspected structure using `.head()` and `.info()`

---

### 2. Exploratory Data Analysis (EDA)

* Checked distribution of target variable (`SalePrice`)
* Identified skewness in data
* Visualized:

  * Histogram (distribution)
  * Boxplot (outliers)
  * Scatter plots (feature relationships)

---

### 3. Data Transformation

* Applied **log transformation** on `SalePrice` to reduce skewness

---

### 4. Missing Value Handling

#### Categorical Features:

* Filled missing values with `'None'`
* Reason: absence of feature (e.g., no pool, no alley)

#### Numerical Features:

* Used **median** for robust imputation
* Used `0` where absence made logical sense (e.g., Garage year)

---

### 5. Feature Engineering

Created new meaningful features:

* `TotalSF` = Total square footage of house
* `HouseAge` = Age of property
* `TotalBath` = Combined bathrooms

---

### 6. Encoding

* Applied **One-Hot Encoding** using `pd.get_dummies()`
* Used `drop_first=True` to avoid multicollinearity

---

### 7. Train-Test Split

* Split data into:

  * 80% training
  * 20% testing

---

### 8. Model Training

Used:

* Linear Regression

Workflow:

* Created model
* Trained using `.fit()`
* Predicted using `.predict()`

---

### 9. Model Evaluation

Used metrics:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

---

## 📊 Key Learnings

* Log transformation improves model performance
* Feature engineering significantly boosts predictive power
* Data cleaning is the most important step in ML
* Visualization helps understand relationships clearly

---

## ⚠️ Challenges Faced

* Handling missing values properly
* Understanding when to use which visualization
* Writing model code from scratch

---

## 💡 Future Improvements

* Try advanced models (Random Forest, XGBoost)
* Perform cross-validation
* Hyperparameter tuning
* Feature importance analysis

---

## 🎯 Conclusion

This project helped me understand the complete ML pipeline and gave me confidence in building regression models from scratch.

---
