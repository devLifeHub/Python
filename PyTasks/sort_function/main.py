def tpl_sort(*args):
    if all(isinstance(x, int) for x in args):
        return tuple(sorted(args))
    else:
        return args


result = tpl_sort(6, 3, -1, 8, 4, 10, -5)
print(result)
