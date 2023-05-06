one_class = []

first_class = list(range(160, 176 + 1, 2))
second_class = list(range(162, 180 + 1, 3))

one_class.extend(first_class)
one_class.extend(second_class)

one_class = sorted(one_class)

print('Отсортированный список учеников:', one_class)