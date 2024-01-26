nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

the_best_list = [nice_list[i][i2] for i in range(2) for i2 in range(3)]
the_best_list1 = [the_best_list[i3][i4] for i3 in range(6) for i4 in range(3)]
print("Ответ:", the_best_list1)

# зачтено
