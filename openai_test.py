import openai
from config import OPENAI_API_KEY

# Инициализация клиента OpenAI с API ключом
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def simple_openai_request(prompt):
    """
    Отправляет простой запрос к API OpenAI
    
    Args:
        prompt (str): Текст запроса для модели
        
    Returns:
        str: Ответ от модели
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Вы полезный ассистент."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"

if __name__ == "__main__":
    # Проверяем, что API ключ установлен
    if not OPENAI_API_KEY:
        print("Ошибка: API ключ OpenAI не найден. Проверьте файл .env")
    else:
        # Тестовый запрос
        user_prompt = "Расскажи мне о Telegram ботах"
        print("Отправляем запрос к OpenAI...")
        response = simple_openai_request(user_prompt)
        print("\nОтвет от OpenAI:")
        print(response) 