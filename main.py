import telebot

API_KEY = '6653887160:AAEd36W_zuXktXWwBQqxGyRlBq792-9cr3o'


bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(commands=['weapon', 'оружие'])
def info_weapon(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, 'Укажите оружие')
    elif len(message.text.split()) == 2:
        weapon = message.text.split()[1]
        bot.send_message(message.chat.id, weapon)
    elif len(message.text.split()) >= 3:
        bot.send_message(message.chat.id, "Выберите только 1 оружие")


@bot.message_handler(commands=['викторина', 'quiz'])
def quiz(message):
    bot.send_message(message.chat.id, 'Quiz now is in development')
    # bot.send_poll(
    # message.chat.id, 'Какой калибр у АК-47?', ['5.56x45', '7.62x39', '7.62x54'], correct_option_id=1, open_period=30
    # )


bot.polling()
