words = {}
while True:
    text = input('Ввод: ')
    if text in words:
        print(f'Слово {text} переводчится как : {words[text]}')
    else:
        print(f'Введите перевод слова : {text}')
        words[text] = input()
    print(words)