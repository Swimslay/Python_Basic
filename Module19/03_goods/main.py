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

# TODO:
#  - Идём циклом for по ключам словаря, т.е. по goods.keys(). Переменная цикла - i_name. В цикле:
#      - Объявляем переменную количества товаров total_quantity, равную 0
#      - Объявляем переменную суммы товаров total_cost, равную 0
#      - Идём циклом for по store[goods[i_name]] (Т.е. по получаем значение в goods, лежащее по ключу i_name,
#      это будет айди. А затем получаем значение из store по ключу, которым является айди полученный ранее.
#      Тем самым мы получаем нужный список с товарами). Переменная цикла - j_good. В цикле:
#          - total_quantity увеличиваем на j_good["quantity"]
#          (т.е. получаем у текущего объекта его кол-во по ключу "quantity")
#          - total_cost увеличиваем на произведение j_good["price"] и j_good["quantity"]
#          (т.е. получаем у текущего объекта его кол-во по ключу "quantity", также получаем цену текущего объекта
#          и перемножаем их)
#      - Печатаем шаблон "{} - {} шт, стоимость {} руб", в котором через .format() подставляем
#      переменные i_name, total_quantity и total_cost
for i_name in goods.keys():
    total_quantity = 0
    total_cost = 0
    for j_good in store[goods[i_name]]:
        total_quantity += j_good['quantity']
        total_cost += j_good['price'] * j_good['quantity']
    print('{0} - {1} шт, стоимость {2} руб'.format(i_name, total_quantity, total_cost))