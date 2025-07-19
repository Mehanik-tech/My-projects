from PIL import Image, ImageFilter
p1 = input('Введінь назву фота: ')
p2 = input('Зробити фото чорно білим: ')



with Image.open(p1) as p:
    p.show()

if p2 == 'так':
    pi = p.convert('L')
    pi.show()
    p3 = input('Зберегти: ')
    if p3 == 'так':
        pi.save(p1)
        p4 = input('Розмити: ')
        if p4 == 'так':
            g = p1.Filter(ImageFilter.BLUR)
            g.show()
        else:
            print('ok')
    else:
        print('ok')
else:
    print('ok')


