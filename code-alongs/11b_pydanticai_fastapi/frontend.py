import streamlit as st
import requests
import pandas as pd
from utils import read_api_endpoint

st.markdown("# MovieDB")

user_prompt = st.text_input("# Search movie:")

if st.button("SEND") and user_prompt.strip() != "":
    response = requests.post("http://127.0.0.1:8000/create_movie", json={"prompt": user_prompt})
    
    data = response.json()
            
    st.markdown(f"## {data['title']}") 
    st.write(f"**Year of release:** {data['year']}") 
    st.write(f"**Genre:** {data['genre']}") 
    st.write(f"**Rating:** {data['rating']}") 

if st.button("List Movies"):
    response = read_api_endpoint("/movies")

    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        st.dataframe(df)
    else:
        st.error("Unable to Movies")