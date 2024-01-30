adress = input("Введите IP: ")
numbers = "0123456789"

if adress.count(".") != 3:
    print("Адрес — это четыре числа, разделённые точками.")
    exit()
else:
    adress_list = adress.split(".")
    for i in range(len(adress_list)):
        for i1 in range(len(adress[i])):
            if not adress_list[i][i1] in numbers:
                print(adress_list[i], "— это не целое число.")
                exit()
        if int(adress_list[i]) > 255:
            print(adress_list[i], "превышает 255")
            exit()

print("IP - адрес корректен")

# зачтено
