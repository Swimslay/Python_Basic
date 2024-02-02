times = int(input("Введите кол-во заказов: "))
names = dict()
for _ in range(times):
    order = input("Введите заказ: ")
    name, pizza, pizzas_count = order.rsplit(maxsplit=3)
    pizzas_count = int(pizzas_count)
    if name not in names:
        names[name] = {pizza: pizzas_count}
    else:
        if pizza not in names[name]:
            names[name] |= {pizza: pizzas_count}
        else:
            names[name][pizza] += pizzas_count
for name, order in sorted(names.items()):
    print(f"{name}:")
    for pizza, pizzas_count in sorted(order.items()):
        print("    ", pizza, pizzas_count)

# зачтено
