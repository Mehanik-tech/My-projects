import g4f

history = []

while True:
    user_input = input("Ты: ")
    history.append({"role": "user", "content": user_input})

    res1 = g4f.ChatCompletion.create(
        model='gpt-4',
        messages=history
    )
    print("chatGpt1:", res1)
    history.append({"role": "assistant", "content": res1})

    res2 = g4f.ChatCompletion.create(
        model='gpt-4',
        messages=history
    )
    print("chatGpt2:", res2)
    history.append({"role": "assistant", "content": res2})
