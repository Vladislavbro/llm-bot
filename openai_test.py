import os
from openai import OpenAI
from config import OPENAI_API_KEY # Предполагаем, что config.py загружает ключ

try:
    # Инициализация клиента OpenAI с API ключом из config
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # Отправляем простой запрос к OpenAI (ChatGPT)
    print("Отправляем запрос к OpenAI...")
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            # Убираем system message для максимальной простоты
            {"role": "user", "content": "Скажи 'Привет!'"} 
        ]
    )
    
    # Выводим ответ
    print("\nОтвет от OpenAI:")
    print(response.choices[0].message.content)

except Exception as e:
    # Простая обработка ошибок
    print(f"\nПроизошла ошибка: {str(e)}")
    if "OPENAI_API_KEY" in str(e) or not OPENAI_API_KEY:
        print("Проверьте правильность API ключа в файле .env")