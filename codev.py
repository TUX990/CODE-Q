import telebot
from telebot import types

bot = telebot.TeleBot('7725840888:AAHZgs-7A3kBL_60jfrX3bigu3AdfKpueIg')

bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Are you ready to know how Bitcoin start?")

    if __name__ == '__main__':
        bot.polling()
