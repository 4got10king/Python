import asyncio
import logging
import os

from telegram import Update
from message_txt import START
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=START
    )

async def booklist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = 'Здесь скоро появится список книг'

    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    booklist_handler = CommandHandler('booklist', booklist)
    application.add_handler(start_handler)
    application.add_handler(booklist_handler)
    
    application.run_polling()


