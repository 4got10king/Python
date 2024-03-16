import asyncio
import logging
import os
import sqlalchemy

from telegram import Update
from message_txt import *
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()

engine = sqlalchemy.create_engine(os.getenv('DB_URL'))
connection = engine.connect()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = START
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = HELP
    )

async def booklist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = BOOKLIST
    )


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    booklist_handler = CommandHandler('booklist', booklist)
    help = CommandHandler('help', help)
    application.add_handler(start_handler)
    application.add_handler(booklist_handler)
    application.add_handler(help)
    application.run_polling()


