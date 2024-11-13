import telebot
from telebot import types
bot = telebot.TeleBot(7725840888:AAHZgs-7A3kBL_60jfrX3bigu3AdfKpueIg)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(welcome)


    if __name__ == '__main__':
        bot.polling()