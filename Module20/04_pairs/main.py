import random

original_list = [random.randint(1, 99999) for i in range(10)]
new_list = []
for i1 in range(0, len(original_list), 2):
    new_list.append((original_list[i1], original_list[i1 + 1]))

print("Оригинальный список:", original_list)
print("Новый список:", new_list)

# зачтено
