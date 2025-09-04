from base_agent import Agent
from aiogram import Bot, Dispatcher, types, Router, F
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
SYSTEMPROMPT = os.getenv("SYSTEMPROMPT")

class SummarizerAgent(Agent):
    """Агент, который делает резюме статей"""

    def __init__(self):
        self.router = Router()
        self.client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API"))
        self.model = "deepseek/deepseek-chat-v3.1:free"
        
    def run(self, articles):
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {"role": "system", "content": SYSTEMPROMPT},
                {"role": "user", "content": f"Данные из статей: {articles}"}
            ]
        )
        text = response.choices[0].message.content.strip()
        
        return text
