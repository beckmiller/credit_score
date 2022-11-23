from fastapi import FastAPI
import pandas as pd
import pickle

from validation import InputData
from database.table import insertData
from database.table import create_table


app = FastAPI()


@app.post("/predict")
def predict_class(clientData: InputData):
    clientData = clientData.dict()
    clientDataFrame = pd.DataFrame([clientData])
    clientDataEncoded = pd.get_dummies(clientDataFrame)

    model_columns = pickle.load(
        open("app/models/model_columns.pkl", "rb")
    )
    clientDataEncoded = clientDataEncoded.reindex(
        columns=model_columns, 
        fill_value=0
    )

    model = pickle.load(
        open("app/models/model.pkl", "rb")
    )

    prediction = model.predict(clientDataEncoded)

    try:
        create_table()
        insertData(clientData, int(prediction[0]))
        if prediction[0] == 1:
            return f"Данный клиент откроет счет"
        else:
            return f"Данный клиент не откроет счет"
    except ValueError as err:
        print(err)
