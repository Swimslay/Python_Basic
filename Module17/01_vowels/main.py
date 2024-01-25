text = input('Введите текст: ')
vowel_symbol = [symbol for symbol in text if (symbol == 'а') or (symbol == 'у') or (symbol == 'е') or (symbol == 'о')
                or (symbol == 'э') or (symbol == 'я') or (symbol == 'и') or (symbol == 'ю')]
print('Список гласных букв:', vowel_symbol)
print('Длина списка:', len(vowel_symbol))