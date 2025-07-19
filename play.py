from gtts import gTTS
from playsound import playsound

text = input('Enter text: ')
lang = 'ru'
sd = gTTS(lang=lang,text=text,slow=False)
sd.save('test.mp3')
playsound('test.mp3')