from fastapi import FastAPI, Query
from data_processing import Iris

app = FastAPI()


@app.get("/iris")
def read_data(limit: int = Query(100, gt=0)):
    iris = Iris(limit)
    return iris.to_json()
    
@app.get("/iris/species")
def filter_species(species: str):
    iris = Iris()
    return iris.filter_species(species).to_json()

@app.get("/iris/kpis")
def kpis(species: str):
     """KPIs based on species"""
    iris = Iris()
    return iris.kpis(species)
     
# @router.get("/kpis")
# async def read_kpis_by_country(country: str):
#     """KPIs based on country"""
#     data_explorer = DataExplorer()
#     return data_explorer.kpis(country=country)
