from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
def call_llm(prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    response = client.chat.completions.create(
        model    = "llama3-8b-8192",   # free & fast model
        messages = [
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content