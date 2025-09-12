from fastapi import FastAPI, Query, HTTPException
from data_processing import BaseModel, glossary_data, Gloss, save_glossary
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

@app.post("/words/create_glossary")
async def create_glossary(glossary_request: Gloss):
    # auto max id +1
    max_id = max((w.id for w in words if w.id is not None), default=0)
    glossary_request.id = max_id + 1
    words.append(glossary_request)
    save_glossary(words)
    return glossary_request

@app.delete("/words/delete_glossary/{id}")
async def delete_glossary(id: int):
    global words
    original_len = len(words)
    words = [w for w in words if w.id != id]
    save_glossary(words)
    return {"message": f"Word with id {id} deleted"}

@app.put("/words/update_glossary")
async def update_glossary(updated_word: Gloss):
    index = next((i for i, w in enumerate(words) if w.id == updated_word.id), None)
    if index is None:
        raise HTTPException(status_code=404, detail=f"No word found with id {updated_word.id}")
    words[index] = updated_word
    save_glossary(words)
    return {
        "message": f"Word with id {updated_word.id} updated",
        "word": updated_word
    }


"""
for i, word in enumerate(words):
        if word.id == id:
            del words[i]
        # Om vi kommer hit hittades inget
    return {"error": f"No word found with id {id}"}
    
@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)
    save_library(books)    
    return new_book

@app.put("/books/updated_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] = updated_book
    return updated_book

"""