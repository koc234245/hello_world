import random
variants = []
user = input("Выберите Камень, Ножницы или Бумага: ")
computer = random.choice (["Камень", "Ножницы", "Бумага"])

match user:
    case "Камень":
        match computer:
            case "Ножницы":
                print("Оппонент выбрал Ножницы, вы победили")
            case "Бумага":
                print("Оппонент выбрал Бумагу, вы проиграли")
            case "Камень":
                print("Оппонент выбрал Камень, ничья")

    case "Ножницы":
        match computer:
            case "Ножницы":
                print("Оппонент выбрал Ножницы, ничья")
            case "Бумага":
                print("Оппонент выбрал Бумагу, вы победили")
            case "Камень":
                print("Оппонент выбрал Камень, вы проиграли")

    case "Бумага":
        match computer:
            case "Ножницы":
                print("Оппонент выбрал Ножницы, вы проиграли")
            case "Бумага":
                print("Оппонент выбрал Бумагу, ничья")
            case "Камень":
                print("Оппонент выбрал Камень, вы победили")
    case _:
        print("Упс, вы что-то не то написали")