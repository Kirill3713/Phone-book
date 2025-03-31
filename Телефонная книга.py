# Импортируем модуль
import os

# Очищаем экран
os.system("cls")

# Телефонная книга
new_book ={
   'Квам-Дамн': '-79899899889',
   'Лук Скамворкер': '112',
   'Петард Вейпер': '1',
   'Лия Моргала': '+09998765432',
   'Эдуард Скамворкер': '0'}


book_phones = {}
with open('Телефонная книга.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
if not lines[0] == "Книга удалена.":
    for line in lines[1:]:
        line = line.split(':')
        name = line[0].strip()
        phone = line[1].strip()
        book_phones[name] = phone
else:
    choice = input("Ваша телефонная книга удалена, чтобы создать новый контакт нажмите 1: ")
    if choice == "1":
        contact = input("Введите имя контакта: ")
        number = input("Введите новый номер телефона с кодом страны, без пробелов и со знаком плюс: ")
        if number[0] == "+" and len(number) > 1 and len(number) < 15 and number[1:].isdigit():
            book_phones[contact] = number
            print("Новая телефонная книга:")
            for k, v in book_phones.items():
                print(f"{k}: {v}")
        else:
            print("Вы ввели некорректное значение. Измените книгу через меню программы.")
            book_phones["Новый контакт"] = "номер нового контакта"



print("Добро пожаловать в программу телефонной книги!")
print("Чтобы выйти из программы введите Exit, а затем нажмите Enter.")
print("Ваша телефонная книга:")
for k, v in book_phones.items():
    print(f"{k}: {v}")

# Что хочет пользователь?
action = input("Введите нужное значение:\n1 — показать контакт, 2 — добавить новый контакт, 3 — изменить контакт, 4 — удалить контакт, 5 — показать все имена в книге, 6 — показать все номера в книге, 7 - вывести теленфонную книгу полностью, 8 - очистить всю книгу.\n")

book_deleted = False # флажок

# Основной цикл
while action != "Exit" and action != "exit":

    # Показать (1)
    if action == "1":
        a = input("Введите точное имя: ")
        if a in book_phones:
            print(book_phones[a])
        else:
            print("Нет в телефонной книге.")

    # Добавить (2) и изменить (3) (т. к. похожие действия)
    elif action == "2" or action == "3":
        contact = input("Введите имя контакта: ")
        number = input("Введите новый номер телефона с кодом страны, без пробелов и со знаком плюс: ")
        if number[0] == "+" and len(number) > 1 and len(number) < 15 and number[1:].isdigit():
            book_phones[contact] = number
            print("Новая телефонная книга:")
            for k, v in book_phones.items():
                print(f"{k}: {v}")
        else:
            print("Введено некорректное значение!")
    # Удалить (4)
    elif action == "4":
        deleted_contact = input("Введите точное имя контакта, который хотите удалить: ")
        if deleted_contact in book_phones:
            del book_phones[deleted_contact]
            print("Новая телефонная книга:")
            for k, v in book_phones.items():
                print(f"{k}: {v}")
        else:
            print("В Вашей телефонной книге нет такого имени.")

    # Показать все имена в книге (5)
    elif action == "5":
        for k, v in book_phones.items():
            print(f"{k}")

    # Показать все номера в книге (6)
    elif action == "6":
        for k, v in book_phones.items():
            print(f"{v}") 

    # Показать всю телефонную книгу (7)
    elif action == "7":
        print("Ваша телефонная книга:")
        for k, v in book_phones.items():
            print(f"{k}: {v}")

    # Клиент сильно разнервнечился (8)
    elif action == "8":
        os.system("cls")
        print("Вы действительно хотите полностью удалить всю информацию без возможности дальнейшего восстановления?")
        print("Важно!!! Это действие необратимо! Вы можете удалить один контакт нажав в меню цифру четыре.")
        clearall = input("Введите Да (очистить книгу) или Нет:\n")
        if clearall == "Да":
            del book_phones
            print("Книга удалена.")
            book_deleted = True
            book_phones = {}
    # Такого действия нет
    else:
        print("Такого действия нет.")    
        print("Допустимые команды: 1, 2, 3, 4, 5, 6, 7, 8, Exit. Попробуйте, пожалуйста еще раз!")   
    
    action = input("Введите нужное значение:\n1 — показать, 2 — добавить, 3 — изменить, 4 — удалить, 5 — показать все имена в книге, 6 — показать все номера в книге, 7 - вывести теленфонную книгу полностью, 8 - очистить всю книгу, Exit - выйти из программы.\n")
    os.system("cls")
# Сохраняем книгу в файле
    with open('Телефонная книга.txt', 'w', encoding = 'utf-8') as file:

        if book_deleted is True:
            file.write("Книга удалена.")
        else:
            file.write("Телефонная книга:\n")
            for k, v in book_phones.items():
                file.write(f"{k}: {v}\n")

os.system("cls")
print('Спасибо за использование нашей программы! Ваша книга сохранена в файле "Телефонная книга.txt".')