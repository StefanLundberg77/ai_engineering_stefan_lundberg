import json
from constants import DATA_PATH
from pydantic import BaseModel, Field, field_validator
from pprint import pprint

# file read method
def read_json(filename):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data


class Glossary(BaseModel):
    id: int
    word: str
    meaning: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 2,
                "word": "coupon",
                "meaning": "a discount coupon used for shopping",   
            }
        }
    }
    
# class Glossary(BaseModel):
#     glossaries: list[Gloss]

def glossary_data(filename):
    """Deserializes glossary json data into a glossary model"""
    json_data = read_json(filename)
    return [Glossary.model_validate(item) for item in json_data]

# def write_json(filename: str, data: Library):
#     with open(DATA_PATH/filename, "w") as file:
#         json.dump(data.model_dump(), file, indent=3)

# def save_library(books: list[Book]):
#     data = Library(name="Coolu Libraru", books=books)
#     write_json("library.json", data) 

if __name__ == '__main__':

    data = glossary_data("fastapi_glossary.json")

    pprint(data)    