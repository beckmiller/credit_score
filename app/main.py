from fastapi import FastAPI
import pandas as pd
import pickle

from app.user import InputData

app = FastAPI()

model = pickle.load(
    open('app/models/model.pkl', 'rb')
)
model_columns = pickle.load(
    open('app/models/model_columns.pkl', 'rb')
)


@app.post("/predict")
def predict_class(query: InputData):
    query = query.dict()
    query = pd.DataFrame([query])
    query = pd.get_dummies(query)
    query = query.reindex(
        columns=model_columns,
        fill_value=0
    )
    prediction = model.predict(query)

    return f"Participant belongs to class {prediction}"
