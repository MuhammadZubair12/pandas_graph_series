from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# @app.get("/pandas-operation")
# def perform_pandas_operation():
#     # Your pandas operations here
#     data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
#     df = pd.DataFrame(data)
#     return df.to_dict()
@app.get("/csv")
def read_csv():
    # Read the CSV file using pandas
    df = pd.read_csv("data.csv")
    # dat = df.columns.tolist()
    # Return the dataframe as JSON
    all = df.to_json(orient="records")
    return all

