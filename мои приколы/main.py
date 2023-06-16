from telebot import TeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
import random

bot = TeleBot("5471370817:AAHYo0DTG-7MVNfqfKlZZDi033cNq59eaWs")
BASE_FILES_DIR = r"C:\Users\Админ\PycharmProjects\28\lesson_2\extra"


def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton("/cats")
    button2 = KeyboardButton("/poem")
    button3 = KeyboardButton("/sticker")
    button4 = KeyboardButton("/music")

    keyboard.add(button1, button2, button3, button4)
    return keyboard


@bot.message_handler(commands=["start", "help"])
def welcome(message: Message):
    keyboard = welcome_keyboard()
    bot.send_message(message.from_user.id, "Привет! Выбери следующие команды:", reply_markup=keyboard)


@bot.message_handler(commands=["cats"])
def cats(message: Message):
    random_img_number = random.randint(1, 9)
    random_img = open(fr"{BASE_FILES_DIR}\{random_img_number}.jpg", "rb")
    bot.send_photo(message.from_user.id, random_img)


@bot.message_handler(commands=["music"])
def music(message: Message):
    audio = open(fr"{BASE_FILES_DIR}\happy.mp3", "rb")
    bot.send_audio(message.from_user.id, audio)


@bot.message_handler(commands=["poem"])
def poem(message: Message):
    bot.send_message(message.from_user.id, "Села муха на варенье, вот и всё стихотворенье!")
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="Перейти", url="https://stihi.ru/")
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Больше стихотворений здесь:", reply_markup=keyboard)


@bot.message_handler(commands=["sticker"])
def sticker(message: Message):
    bot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEG-ARjpcr2-W3KLvx5WuPtrSD3HZFNUwACHSYAAvBkKElgG1EAARdJBGAsBA")


bot.polling()
