import pyttsx3

engine = pyttsx3.init()

# Получаем доступные голоса
voices = engine.getProperty('voices')

# Попробуем найти мужской русский голос
for voice in voices:
    lang = voice.languages[0].decode() if voice.languages else ''
    if "ru" in lang.lower() and "male" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        print(f"Выбран голос: {voice.name}")
        break
else:
    print("Мужской русский голос не найден, используется голос по умолчанию.")

# Ввод и озвучивание текста
text = input("Введите текст: ")
engine.say(text)
engine.runAndWait()
