while(True):
    number = int(input("Введите число от 3 до 20: "))
    if number in range(3, 21):
        print("n =", number)
        list_a = list(range(1, 21))
        for a in list_a:
            list_b = list(range(a + 1, number))
            for b in list_b:
                if number % (a + b) == 0 and a != b:
                    print(a, b, end=" ")
    else:
       print("Неверное число, Вам капут ☹")
