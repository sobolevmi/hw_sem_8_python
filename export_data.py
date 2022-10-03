def export_data_from_file():
    """Функция по экспорту информации, содержащейся в телефонном справочнике, в другой файл"""
    while True:
        choice_export = str(input("Нажмите 1, если данные в файле хранятся в следующем формате:\n"
                                    "Фамилия,\n"
                                    "Имя,\n"
                                    "Телефон,\n"
                                    "Описание\n"
                                    "\n"
                                    "или нажмите 2, если данные в файле хранятся в следующем формате:\n"
                                    "Фамилия, Имя, Телефон, Описание\n"
                                    "\n"
                                    "Чтобы выйти в главное меню, нажмите q" "\n"))
        if choice_export == "1":
            with open("telephone_book_format_1.txt", "r") as a_file:
                with open("export_telephone_book_format_1.txt", "a") as b_file:
                    for line in a_file:
                        b_file.write(line)
                    a_file.close()
                    b_file.close()
            print("Ваши данные успешно экспортированы!")
            break
        if choice_export == "2":
            with open("telephone_book_format_2.txt", "r") as a_file:
                with open("export_telephone_book_format_2.txt", "a") as b_file:
                    for line in a_file:
                        b_file.write(line)
                    a_file.close()
                    b_file.close()
            print("Ваши данные успешно экспортированы!\n")
            break
        elif choice_export == "q":
            break
        else:
            while choice_export != "1" and choice_export != "2" and choice_export != "q":
                choice_export = str(input("Вы ввели неверное число, попробуйте снова \n"))