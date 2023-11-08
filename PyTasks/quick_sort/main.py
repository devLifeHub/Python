def partition(arr):
    support = arr[-1]
    less_spt, equal_spt, greater_spt = [], [], []

    for num in arr:
        if num < support:
            less_spt += [num]
        elif num == support:
            equal_spt += [num]
        else:
            greater_spt += [num]

    return less_spt, equal_spt, greater_spt


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    less, equal, greater = partition(arr)

    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)

    return sorted_less + equal + sorted_greater


numbers = [5, 8, 9, 4, 2, 9, 1, 8]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
