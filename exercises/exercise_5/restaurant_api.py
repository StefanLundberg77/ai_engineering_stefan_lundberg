from fastapi import FastAPI
from utils import query_duckdb
from agents import restaurant_agent
from data_models import Prompt

app = FastAPI()


@app.get("/restaurants")
async def read_restaurants():
    # fetch all restaurants from db
    restaurants = query_duckdb("FROM restaurants;")
    return restaurants.to_dict(orient="records")


@app.post("/create_restaurant")
async def create_restaurant(query: Prompt):
    # Run the agent to generate restaurants
    result = await restaurant_agent.run(query.prompt)

    # Loop through each generated restaurant and insert into DB
    for restaurant in result.output:
        query_duckdb(
            "INSERT INTO restaurants VALUES (?,?,?,?,?,?,?)",
            parameters=[restaurant.name, 
                        restaurant.cuisine,
                        restaurant.price_level,
                        restaurant.rating,
                        restaurant.description,
                        restaurant.opening_hours,
                        restaurant.location],
        )
    #return restaurants
    return {"inserted": len(result.output)}

    #result = await restaurant_agent.run(query.prompt)

