b1 = int(input('Enter number(only 1 number): '))
b2 = int(input('Enter number: '))
b3 = int(input('Enter number: '))
b4 = int(input('Enter number: '))
b5 = int(input('Enter number: '))
b6 = int(input('Enter number: '))
b7 = int(input('Enter number: '))
b8 = int(input('Enter number: '))
b9 = int(input('Enter number: '))
b10 = int(input('Enter number: '))
b11 = int(input('Enter number: '))
b12 = int(input('Enter number: '))
b13 = int(input('Enter number: '))


def op():
    b21 = b2+b4+b6+b8+b10+b12
    print(b21)
    f3 = b21*3
    print(f3)
    b12c = b1+b3+b5+b7+b9+b11
    print(b12c)
    fun = f3+b12c
    print(fun)
    tens = (fun //10)*10
    result = fun - tens
    print(result)
    final = 10 - result
    print(final)

    if final == b13:
        print('Товар з лицензией')
    else:
        print('Товар без лицензии')

op()