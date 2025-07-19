
class Car:
    def SpeedLimit():

        s = int(input('Enter speed: '))
        if s>=120:
            print('Перевищення швидкості')
        else:
            if 20>=s:
                print("Занадто повільно")
            else:
                print('норм')
    SpeedLimit()

Car()