def numbers(n):
    if n == 0:
        return 1
    cur_num = numbers(n - 1)
    print(n)
    return cur_num

num = int(input('Введите число: '))
numbers(num)