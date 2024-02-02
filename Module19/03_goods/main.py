goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}

store = {
    "12345": [
        {"quantity": 27, "price": 42},
    ],
    "23456": [
        {"quantity": 22, "price": 510},
        {"quantity": 32, "price": 520},
    ],
    "34567": [
        {"quantity": 2, "price": 1200},
        {"quantity": 1, "price": 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}


for i_name in goods.keys():
    total_quantity = 0
    total_cost = 0
    for j_good in store[goods[i_name]]:
        total_quantity += j_good["quantity"]
        total_cost += j_good["price"] * j_good["quantity"]
    print("{0} - {1} шт, стоимость {2} руб".format(i_name, total_quantity, total_cost))

# зачтено
