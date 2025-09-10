from fastapi import FastAPI
from data_processing import library_data, Book, save_library

app = FastAPI()

library = library_data("library.json")
books = library.books

@app.get("/books")
async def read_books():
    return books

# path parameter
@app.get("/books/title/{title}")
async def read_book_by_title(title:str):
    return[book for book in books if book.title.casefold() == title.casefold()]

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

@app.delete("/books/delete_book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
        break

@app.get("/books/genres/{genre}")
async def read_books_by_genre(genre: str):
    return [book for book in books if genre in book.genres]

# TODO:

# query parameters

