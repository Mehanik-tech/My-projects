with open('file.txt', 'r', encoding = "UTF-8") as file:
    for data in file:

        print(data)

a = input('Добавити свій вірш:')
if a == 'так':
    b = input('Пиши:')
    with open('just_file.txt', 'a') as file:
        file.write(b)
else:
   print('Ок')
with open('just_file.txt', 'r', encoding = "UTF-8") as file:
    for data in file:

        print(data)