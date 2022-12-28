def input_name():
    name = input("Введите имя: ")
    if name == "Вячеслав":
        print("Привет, Вячеслав!")
    elif name.isdigit() or name == "":
        print("Вы ввели число. Нужно ввести имя.")
    else:
        print("Нет такого имени.")


if __name__ == "__main__":
    input_name()
