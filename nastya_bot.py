import telebot
import random

bot = telebot.TeleBot('5628233116:AAGKEtotlCtyFmAq19RvNxbue3x6YlUUSC8')
from telebot import types

first = ["Today is the perfect day for new beginnings.",
         "The optimal day to decide on a bold act!",
         "Be careful, today the stars can affect your financial condition.",
         "The best time to start a new relationship or sort out old ones.",
         "A fruitful day to sort out the accumulated cases."]

second = ["But remember that even in this case, you should not forget about",
          "If you go out of town, think about it in advance",
          "Those who are aiming to do a lot of things today should remember about",
          "If you have a breakdown, pay attention to",
          "Remember that thoughts are material, which means that you need to constantly think about"]

second_add = ["relationships with friends and family.",
              "work and business issues that can interfere with plans so inopportunely.",
              "yourself and your health, otherwise a complete breakdown is possible by the evening.",
              "household issues — especially those that you did not finish yesterday.",
              "rest, so as not to turn yourself into a hunted horse at the end of the month."]

third = ["Evil tongues may tell you the opposite, but you don't need to listen to them today.",
         "Know that success favors only the persistent, so dedicate this day to the education of the spirit.",
         "Even if you cannot reduce the influence of retrograde Mercury, then at least bring things to an end.",
         "There is no need to be afraid of lonely meetings — today is the time when they mean a lot.",
         "If you meet a stranger on the way, take part, and then this meeting will promise you pleasant troubles."]


def command_answer(message: str) -> str:
    if message == "/start":
        return "Hi! I can tell you your horoscope for today"
    elif message == "/help":
        return "This bot can predict your horoscope for today. To get started, write /start"
    else:
        return "I don't understand you. Please write /help."


def generate_advice() -> str:
    return random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
        second_add) + ' ' + random.choice(third)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":

        bot.send_message(message.from_user.id, command_answer("/start"))

        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака

        key_aries = types.InlineKeyboardButton(text='Aries', callback_data='zodiac')

        # И добавляем кнопку на экран

        keyboard.add(key_aries)

        key_taurus = types.InlineKeyboardButton(text='Taurus', callback_data='zodiac')

        keyboard.add(key_taurus)

        key_gemini = types.InlineKeyboardButton(text='Gemini', callback_data='zodiac')

        keyboard.add(key_gemini)

        key_cancer = types.InlineKeyboardButton(text='Cancer', callback_data='zodiac')

        keyboard.add(key_cancer)

        key_leo = types.InlineKeyboardButton(text='Leo', callback_data='zodiac')

        keyboard.add(key_leo)

        key_virgo = types.InlineKeyboardButton(text='Virgo', callback_data='zodiac')

        keyboard.add(key_virgo)

        key_libra = types.InlineKeyboardButton(text='Libra', callback_data='zodiac')

        keyboard.add(key_libra)

        key_scorpio = types.InlineKeyboardButton(text='Scorpio', callback_data='zodiac')

        keyboard.add(key_scorpio)

        key_sagittarius = types.InlineKeyboardButton(text='Sagittarius', callback_data='zodiac')

        keyboard.add(key_sagittarius)

        key_capricorn = types.InlineKeyboardButton(text='Capricorn', callback_data='zodiac')

        keyboard.add(key_capricorn)

        key_aquarius = types.InlineKeyboardButton(text='Aquarius', callback_data='zodiac')

        keyboard.add(key_aquarius)

        key_pisces = types.InlineKeyboardButton(text='Pisces', callback_data='zodiac')

        keyboard.add(key_pisces)

        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text="Choose your zodiac sign:", reply_markup=keyboard)

    else:
        bot.send_message(message.from_user.id, command_answer(message.text))


# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп

    if call.data == "zodiac":
        # Формируем гороскоп

        msg = generate_advice()

        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме


def main():
        bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()


def calc(a: int, b: int) -> int:
    return a + b