import cv2
import numpy as np

# Открытие видеопотока с камеры
cap = cv2.VideoCapture(0)  # Индекс 0 для первой камеры

# Проверка, что камера открыта
if not cap.isOpened():
    print("Ошибка: не удалось открыть камеру.")
    exit()

# Настройка VideoWriter для записи видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Кодек для записи (например, XVID, MJPG, etc.)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Параметры: имя файла, кодек, FPS, размер кадра

while True:
    ret, frame = cap.read()  # Захват кадра с камеры
    if not ret:
        print("Ошибка: не удалось захватить кадр.")
        break

    # Получаем второй кадр с той же камеры (для примера можно сделать небольшую задержку)
    ret, frame2 = cap.read()
    if not ret:
        print("Ошибка: не удалось захватить второй кадр.")
        break

    # Объединяем два изображения горизонтально (или вертикально)
    combined_frame = cv2.hconcat([frame, frame2])  # Можно использовать vconcat для вертикального объединения

    # Запись кадра в видеофайл
    out.write(combined_frame)

    # Показываем объединённое изображение
    cv2.imshow('Combined Frames', combined_frame)

    # Прерывание по нажатию клавиши 'ESC' (код клавиши ESC = 27)
    if cv2.waitKey(1) & 0xFF == 27:
        print("Запись завершена.")
        break

# Освобождение ресурсов
cap.release()
out.release()  # Закрытие файла записи
cv2.destroyAllWindows()
