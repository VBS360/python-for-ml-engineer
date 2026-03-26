# 🧠 Machine Learning Interview Practice (Day 4)

## 🔹 Model Selection

### Q1: Why start with Logistic Regression?
**Answer:**
Logistic Regression is used as a baseline model because it is simple, fast, and interpretable. It helps establish a benchmark and works well when relationships are approximately linear.

---

### Q2: Why can Decision Tree perform better?
**Answer:**
Decision Trees capture non-linear relationships and feature interactions, making them more suitable for complex datasets.

---

### Q3: Why Random Forest over Decision Tree?
**Answer:**
Random Forest reduces overfitting by combining multiple decision trees trained on different subsets of data, improving generalization.

---

## 🔹 Model Comparison

### Q4: Logistic (82%) vs Random Forest (84%) — which to choose?
**Answer:**
The decision depends on whether the improvement is significant and consistent. If not, Logistic Regression may be preferred due to interpretability. Otherwise, Random Forest can be used for better performance.

---

### Q5: If both models give same accuracy?
**Answer:**
Prefer the simpler model (Logistic Regression) due to better interpretability and efficiency.

> Principle: Simpler model is preferred when performance is similar.

---

## 🔹 Overfitting & Generalization

### Q6: Decision Tree → 90% train, 70% test — what is happening?
**Answer:**
The model is overfitting. It memorizes training data but fails to generalize to unseen data.

---

### Q7: Why Random Forest performs better here?
**Answer:**
It reduces overfitting by averaging multiple trees, improving generalization.

---

### Q8: What concept is this?
**Answer:**
Overfitting, Generalization, and Bias-Variance Tradeoff.

---

## 🔹 Metrics

### Q9: Why different metrics for classification and regression?
**Answer:**
Classification predicts categories → use accuracy/F1.  
Regression predicts continuous values → use MAE, RMSE, R².

---

### Q10: What is F1 Score?
**Answer:**
F1 Score is the harmonic mean of Precision and Recall, used when data is imbalanced.

---

### Q11: What is MAE, MSE, RMSE?
**Answer:**
- MAE → average error  
- MSE → squared error (penalizes large errors)  
- RMSE → square root of MSE (same unit as target)

---

### Q12: What is R² Score?
**Answer:**
Measures how well the model explains variance in the data. Range: 0 to 1.

---

## 🔹 Data Concepts

### Q13: What is imbalanced dataset?
**Answer:**
A dataset where one class significantly outnumbers others, making accuracy misleading.

---

### Q14: How to handle imbalanced data?
**Answer:**
- Use F1 Score  
- Apply resampling techniques  
- Use class weights  

---

## 🔹 Cross Validation

### Q15: What is cross-validation?
**Answer:**
A technique where data is split multiple times to evaluate model performance more reliably.

---

## 🔹 Final Key Insight

> “A good model is not the one that performs best on training data, but the one that generalizes well to unseen data.”