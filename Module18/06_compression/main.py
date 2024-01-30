text = input("Введите строку: ")
count = 1
new_text = ""

for i in range(len(text)):
    if i < len(text) - 1:
        if text[i] == text[i + 1]:
            count += 1
        else:
            new_text = "".join([new_text, text[i], str(count)])
            count = 1
    else:
        new_text = "".join([new_text, text[i], str(count)])

print("Закодированная строка:", new_text)

# зачтено
