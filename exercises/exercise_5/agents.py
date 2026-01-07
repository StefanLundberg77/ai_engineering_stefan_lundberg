from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import Restaurant

load_dotenv()

restaurant_agent = Agent(    
    model="google-gla:gemini-2.5-flash",
    system_prompt="""You are an expert restaurant guide. 
        Given a location from user, you must suggest 5 restaurants that are located near that location, 
        if no real restaurants exist in the area you are allowed to make up fictional but realistic restaurants. 
        Each restaurant must strictly follow the structure defined in the Restaurant Pydantic model:
        - name
        - cuisine (type of food)
        - price_level (cheap, medium, expensive)
        - rating (1–10)
        - description (short and informative)
        - opening_hours (structured according to the OpeningHours model)
        - location (short description of where the restaurant is located)

        Keep descriptions concise, realistic, and helpful.
        """,
    output_type=Restaurant,
)
