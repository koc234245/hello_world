act = input("Выберите +, -, *, /")
a = float(input("Введите первое число"))
b = float(input("Введите второе число"))
if act == "+" :
    c = a + b
elif act == "-" :
    c = a - b
elif act == "/" :
    c = a / b
elif act == "*" :
    c = a * b
print("Результат:", c)