document = input('Введите название файла: ')
if (document.startswith('@') or document.startswith('№') or document.startswith('$') or document.startswith('%')
    or document.startswith('^') or document.startswith('&') or document.startswith('\ ')
    or document.startswith('*') or document.startswith('(') or document.startswith(')')):
    print('Ошибка: название начинается на один из специальных символов.')
    exit()

if document.endswith('.txt') or document.endswith('.docx'):
    print('Файл назван верно')
    exit()

print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')