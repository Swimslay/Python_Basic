first_text = input('Введите первую строку: ')
second_text = input('Введите вторую строку: ')

first_slice = first_text[:len(first_text) // 2]
second_slice = first_text[len(first_text) // 2:]
final_text = ''.join([second_slice, first_slice])

if final_text == second_text:
    print('Первая строка получается из второй со сдвигом', len(first_text) // 2)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')