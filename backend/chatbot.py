from groq import Groq
from dotenv import load_dotenv
import os
from personalities import PERSONALITIES

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(personality_key, user_message):
    personality = PERSONALITIES.get(personality_key)
    if not personality:
        return "Invalid personality selected."

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": personality["prompt"]},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content
