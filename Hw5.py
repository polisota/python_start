import Hw5Funcs as h5f

# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
print('Задача 26: ')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(h5f.MulRec(a, b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую
# сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
print('Задача 28: ')
a1 = int(input('Введите число a: '))
b1 = int(input('Введите число b: '))
print(h5f.SumRec(a1, b1))