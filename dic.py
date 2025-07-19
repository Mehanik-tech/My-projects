class Discount:
    dic = int(input('Запиши ціну:'))
    if dic > 1000:
        off = 0.1
        print(dic*off)
    else:
        print('Немає знижки')
Discount()