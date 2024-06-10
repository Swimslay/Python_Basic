def list_of_lists(list_):
    new_list = list()
    for index in list_:
        if isinstance(index, list):
            list_ = index
            new_list += list_of_lists(list_)
        else:
            new_list.append(index)

    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(list_of_lists(nice_list))

# зачтено
