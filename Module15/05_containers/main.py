container_count = int(input('Введите количество контейнеров: '))
container_list = []
count = 1

while container_count > 0:
    weight = int(input('Введите вес контейнера (не больше 200): '))
    if weight > 200:
        print('Ошибка. Вес не может быть больше 200')
    else:
        container_count -= 1
        container_list.append(weight)

new_weight = int(input('Введите вес нового контейнера: '))

for i in container_list:
    if i >= new_weight:
        count += 1

print('Номер, который получит новый контейнер:', count)

# зачтено
