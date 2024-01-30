alphabet = "abcdefghijkolmnpqrstuvwxyz"
alphabet_upper = alphabet.upper()
numbers = "0123456789"
count = 0
count1 = 0

while True:
    password = input("Придумайте пароль: ")
    for i in range(len(numbers)):
        if numbers[i] in password:
            count += 1
    for i1 in range(len(alphabet_upper)):
        if alphabet_upper[i1] in password:
            count1 += 1
    if len(password) >= 8 and count >= 3 and count1 >= 1:
        print("Это надёжный пароль!")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

# зачтено
