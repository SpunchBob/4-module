from telebot import TeleBot
from telebot.types import (Message,
                           ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from game_parsing import (action_games, 
                          action_games_url,
                          adventure_games,
                          adventure_games_url,
                          rpg_games,
                          rpg_games_url,
                          simulation_games,
                          simulation_games_url,
                          strategy_games,
                          strategy_games_url,
                          sports_and_racing_games,
                          sports_and_racing_games_url,
                          best_games)

from dvach_parsing import pastas
import random

token = "5632737558:AAGaM-AxIvmA1Jl0ni4OE9Te-DVXI8cRUmY"

bot = TeleBot(token)

def welcome_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    button1 = KeyboardButton("😂Посмотреть мемчики😂")
    button2 = KeyboardButton("🤬Пасты на Дваче🤬")
    button3 = KeyboardButton("🎼Мемное музло🎼")
    button4 = KeyboardButton("👾Игры👾")

    keyboard.add(button1, button2, button3, button4)
    return keyboard

def game_genere_keyboard():
    
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button1 = KeyboardButton("Экшен")
    button2 = KeyboardButton("Адвенутре")
    button3 = KeyboardButton("RPG")
    button4 = KeyboardButton("Стимуляторы")
    button5 = KeyboardButton("Стратежки")
    button6 = KeyboardButton("Спортик игры и гонки")
    best_games = KeyboardButton("Лучшие игры")
    enter_button = KeyboardButton("Выйти в окно")

    keyboard.add(button1, button2, button3, button4, button5, button6, enter_button, best_games)
    return keyboard

@bot.message_handler(commands=["start"])
def welcome_bot_start(message: Message):
    keyboard = welcome_keyboard()
    image1 = open("MaximumProject\data\pictures\doomer.jpg", "rb")
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    inline_button1 = InlineKeyboardButton(text="Двач", url="https://2ch.hk/")
    inline_button2 = InlineKeyboardButton(text="Реддит", url="https://www.reddit.com/")
    inline_keyboard.add(inline_button1, inline_button2)
    bot.send_photo(message.from_user.id, photo=image1, reply_markup=inline_keyboard)
    bot.send_message(message.from_user.id, "Привет анон, меня зовут Боря.\n Ну чё, опять будем трындеть о том как:\n1.Как тебя на миду в дотке пудж хукнул?\n2.Или послушаем индастриал ноиз пост дарк ретровэйв?\n\nКстати сверху под фоточкой меня ссылки на твои любимые сайты!", reply_markup=keyboard)
    bot.send_message(message.from_user.id, "Кстати, я ещё тебе могу рекомендовать различные игры! Просто скажи что тебе нравится, а я тебе подкскажу!")

@bot.message_handler(content_types="text")
def bot_action(message: Message):
    
    #игрули

    if (message.text == "👾Игры👾"):
        image_steam = open("MaximumProject\data\pictures\i.jpeg", "rb")
        keyboard = game_genere_keyboard()
        inline_keyboard = InlineKeyboardMarkup(row_width=2)
        inline_button1 = InlineKeyboardButton(text="Steam", url="https://store.steampowered.com/")
        inline_button2 = InlineKeyboardButton(text="Торрент", url="https://m.moreigr.com/")
        inline_keyboard.add(inline_button1, inline_button2)
        bot.send_photo(message.from_user.id, photo=image_steam, reply_markup=inline_keyboard)
        bot.send_message(message.from_user.id, "Не ссы бродяга, выбирай жанр играшки. К сожалению, я тебе могу дать только ссылки на поджанры в стиме, но не ссы x2, я дам тебе свои предпочтения по игрушкам!", reply_markup=keyboard)
    if (message.text == "Экшен"):
        bot_say_games = action_games()
        bot_say_url = action_games_url()
        bot.send_message(message.from_user.id, 'Вот что я могу тебе предложить, ниже ссылочки, ознакомься: \n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "Адвенутре"):
        bot_say_games = adventure_games()
        bot_say_url = adventure_games_url()
        bot.send_message(message.from_user.id, '\n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "RPG"):
        bot_say_games = rpg_games()
        bot_say_url = rpg_games_url()
        bot.send_message(message.from_user.id, '\n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "Стимуляторы"):
        bot_say_games = simulation_games()
        bot_say_url = simulation_games_url()
        bot.send_message(message.from_user.id, '\n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "Стратежки"):
        bot_say_games = strategy_games()
        bot_say_url = strategy_games_url()
        bot.send_message(message.from_user.id, '\n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "Спортик игры и гонки"):
        bot_say_games = sports_and_racing_games()
        bot_say_url = sports_and_racing_games_url()
        bot.send_message(message.from_user.id, '\n'.join(bot_say_games))
        bot.send_message(message.from_user.id, '\n'.join(bot_say_url))
    if (message.text == "Лучшие игры"):
        bot_say_best_games = best_games()
        bot.send_message(message.from_user.id, "Могу порекомендовать тебе вот эти игры: ")
        bot.send_message(message.from_user.id, "\n".join(bot_say_best_games))
    if (message.text == "Выйти в окно"):
        bot.send_message(message.from_user.id, "Ну шо, надеюсь я тебе бродяга помог. Увидимся в лобби попуск!")
        welcome_bot_start(message=message)

    #мемасы

    if (message.text == "😂Посмотреть мемчики😂"):
        meme1 = open("MaximumProject\data\pictures\meme1.jpg", "rb")
        meme2 = open("MaximumProject\data\pictures\mem2.jpeg", "rb")
        meme3 = open("MaximumProject\data\pictures\meme3.jpg", "rb")
        meme4 = open("MaximumProject\data\pictures\meme4.jpg", "rb")
        random_list = [meme1, meme2, meme3, meme4]
        random_meme = random.choice(random_list)
        bot.send_message(message.from_user.id, "Наслаждайся чувачело!")
        bot.send_photo(message.from_user.id, photo=random_meme)

    if (message.text == "🤬Пасты на Дваче🤬"):
        random_past = random.choice(pastas)
        bot.send_message(message.from_user.id, random_past)

    if (message.text == "🎼Мемное музло🎼"):
        music1 = open("MaximumProject\data\music\Background - Gotham love.mp3", "rb")
        music2 = open("MaximumProject\data\music\kindashit - Remorse.mp3", "rb")
        music3 = open("MaximumProject\data\music\Scatman_John_-_Scatmans_World_73330107.mp3", "rb")
        music4 = open("MaximumProject\data\music\Yot Club - japan.mp3", "rb")
        music5 = open("MaximumProject\data\music\Yot Club - YKWIM.mp3", "rb")
        music6 = open("MaximumProject\data\music\Борис МОИСЕЕВ - Голубая луна.mp3", "rb")
        all_music = [music1, music2, music3, music4, music5, music6]
        bot.send_audio(message.from_user.id, random.choice(all_music))


bot.polling()

