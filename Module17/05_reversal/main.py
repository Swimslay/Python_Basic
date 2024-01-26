text = input("Введите строку: ")
reversal = ""
new_text = ""
count = 0
count1 = 0

for i in text:
    if i != "h":
        count += 1
    else:
        break

new_text = text[count:]
new_text_1 = new_text[::-1]

for i1 in new_text_1:
    if i1 != "h":
        count1 += 1
    else:
        break

reversal = new_text_1[count1 + 1 : -1]

print("Развёрнутая последовательность между первым и последним h:", reversal)

# зачтено
