import streamlit as st
import pandas as pd
from pathlib import Path
from utils import DATA_PATH
from restaurant_api import read_restaurants, search_restaurant


# filepath
path = DATA_PATH

# api
data = read_restaurants() # göra om till dataframe

df = ""


def layout():
    

    # run layout when script executed
    if __name__ == '__main__':
        layout()