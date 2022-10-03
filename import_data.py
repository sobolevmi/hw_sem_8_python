def add_data_to_file():
    """Функция по добавлению контактов в телефонный справочник"""
    while True:
        choice_format = str(input("В каком формате вы хотите ввести новые данные в справочник?\n"
                                "Нажмите 1, если в следующем формате:\n"
                                "Фамилия,\n"
                                "Имя,\n"
                                "Телефон,\n"
                                "Описание\n"
                                "\n"
                                "Нажмите 2, если в следующем формате:\n"
                                "Фамилия, Имя, Телефон, Описание\n"
                                "\n"
                                "Чтобы выйти в главное меню, нажмите q\n"))
        if choice_format == "1":
            with open("telephone_book_format_1.txt", "a") as file:
                user_surname = str(input("Введите фамилию: "))
                file.write(str(user_surname + "\n"))
                user_name = str(input("Введите имя: "))
                file.write(str(user_name + "\n"))
                user_phone = str(input("Введите номер телефона: "))
                file.write(str(user_phone + "\n"))
                user_description = str(input("Введите описание номера телефона: "))
                file.write(str(user_description + "\n"))
                file.write("\n")
        elif choice_format == "2":
            with open("telephone_book_format_2.txt", "a") as file:
                user_surname = str(input("Введите фамилию: "))
                file.write(str(user_surname + " *** "))
                user_name = str(input("Введите имя: "))
                file.write(str(user_name + " *** "))
                user_phone = str(input("Введите номер телефона: "))
                file.write(str(user_phone + " *** "))
                user_description = str(input("Введите описание номера телефона: "))
                file.write(str(user_description) + "\n")
        elif choice_format == "q":
            break
        else:
            while choice_format != "1" and choice_format != "2" and choice_format != "q":
                choice_format = str(input("Вы ввели неверное число, попробуйте снова\n"))
        while True:
            continue_input = str(input("Нажмите 1, если хотите добавить еще один контакт, "
                                   "или нажмите q, чтобы завершить добавление контактов\n"))
            if continue_input == "q":
                break
            if continue_input != "1" and continue_input != "q":
                while continue_input != "1" and continue_input != "q":
                    continue_input = str(input("Вы ввели неверное число, попробуйте снова\n"))