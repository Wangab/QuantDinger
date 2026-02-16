from typing import Optional

import telebot


class TelegramService:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def send_message(self, chat_id: str, message: str, parse_mode: Optional[str]=None):
        self.bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
