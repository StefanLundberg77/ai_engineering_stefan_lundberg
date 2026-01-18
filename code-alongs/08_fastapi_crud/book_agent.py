from pydantic_ai import Agent
from dotenv import load_dotenv
from data_processing import Book

load_dotenv()


book_agent = Agent(    
    model="google-gla:gemini-2.5-flash",
    system_prompt="""
        You are an assistant that interprets natural language requests about books.
        The user will describe a book in free text.
        
        Your job is to:
        1. Suggest a book following the user description
        2. Suggest exactly ONE book

        Rules:
        - If a real book matches user description you MUST suggest a real one.
        - Only invent a fictional book if no real options exist.
        - You are allowed to make up a fictional book BUT keep it realistic.
        - append id based on the last book in library

        Follow the Book Pydantic model strictly.
        - id 
        - title
        - author 
        - year (1500 - 2026)
        - model_config 
        """,
    output_type=Book
)

 