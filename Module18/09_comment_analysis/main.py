def count_uppercase_lowercase(symbols):
    count_upper = 0
    count_lower = 0
    for i in range(len(symbols)):
        if (symbols[i] != ' ') and (symbols[i] != ',') and (symbols[i] != '.') and (symbols[i] != '!'):
            if symbols[i] == symbols[i].upper():
                count_upper += 1
            if symbols[i] == symbols[i].lower():
                count_lower += 1
    return count_upper, count_lower

text = input("Введите строку для анализа: ")
count_upper, count_lower = count_uppercase_lowercase(text)
print("Количество заглавных букв:", count_upper)
print("Количество строчных букв:", count_lower)
