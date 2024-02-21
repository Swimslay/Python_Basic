n = int(input("Количество чисел: "))
arr = []
for i in range(n):
    arr.append(int(input("Число: ")))
    i = 0
while arr != arr[::-1]:
    arr.insert(n, arr[i])
    i += 1
print(i)
print(*arr[:i][::-1])
