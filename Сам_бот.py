import telebot
import g4f
import time
import mouse
import ctypes
import threading

TOKEN = '7931235546:AAGvviGseGkw6wM3NZDG4xR1BSIKHMy_grQ'
bot = telebot.TeleBot(TOKEN)

# Отдельный цикл с мышкой каждые 5 секунд
def background_mouse_loop():
    while True:
        time.sleep(5)
        ctypes.windll.user32.SetCursorPos(1263, 55)
        mouse.click()

threading.Thread(target=background_mouse_loop, daemon=True).start()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Пиши, что волнует.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        res = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{
                'role': 'user',
                'content': message.text
            }]
        )
        bot.send_message(message.chat.id, res)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

if __name__ == '__main__':
    bot.polling(none_stop=True)