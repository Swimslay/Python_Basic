def add_name(name):
    phonebook[name] = int(input("Введите номер телефона: "))
    print("Текущий словарь контактов:", phonebook)
    return phonebook


def find_person(name):
    for i in phonebook:
        if name.lower() in i[1].lower():
            print(i[0], i[1], phonebook[i])


phonebook = dict()
while True:
    print("Введите номер действия:")
    print("1 - Добавить контакт")
    choice = int(input("2 - Найти человека"))
    if choice == 1:
        name = input("Введите имя и фамилию нового контакта (через пробел): ")
        name = tuple(name.split())
        if name not in phonebook:
            add_name(name)
        else:
            print("Такой человек уже есть в контактах.")
            print(phonebook)

    elif choice == 2:
        name = input("Введите фамилию: ")
        find_person(name)

    else:
        print("Ошибка ввода")

# зачтено
