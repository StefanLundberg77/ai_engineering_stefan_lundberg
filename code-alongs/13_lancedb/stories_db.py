"""
Här är några sagor, urklippta från wikipedia manuellt

Ni ska lägga in dem i lancedb table med embeddings
Göra vektorsökning på olika queries

exempel: Vad heter de sju dvärgarna?

Plocka fram närmaste dokumentet och använd LLM för att generera en sammanfattning av dokumentet

"""
import os
from pathlib import Path
import pandas as pd
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from dotenv import load_dotenv
from pydantic_ai import Agent

load_dotenv()

db = lancedb.connect("vector_database")

embedding_model = (get_registry().get("gemini-text").create(name="gemini-embedding-001"))

class FairytaleModel(LanceModel):
    filename: str
    filepath: str
    content: str = embedding_model.SourceField()
    embedding: Vector(3072) = embedding_model.VectorField()

table = db.create_table("fairytales", schema=FairytaleModel, exist_ok=True)

data_dir = Path("data")
fairytale = []

for file in data_dir.glob("*.txt"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    fairytale.append({
        "filename": file.name,
        "filepath": str(file),
        "content": content
    })

df = pd.DataFrame(fairytale)

# insert into LanceDB
if len(df) > 0:
    table.add(df)
    print(f"Inserted {len(df)} stories into LanceDB")
else:
    print("No .txt files found in /data")


# llm agent
rag_agent = Agent(
    model="google-gla:gemini-2.5-flash",
    system_prompt=(
        "You are an expert summarizer of fairytales.",
        "Keep summaries short, clear and factual.",
        "Never hallucinate missing details.",
        "Always mention which file was used as the source."
    )#output_type=RagResponse
)


# query
def ask_question(query: str):
    print(f"\nQuery: {query}")

    # vector search
    results = table.search(query).limit(1).to_list()
    top = results[0]

    print(f"Closest match: {top['filename']}")

    # ask LLM to summarize
    summary = rag_agent.run_sync(
        f"Summarize this fairytale in 4 sentences:\n\n{top['content']}\n\n"
        f"Source file: {top['filename']}"
    )

    print("\nSummary:")
    print(summary.output)

# query 
ask_question("Vad heter de sju dvärgarna?")

