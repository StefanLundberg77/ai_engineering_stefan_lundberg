#%%
from pathlib import Path
import duckdb
from urllib.parse import urljoin
import requests

DATA_PATH = Path(__file__).parent / "data"

DATA_PATH.mkdir(exist_ok=True)

# send get request to the specified API endpoint
def read_api_endpoint(endpoint = "/", base_url = "http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint) # adds the str endpoint and a endpoint "/" if missing for proper url formatting
    response = requests.get(url) # returns a response object
    return response

def query_duckdb(sql_code, parameters = None):
    with duckdb.connect(DATA_PATH / "movies.duckdb") as conn:

        cursor = conn.execute(sql_code, parameters)

        sql_code = sql_code.strip().casefold()
        if sql_code.startswith(("select", "from", "desc", "pragma")):
            return cursor.df()
    

#%%