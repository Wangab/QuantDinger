import telebot


class TelegramService:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def send_message(self, chat_id: str, message: str):
        self.bot.send_message(chat_id, message)
