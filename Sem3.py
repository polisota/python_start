# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

myList = [1, 1, 2, 0, -1, 3, 4, 6, 2, 3]
print(len(set(myList)))

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

n = int(input("Введите сдвиг: ")) % len(myList)
for i in range(n):
    myList.insert(0, myList.pop())
print(myList)

# Напишите программу для печати всех уникальных
# значений в словаре. 

myDict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {"VIII":" S007 "}]
res = []
for item in myDict:
    res.append(list(item.values())[0])
print(set(res))

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 

count = 0
for j in range(1, len(myList)):
    if myList[i] > myList[i-1]:
        count += 1
print(count)

result = [myList[i] for i in range(1, len(myList)) if myList[i] > myList[i-1]]
print(result)