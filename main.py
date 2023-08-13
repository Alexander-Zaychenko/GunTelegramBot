import telebot

API_KEY = 'Это секретное значение'


bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет!")


bot.polling()
