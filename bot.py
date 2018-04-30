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
/nod a b c d ... - GCD(a, b, c, d, ...) - Greatest Common Divisor.
/nok a b c d ... - LCM(a, b, c, d, ...) - Least Common Multiple.
/factor a - Factorization of number а.
/polynoms_add a1 a2 a3 ... an + b1 b2 b3 ... bn - Sum polynomials with
coefficients a1, a2, a3, ... , an and b1, b2, b3, ... , bn, where
these coefficients begin with the highest power of the polynomial.
If some power is not - write '0'.
Example, for (2x^5+7x^3-x+14)+(8x^4+11x^3-2)
please write '2 0 7 0 -1 14 + 0 8 11 0 0 -2'.
ATTENTION! Please write spaces around '+'.
/polynoms_sub - the same thing, only subtraction of polynomials.
Instead of '+' please write '-'.

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
    

@bot.message_handler(commands=['polynoms_add'])
def polynoms_add(message):
    msg = bot.send_message(message.chat.id, mathfunc.polynoms_add(message))
    
    
@bot.message_handler(commands=['polynoms_sub'])
def polynoms_sub(message):
    msg = bot.send_message(message.chat.id, mathfunc.polynoms_sub(message))
    

bot.polling()