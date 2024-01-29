text = input('Введите строку: ')
words = text.split()
max_len = 0
for i in range(len(words)):
    current_len = len(words[i])
    if current_len >= max_len:
        max_len = current_len
        max_word = words[i]
print('Самое длинное слово:', max_word)
print('Длина этого слова:', max_len)