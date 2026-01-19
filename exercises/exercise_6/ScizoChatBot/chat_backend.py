from agents import BOTS
import random

def run_chat(theme: str, message: str) -> dict:
    if theme == "random": 
        theme = random.choice(list(BOTS.keys()))
    bot = BOTS[theme]
    result = bot.chat(message)
    
    result["bot_type"] = theme 
    return result

