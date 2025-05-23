import telebot
import random
import string
import threading
from telebot import types
from googletrans import Translator

bot = telebot.TeleBot("7673436683:AAEGDgFvexxgDfFYuRnNA9pGOqLkHtjdewY")
translator = Translator()

# Состояния
secret_numbers = {}
waiting_for_timer = set()
waiting_for_translate = set()

# /start с кнопками
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Сайт 🇦🇲", url="https://travel.yandex.ru/journal/armeniya-na-mashine-idealnyy-marshrut"),
        types.InlineKeyboardButton("Играть 🎲", callback_data="play_game"),
        types.InlineKeyboardButton("Таймер ⏱️", callback_data="set_timer"),
        types.InlineKeyboardButton("Переводчик 💬", callback_data="translator"),
        types.InlineKeyboardButton("Пароль 🔐", callback_data="password")
    )
    bot.send_message(message.chat.id, f"Барев Дез, {message.from_user.first_name}!", reply_markup=markup)

# Игра "Угадай число"
@bot.callback_query_handler(func=lambda call: call.data == "play_game")
def callback_game(call):
    secret_numbers[call.message.chat.id] = random.randint(1, 5)
    bot.send_message(call.message.chat.id, "Я загадал число от 1 до 5. Введи число:")

@bot.message_handler(func=lambda message: message.chat.id in secret_numbers)
def guess(message):
    try:
        num = int(message.text)
        secret = secret_numbers[message.chat.id]
        if num == secret:
            bot.send_message(message.chat.id, "Правильно! Ты угадал!")
            del secret_numbers[message.chat.id]
        else:
            bot.send_message(message.chat.id, "Нет. Попробуй ещё раз!")
    except:
        bot.send_message(message.chat.id, "Введи число от 1 до 5.")

# Таймер
@bot.callback_query_handler(func=lambda call: call.data == "set_timer")
def callback_timer(call):
    waiting_for_timer.add(call.message.chat.id)
    bot.send_message(call.message.chat.id, "Введи количество минут для таймера:")

@bot.message_handler(func=lambda message: message.chat.id in waiting_for_timer)
def set_timer(message):
    try:
        minutes = int(message.text)
        if minutes <= 0:
            raise ValueError
        bot.send_message(message.chat.id, f"Таймер на {minutes} минут запущен!")
        waiting_for_timer.remove(message.chat.id)

        def reminder():
            bot.send_message(message.chat.id, f"Прошло {minutes} минут!")

        threading.Timer(minutes * 60, reminder).start()
    except:
        bot.send_message(message.chat.id, "Пожалуйста, введи корректное число минут.")

# Переводчик
@bot.callback_query_handler(func=lambda call: call.data == "translator")
def start_translation(call):
    waiting_for_translate.add(call.message.chat.id)
    bot.send_message(call.message.chat.id, "Напиши фразу на русском, и я переведу её на английский:")

@bot.message_handler(func=lambda message: message.chat.id in waiting_for_translate)
def translate(message):
    try:
        translated = translator.translate(message.text, src='ru', dest='en')
        bot.send_message(message.chat.id, f"Перевод: {translated.text}")
        waiting_for_translate.remove(message.chat.id)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка при переводе: {e}")

# Генератор пароля
@bot.callback_query_handler(func=lambda call: call.data == "password")
def generate_password(call):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=10))
    bot.send_message(call.message.chat.id, f"Твой новый пароль:\n{password}", parse_mode="Markdown")

# Запуск бота
bot.polling(non_stop=True)