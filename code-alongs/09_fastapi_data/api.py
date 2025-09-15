from fastapi import FastAPI, Query
from data_processing import DataExplorer

# from constants import DATA_PATH
app = FastAPI()

data_explorer = DataExplorer

@app.get("/api/sales")
async def read_sales():
    # implement this code to return json data in this endpoint
    #data = DataExplorer()
    return data_explorer.json_response()

@app.get("/api/summary")
async def read_summary_data():
    """shows summary statistics"""
   # data = DataExplorer(app._df)
    return data_explorer.summary().json_response()
  

