import random
import time
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import *
def listen_command():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите вашу команду: ")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        our_speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError:
        return "ошибка"


def do_this_command(message):
    message = message.lower()
    if "привет" in message:
        text = 'Привет друг'
        lang = 'ru'
        sd = gTTS(lang=lang, text=text, slow=False)
        sd.save('test.mp3')
        playsound('test.mp3')
    elif "пока" in message:
        say_message("Пока!")
        exit()
    else:
        say_message("Команда не распознана!")


def say_message(message):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the properties for male voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Index 0 usually corresponds to the male voice

    # Set the rate of speech (optional)
    engine.setProperty('rate', 150)  # Adjust the speed of the voice if needed

    # Speak the message
    engine.say(message)
    engine.runAndWait()

    print("Голосовой ассистент: "+message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
