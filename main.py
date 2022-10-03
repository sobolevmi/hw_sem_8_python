import import_data
import export_data
import view

while True:
    choice = str(input("Телефонный справочник\n"
                        "Если вы хотите добавить контакт, нажмите 1\n"
                        "Если вы хотите просмотреть содержимое справочника, нажмите 2\n"
                        "Если вы хотите экспортировать данные из справочника, нажмите 3\n"
                        "Если вы хотите завершить работу программы, нажмите q\n"))
    if choice == "1":
        import_data.add_data_to_file()
    if choice == "2":
        view.view_file()
    if choice == "3":
        export_data.export_data_from_file()
    if choice == "q":
        break
    else:
        while choice != "1" and choice != "2" and choice != "3" and choice != "q":
            choice = str(input("Вы ввели неверное число. Попробуйте снова:\n"))