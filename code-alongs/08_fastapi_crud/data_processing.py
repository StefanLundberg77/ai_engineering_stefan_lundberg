from constants import DATA_PATH
import json
from models import Book, Library
import duckdb

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

# async def create_book(prompt: str):
#     result = await book_agent.run(prompt)
#     return result.output

# function for executing a sql query to the database
def query_duckdb(sql_code, parameters = None):
    
    # connection to duckdb file
    with duckdb.connect(DATA_PATH / "restaurants.duckdb") as conn:
        
        # run sql code injection safe
        cursor = conn.execute(sql_code, parameters)
        
        # trim whitespaces and make lower case
        sql_code = sql_code.strip().casefold()
        
        # assuring code is read only
        if sql_code.startswith(("select", "from", "desc", "pragma")):
            
            # return sql data as dataframe
            return cursor.df()

# if __name__ == '__main__':

#     data = library_data("library.json")

#     pprint(data)