import sqlite3

import telebot
from telebot import types
import tools
bot=telebot.TeleBot("6963512378:AAFYso5nik4t6BoqkDFBvyEbadcv2X9E8BQ")
name=""
id=""

@bot.message_handler(commands=["start"])
def CMstart(message):
    markup=types.ReplyKeyboardMarkup()
    fastReg=types.KeyboardButton("Быстрая регистрация 🚀")
    normReg=types.KeyboardButton("Обычная регистрация 🚛")
    markup.row(fastReg,normReg)

    helpMarkup=types.InlineKeyboardMarkup()
    CLhelp=types.InlineKeyboardButton("Чем одна регистрация отличается от другой",callback_data="help")
    helpMarkup.row(CLhelp)

    text=f"Привет {message.from_user.first_name} мы рады тебя видеть в нашем боте. Перед Тем как вы продолжите работы, вам необходимо пройти регистрацию пожалуйста выберите её тип"
    bot.send_message(message.chat.id,text,reply_markup=markup)
    bot.send_message(message.chat.id,"Если вы не понимаете, то нажмите на кнопку ниже",reply_markup=helpMarkup)
    print(message.from_user.first_name)
    bot.register_next_step_handler(message,Reg)

def Reg(message):
    if message.text == "Быстрая регистрация 🚀":
        regUser=tools.User(message.from_user.first_name,photo="abc",balance=0)
    elif message.text == "Обычная регистрация 🚛":
        bot.send_message(message.chat.id,"Выберите име:")
        bot.register_next_step_handler()
    else:
        CMstart()
def getName(message):
    name=message.text
    if checkName(name):
        markup=types.InlineKeyboardMarkup()
        done=types.InlineKeyboardButton("⚠️Я хочу продолжить с этим именем⚠️",callback_data="doneName")
        again=types.InlineKeyboardButton("✅Я хочу ввести имя заново✅",callback_data="againName")
        bot.send_message(message.chat.id,"Данное имя уже используется пользователями, но вы можете продолжить и зарегестрироваться с этим именем или ввести имя ещё раз")
    pass
def checkName(name):
    with sqlite3.connect("my_database.db") as con:
        cur=con.cursor()
        cur.execute(f"SELECT EXISTS(SELECT * FROM Users where username = '{name}')")
        x=cur.fetchall()
        return bool(x[0][0])
@bot.callback_query_handler(func=lambda callback: True)
def callbackHandler(callback):
    if callback.data=="help":
        bot.send_message(callback.message.chat.id,"При обычной регистрации вы вручную указываете ваш никнейм, фото профиля, и также можете перенести информацию с другого аккаунта, а при обычной вы позже сможете установить ваше фото, но вы не сможете в автоматическом режиме перенести все дымки и лоты на продажу с другого аккаунта на этот\nВ автоматическом режиме в регистрируетесь по одному нажатию кнопки, а никнейм будет установлен в соответствии с вашим именем, под которым вы зарегестрированы в телеграме")
    elif callback.data=="doneName":
        pass
    elif callback.data=="againName":
        CMstart(callback)
bot.polling(none_stop=True)