import telebot

from config import keys, TOKEN
from utils import CovertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'To get started, enter the bot command in the following format: \n <value start> \ <value end> \ <many> \nget available values: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    text = 'Values:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise CovertionException('Wrong parameters')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except CovertionException as e:
        bot.reply_to(message, f'User error: {e}')

    except Exception as e:
        bot.reply_to(message, f'Error : {e}')
    else:
        text = f'Price {amount} {quote} in {base} : {total_base * float(amount)}'
        bot.send_message(message.chat.id, text)


bot.polling()