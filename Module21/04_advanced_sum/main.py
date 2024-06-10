def adv_sum(*args):
    summ = 0
    for index in args:
        if isinstance(index, list):
            args = index
            summ += adv_sum(*args)
        else:
            summ += index

    return summ

print(adv_sum(1, 2, 3, 4, 5))