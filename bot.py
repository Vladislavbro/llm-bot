import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from config import TELEGRAM_BOT_TOKEN
from openai_test import simple_openai_request

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /start."""
    await update.message.reply_text(
        "Привет! Я бот, который использует OpenAI и Google Gemini. "
        "Просто отправь мне сообщение, и я передам его в OpenAI."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /help."""
    await update.message.reply_text(
        "Я могу отправлять твои сообщения в OpenAI и возвращать ответы. "
        "Просто напиши что-нибудь и отправь мне."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает входящие сообщения и отправляет их в OpenAI."""
    user_message = update.message.text
    
    # Отправляем запрос в OpenAI
    await update.message.reply_text("Думаю...")
    response = simple_openai_request(user_message)
    
    # Отправляем ответ пользователю
    await update.message.reply_text(response)

def main() -> None:
    """Запускает бота."""
    # Проверяем наличие токена бота
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN не найден в .env файле")
        return
        
    # Создаем приложение и получаем диспетчер
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Регистрируем обработчик сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    logger.info("Бот запущен")
    application.run_polling()

if __name__ == "__main__":
    main() 