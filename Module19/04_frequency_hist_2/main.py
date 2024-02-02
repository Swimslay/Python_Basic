text = input("Введите текст: ").lower()
hist = dict()

for i_hist in text:
    if i_hist in hist:
        hist[i_hist] += 1
    else:
        hist[i_hist] = 1

for i_sym in hist.keys():
    print(i_sym, ":", hist[i_sym])

count = max(hist.values())

reverse = []
for i in range(1, count + 1):
    for sym in hist.keys():
        if hist[sym] == i:
            reverse.append(sym)
    print(i, ":", reverse)
    reverse = []

# зачтено
