class BankAc:
    def __init__(self, Banknum):
        self.Banknum = Banknum


        print(Banknum,"$")
        en = input('Зняти:')
        if en == 'так':
            sum1 = int(input('Яка сумма: '))

            if sum1 > Banknum:
                print('Нельзя')
            else:
                Banknum1 = Banknum - sum1
                print('Кількість грошей на карті - ',Banknum1)


        else:
            print('ok')

BankAc(23)