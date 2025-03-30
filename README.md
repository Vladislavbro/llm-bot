# Telegram AI Bot

Проект Telegram бота, использующего API OpenAI и Google Gemini для различных задач.

## Описание
Этот бот предоставляет интерфейс в Telegram для взаимодействия с моделями искусственного интеллекта OpenAI (GPT) и Google Gemini.

## Установка

1. Клонировать репозиторий
2. Установить зависимости:
```
pip install -r requirements.txt
```
3. Создать файл `.env` с необходимыми API ключами:
```
OPENAI_API_KEY=ваш_ключ_openai
TELEGRAM_BOT_TOKEN=ваш_токен_телеграм_бота
GEMINI_API_KEY=ваш_ключ_gemini
```

## Использование
Запустить бота:
```
python bot.py
```

## Функции
- Отправка запросов к OpenAI API
- Отправка запросов к Google Gemini API 