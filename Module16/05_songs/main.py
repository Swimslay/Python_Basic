violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
def total_time():
    num_of_songs = int(input('Сколько песен выбрать? '))
    time = 0
    for _ in range(num_of_songs):
        song = input(f'Название {_ + 1}-й песни: ')
        for i in range(len(violator_songs)):
            if song == violator_songs[i][0]:
                time += violator_songs[i][1]
    print(f'\nОбщее время звучания песен: {round(time, 2)} минуты')


total_time()
