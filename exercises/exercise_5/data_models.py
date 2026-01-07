from pydantic import BaseModel, Field
from typing import Literal
    
class Restaurant(BaseModel):
    name: str
    cuisine: str
    price_level: Literal["cheap", "medium", "expensive"]
    rating: int = Field(
        gt=0,
        lt=11,
        description="General rating of the restaurant between 1 and 10, the higher the better"
    )
    description: str
    opening_hours: str
    location: str
    
class Prompt(BaseModel):
    prompt: str