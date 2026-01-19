from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()


class Chat_Bot:
    def __init__(self,
        system_prompt: str, 
        model: str = "google-gla:gemini-2.5-flash"): 
        
        self.chat_agent = Agent( 
            model=model, 
            system_prompt=system_prompt,
            retries=2, 
        ) 
        self.result = None

    def chat(self, prompt: str) -> dict:
        history = self.result.all_messages() if self.result else None 
        
        self.result = self.chat_agent.run_sync( prompt, message_history=history ) 
        
        return { "user": prompt, "bot": self.result.output }
    
    
# bot registry with different themes
class StoryBot(Chat_Bot):
    def __init__(self):
        super().__init__(
            "You are a friendly storyteller for children. Always answer with a safe, child-appropriate story."
        )
        
class InstructorBot(Chat_Bot):
    def __init__(self):
        super().__init__(
            "You are a programming instructor. Explain clearly, avoid hallucinations, and be helpful."
        )

class SportsBot(Chat_Bot):
    def __init__(self):
        super().__init__(
            "You are a sports commentator. Always answer with a cool sports comment."
        )
        
class JokeBot(Chat_Bot):
    def __init__(self):
        super().__init__(
            "Be a joking nerd. Always answer with a nerdy joke and use emojis."
        )

class KarenBot(Chat_Bot):
    def __init__(self):
        super().__init__(
            "You are an angry Karen. You complain loudly and overreact to small issues."
        )

BOTS = {
    "joker": JokeBot(),
    "storyteller": StoryBot(),
    "instructor": InstructorBot(),
    "sporty": SportsBot(),
    "karen": KarenBot(),
}

#%