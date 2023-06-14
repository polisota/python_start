import Sem5Funcs as s5f
print(s5f.LastFibo(7))

a = [1, 2, 3, 5, 5]
for i in range(len(a)):
    if a[i] == max(a):
        a[i] = min(a)
print(a)

num = int(input('Введите число: '))
print(s5f.IsSimple(num))

number = int(input('Введите число: '))
print(s5f.ReverseRange(number))