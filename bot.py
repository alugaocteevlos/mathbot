#!/usr/bin/env python3

import config
import telebot
import mathfunc
from telebot import apihelper


apihelper.proxy = {
    'https': f'socks5://{config.log}:{config.pas}@{config.host}:{config.port}'
}


bot = telebot.TeleBot(config.token)


command_list = '''Telegram-bot with mathematical functions (v. 0.0.1)
Math functions:
/nod a b c d ... - НОД(a, b, c, d, ...)
/nok a b c d ... - НОК(a, b, c, d, ...)
/factor a - Факторизация числа а

For help type /help.'''


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, command_list)

    
@bot.message_handler(commands=['help'])
def help(message):
    msg = bot.send_message(message.chat.id, command_list)
    
    
@bot.message_handler(commands=['nod'])
def nod(message):
    msg = bot.send_message(message.chat.id, mathfunc.nod(message))
    
    
@bot.message_handler(commands=['nok'])
def nok(message):
    msg = bot.send_message(message.chat.id, mathfunc.nok(message))

    
@bot.message_handler(commands=['factor'])
def factor(message):
    msg = bot.send_message(message.chat.id, mathfunc.factor(message))

    
bot.polling()