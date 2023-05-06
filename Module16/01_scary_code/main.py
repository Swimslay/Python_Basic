a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
count = 0
count1 = 0

a.extend(b)
for i_a in a:
    if i_a == 5:
        count += 1
        a.remove(i_a)

a.extend(c)
for i_a in a:
    if i_a == 3:
        count1 += 1

print('Количество цифр 5 при первом объединении:', count)
print('Количество цифр 3 при втором объединении:', count1)
print('Итоговый список:', a)