from agents import AGENTS

def run_chat(theme: str, user_message: str):
    agent = AGENTS[theme]
    result = agent.run(user_message)
    return result.data
