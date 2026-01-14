from fastapi import FastAPI
from utils import query_duckdb, save_restaurant, google_places_search, extract_location_and_cuisine, enrich_restaurant_with_ai
from agents import restaurant_agent, restaurant_expert_agent
from data_models import Prompt


app = FastAPI()

# root page message
@app.get("/")
def root():
    return {"Restaurant API is runnin. http://127.0.0.1:8000/docs for swagger UI"}

@app.get("/restaurants")
async def read_restaurants():
    # fetch all restaurants from db
    restaurants = query_duckdb("FROM restaurants;")
    return restaurants.to_dict(orient="records")


@app.post("/search_restaurant")
async def search_restaurant(query: Prompt):

    # extract location + cuisine from natural language
    location, cuisine = await extract_location_and_cuisine(query.prompt)

    # 2. Check DuckDB first 
    db_matches = find_restaurants_in_db(location, cuisine)
    
    if not db_matches.empty: 
        return { "source": "database", "restaurants": db_matches.to_dict(orient="records") }

    # search web
    place = await google_places_search(location, cuisine)


    if place:
        # 3. Enrich missing fields using AI
        restaurant = await enrich_restaurant_with_ai(place, cuisine)
        save_restaurant(restaurant)

        return {
            "source": "google_places + ai enrichment",
            "restaurant": restaurant
        }

    # fallback: generate a fictional but realistic restaurant
    generated = await restaurant_agent.run(query.prompt)
    restaurant = generated.output
    save_restaurant(restaurant)

    return {
        "source": "ai-generated",
        "restaurant": restaurant
    }
  

@app.post("/create_restaurants")
async def create_restaurants(query: Prompt):
    # Run the agent to generate restaurants
    result = await restaurant_expert_agent.run(query.prompt)

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

def find_restaurants_in_db(location: str, cuisine: str):
    result = query_duckdb(
        "SELECT * FROM restaurants WHERE location ILIKE ? AND cuisine ILIKE ?",
        parameters=[f"%{location}%", f"%{cuisine}%"]
    )
    return result

