import joblib
import numpy as np


def predict_price(Open, High, Low, Volume):
    test_data = np.array([[Open, High, Low, Volume]])
    trained_model = joblib.load("linear_model.pkl")
    predictions = trained_model.predict(test_data)

    return predictions
