text = input('Введите строку: ').lower()
list_text = text.split()

print('Результат:', end=' ')

for i in range(len(list_text)):
    word_upper = list_text[i][0].upper()
    word_upper = ''.join([word_upper, list_text[i][1:]])
    print(word_upper, end=' ')