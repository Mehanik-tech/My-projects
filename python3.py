import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)  # ← змінити на правильний COM
time.sleep(2)  # Дати час Arduino завантажитись

arduino.write(b'1')  # Увімкнути LED
time.sleep(1)
arduino.write(b'0')  # Вимкнути LED
