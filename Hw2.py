# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
print('Задача 10:')
n = int(input('Введите количество монет: '))
count1 = 0
for i in range(n):    
    side = int(input("Идентифицируйте монеты: "))
    if side == 1:
        count1 += 1
if n - count1 > count1:
    print(count1)
else:
    print(n-count1)

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
print('Задача 12:')
sum = int(input('Введите сумму чисел: '))
pr = int(input('Введите произведение чисел: '))
r = range(0, sum)
for i in r:
    if i * (sum - i) == pr:
        print (f"Первое число {i}, Второе число {sum - i}")
        # break

# Требуется вывести все целые степени двойки, не превосходящие числа N.
print('Задача 14:')
a = int(input('Введите число: '))
i = 1
while i <= a:
    print(i)
    i *= 2
