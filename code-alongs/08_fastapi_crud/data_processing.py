from constants import DATA_PATH
import json
from data_models import Book, Library
from book_agent import book_agent

def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data

def library_data(filename):
    """Deserializes library json data into a Library model"""
    json_data = read_json(filename)
    return Library.model_validate(json_data)

def write_json(filename: str, data: Library):
    with open(DATA_PATH/filename, "w") as file:
        json.dump(data.model_dump(), file, indent=3)

def save_library(books: list[Book]):
    data = Library(name="Coolu Libraru", books=books)
    write_json("library.json", data) 

async def create_book(prompt: str):
    result = await book_agent.run(prompt)
    return result.output


# if __name__ == '__main__':

#     data = library_data("library.json")

#     pprint(data)