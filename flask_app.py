import json
import pandas as pd
from xgboost import XGBRegressor
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    print(pd.read_json(request.data).head())
    df = pd.read_json(request.data)
    return jsonify(predict_xgb(df))

def predict_xgb(df: pd.DataFrame) -> float:
    loaded_model = XGBRegressor()
    loaded_model.load_model('model-housing-prices')
    return float(loaded_model.predict(df)[0])

if __name__ == "__main__":
    app.run(debug=True)