x = float(input('Введите координату икс: '))
y = float(input('Введите координату игрек: '))
r = int(input('Введите радиус окружности: '))
if x ** 2 + y ** 2 <= r ** 2:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')

# зачтено
