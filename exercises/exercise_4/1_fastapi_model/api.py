from fastapi import FastAPI, Query
from data_processing import MYH


app = FastAPI()

@app.get("/myh/")
def read_myh_data(limit: int = Query(100, gt=0)): #, school: str = Query(None)):
    myh = MYH(limit)
    return myh.to_json()
    
    # TODO: filter out the school
    # you probably need to add a method in MYH class in data_processing as well

@app.get("/myh/school/")
def filter_school(school: str):
    myh = MYH()
    return myh.filter_school(school).to_json()