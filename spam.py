import telebot





tok = '7677850873:AAGgSuCqbkSYbElsgIQvWELEn1jx6B3oHe4'
bot = telebot.TeleBot(tok)



while True:

    def f(message):
        bot.send_message(message.chat.id, 'hello')


    bot.polling(none_stop=True)