from pydantic_ai import Agent
from dotenv import load_dotenv
from data_models import Restaurant

load_dotenv()

# assistant for natural language that will web search if no hits in db
restaurant_agent = Agent(    
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt="""
        You are an assistant that interprets natural language requests about restaurants.
        The user will describe a location and optionally a type of food in free text.
        Your job is to extract:
        1. Extract the location and cuisine.
        2. Suggest exactly ONE restaurant

        Rules:
        - If real restaurants exist in that location matching the cuisine, you MUST choose a real one.
        - Only invent a fictional restaurant if no real options exist.
        - Never claim uncertainty; choose the best match.

        Follow the Restaurant Pydantic model strictly.
        - name
        - cuisine (type of food)
        - price_level (cheap, medium, expensive)
        - rating (1-10)
        - description (short and informative)
        - opening_hours (structured according to the OpeningHours model)
        - location (street address and city of the restaurant)
        """,
    output_type=Restaurant
)    
    
    
restaurant_expert_agent = Agent(    
    model="google-gla:gemini-2.5-flash",
    retries=2,
    system_prompt="""You are an expert restaurant guide. 
        Given a location from user, you must suggest 5 restaurants that are located near the user location, 
        if no real restaurants exist in the area you are allowed to make up fictional but realistic restaurants. 
        Each restaurant must strictly follow the structure defined in the Restaurant Pydantic model:
        - name
        - cuisine (type of food)
        - price_level (cheap, medium, expensive)
        - rating (1-10)
        - description (short and informative)
        - opening_hours (structured according to the OpeningHours model)
        - location (street address and city of the restaurant)

        Keep descriptions concise, realistic, and helpful.
        """,
    output_type=list[Restaurant],
)
