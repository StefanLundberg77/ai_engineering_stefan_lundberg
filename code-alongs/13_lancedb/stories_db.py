from lancedb.pydantic import Vector
from lancedb.embeddings import get_registry

model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

model

embeddings = model.generate_embeddings("Why are SQL good at relationships? Because they are relational")

import numpy as np 
np.array(embeddings).shape

from lancedb.pydantic import LanceModel


class StoryModel(LanceModel):
    story: str = model.SourceField() # input to embedding function
    embedding: Vector(3072) = model.VectorField() # computed embedding in this column

db.create_table("stories", schema=StoryModel, exist_ok=True) 

import pandas as pd

df_stories = pd.DataFrame([str], columns=['stories'])

with open("data/askungen.txt", "r") as file:
    stories_data = file.read() # ?
    
df_stories.head()

# läs in stories som typ list. embedda. etc