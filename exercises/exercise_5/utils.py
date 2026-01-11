from pathlib import Path
import duckdb
from agents import restaurant_agent
from dotenv import load_dotenv
import os
from googlemaps import Client as GoogleMaps
import requests 
from urllib.parse import urljoin

load_dotenv()

# filepath
DATA_PATH = Path(__file__).parent / "data"

# if not path "data" exist then create one
DATA_PATH.mkdir(exist_ok=True)

gmaps = GoogleMaps(os.getenv("GOOGLE_PLACES_API_KEY"))

###########################
# send get request to the specified API endpoint
def read_api_endpoint(endpoint = "/", base_url = "http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint) # adds the str endpoint and a endpoint "/" if missing for proper url formatting
    response = requests.get(url) # returns a response object
    return response

# Send a post request with json payload to the specified api endpoint
def post_api_endpoint(payload, endpoint = "/", base_url = "http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint)
    response = requests.post(url=url, json=payload)

    return response
#####################

# function for executing a sql query to the database
def query_duckdb(sql_code, parameters = None):
    
    # connection to duckdb file
    with duckdb.connect(DATA_PATH / "restaurants.duckdb") as conn:
        
        # run sql code injection safe
        cursor = conn.execute(sql_code, parameters)
        
        # trim whitespaces and make lower case
        sql_code = sql_code.strip().casefold()
        
        # assuring code is read only
        if sql_code.startswith(("select", "from", "desc", "pragma")):
            
            # return sql data as dataframe
            return cursor.df()
        

async def google_places_search(location: str, cuisine: str):
    query = f"{cuisine} restaurant in {location}"
    result = gmaps.places(query=query)

    if not result.get("results"):
        return None

    return result["results"][0]  # best match

        
        
async def enrich_restaurant_with_ai(place, cuisine):
    prompt = f"""
    We found this real restaurant:

    Name: {place.get('name')}
    Address: {place.get('formatted_address')}
    Rating: {place.get('rating')}
    Price level: {place.get('price_level')}
    Cuisine: {cuisine}

    Write:
    - a short description
    - realistic opening hours
    - ensure price_level is cheap/medium/expensive (convert if needed)

    Return a complete Restaurant model.
    """

    enriched = await restaurant_agent.run(prompt)
    return enriched.output



async def extract_location_and_cuisine(prompt: str):
    extraction_prompt = f"""
    Extract ONLY:
    - location
    - cuisine

    From this user request: "{prompt}"

    Return as a Restaurant model but leave other fields empty.
    """
    result = await restaurant_agent.run(extraction_prompt)
    return result.output.location, result.output.cuisine


async def generate_restaurant(prompt: str):
    result = await restaurant_agent.run(prompt)
    return result.output


def save_restaurant(r):
    query_duckdb(
        "INSERT INTO restaurants VALUES (?,?,?,?,?,?,?)",
        parameters=[
            r.name,
            r.cuisine,
            r.price_level,
            r.rating,
            r.description,
            r.opening_hours,
            r.location,
        ],
    )