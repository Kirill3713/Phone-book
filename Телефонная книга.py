# Импортируем модули
import os
import datetime
import json
import colorama

# Работа с colorama
colorama.init()
green = colorama.Fore.GREEN
red = colorama.Fore.RED
white = colorama.Fore.WHITE
reset = colorama.Fore.RESET

# Очищаем экран
os.system("cls")

# Создаем функцию
def two_symb_format(n:int) -> str:
    if len(str(n))==1: return f"0{n}"
    else: return n
# Загружаем данные из файла
with open("Data.json", "r", encoding="utf-8") as file:
    data_dict = json.load(file)
# Загружаем книгу из файла
book_phones = {}
with open('Телефонная книга.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
for i in range(1):
    if not lines[0] == "Книга удалена.":
        for line in lines[1:]:
            line = line.split(':')
            name = line[0].strip()
            phone = line[1].strip()
            book_phones[name] = phone
    else:
        # Создаем новую книгу
        choice = input("Ваша телефонная книга удалена, чтобы создать новый контакт нажмите 1: ")
        if choice == "1":
            # Новый номер и контакт
            contact = input("Введите имя контакта: ")
            number = input("Введите новый номер телефона с кодом страны, без пробелов и со знаком плюс: ")
            # День рождения и описание
            dr_choice = input("Хотите ли Вы добавить дату рождения контакта? 1-да, 2-нет ")
            if dr_choice == "1":
                data_dict[contact] = {}
                dr = input("Введите дату в формате дд.мм.гггг: ")
                # Проверка введенных данных
                if len(dr) > 10 or not dr[:2].isdigit() or not dr[3:5].isdigit() or not dr[6:].isdigit() or not dr[2]=="." or not dr[5]=="." or dr.count(".") != 2 or "-" in dr:
                    print("Вы ввели некорректное значение!")
                    break
                dr = list(map(int, dr.split(".")))
                today = list(map(int, str(datetime.date.today()).split("-")[::-1]))

                if dr[0] > 31 or dr[1] > 12 or dr[2] > today[2] or (today[2] == dr[2] and dr[1] > today[1]) or (today[2] == dr[2] and dr[1] == today[1] and today[0] < dr[0]):
                    print("Вы ввели некорректное значение!")
                    break
                data_dict[contact]["dr"] = dr
            describtion_choice = input("Хотите ли Вы добавить описанние контакта? 1-да, 2-нет ")
            if describtion_choice == "1":
                if not contact in data_dict.keys():
                    data_dict[contact] = {}
                data_dict[contact]["info"] = input("Введите описание контакта: ")
            if number[0] == "+" and len(number) > 1 and len(number) < 17 and number[1:].isdigit():
                book_phones[contact] = number
                print("Новая телефонная книга:")
                for k, v in book_phones.items():
                    print(f"{k}: {v}")
            else:
                print("Вы ввели некорректное значение. Измените книгу через меню программы.")
                book_phones["Новый контакт"] = "номер нового контакта"

# Приветствие
print(white + "Добро пожаловать в программу телефонной книги!")
print("Чтобы выйти из программы введите Exit, а затем нажмите Enter.")
print("Ваша телефонная книга:")
for k, v in book_phones.items():
    print(f"{k}: {v}")
    if k in data_dict.keys():
        for key in data_dict[k].keys():
            if key == "dr":
                print(f"Дата рождения: {two_symb_format(data_dict[k][key][0])}.{two_symb_format(data_dict[k][key][1])}.{data_dict[k][key][2]}")
            else:
                print(f"Описание контакта: {data_dict[k][key]}.")

# Что хочет пользователь?
action = input("Введите нужное значение:\n1 — показать контакт, 2 — добавить новый контакт, 3 — изменить контакт, 4 — удалить контакт, 5 — показать все имена в книге, 6 — показать все номера в книге, 7 - вывести теленфонную книгу полностью, проверить день рождения контактов сегодня - 8, 9 - очистить всю книгу.\n" + reset)

# Основной цикл
while action != "Exit" and action != "exit":
    # Показать (1)
    if action == "1":
        name = input("Введите точное имя: ")
        if name in book_phones:
            print(book_phones[name])
        else:
            print("Нет в телефонной книге.")
        if name in data_dict.keys():
            for key in data_dict[name].keys():
                print(data_dict[name][key])
    # Добавить (2) и изменить (3) (т. к. похожие действия)
    elif action == "2" or action == "3":
        contact = input("Введите имя контакта: ")
        number = input("Введите новый номер телефона " + red + "с кодом страны, без пробелов и со знаком плюс: " + reset)
        # День рождения и описание
        dr_choice = input(reset + "Хотите ли Вы изменить дату рождения контакта? 1-да, 2-нет ")
        if dr_choice == "1":
            if action == "2":
                data_dict[contact] = {}
            dr = input("Введите дату в формате " + red + "дд.мм.гггг: " + reset)
            # Проверка введенных данных
            if len(dr) > 10 or not dr[:2].isdigit() or not dr[3:5].isdigit() or not dr[6:].isdigit() or not dr[2]=="." or not dr[5]=="." or dr.count(".") != 2 or "-" in dr:
                input("Вы ввели некорректное значение! Нажмите Enter.")
                continue
            dr = list(map(int, dr.split(".")))
            today = list(map(int, str(datetime.date.today()).split("-")[::-1]))

            if dr[0] > 31 or dr[1] > 12 or dr[2] > today[2] or (today[2] == dr[2] and dr[1] > today[1]) or (today[2] == dr[2] and dr[1] == today[1] and today[0] < dr[0]):
                input("Вы ввели некорректное значение! Нажмите Enter.")
                continue
            data_dict[contact]["dr"] = dr
        describtion_choice = input("Хотите ли Вы изменить описанние контакта? 1-да, 2-нет ")
        if describtion_choice == "1":
            if action == "2":
                data_dict[contact] = {}
            data_dict[contact]["info"] = input("Введите описание контакта: ")
        if number[0] == "+" and len(number) > 1 and len(number) < 17 and number[1:].isdigit():
            book_phones[contact] = number
            print("Новая телефонная книга:")
            for k, v in book_phones.items():
                print(f"{k}: {v}")
                if k in data_dict.keys():
                    for key in data_dict[k].keys():
                        if key == "dr":
                            print(f"Дата рождения: {two_symb_format(data_dict[k][key][0])}.{two_symb_format(data_dict[k][key][1])}.{data_dict[k][key][2]}")
                        else:
                            print(f"Описание контакта: {data_dict[k][key]}.")
        else:
            print("Введено некорректное значение!")
    # Удалить (4)
    elif action == "4":
        deleted_contact = input("Введите точное имя контакта, который хотите удалить: ")
        if deleted_contact in book_phones:
            del book_phones[deleted_contact]
            del data_dict[deleted_contact]
            print("Новая телефонная книга:")
            for k, v in book_phones.items():
                print(f"{k}: {v}")
                if k in data_dict.keys():
                    for key in data_dict[k].keys():
                        if key == "dr":
                            print(f"Дата рождения: {two_symb_format(data_dict[k][key][0])}.{two_symb_format(data_dict[k][key][1])}.{data_dict[k][key][2]}")
                        else:
                            print(f"Описание контакта: {data_dict[k][key]}.")
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
            if k in data_dict.keys():
                for key in data_dict[k].keys():
                    if key == "dr":
                        print(f"Дата рождения: {two_symb_format(data_dict[k][key][0])}.{two_symb_format(data_dict[k][key][1])}.{data_dict[k][key][2]}")
                    else:
                        print(f"Описание контакта: {data_dict[k][key]}.")
    # Напоминалка о днях рождения (8)
    elif action == "8":
        today = list(map(int, str(datetime.date.today()).split("-")[::-1]))
        for contact in data_dict.keys():
            if "dr" in data_dict[contact].keys():
                dr = data_dict[contact]["dr"]
                if today[1] == dr[1]:
                    if today[0] == dr[0]:
                        print(green + f"У контакта {contact} сегодня день рождения! Ему/ей исполняется {today[2]-dr[2]}." + reset)
                    else:
                        if dr[0] > today[0]:
                            print(f"У контакта {contact} скоро день рождения! Осталось " + green + f"{dr[0]-today[0]}" + reset + "дней!")
                else:
                    print(f"У контакта {contact} будет день рождения {dr[0]}.{dr[1]}.{dr[2]}.")

    # Клиент сильно разнервнечился (9)
    elif action == "9":
        os.system("cls")
        print("Вы действительно хотите полностью удалить всю информацию без возможности дальнейшего восстановления?")
        print("Важно!!! Это действие необратимо! Вы можете удалить один контакт нажав в меню цифру четыре.")
        clearall = input("Введите Да (очистить книгу) или Нет:\n")
        if clearall == "Да":
            del book_phones
            print("Книга удалена.")
            book_phones = {}
            data_dict = {}
        with open('Телефонная книга.txt', 'w', encoding = 'utf-8') as file:
                file.write("Книга удалена.")
        with open('Data.json', 'w', encoding = 'utf-8') as file:
            json.dump(data_dict, file, ensure_ascii = False)
    # Такого действия нет
    else:
        print("Такого действия нет.")
        print("Допустимые команды: 1, 2, 3, 4, 5, 6, 7, 8, 9, Exit. Попробуйте, пожалуйста еще раз!")
    
    action = input(white + "Введите нужное значение:\n1 — показать, 2 — добавить, 3 — изменить, 4 — удалить, 5 — показать все имена в книге, 6 — показать все номера в книге, 7 - вывести теленфонную книгу полностью, 8 - проверить дни рождения, 9 - очистить всю книгу, Exit - выйти из программы.\n" + reset)
    os.system("cls")
# Сохраняем книгу в файле
    with open('Телефонная книга.txt', 'w', encoding = 'utf-8') as file:
        file.write("Телефонная книга:\n")
        for k, v in book_phones.items():
            file.write(f"{k}: {v}\n")
    with open('Data.json', 'w', encoding = 'utf-8') as file:
        json.dump(data_dict, file, ensure_ascii = False)
os.system("cls")
print(white + 'Спасибо за использование нашей программы! Ваша книга сохранена в файле "Телефонная книга.txt".' + reset)