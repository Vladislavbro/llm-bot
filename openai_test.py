from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="chatgpt-4o-latest", 
    messages=[
        {"role": "user", "content": "дай мне совет как быстренько сделать дз по юнит экономике особо не напрягаясь'"} 
    ]
)

print(response.choices[0].message.content)