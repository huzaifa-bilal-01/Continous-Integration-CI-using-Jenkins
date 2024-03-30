import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib
import pytest


@pytest.fixture
def trained_model():
    # Load the trained model from the file
    model = joblib.load("model.pkl")
    return model


def testdata():
    data = pd.read_csv("ice-cream-dataset.csv")
    X_test = data.iloc[:, :-1]
    y_test = data.iloc[:, -1]
    return X_test, y_test


def meansquarefunction(trained_model, X_test, y_test):
    model_file = trained_model
    model = joblib.load(model_file)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)
    return mse
