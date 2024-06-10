def help_fast_sort(list_):
    low_list = list()
    same_list = list()
    high_list = list()
    step = list_[-1]
    for index in list_:
        if index < step:
            low_list.append(index)
        elif index == step:
            same_list.append(index)
        else:
            high_list.append(index)
    return low_list, same_list, high_list


def fast_sort(list1):
    if len(list1) <= 1:
        return list1
    low_list, same_list, high_list = help_fast_sort(list1)

    sorted_low = fast_sort(low_list)
    sorted_high = fast_sort(high_list)

    return sorted_low + same_list + sorted_high


print(fast_sort([5, 8, 9, 4, 2, 9, 1, 8]))

# зачтено
