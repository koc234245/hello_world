import random

variants = ["Камень", "Ножницы", "Бумага"]
computer = random.choice([0, 1, 2])
user = int(input(f"Выберите {variants[0]}(0), {variants[1]}(1) или {variants[2]}(2): "))
print("Ваш выбор", variants[user])
print("Оппонент выбрал", variants[computer])

def game():
  # здест логика игры
  # используй elif, or, and
  if user == computer:
    print("Ничья!")
  # ничья
  elif user == computer + 1:
    print("Вы проиграли!")
  # компьютер выйграл
  elif user + 1 == computer:
    print("Вы выйграли!")
  # пользователь выйграл
  else:
    print("Упс, вы что-то не то ввели")
  # что-то не то ввели
  print("Результат")
game()

# match user:
#   case "Камень":
#       if computer == "Ножницы":
#           print("Вы победили!")
#       else:
#           print('Вы проиграли')

#   case "Ножницы":
#       if computer == "Бумага":
#           print("Вы победили!")÷
#       else:
#           print('Вы проиграли')

#   case "Бумага":
#       if computer == "Камень":
#           print("Вы победили!")
#       else:
#           print('Вы проиграли')
#   case _:
#       print("Упс, вы что-то не то написали")
