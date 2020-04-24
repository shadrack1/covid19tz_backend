import os
import pandas as pd
from fastapi import FastAPI


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

dataset = os.path.join(DATA_DIR, 'Compiled_data.csv')
app = FastAPI()

@app.get('/')
def hello():
    return {"message": "Hello Shadrack"}

@app.get("/get_data")
def read_data():
    df = pd.read_csv(dataset)
    return df.to_dict("Region")