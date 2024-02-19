import telebot
import requests

token = "6955005713:AAG9uLr-xSq2x5G96VmI4fPU-EoYfbuFU44"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """
Это бот-конвертер валют
Переводите самые популярные валюты здесь
/convert - команда для перевода""")


@bot.message_handler(commands=['convert'])
def convert_message(message):
    bot.send_message(message.chat.id, """Конвертер валют. Пишите запрос так:
<Код валюты, из которой переводите переводите> <код валюты, в которую переводите> <сколько валюты переводите>
Например: USD RUB 1.25""")


@bot.message_handler()
def get_user_text(message):
    convert_list = message.text.split(" ")
    before = convert(convert_list[0], convert_list[1], float(convert_list[2].replace(",", ".")))
    after = "%.2f" % before
    bot.send_message(message.chat.id,
                     convert_list[2] + " " + convert_list[0] + " --> " + str(after) + " " + convert_list[1])


def convert(fr, to, amount):
    cur_list = ["RUB", "USD", "EUR"]
    if fr not in cur_list:
        return f"Валюты '{fr}' нет в списке популярных"
    if to not in cur_list:
        return f"Валюты '{to}' нет в списке популярных"
    else:
        url = f"https://api.tinkoff.ru/v1/currency_rates?from={fr}&to={to}"
        return requests.get(url).json()['payload']['rates'][-1]['buy'] * amount


bot.infinity_polling()
