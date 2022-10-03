def view_file():
    """Функция по выводу информации, содержащейся в справочнике, в консоль"""
    print("Данные в телефонном справочнике:\n")
    with open("telephone_book_format_1.txt", "r") as file_all:
        for line in file_all:
            print(line)
    with open("telephone_book_format_2.txt", "r") as file:
        for line in file:
            print(line)