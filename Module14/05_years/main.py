def triple_number(year):
    number1 = year % 10
    number2 = year // 10 % 10
    number3 = year // 100 % 10
    number4 = year // 1000
    if (number1 == number2 == number3 != number4) or (number1 == number2 == number4 != number3) or (number1 == number3 == number4 != number2) or (number2 == number3 == number4 != number2):
        return True

year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))
print('Годы от', year1, 'до', year2, 'с тремя одинаковыми цифрами:')
for year in range(year1, year2 + 1):
    if triple_number(year):
        print(year)
