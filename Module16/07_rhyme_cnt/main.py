total_players = int(input("Кол-во человек: "))
rhyme_number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {rhyme_number}-й человек")
players = list(range(1, total_players + 1))
removed_player = 0

while len(players) != 1:
    print(f"\nТекущий круг людей: {players}")
    start = removed_player % len(players)
    removed_player = (start + rhyme_number - 1) % len(players)
    print(f"Начало счёта с номера {players[start]}")
    print(f"Выбывает человек под номером {players[removed_player]}")
    players.remove(players[removed_player])
print(f"\nОстался человек под номером {players[0]}")
