def summa(n):
    x = 0
    count = 0
    while n > 0:
        x = n % 10
        n //= 10
        count += x
    print('Сумма чисел:', count)
    return count

def number_count(n):
    count1 = 0
    while n > 0:
        n //= 10
        count1 += 1
    print('Количество цифр в числе:', count1)
    return count1

n = int(input('Введите положительное число: '))
if n <= 0:
    print('Ошибка ввода. Введите положительное число')
else:
    difference = summa(n) - number_count(n)
    print('Разность суммы и количества цифр:', difference)