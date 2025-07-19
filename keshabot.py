import telebot
from telebot import types
import time
import mouse
import random




tok = '7471835497:AAFJTzB_q-wr0bLHCaat8Mp9bnoDVvniy5k'
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def ffg(message):
    bot.send_message(message.chat.id, 'Здаров, че зумер вот команды')
    bot.send_message(message.chat.id, '/start, /help, /doc')

@bot.message_handler(commands=['help'])
def ffgfxx(message):
    bot.send_message(message.chat.id, 'У меня вопрос. Как, я по твоему тебе должен помочь????')

@bot.message_handler(commands=['doc'])
def ffgfxx(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton('Рандомное число от 1 до 1000000000')
    i2 = types.KeyboardButton('Как дела')
    i3 = types.KeyboardButton('Игры')
    markup.add(i1, i2, i3)
    bot.send_message(message.chat.id, 'Поздавляю, у тебя клава', reply_markup=markup)
    #keyboard

@bot.message_handler(content_types=['text'])
def fsd(message):
    if message.chat.type == 'private':
        if message.text == 'Как дела':
            bot.send_message(message.chat.id, 'Норм, а на твои мне всеровно')
        elif message.text == 'Рандомное число от 1 до 1000000000':
            bot.send_message(message.chat.id, random.randint(1, 10000000000))
        elif message.text == 'Игры':
            bot.send_message(message.chat.id, 'Бравл старс,майнкрафт,кс гоу,пабг,роблокс,школьник против родитилей,райс ап,чикен ган,кроссаут')

        else:
            bot.send_message(message.chat.id, message.text)




@bot.message_handler(content_types=['text'])
def f(message):
    bot.send_message(message.chat.id, message.text)
@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    #sticker_id = message.sticker.file_id
    bot.send_message(message.chat.id, message.sticker.file_id +' - sticker')


bot.polling()
#none_stop=True
