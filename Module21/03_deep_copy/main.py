import copy

site = {
    "html": {
        "head": {"title": "Куплю/продам телефон недорого"},
        "body": {"h2": "У нас самая низкая цена на телефон", "div": "Купить", "p": "продать"},
    }
}


def changer(struct, name):
    for key, sub_struct in struct.items():
        if isinstance(sub_struct, dict):
            changer(sub_struct, name)
        else:
            str_sub_struct = str(sub_struct)
            if "телефон" in str_sub_struct:
                struct[key] = str_sub_struct.replace("телефон", name)

    return struct


sites_list = []
counters = int(input("Введите количество сайтов: "))
for i in range(counters):
    site1 = copy.deepcopy(site)
    name = input("Введите название продукта для нового сайта: ")
    value = changer(site1, name)
    sites_list.append(value)
    print(sites_list)

# зачтено
