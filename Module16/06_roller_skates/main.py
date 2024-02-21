skates = []
people = []
counter = 0

num_skates = int(input("Кол-во коньков: "))

for i in range(num_skates):
    skates.append(int(input(f"Размер {i + 1}-й пары: ")))
num_people = int(input("\nКол-во людей: "))

for i in range(num_people):
    people.append(int(input(f"Размер ноги {i + 1}-го человека: ")))

for skate in skates:
    if skate in people:
        counter += 1
        people.remove(skate)

print(f"Наибольшее кол-во людей, которые могут взять ролики: {counter}")
print(skates, people)
