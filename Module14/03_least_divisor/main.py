def smallest_divisor(n):
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            print('Наименьший делитель, отличный от единицы:', divisor)
            break


n = int(input('Введите натуральное число, большее единицы: '))
if n <= 1:
    print('Ошибка ввода. Введите число, большее единицы')
else:
    smallest_divisor(n)

# зачтено
