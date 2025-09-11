from fastapi import FastAPI, Query
from data_processing import BaseModel, glossary_data, Gloss
from pprint import pprint

app = FastAPI()

glossary = glossary_data("fastapi_glossary.json")
words = glossary.words
#pprint(glossary)

@app.get("/words")
async def read_glossary():
    return words

# path parameter
@app.get("/words/id/{id}")
async def read_glossary_by_id(id: int):
    return [i for i in words 
            if i.id == id]

# query param for filtering by word
@app.get("/words/")
async def filter_glossary(
    word: str = Query(None, description="Word to filter")):
    filter_word = [w for w in words if w.word.casefold() == word.casefold()]
    if filter_word: 
        return filter_word

