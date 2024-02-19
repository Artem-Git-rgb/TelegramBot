import telebot

token = "6955005713:AAG9uLr-xSq2x5G96VmI4fPU-EoYfbuFU44"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Доброго времени суток!
Это бот-портфолио моих проектов
Создатель: Васильев Артём
/info - Информация об авторе
Список моих проектов, сделанных с помощью Pygame в GitHub:
/Underwater - игра с подводной лодкой
/Plane_and_Rockets - игра с самолётиком""")


@bot.message_handler(commands=['info'])
def info_message(message):
    bot.send_message(message.chat.id, """Васильев Артём, 2008
Языки программирования: Python
""")


@bot.message_handler(commands=['Underwater'])
def Underwater_msg(message):
    photo = open("screenUnderwater.png", 'rb')
    bot.send_photo(message.chat.id, photo, "https://github.com/Artem-Git-rgb/Underwater")


@bot.message_handler(commands=['Plane_and_Rockets'])
def Plane_and_rockets_msg(message):
    photo = open("screenPlane-and-rockets.png", 'rb')
    bot.send_photo(message.chat.id, photo, "https://github.com/Artem-Git-rgb/Plane-and-rockets")


bot.infinity_polling()
