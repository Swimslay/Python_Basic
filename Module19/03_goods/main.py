goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

codes = dict()
multipl = 1
summ_multi = 0
number = 12345
for i2 in range(4):
    multipl = 1
    summ_multi = 0
    for i1 in range(len(store[str(number)])):
        first_total_price = store[str(number)][i1].values()
        for i in first_total_price:
            multipl *= int(i)
        summ_multi += multipl
        multipl = 1
    codes[str(number)] = 'общая стоимость {0} рубля'.format(str(summ_multi))
    number += 11111
print(codes)
