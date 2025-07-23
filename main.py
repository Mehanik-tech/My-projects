import telebot
from telebot import types
import webbrowser as web
import keyboard
from playsound import playsound
import os
from gtts import gTTS
import pyglet

TOKEN = '7979430067:AAEaAxdEGb2Sx3eEroywCS9Xv0jqy9pf00c'
jarvis = telebot.TeleBot(TOKEN)




# Обработка команды /start
@jarvis.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('black in black')
    btn2 = types.KeyboardButton('Open the YouTube')
    b3 = types.KeyboardButton('Stop song')
    markup.add(btn1, btn2, b3)
    jarvis.send_message(message.chat.id, "Hi! I'm Jarvis.Click to the button or write text — I am will be generation.",reply_markup=markup)

@jarvis.message_handler(commands=['help'])
def send_local_image(message):
    jarvis.send_message(message.chat.id, "I have commands - /start(I begin work),"
                                         "  /image(I showing image of iron man"
                                         "  /turn_off_comp(I turn off computer")

@jarvis.message_handler(commands=['turn_off_comp'])
def send_local_image(message):
    os.system("shutdown -s -t 0")


@jarvis.message_handler(commands=['image'])
def send_local_image(message):

    with open('images.jpg', 'rb') as photo:
        jarvis.send_photo(message.chat.id, photo)

@jarvis.message_handler(func=lambda message: True)


def text_handler(message):
    if message.chat.type == 'private':
        if message.text.lower() == 'Open the YouTube':
            jarvis.send_message(message.chat.id, 'Opening YouTube...')
            web.open("https://www.youtube.com")
        elif message.text.lower() == 'Stop song':

            jarvis.polling(none_stop=False)
            exit()
            playsound.stop()
        elif message.text.lower() == 'black in black':

            playsound('ac-dc-back-in-black.mp3')

        else:

            if message.text.lower() == 'hi jarvis':
                text = 'hi'
                lan = 'en'
                ofj = gTTS(text=text,lang=lan,slow=False)

                ofj.save('hi.mp3')
                mus = pyglet.resource.media('hi.mp3')
                mus.play()

                jarvis.send_message(message.chat.id, 'hi')


            elif message.text.lower() == 'How are you':
                jarvis.send_message(message.chat.id, 'very well')
            elif message.text.lower() == 'Stop song':

                jarvis.polling(none_stop=False)
                exit()
            elif message.text.lower() == 'phonk':
                playsound('Atlxs - Passo Bem Solto (Super Slowed).mp3')

            elif message.text.lower() == 'start combat mode':
                jarvis.send_message(message.chat.id, 'I Starting combat mode')
                web.open('https://www.youtube.com/watch?v=9sCuyYOo3tQ')

            else:
                jarvis.send_message(message.chat.id, 'You did write ' + message.text)

jarvis.polling(none_stop=True)
pyglet.app.run()