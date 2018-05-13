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
/gcd a b c d ... - GCD(a, b, c, d, ...) - Greatest Common Divisor.
/lcm a b c d ... - LCM(a, b, c, d, ...) - Least Common Multiple.
/factor a - Factorization of number а.
/polynoms_add (a1+a2+...+an)+(b1+b2+...+bn) - Addition of 
polynomials with coefficients a1, a2, ... , an and b1, b2, ... , bn, 
where these coefficients begin with the highest power of the 
polynomial. If some power is not - write '0'.
Example, for (2x^5+7x^3-x+14)+(8x^4+11x^3-2)
please write '(2+0+7+0-1+14)+(8+11+0+0-2)'.
/polynoms_sub - the same thing, only subtraction of polynomials.
Instead of '+' please write '-'.
/polynoms_mul (a1+a2+...+an)*(b1+b2+...+bn) - Multiplication of
polynomials with coefficients a1, a2, ... , an and b1, b2, ... , bn, 
where these coefficients begin with the highest power of the 
polynomial. If some power is not - write '0'.
Example, for (2x^5+7x^3-x+14)*(8x^4+11x^3-2)
please write '(2+0+7+0-1+14)*(8+11+0+0-2)'.
/polynoms_div - the same thing, only division of polynomials.
Instead of '*' please write '/'.
/lin_dep a b - Linear Decomposition of numbers a and b.
Linear Decomposition is a*m + b*n = GCD(a, b).

For help type /help.'''


error = ''''Oops! Something is written incorrectly...
Please use /help for correct answer.'''


@bot.message_handler(commands=['start'])
def start(message):
    try:
        msg = bot.send_message(message.chat.id, command_list)
    except:
        bot.send_message(message.chat.id, command_list)
    
    
@bot.message_handler(commands=['help'])
def help(message):
    try:
        msg = bot.send_message(message.chat.id, command_list)
    except:
        bot.send_message(message.chat.id, command_list)
    
    
@bot.message_handler(commands=['gcd'])
def gcd(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.gcd(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['lcm'])
def lcm(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.lcm(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['factor'])
def factor(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.factor(msg))
    except:
        bot.send_message(message.chat.id, error)

        
@bot.message_handler(commands=['polynoms_add'])
def polynoms_add(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_add(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polynoms_sub'])
def polynoms_sub(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_sub(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polynoms_mul'])
def polynoms_mul(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_mul(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['polynoms_div'])
def polynoms_div(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.polynoms_div(msg))
    except:
        bot.send_message(message.chat.id, error)
    
    
@bot.message_handler(commands=['lin_dep'])
def lin_dep(message):
    try:
        msg = f'{message.text}'
        answer = bot.send_message(message.chat.id, mathfunc.lin_dep(msg))
    except:
        bot.send_message(message.chat.id, error)
        

bot.polling()
