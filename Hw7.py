# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может
# состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

print('Задача 34:')
poem = input('Введите стих: ')
# poem = 'пара-рам рам-пам-папам па-ра-па-да'
print(poem)
vovels = set('ёуеыаоэяию')
poem_list = poem.lower().split()
res = []
print(poem_list)
for elem in poem_list:
    temp = 0
    for letter in elem:
        if letter in vovels:
            temp += 1
    res.append(temp)
res_set = set(res)
if len(res_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

list = poem.lower().split()
f = lambda x: sum(1 for i in x if i in 'ёуеыаоэяию')
temp1 = f(list[0])
if all([f(i) == temp1 for i in list]):
    print('Парам пам-пам')
else:
    print('Пам парам')

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows
# и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация
# строк и столбцов идет с единицы (подумайте, почему не с нуля).

print('Задача 36:')

def print_operation_table(operation, num_rows = 6, num_сolumns = 6):
    list = [[operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_сolumns + 1)]
    for i in list:
        print(i)
rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x * y, rows, columns)