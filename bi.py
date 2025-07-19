import webbrowser as wb
import time
import mouse
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import datetime

now = datetime.datetime.now()


while True:
    web = input('Введи сайт: ')


    if web == 'bitcoin':
        wb.get().open('https://www.nicehash.com/my/dashboard')
        time.sleep(3)
        user32 = ctypes.windll.user32
        user32.SetCursorPos(200, 140)
        time.sleep(1)
        mouse.click()
    elif web == 'telegram':
        wb.get().open('https://web.telegram.org/a/')
    elif web == 'зам':
        with open('заметки.txt','r',encoding='utf-8') as file:
            print(file.read())

    elif web == 'зам1':
        with open('заметки.txt','a',encoding='utf-8') as file:
            write = input()
            nowin = write
            file.write(nowin+' ')
    elif web == 'exit':
        exit()
    elif web == 'volue':
        def increase_volume(step=0.05):  # 0.05 = 5%
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            current = volume.GetMasterVolumeLevelScalar()
            new_volume = min(current + step, 1.0)  # ограничение до 100%
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            print(f"Громкость установлена на {int(new_volume * 100)}%")


        # Пример: увеличить громкость на 5%
        increase_volume()
    elif web == 'youtube':
        wb.get().open('https://youtube.com')

    else:
        print('Такой команды нема')