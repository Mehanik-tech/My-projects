class Triagle:
    a = int(input('Перша сторона: '))
    b = int(input('Друга сторона: '))
    c = int(input('Основа: '))

    ba = b+a
    if ba > c:
        print('yeah')
    else:
        print('no')
Triagle()
