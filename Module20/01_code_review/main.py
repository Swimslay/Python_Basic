students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    for i in dict:
        lst += (dict[i]['interests'])
    string1 = [dict[i]['surname'] for i in dict]
    string = ''.join(string1)
    cnt = len(string)
    return lst, cnt

pairs = []
for i1 in students:
    pairs.append((i1, students[i1]['age']))

print('Полный список интересов всех студентов:', f(students)[0])
print('Общая длина всех фамилий студентов:', f(students)[1])
print('Список пар "ID студента — возраст":', pairs)