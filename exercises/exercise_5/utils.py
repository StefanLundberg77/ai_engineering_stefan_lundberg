from pathlib import Path
import duckdb

# filepath
DATA_PATH = Path(__file__).parent / "data"

# if not path "data" exist then create one
DATA_PATH.mkdir(exist_ok=True)

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