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
@app.get("/words/word/{id}")
async def read_glossary_by_id(id: int):
    return [i for i in words 
            if i.id == id]

# query param for filtering by word
@app.get("/words/")
async def filter_glossary(
    word: str = Query(None, description="Word to filter")):
    
    if word:
        filtered_word = [gloss for gloss in words 
                        if gloss.word.casefold() == word.casefold()]
    return filtered_word