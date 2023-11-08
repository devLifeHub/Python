violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_song = int(input('Сколько песен выбрать? '))
total_song = 0

for i in range(1, count_song + 1):
    name_song = input('Название {}-ой песни: '.format(i))
    total_song += violator_songs[name_song]
print('Общее время звучания песен: {:.2f}'.format(total_song))