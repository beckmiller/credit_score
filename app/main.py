from fastapi import FastAPI
from app.user import InputData
import pickle
import pandas as pd

app = FastAPI()

with open("app/model.pkl", "rb") as pickle_in:
    model = pickle.load(pickle_in)


@app.post("/predict")
def predict_class(data: InputData):
    data = data.dict()
    test_data = pd.DataFrame([data])
    predicted_class = model.predict(test_data)
    return f"Participant belongs to class {'predicted'}"