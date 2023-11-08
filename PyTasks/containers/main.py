num_containers = int(input('Введите количество контейнеров: '))
list_container = []
new_num_container = 0

for container in range(num_containers):
    while True:
        weight_container = int(input('Введите вес контейнера: '))
        if (weight_container <= 200) and (weight_container >= 0):
            list_container.append(weight_container)
            break
        print('Введите корректный вес контейнера от 0 до 200')

list_container.sort(reverse=True)

while True:
    print()
    new_weight_container = int(input('Введите вес нового контейнера: '))
    if (new_weight_container <= 200) and (new_weight_container >= 0):
        break
    print('Введите корректный вес нового контейнера от 0 до 200')

for i in range(len(list_container)):
    if list_container[i] < new_weight_container:
        list_container.insert(i, new_weight_container)
        new_num_container = i
        break
print('Номер, который получит новый контейнер:', new_num_container + 1)
