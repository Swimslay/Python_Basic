films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
like_films = []
count_films = int(input('Сколько фильмов хотите добавить? '))
count = 0

for film1 in range(count_films):
    film = input('Введите название фильма: ')
    for film2 in films:
        if film2 == film:
            like_films.append(film2)
            break
        count += 1
        if len(films) == count:
            print('Ошибка: фильма', film, 'у нас нет :(')

print('Ваш список любимых фильмов: ', end='')
for i in like_films:
    print(i, end=' ')
