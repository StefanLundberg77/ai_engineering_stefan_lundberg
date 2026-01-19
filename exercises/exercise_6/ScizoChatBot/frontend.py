import streamlit as st
from chat_backend import run_chat

st.title("SchizoChatBot")

if "random_theme" not in st.session_state: 
    st.session_state.random_theme = None

if "awaiting_guess" not in st.session_state:
    st.session_state.awaiting_guess = False
    
mode = st.selectbox(
    "Play SchitzoRoulette or just chat with your persona of choice",
    ["SchitzoRoulette", "Chat"])

if mode == "Chat":
    theme = st.selectbox(
    "Choose personality",
    ["joker", "storyteller", "code instructor", "sporty guy", "karen"]
)
    
else: 
    theme = "random"
    
user_message = st.text_input("message")

if st.button("Send") and user_message != "":
    response = run_chat(theme, user_message)
    
    st.write(f"you: {response['user']}")
    
    if theme == "random":
        st.session_state.random_theme = response["bot_type"] 
        st.session_state.awaiting_guess = True
        st.write(f"?: {response['bot']}") 
        
    else: 
        st.write(f"{theme}: {response['bot']}") 
        st.session_state.random_theme = None
    
if mode == "SchitzoRoulette" and st.session_state.awaiting_guess:
    guess = st.selectbox(
        "Guess who?",
        ["joker", "storyteller", "code instructor", "sporty guy", "karen"]
    )

    if st.button("Guess"):
        if guess == st.session_state.random_theme:
            st.success("Yeeeey you won!")
            
        else:
            st.error(f"Wrong! It was actually the... {st.session_state.random_theme}")
            
        st.session_state.awaiting_guess = False
