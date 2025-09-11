from fastapi import FastAPI, Query
from data_processing import BaseModel, glossary_data
from pprint import pprint

app = FastAPI()

glossary = glossary_data("fastapi_glossary.json")
# glossaries = glossary.glossaries
pprint(glossary)

# @app.get("/glossary_list")
# async def read_glossaries():
#     return glossaries