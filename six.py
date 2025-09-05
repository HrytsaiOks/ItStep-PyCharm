# string1 = "12345"
# string2 = "123a45"
# string3 = "67890"
# string4 = "123 45"
#
# print(string1.isdigit())
# print(string2.isdigit())
# print(string3.isdigit())
# print(string4.isdigit())

# user_input = input('Введите число')
# if user_input.isdigit():
#     number = int(user_input)
#     print(f'Вы ввели число:  {number}')
#
# else:
#     print('Пожалуйста, введите корректное число.')


# x = 5
# # while x < 10:
# #     print(f'x= {x}')
# #     x += 1


# while True:
#     print(f'x= {x}')
#     x += 1
#     if x >=10:
#         break


# while True:
#     user_input = input('Введите число')
#     if user_input.isdigit():
#         number = int(user_input)
#         print(f'Вы ввели число:  {number}')
#         break
#     else:
#         print('Пожалуйста, введите корректное число.')

# while True:
#
#     num1 = input('Введите первое число:')
#     if  num1.isdigit():
#         num1 = int(num1)
#     else:
#         print(f'Введите корректное число')
#         continue
#     operation = input('Введите операцию (+, -, *, /): ')
#     if operation not in ['+', '-', '*', '/']:
#         print('Ошибка: допустимы только +, -, *, /')
#         continue
#     num2 = input('Введите второе число:')
#     if num2.isdigit():
#         num2 = int(num1)
#     else:
#         print(f'Введите корректное число')
#         continue
#
# if operation == '+':
#     print(f'result = {num1 + num2}')
# elif operation == '-':
#     print(f'result = {num1 - num2}')
# elif operation == '+':
#     print(f'result = {num1 * num2}')
# elif operation == '/':
#     if num2 != 0:
#         print("Результат:", num1 / num2)
#     else:
#         print("Деление на ноль невозможно!")
#
#
# s = ' Hello World! '
# uppercase_s = s.upper()
# lowercase_s = s.lower()
# strip_s = s.strip() #убирает пробел в начале и в конце строки
#
# combo_s = s.strip().upper()
# lstrip_s = s.lstrip()
# rstrip_s = s.rstrip()
#
#
# print(s)
# print(uppercase_s)
# print(lowercase_s)
# print(strip_s)
# print(combo_s)
# print(lstrip_s)
# print(rstrip_s)

# Пользователь вводит с клавиатуры номер месяца (от 1 до 12). В зависимости от полученного номера месяца программа выводит на экран надпись:
# Winter (если введено значение 1, 2 или 12), Spring (если введено значение от 3 до 5), Summer (если введено значение от 6 до 8), Autumn (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1 до 12 требуется вывести сообщение об ошибке.

# while True:
#     month = input('Введите номер месаця (от 1 до 12): ')
#     if month.isdigit():
#         month = int(month)
#     else:
#         print(f'Введите корректное число')
#         continue
#
#     if  1 <= month <= 12:
#         if month in [12, 1, 2]:
#             print('Winter')
#         elif month in [3, 4, 5]:
#             print('Spring')
#         elif month in [6, 7, 8]:
#             print('Summer')
#         elif month in [9, 10, 11]:
#             print('Autumn')
#         else:
#             print('Enter correct number between 1 and 12')
#             continue
#         break
#     else:
#         print('Enter correct number')



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



