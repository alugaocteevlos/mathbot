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

For help type /help.'''


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, command_list)

    
@bot.message_handler(commands=['help'])
def help(message):
    msg = bot.send_message(message.chat.id, command_list)
    
    
@bot.message_handler(commands=['gcd'])
def gcd(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.gcd(msg))
    
    
@bot.message_handler(commands=['lcm'])
def lcm(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.lcm(msg))

    
@bot.message_handler(commands=['factor'])
def factor(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.factor(msg))
    

@bot.message_handler(commands=['polynoms_add'])
def polynoms_add(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.polynoms_add(msg))
    
    
@bot.message_handler(commands=['polynoms_sub'])
def polynoms_sub(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.polynoms_sub(msg))
    
    
@bot.message_handler(commands=['polynoms_mul'])
def polynoms_mul(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.polynoms_mul(msg))
    
    
@bot.message_handler(commands=['polynoms_div'])
def polynoms_div(message):
    msg = f'{message.text}'
    answer = bot.send_message(message.chat.id, mathfunc.polynoms_div(msg))


bot.polling()