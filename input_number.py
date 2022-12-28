def input_number_bigger_than_7():
    try:
        number = int(input("Введите число больше 7: "))
        if number > 7:
            print("Привет")
        else:
            print("Введенное число не больше 7")
    except ValueError:
        print("Некорректный ввод, введите число")
        return input_number_bigger_than_7()


if __name__ == "__main__":
    input_number_bigger_than_7()

