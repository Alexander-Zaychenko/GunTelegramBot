import telebot

API_KEY = '6653887160:AAEd36W_zuXktXWwBQqxGyRlBq792-9cr3o'


bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет!")


bot.polling()
