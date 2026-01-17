"""
Här är några sagor, urklippta från wikipedia manuellt

Ni ska lägga in dem i lancedb table med embeddings
Göra vektorsökning på olika queries

exempel: Vad heter de sju dvärgarna?

Plocka fram närmaste dokumentet och använd LLM för att generera en sammanfattning av dokumentet

"""
import lancedb
from pathlib import Path
from lancedb.pydantic import Vector, LanceModel
from lancedb.embeddings import get_registry
import numpy as np 

import time
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

db = lancedb.connect(uri="vector_database")

model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

embeddings = model.generate_embeddings("Why are SQL good at relationships? Because they are relational")

class FairytaleModel(LanceModel):
    filename: str
    filepath: str
    content: str = model.SourceField()
    embedding: Vector(3072) = model.VectorField()

db.create_table("fairytales", schema=FairytaleModel, exist_ok=True) 


df_fairytale = pd.DataFrame([str], columns=['stories'])

with open("data/askungen.txt", "r") as file:
    stories_data = file.read() # ?

path = Path(path).mkdir(exist_ok=True)


 


# läs in stories som typ list. embedda. etc