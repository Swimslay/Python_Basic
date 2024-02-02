violator_songs = {
    "World in My Eyes": 4.86,
    "Sweetest Perfection": 4.43,
    "Personal Jesus": 4.56,
    "Halo": 4.9,
    "Waiting for the Night": 6.07,
    "Enjoy the Silence": 4.20,
    "Policy of Truth": 4.76,
    "Blue Dress": 4.29,
    "Clean": 5.83,
}

time_sum = 0

times = int(input("Введите количество песен: "))
for i in range(times):
    names = input("Введите название песни: ")
    time = violator_songs.get(str(names))
    time_sum += time

print("Общее время звучания песен:", round(time_sum, 2), "минут")

# зачтено
