with open(r"C:\Users\abrya\pythonProject\gb-python-ls5\new.txt", 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите текст, для окончания ввода введите пустую строку: ')
        if not line:
            break
        # f.write(line + '\n')
        print(line, file=f)
