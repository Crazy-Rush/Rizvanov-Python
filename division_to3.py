
def division_to3():
    try:
        my_list_of_numbers = [int(num) for num in input("Введите чилсла через пробел: ").split()]
        count = 0
        for num in my_list_of_numbers:
            if num % 3 == 0:
                count +=1
                print(num)
        if count == 0:
            print("Нет чисел кратных 3")
    except ValueError:
        print("Нужно ввести числа через пробел.")
        division_to3()


if __name__ == "__main__":
    division_to3()
