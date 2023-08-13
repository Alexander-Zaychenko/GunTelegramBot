import telebot
import sqlite3

API_KEY = '6653887160:AAEd36W_zuXktXWwBQqxGyRlBq792-9cr3o'


bot = telebot.TeleBot(API_KEY)


# def sql_connection():
#     try:
#         connection = sqlite3.connect('database.db')
#         return connection
#     except sqlite3.Error:
#         print(sqlite3.Error)
#
#
# def sql_table(connection):
#     cursor = connection.cursor()
#     cursor.execute(CREATE TABLE "guns" ( "id" INTEGER, "gun" TEXT, "info" TEXT ))
#     connection.commit()


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет!")
    print(f'Start command used by {message.chat.username}')


@bot.message_handler(commands=['weapon', 'оружие'])
def info_weapon(message):
    if len(message.text.split()) == 1:
        bot.send_message(message.chat.id, 'Укажите оружие')
    elif len(message.text.split()) == 2:
        weapon = message.text.split()[1]
        bot.send_message(message.chat.id, weapon)
    elif len(message.text.split()) >= 3:
        bot.send_message(message.chat.id, "Выберите только 1 оружие")
    print(f'Weapon command used by {message.chat.username}')


@bot.message_handler(commands=['викторина', 'quiz'])
def quiz(message):
    bot.send_message(message.chat.id, 'Quiz now is in development')
    # bot.send_poll(
    # message.chat.id, 'Какой калибр у АК-47?', ['5.56x45', '7.62x39', '7.62x54'], correct_option_id=1, open_period=30
    # )
    print(f'Quiz command used by {message.chat.username}')


# connection = sql_connection()
# sql_table(connection)

bot.polling()
