list1 = [1, 4, -3, 0, 10]
print('Начальный список:', list1)
for index in range(len(list1)):
    for index1 in range(len(list1) - index - 1):
        if list1[index1] > list1[index1 + 1]:
            list1[index1], list1[index1 + 1] = list1[index1 + 1], list1[index1]

print('Сортированный список', list1)

# зачтено
