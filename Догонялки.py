import pyfirmata
import time

# Замените 'COM3' на правильный порт вашей Arduino, например, 'COM4' или '/dev/ttyUSB0'
board = pyfirmata.Arduino('COM4')  # Укажите правильный порт

while True:
    board.digital[13].write(1)  # Включаем светодиод на пине 13
    time.sleep(1)               # Ждем 1 секунду
    board.digital[13].write(0)  # Выключаем светодиод на пине 13
    time.sleep(1)               # Ждем 1 секунду
