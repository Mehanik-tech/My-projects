
password = input('enter password: ')

with open('dopa', 'r', encoding='utf-8') as file:
    dd = file.read()
print(dd)

ss = input('save: ')

if ss == 'yes':
    with open('dopa', 'w', encoding='utf-8') as file:
        file.write(password+" ")
    print('your password download')
    sdf = input('append password: ')
    if sdf == 'yes':
        with open('dopa', 'a', encoding='utf-8') as file:
            file.write(sdf+" ")
    else:
        print('ok')
else:
    print('ok')







