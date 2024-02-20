def is_prime(text):
    dividers = []
    for i in range(2, len(text) + 1):
        count = 0
        for j in range(2, len(text) + 1):
            if i % j == 0:
                count += 1
        if count <= 1:
            dividers.append(i)
    return dividers
def simpl(text):
    simple_list = [text[i1] for i1 in is_prime(text) if i1 < len(text)]
    return simple_list

print(simpl('О Дивный Новый мир!'))
