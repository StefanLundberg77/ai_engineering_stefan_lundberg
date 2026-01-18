from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int 
    title: str 
    author: str 
    year: int = Field(gt = 1500, lt = 2026)
    #genre: list[str]
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 11,
                "title": "Learn with AIgineer",
                "author": "Kokchun Giang",
                "year": 2025,
            }
        }
    }
    
class Library(BaseModel):
    name: str 
    books: list[Book]
    #genre: list[str]
    
class Prompt(BaseModel):
    prompt: str