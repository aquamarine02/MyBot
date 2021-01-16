import random
import string
import telebot
import creds

bot = telebot.TeleBot(creds.TELEGRAM_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Привет. Введи цифру от одного до трех: 1 - простой пароль, 2 - пароль '
                     'средней сложности, 3 - сложный пароль')


@bot.message_handler(content_types=['text'])
def send_text(message):
    size = random.randint(8, 12)
    special_chars: str = '+-/*!&$#?=@<>'
    if message.text == '1':
        chars = string.digits
        bot.send_message(message.chat.id, ''.join(random.choice(chars) for x in range(size)))
    elif message.text == '2':
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        while True:
            password = ''.join(random.choice(chars) for x in range(size))
            a = len((set(password) & set(string.ascii_uppercase)))
            b = len((set(password) & set(string.ascii_lowercase)))
            c = len((set(password) & set(string.digits)))
            if a != 0 and b != 0 and c != 0:
                bot.send_message(message.chat.id, password)
                break

    elif message.text.lower() == '3':
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + special_chars
        while True:
            password = ''.join(random.choice(chars) for x in range(size))
            a = len((set(password) & set(string.ascii_uppercase)))
            b = len((set(password) & set(string.ascii_lowercase)))
            c = len((set(password) & set(string.digits)))
            d = len((set(password) & set(special_chars)))
            if a != 0 and b != 0 and c != 0 and d != 0:
                bot.send_message(message.chat.id, password)
                break

    else:
        bot.send_message(message.chat.id, "я вас не понимаю")


bot.polling(none_stop=True, interval=0)
