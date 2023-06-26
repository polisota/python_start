import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()
        for contact in data:
            print(contact, end = '')
    input('\nНажмите любую клавишу.')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Введите фамилию: ').replace(' ', '').upper() + ' '
        res += input('Введите имя: ').replace(' ', '').upper() + ' '
        res += input('Введите номер телефона: ').replace(' ', '').replace(')', '').replace('(', '').replace('-', '')
        file.write('\n' + res)
    input('\nКонтакт создан. Нажмите любую клавишу.')

def search_contact(file_name):
    os.system('CLS')
    target = input('Введите имя для поиска: ').upper()
    with open(file_name, 'r') as file:
        contacts = file.readlines()        
        for contact in contacts:
            if target in contact:
                print(contact)
                break
            else:
                print('Такого контакта нет.')
    input('\nПоиск завершен. Нажмите любую клавишу.')

def change_contact(file_name):
    show_contacts(file_name)
    os.system('CLS')
    target = input('Введите текст для замены: ').upper()
    target += ' '
    with open(file_name, 'r') as file:
        contacts = iter(file.readlines())
    with open(file_name, 'w') as file:    
        for contact in contacts:                
            if target not in contact:
                file.write(contact)
            else:
                temp = contact.replace(target, input('Введите новые данные: ').upper() + ' ')
                file.write(temp)

    input('\nИзменение завершено. Нажмите любую клавишу.')

def delete_contact(file_name):
    os.system('CLS')
    target = input('Введите имя для поиска: ').upper()
    with open(file_name, 'r') as file: 
        contacts = iter(file.readlines())
    with open(file_name, 'w') as file:    
        for contact in contacts:                
            if target not in contact:
                file.write(contact)  
    input('\nУдаление завершено. Нажмите любую клавишу.')

def drawing():
    print('1 - просмотреть контакты')
    print('2 - добавить контакт')
    print('3 - искать контакт')
    print('4 - изменить контакт')
    print('5 - удалить контакт')
    print('6 - выход')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input('Введите число от 1 до 6\n'))
        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            change_contact(file_name)
        elif user_choice == 5:
           delete_contact(file_name)
        elif user_choice == 6:
            print('Хорошего дня!')
            return
        else:
            print('Введен неверный код')