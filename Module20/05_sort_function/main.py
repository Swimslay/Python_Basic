def tpl_sort(tpl):
    flag = True
    for i in tpl:
        if i != int(i):
            flag = False
            return tpl
            break
    if flag == True:
        return tuple(sorted(tpl))

tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))