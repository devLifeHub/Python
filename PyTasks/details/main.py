shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

product = input('Название детали: ').lower()
total_count = 0
total_cost = 0

for i_item in shop:
    if i_item[0] == product:
        total_count += 1
        total_cost += i_item[1]

if total_count == 0:
    print('Такой детали в списке нет!')
else:
    print('Кол-во деталей -', total_count)
    print('Общая стоимость —', total_cost)