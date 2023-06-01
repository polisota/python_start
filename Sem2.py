print('Задача 13: ')
count = 0
max = 0
n = int(input("Input a quantity of days: "))
for dayCount in range(n) :
    day = int(input("Input a temperature of a day: "))
    if day > 0 :
        count += 1
    elif count >= max :
        max = count
        count = 0
if count > max :
    max = count
print('Max quantity of warm days is ', max)


print('Задача 9:')
a = int(input("Введите число: "))
res = 1
while a != 0:
    res *= a
    a -= 1
print(res)


print('Задача 11:')
number = int(input("Введите число: "))
f1 = 0
f2 = 1
count = 1
while f2 < number:    
    f1 = f2
    f2 = f2 + f1
    count += 1
if f2 != number:
    print('-1')
else:
    print(count)


print('Задача 15: ')
max1 = 0
min = 0
n = int(input("Введите кол-во арбузов: "))
for wm in range(n) :
    weight = int(input("Введите вес каждого арбуза: "))
    if max1 == 0:
        max1 = weight
        min = weight
    elif weight > max1:
        max1 = weight
    else:
        min = weight
print(min, max1)