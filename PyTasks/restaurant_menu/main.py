menu = 'утиное филе;фланк-стейк;банановый пирог;плов'

menu_list = menu.split(';')
menu_str = ', '.join(menu_list)

print('Доступное меню:', menu)
print('На данный момент в меню есть:', menu_str)
