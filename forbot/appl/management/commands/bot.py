from django.conf import settings
from django.core.management.base import BaseCommand

from dotenv import load_dotenv
import os
from telebot import TeleBot

load_dotenv()

telegram_bot_api_key = os.getenv('TELEGRAM_BOT_API_KEY')

# Объявление переменной бота
bot = TeleBot(telegram_bot_api_key, threaded=False)


# Название класса обязательно - "Command"
class Command(BaseCommand):
    # Используется как описание команды обычно
    help = 'A command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        # bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        # bot.load_next_step_handlers()				# Загрузка обработчиков

        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, "Привет")

        bot.infinity_polling()
