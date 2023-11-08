num_orders = int(input('Введите количество заказов: '))
orders = {}

for i_order in range(num_orders):
    order = input('{}-й заказ: '.format(i_order + 1)).split()
    buyer, pizza, quantity = order[0], order[1], int(order[2])

    if buyer in orders:
        if pizza in orders[buyer]:
            orders[buyer][pizza] += quantity
        else:
            orders[buyer][pizza] = quantity
    else:
        orders[buyer] = {pizza: quantity}

print()
for buyer, pizza_info in sorted(orders.items()):
    print('{}:'.format(buyer))
    for pizza, quantity in sorted(pizza_info.items()):
        print('\t {}: {}'.format(pizza, quantity))
