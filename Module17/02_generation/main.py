N = int(input("Введите длину списка: "))
new_list = [(1 if number % 2 == 0 else number % 5) for number in range(N)]
print("Результат:", new_list)

# зачтено
