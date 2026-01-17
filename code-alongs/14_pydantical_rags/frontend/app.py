import streamlit as st
import requests
from pathlib import Path

ASSETS_PATH = Path(__file__).absolute().parents[1] / "assets"

st.markdown("# RAGBIT")
st.markdown("# Ask something about rabbits:")

user_prompt = st.text_input("Question")

if st.button("SEND") and user_prompt.strip() != "":
    response = requests.post("http://127.0.0.1:8000/rag/query", json={"prompt": user_prompt})
    
    data = response.json()
    
    st.markdown("## Question:")
    st.markdown(user_prompt)
    
    st.markdown("## Answer:")
    st.markdown(data["answer"])
    
    st.markdown("## Source:")
    st.markdown(data["filepath"])
    
    st.image(ASSETS_PATH / f"{data['filename']}.png")
    
