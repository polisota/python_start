# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве.

first = list(map(int, input('Введите элементы первого массива через пробел: ').split()))
second = list(map(int, input('Введите элементы второго массива через пробел: ').split()))

result = [i for i in set(first) if i not in second]
print(result)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. 

list1 = list(map(int, (input('Введите элементы через пробел: ')).split()))
c = 0
for i in range(1, len(list1) - 1):
    if (list1[i] > list1[i - 1]) & (list1[i] > list1[i + 1]):
        c += 1
print(c)

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

from random import randint
list = list(randint(1, 10) for i in range(int(input('Введите количество элементов: '))))
print(list)
count = 0
temp = []
for i in range(len(list)):
    if list[i] in temp:
        count += 1
        temp.remove(list[i])
    else:
        temp.append(list[i])
print(count)

# Задача 45

def SumOfDiv(n):
    sum = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum

n = int(input('Введите число: '))

for i in range(2, n):
    partner = SumOfDiv(i)
    if i == SumOfDiv(partner) and i > partner:
        print(f'{i} - {partner}')


