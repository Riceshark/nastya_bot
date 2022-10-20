from telegram import bot
import requests

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5628233116:AAGKEtotlCtyFmAq19RvNxbue3x6YlUUSC8",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")

def calc(update: Update, context: CallbackContext):
    try:
        number1 = int(context.args[0])
        number2 = int(context.args[1])
        result = number1+number2
        update.message.reply_text('The sum is: '+str(result))
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /calc number1 number2 - To sum two numbers""")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def main_loop():
    while True:
        updater = Updater("5628233116:AAGKEtotlCtyFmAq19RvNxbue3x6YlUUSC8", use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('start', start))
        dp.add_handler(CommandHandler('help', help))
        dp.add_handler(CommandHandler('calc', calc))

        dp.add_handler(MessageHandler(Filters.text, unknown))
        dp.add_handler(MessageHandler(
            Filters.command, unknown))
        dp.add_handler(MessageHandler(Filters.text, unknown_text))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    main_loop()
