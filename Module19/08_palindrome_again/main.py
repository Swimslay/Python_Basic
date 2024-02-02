text = input("Введите строку: ")
palin = dict()
count_odd = 0


def odds(text, count_odd):
    count_odd = 0
    for i_palin in text:
        if i_palin in palin:
            palin[i_palin] += 1
        else:
            palin[i_palin] = 1
    for i in palin.values():
        if i % 2 == 1:
            count_odd += 1
    return count_odd


if odds(text, count_odd) > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")

# зачтено
