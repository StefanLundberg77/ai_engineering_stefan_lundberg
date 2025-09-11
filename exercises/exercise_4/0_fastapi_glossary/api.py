from fastapi import FastAPI, Query
from data_processing import BaseModel, glossary_data
from pprint import pprint

app = FastAPI()

glossary = glossary_data("fastapi_glossary.json")
# glossaries = glossary.glossaries
pprint(glossary)

@app.get("/glossary")
async def read_glossary():
    return glossary

# path parameter
@app.get("/glossary/word/{word}")
async def read_glossary_by_word(word:str):
    return [gloss for gloss in glossary if glossary.word.casefold() == word.casefold()]

# query param for word
@app.