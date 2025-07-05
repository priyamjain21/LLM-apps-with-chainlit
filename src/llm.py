from groq import Groq
from src.prompt import system_instruction

client = Groq()

messages = [
    {"role": "system", "content": system_instruction}
]

def ask_order(messages, model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )

    return response.choices[0].message.content
