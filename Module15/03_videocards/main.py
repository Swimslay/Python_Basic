cards_count = int(input('Введите количество видеокарт: '))
old_list = []
new_list = []
max_card = 0
for i in range(1, cards_count + 1):
    print('Видеокарта', i, end=' ')
    card = int(input(': '))
    old_list.append(card)
    if card >= max_card:
        max_card = card

for i1 in old_list:
    if i1 != max_card:
        new_list.append(i1)

print('Старый список видеокарт:', old_list)
print('Новый список видеокарт:', new_list)

# зачтено
