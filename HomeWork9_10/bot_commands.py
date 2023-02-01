from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 53454
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.today()
    NY = datetime.datetime(now.year + 1, 1, 1)
    d = NY-now

    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    await update.message.reply_text('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))
