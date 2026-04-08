from flask import Flask, request, jsonify
import joblib
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("churn_model.pkl")
columns = joblib.load("columns.pkl")

@app.route("/")
def home():
    return "Churn Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Convert input into dataframe
    input_df = pd.DataFrame([data])

    # Apply one-hot encoding
    input_df = pd.get_dummies(input_df)

    # Align with training columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    return jsonify({
        "prediction": int(prediction)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)