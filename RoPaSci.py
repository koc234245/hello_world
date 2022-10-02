import random

user = input("Выберите Камень, Ножницы или Бумага: ")
computer = random.choice (["Камень", "Ножницы", "Бумага"])
print("Оппонент выбрал", computer)
match user:
    case "Камень":
        if computer == "Ножницы":
            print("Вы победили!")
        else:
            print('Вы проиграли')

    case "Ножницы":
        if computer == "Бумага":
            print("Вы победили!")
        else:
            print('Вы проиграли')

    case "Бумага":
        if computer == "Камень":
            print("Вы победили!")
        else:
            print('Вы проиграли')
    case _:
        print("Упс, вы что-то не то написали")