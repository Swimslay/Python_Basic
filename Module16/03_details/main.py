shop = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]


def num_of_details():
    detail = input("Название детали: ")
    total_details = 0
    total_cost = 0
    for i in shop:
        if i[0] == detail:
            total_details += 1
            total_cost += i[1]
    if total_details == 0:
        print("Таких деталей не найдено")
    else:
        print(f"Кол-во деталей — {total_details}\nОбщая стоимость — {total_cost}")


num_of_details()
