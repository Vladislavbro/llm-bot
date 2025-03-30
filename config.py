import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# API ключи
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 