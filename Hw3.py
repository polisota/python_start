# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов
# в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X
print('Задача 16:')
n = int(input('Введите количество элементов списка: '))
myList = [int(input('Введите элемент списка: ')) for i in range(n)]
# myList = list(range(1, n + 1)) # по условию выглядит будто нужно заполнить список числами от 1 до n, это ведь не так?
x = int(input('Введите число: '))
count = 0
for i in myList:
    if i == x:
        count += 1
print(myList, count)

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
print('Задача 18:')
m = int(input('Введите количество элементов списка: '))
k = int(input('Введите искомое число: '))
from random import randint
randomList = [randint(1, 100) for i in range(m)]
print(randomList)
min = randomList[0]
for i in range(1, m):
    if abs(k - randomList[i]) < abs(k - min):
        min = randomList[i]
print(min)


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; 
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков. 
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
print('Задача 20:')
point1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
point2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
point3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
point4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
point5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
point8 = ['J', 'X', 'Ш', 'Э', 'Ю']
point10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
word = input('Введите слово: ').upper()
wordList = list(word)
sum = 0
for i in range(len(wordList)):
    for j in range(len(point1)):
        if wordList[i] == point1[j]:
            sum += 1
    for q in range(len(point2)):
        if wordList[i] == point2[q]:
            sum += 2
    for w in range(len(point3)):
        if wordList[i] == point3[w]:
            sum += 3
    for e in range(len(point4)):
        if wordList[i] == point4[e]:
            sum += 4
    for r in range(len(point5)):
        if wordList[i] == point5[r]:
            sum += 5
    for t in range(len(point8)):
        if wordList[i] == point8[t]:
            sum += 8
    for y in range(len(point10)):
        if wordList[i] == point10[y]:
            sum += 10
print(sum)
    