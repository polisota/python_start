# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

print('Задача 30:')
a = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите шаг прогрессии: '))
n = int(input('Введите количество элементов прогрессии: '))
lis = []
for i in range(n):
    temp = a + i * d
    lis.append(temp)
print(lis)

# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

print('Задача 32:')
from random import randint
list1 = list(randint(1, 100) for i in range(15))
print(list1)
min = int(input('Введите минимум диапазона: '))
max = int(input('Введите максимум диапазона: '))
list2 = []
for i in range(len(list1)):
    if list1[i] <= max and list1[i] >= min:
        list2.append(i)
print(list2)