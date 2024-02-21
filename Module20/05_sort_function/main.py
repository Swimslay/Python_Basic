def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
            return tpl

    return tuple(sorted(tpl))


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))

# зачтено
