guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]

visit = ""
while visit != "Пора спать":
    print("Сейчас на вечеринке", len(guests), "человек:", guests)
    visit = input("Гость пришел или ушел? ")
    name = input("Имя гостя: ")
    if visit == "пришел":
        if len(guests) < 6:
            print("Привет,", name)
            guests.append(name)
        else:
            print("Прости,", name, ", но мест нет")
            visit = input("Гость пришел или ушел? ")
    if visit == "ушел":
        print("Пока, Ваня")
        guests.remove(name)

print("Вечеринка закончилась, все легли спать")
