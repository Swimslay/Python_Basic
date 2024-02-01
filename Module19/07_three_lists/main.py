array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# array_1 = set(array_1)
# array_2 = set(array_2)
# array_3 = set(array_3)
# inter1 = array_1.intersection(array_2, array_3)
# print('Элементы, которые есть в каждом списке:', inter1)

print('Элементы, которые есть в каждом списке: ', end='')
for i in array_1:
    if (i in array_2) and (i in array_3):
        print(i, end=' ')
print()

# array_1 = set(array_1)
# array_2 = set(array_2)
# array_3 = set(array_3)
# inter2 = array_1.difference(array_2, array_3)
# print('Элементы из первого списка, которых нет во втором и третьем списках:', inter2)

print('Элементы из первого списка, которых нет во втором и третьем списках: ', end='')
for i in array_1:
    if not (i in array_2) and not (i in array_3):
        print(i, end=' ')
