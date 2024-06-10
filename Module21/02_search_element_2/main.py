site = {
    "html": {
        "head": {"title": "Мой сайт"},
        "body": {
            "h2": "Здесь будет мой заголовок",
            "div": "Тут, наверное, какой-то блок",
            "p": "А вот здесь новый абзац",
        },
    }
}


def finder(struct, key, deep):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        deep -= 1
        if deep > 0:
            if isinstance(sub_struct, dict):
                result = finder(sub_struct, key, deep)
                if result:
                    break
    else:
        result = None

    return result


user_key = input("Введите искомый ключ: ")
deep_answer = input("Хотите ввести максимальную глубину? Y/N: ").upper()
if deep_answer == "Y":
    deep = int(input("Введите максимальную глубину: "))
elif deep_answer == "N":
    deep = 999999999999999999999
else:
    print("Ошибка ввода.")
    exit()

value = finder(site, user_key, deep)
print("Значение ключа:", value)

# зачтено
