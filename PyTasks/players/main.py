players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# result = [(i_name[0], i_name[1], *i_elem) for i_name, i_elem in players.items()]
result = [(i_name + i_elem) for i_name, i_elem in players.items()]
print('результат:', result)
