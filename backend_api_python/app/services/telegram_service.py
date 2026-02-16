import telebot


class TelegramService:

    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def send_message(self, chat_id: str, message: str):
        self.bot.send_message(chat_id, message)


if __name__ == '__main__':
    try:
        TelegramService("8017544088:AAG9WlkN9p4nXmqX-NL1BsC3J_scxm6udrg").send_message("6927283812","Test notification settings telegram")
    except Exception as e:
        print(e)