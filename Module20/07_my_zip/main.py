text = "abcd"
tup = (10, 20, 30, 40)


def zip_analog(text, tup):
    count = min(len(text), len(tup))
    for i in range(count):
        print((text[i], tup[i]))


zip_analog(text, tup)

# TODO:
#  Генератор использует ключевое слово yield или используется генераторное выражение.
#  Поэтому код должен выглядеть так:
string = "abcd"
nums_tpl = (10, 20, 30, 40)


def zip_analog(text, tup):
    count = min(len(text), len(tup))
    for i in range(count):
        yield text[i], tup[i]


answer = zip_analog(string, nums_tpl)
print(answer)
for x in answer:
    print(x)

# TODO:
#  Либо так:
string = "abcd"
nums_tpl = (10, 20, 30, 40)
answer = ((string[i], nums_tpl[i]) for i in range(min(len(string), len(nums_tpl))))
print(answer)
for x in answer:
    print(x)
