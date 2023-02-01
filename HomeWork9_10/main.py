
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5807751052:AAF0wKkxtkG_DVkAxBe5Ae644jXJx5xPmvo").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler('sum', sum_command))
app.add_handler(CommandHandler('new_year', new_year_command))

app.run_polling()