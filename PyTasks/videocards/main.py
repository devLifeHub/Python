# Количество видеокарт: 5
# 1 Видеокарта: 3070
# 2 Видеокарта: 2060
# 3 Видеокарта: 3090
# 4 Видеокарта: 3070
# 5 Видеокарта: 3090
#
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]

# list_video_card = [3070, 2060, 3090, 3070, 3090]
# new_list_video_card = list_video_card[:]
# max_number = max(list_video_card)
#
# for card in range(len(list_video_card)):
#     # print(list_video_card[card])
#     print(card, 'Видеокарта:', list_video_card[card])
#     # if card != max_number:
#     #     new_list_video_card.append(list_video_card[card])
#     new_list_video_card.remove(max_number)
#
# print(new_list_video_card)

list_video_card = [3070, 2060, 3090, 3070, 3090]
new_list_video_card = []
max_number = max(list_video_card)

for num in range(len(list_video_card)):
    print(num + 1, 'Видеокарта:', list_video_card[num])

for card in list_video_card:
    if card != max_number:
        new_list_video_card.append(card)

print()
print('Старый список видеокарт:', list_video_card)
print('Новый список видеокарт:', new_list_video_card)



