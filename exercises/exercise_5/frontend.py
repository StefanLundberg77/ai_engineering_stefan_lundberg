import streamlit as st
import pandas as pd
from utils import read_api_endpoint, post_api_endpoint

st.title("Restaurants")

prompt = st.text_input("What are you looking for?")

if st.button("Your search"): 
    if not prompt.strip(): 
        st.warning("Write something first.") 
    else: 
        with st.spinner("Searching for restaurant..."):
            response = post_api_endpoint(
            payload={"prompt": prompt},
            endpoint="/search_restaurant"
        )

             
        if response.status_code != 200:
            st.error(f"Error from API: {response.text}") 
        else: 
            data = response.json() 
            
            restaurant = data["restaurant"] 
            
            st.markdown(f"### {restaurant['name']}") 
            st.write(f"**Type of Food:** {restaurant['cuisine']}") 
            st.write(f"**Price Level:** {restaurant['price_level']}") 
            st.write(f"**Rating:** {restaurant['rating']}/10") 
            st.write(f"**Address:** {restaurant['location']}") 
            st.write(f"**Opening Hours:** {restaurant['opening_hours']}") 
            st.write(f"**Description:** {restaurant['description']}")

            st.write(f"Source: {data['source']}") 
            
if st.button("Load Restaurants"):
    response = read_api_endpoint("/restaurants")

    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        st.dataframe(df)
    else:
        st.error("Unable to load Restaurants")