act = input("Выберите +, -, *, /")
first_number = float(input("Введите первое число"))
second_number = float(input("Введите второе число"))
match act:
    case "+":
        print(first_number + second_number)

    case "-":
        print(first_number - second_number)

    case "*":
        print(first_number * second_number)

    case "/":
        print(first_number / second_number)