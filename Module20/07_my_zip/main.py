text = 'abcd'
tup = (10, 20, 30, 40)

def zip_analog(text, tup):
    count = min(len(text), len(tup))
    for i in range(count):
        print((text[i], tup[i]))

zip_analog(text, tup)