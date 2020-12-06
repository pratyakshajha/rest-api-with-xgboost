# README.md

*This repo is a work in progress*


- The `train-model.ipynb` notebook trains a simple XGBoost model on [house prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) from kaggle. 
- The `flask_app.py` file creates a flask application which returns model's prediction. It is a `POST` at `\predict` endpoint. 
- There is a sample body of the request in `sample.json` file. 

## Setting up
- Clone this repo in your system.
- Model training can be skipped.
- Start the application by running `python flask_app.py`
- Hit the POST endpoint `http://127.0.0.1:5000/predict` with body from `sample.json` file. It should return `86808.45`.

## Dependent libraries
json, pandas, sklearn, xgboost, flask.