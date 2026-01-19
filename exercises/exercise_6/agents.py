from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

model = "google-gla:gemini-2.5-flash"

def chat_agent(system_prompt: str) -> Agent:
    return Agent(
        model=model,
        retries=2,
        system_prompt=system_prompt,
    )

StoryTeller = chat_agent(
    "You are an expert storyteller for children. "
    "Always answer with child-appropriate stories."
)

ProgrammingInstructor = chat_agent(
    "You are an expert programming instructor. "
    "Explain clearly, step by step, and avoid hallucinations."
)

SportsCommentator = chat_agent(
    "You are a sports commentator. "
    "Always answer with a cool, energetic sports-style comment."
)

NerdyJoker = chat_agent(
    "You are a nerdy joker. "
    "Always answer with a nerdy, programming or science-related joke."
)

AngryKaren = chat_agent(
    "You are an angry Karen. "
    "You complain a lot and overreact to small issues."
)

AGENTS = {
    "storyteller": StoryTeller,
    "instructor": ProgrammingInstructor,
    "sports": SportsCommentator,
    "joker": NerdyJoker,
    "karen": AngryKaren,
}
#%