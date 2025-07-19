def enter():
    print('Fтж '
          'Fтр '
          'Fтс '
          'Fпр '
          'Fарх '
          'P '
          'p(густина) '
          'p '
          'u '
          'p(тиск) '
          'p(гідростатичний тиск)')
    fun()


def fun():
    phy = input(': ')
    if phy == 'Fтж':
        massa = int(input('massa: '))
        print(massa*9.8,'H')
    elif phy == 'Fтр':
        massa2 = int(input('massa: '))
        b = massa2*9.8
        U =int(input('Коєфиціент: '))
        print(b*U,'H')

    elif phy == 'Fтс':
        massa3 = int(input('massa: '))
        S = int(input('S: '))
        F = massa3*9.8
        print(F/S,'Па')

    elif phy == 'Fпр':
        x = int(input('x: '))
        k = int(input('Коефіціент:'))
        print(x*k,'H')

    elif phy == 'Fарх':
        print('1)Теоритична',
              '2)Експерементальна')
        num = int(input())
        if num == 1:
            p = 1000
            print(p,'густина')
            h = int(input("Занурений об'єм: "))
            print(p*9.8*h,'H')

    elif phy == 'P':
        massa3 = int(input('massa: '))
        print(massa3 * 9.8, 'H')
    elif phy == 'p(густина)':
        massa4 = int(input('massa: '))
        V = int(input("Oб'єм: "))
        print(massa4/V,'m/V')

    elif phy == 'p':
        massa5 = int(input('massa: '))
        u = int(input('Скорость: '))
        print(massa5*u,'p')

    elif phy == 'u':
        s = int(input('km: '))
        t = int(input('time:'))
        print(s/t,'km/h')

    elif phy == 'Fтр':
        pass
    elif phy == 'Fтр':
        pass








enter()
