n = int(input("Введите количество элементов в списке: "))
k = int(input("Введите сдвиг: "))
list1 = []
list2 = []

for _ in range(n):
    number = int(input("Введите элемент: "))
    list1.append(number)

list2 = list1[-k:] + list1[:-k]

print("Изначальный список", list1)
print("Сдвинутый список", list2)

# зачтено
