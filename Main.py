from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.environ.get("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🎵 Hello! I am your music bot. Type /song to get a track.")

def song(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    audio_path = "sample.mp3"
    context.bot.send_audio(chat_id=chat_id, audio=open(audio_path, "rb"))

updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("song", song))

updater.start_polling()
updater.idle()
