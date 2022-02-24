from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, \
    InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, InlineQueryHandler, \
    CallbackQueryHandler
import logging
import pyowm
from config import BOT_TOKEN
from weather import get_forecast

# Check for new messages from API
updater = Updater(token=BOT_TOKEN)

# Allows registering handlers (e.g. commands, text, video, audio, etc.)
dispatcher = updater.dispatcher

# Setup logging which will let you know when and why something went wrong
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

HELP_MSG = '''
Hello there!
I can give you a weather forecast for your current location.

Use any of the following commands for interactions:
/help - Display this message
/forecast - Show weather forecast for your location 
'''


# Define command callback function
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG)


# Define command callback function
def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG)


# Define message callback function
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MSG)


def get_location(update: Update, context: CallbackContext):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(button)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Mind sharing your location?",
                             reply_markup=reply_markup)


def location(update: Update, context: CallbackContext):
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    forecast = get_forecast(lat, lon)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=forecast,
                             reply_markup=ReplyKeyboardRemove())


def main():
    # Create handlers and add them to the dispatcher
    start_handler = CommandHandler("start", start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler("help", help)
    dispatcher.add_handler(help_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    get_location_handler = CommandHandler("forecast", get_location)
    dispatcher.add_handler(get_location_handler)

    location_handler = MessageHandler(Filters.location, location)
    dispatcher.add_handler(location_handler)

    # Run the bot
    updater.start_polling()


if __name__ == "__main__":
    main()
