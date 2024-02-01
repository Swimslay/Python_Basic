times = int(input('Введите количество пар слов: '))
diction = dict()
for i in range(times):
    word = input('Введите слово: ').lower()
    word_syn = input('Введите синоним: ').lower()
    diction[word] = word_syn
    diction[word_syn] = word
print()

user_word = input('Введите слово: ').lower()
if user_word in diction:
    answer = diction[user_word]
    print('Синоним:', answer)
else:
    print('Такого слова в словаре нет')