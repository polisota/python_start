# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n

text = 'a a a b c a a d c d d'
myList = text.split()
dictionary = {}
count = str()
for letter in myList:
    if letter in dictionary.keys():
        dictionary[letter] += 1
        count += f'{letter}_{dictionary[letter]} '
    else:
        dictionary[letter] = 0
        count += f'{letter} '
print(count)

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

text1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
my_list = text1.upper().split()
length = len(set(my_list))
print(length)
