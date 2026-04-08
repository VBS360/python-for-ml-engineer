import requests

url = "http://127.0.0.1:5000/predict"

data = {
  "SeniorCitizen": 0,
  "tenure": 12,
  "MonthlyCharges": 70.5,
  "TotalCharges": 850.0,
  "gender_Male": 1,
  "Partner_Yes": 1,
  "Dependents_Yes": 0,
  "PhoneService_Yes": 1,
  "MultipleLines_No phone service": 0,
  "MultipleLines_Yes": 1,
  "InternetService_Fiber optic": 1,
  "InternetService_No": 0,
  "OnlineSecurity_No internet service": 0,
  "OnlineSecurity_Yes": 1,
  "OnlineBackup_No internet service": 0,
  "OnlineBackup_Yes": 1,
  "DeviceProtection_No internet service": 0,
  "DeviceProtection_Yes": 1,
  "TechSupport_No internet service": 0,
  "TechSupport_Yes": 1,
  "StreamingTV_No internet service": 0,
  "StreamingTV_Yes": 1,
  "StreamingMovies_No internet service": 0,
  "StreamingMovies_Yes": 1,
  "Contract_One year": 0,
  "Contract_Two year": 1,
  "PaperlessBilling_Yes": 1,
  "PaymentMethod_Credit card (automatic)": 1,
  "PaymentMethod_Electronic check": 0,
  "PaymentMethod_Mailed check": 0
}

response = requests.post(url, json=data)

print(response.json())