text = input("Введите слово: ")
list_text = list(text)
lenght = len(list_text)
x = True

for i in range(lenght):
    if list_text[lenght - 1 - i] != list_text[i]:
        print("Слово не является палиндромом")
        x = False
        break

if x:
    print("Слово является палиндромом")

# зачтено
