import json

import telebot
from config import token

import json

bot = telebot.TeleBot(token)


def load():
    try:
        with open('users.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


users = load()


def save():
    with open('users.json', 'w') as file:
        json.dump(users, file)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, '🏓')


@bot.message_handler(commands=["subscribe"])
def subscribe(message):
    if message.chat.id not in users:
        users.append(message.chat.id)
    bot.send_message(message.chat.id, 'Подключили опросник!')
    save()


@bot.message_handler(commands=["unsubscribe"])
def unsubscribe(message):
    if message.chat.id in users:
        users.remove(message.chat.id)
    bot.send_message(message.chat.id, 'Отключили опросник!')
    save()


if __name__ == "__main__":
    bot.polling(none_stop=True)
