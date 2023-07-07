from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Read the uploaded CSV file
        df = pd.read_csv(file.file)

        # Perform some operations on the DataFrame
        # For example, let's calculate the mean of a column
        # mean = df['Duration'].mean()

        # return {"mean": mean}
        return df.to_json(orient="records")
    except Exception as e:
        return {"error": str(e)}
