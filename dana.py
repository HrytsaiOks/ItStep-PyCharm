a, b, c = map(int, input("Введите три стороны: ").split())

if a <= 0 or b <= 0 or c <= 0:
    print("Некорректные стороны")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Некорректные стороны")
else:
    if a == b and b == c:
        print("Равносторонний")
    elif a == b or a == c or b == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")