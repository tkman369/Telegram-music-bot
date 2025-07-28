import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot!")

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
