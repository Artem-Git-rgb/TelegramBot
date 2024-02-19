import telebot
from telebot import types

token = "6955005713:AAG9uLr-xSq2x5G96VmI4fPU-EoYfbuFU44"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Привет! Список доступных команд этого бота:
/help - Помощь
/info - Информация об авторе
/hobby - Мои хобби
/song - моя любимая песня
/photo - фото моего рабочего стола
/history - История
/sus - Нажми
/sing - Споёт песенку""")


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    if callback.data == "start":
        start_message(callback.message)


@bot.message_handler(commands=['help'])
def help_message(message):  # помощь
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, "HELP :", reply_markup=markup)


@bot.message_handler(commands=['info'])
def info_message(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, "Васильев Артём, 15 Учусь в 9 классе", reply_markup=markup)


@bot.message_handler(commands=['hobby'])
def hobby_message(message):
    markup = types.InlineKeyboardMarkup()  # помощь
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, """Мои хобби:
Рисовать, моделировать, придумывать""", reply_markup=markup)


@bot.message_handler(commands=['song'])
def song_music(message):
    markup = types.InlineKeyboardMarkup()  # помощь
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    music = open("The_Red_Sun_In_The_Sky_BASS_BOOSTED.mp3", 'rb')
    bot.send_audio(message.chat.id, music, "Погромче поставь", reply_markup=markup)


@bot.message_handler(commands=['photo'])
def photo_message(message):
    markup = types.InlineKeyboardMarkup()  # помощь
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    photo = open("table_photo.jpg", 'rb')
    bot.send_photo(message.chat.id, photo, "Загрузки:Мой рабочий стол (настоящий)", reply_markup=markup)


@bot.message_handler(commands=['history'])
def history_message(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, """История:
Шёл медведь по лесу
Видит: машина горит
Сел в неё и сгорел""", reply_markup=markup)


@bot.message_handler(commands=['sus'])
def sus_message(message):
    markup = types.InlineKeyboardMarkup()  # помощь
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, "Тум тум тум тум тудум тум тум тум тудум", reply_markup=markup)


@bot.message_handler(commands=['sing'])
def sing_message(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="На главную", callback_data="start")
    markup.row(button)
    bot.send_message(message.chat.id, """У моей охраны есть охрана
И у той охраны есть охрана  
И у той охраны есть охрана  
И зовут его Иван
И у той охраны есть охрана  
И у той охраны есть охрана  
И зовут его Димоооон""", reply_markup=markup)


bot.infinity_polling()
