import telebot
from telebot import types
import random  

token = '5359374702:AAFns2LPkQLGP75C1YXVZMuhrTZ0LLvqRQs'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def send_same_message(message):
    msg = bot.send_message(message.chat.id, message.text)

bot.polling()
