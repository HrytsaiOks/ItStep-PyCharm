secret_number = 7
while True:

    myNumber = input("Введите число от 1 до 100: ")
    if myNumber.isdigit():
        myNumber = int(myNumber)
        if secret_number == myNumber:
            print("Поздравляем! Вы выиграли!")
            break
        elif secret_number < myNumber:
            print("Загаданное число меньше")
        elif secret_number > myNumber:
            print("Загаданное число больше")
    else:
        print('Enter correct number')



is_admin = False
is_premium = True
has_trial = True
# route = '/admin'
route = '/premium'
# route = '/home'


if route == "/admin" and is_admin:
    print('Доступ разрешен: admin')
elif route == "/premium" and (has_trial or is_premium):
    print('Доступ разрешен: premium')
elif route == "/home":
    print('Доступ разрешен: home')
else:
    print('Доступ запрещен')



value = float(input("Введите значение: "))
percent = float(input("Введите процент, который нужно посчитать: "))
result = value * (percent / 100)
print(f"{percent} процентов от {value} составляет = {result}")


username = 'user'
password = 'pass'

input_username = input('Enter username: ')
input_password = input('Enter passwor: ')

is_username_correct = input_username == username
is_password_correct = input_password == password

if is_username_correct and is_password_correct:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")

    age = int(input("Введите ваш возраст: "))

    if age < 18:
        print("Вы несовершеннолетний.")
    elif age < 65:
        print("Вы взрослый.")
    else:
        print("Вы пенсионер.")



light = "green"
is_raining = True
has_umbrella = False

if light == "red":
    msg = "Стой"
elif light == "yellow":
    msg = "Подожди"
elif light == "green":
    msg = "Иди"
else:
    msg = "Ошибка: неизвестный сигнал"

if is_raining and not has_umbrella:
    msg = msg + ", но без зонта лучше ускориться"
    # msg += ", но без зонта лучше ускориться"

print(msg)
















