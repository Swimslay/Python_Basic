def change(sym1, K):
    if sym1 == ' ' or sym1 == '.':
        return sym1
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    count = alphabet.index(sym1)
    new_count = count + K
    if new_count <= 32:
        return alphabet[new_count]
    else:
        return alphabet[new_count - 33]

text = input('Введите текст: ')
K = int(input('Введите сдвиг: '))
new_text = ''

for i in range(len(text)):
    new_text = new_text + change(text[i], K)

print('Зашифрованное сообщение:', new_text)