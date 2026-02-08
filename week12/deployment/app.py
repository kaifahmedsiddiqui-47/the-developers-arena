from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("src/models/xgb_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Example: data = {"Tenure": 12, "MonthlyCharges": 70, "Contract_Month-to-month": 1, ...}
    features = np.array([list(data.values())]).astype(float)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    return jsonify({
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)