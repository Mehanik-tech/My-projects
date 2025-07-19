import g4f

name = input('Введи имя')

while True:
    user = input(name+': ')
    res = g4f.ChatCompletion.create(
        model = ('gpt-4'),
        messages = [{
            'role': 'user',
            'content': user}])

    print('Chat gpt: '+res)
