# def get_number(intText = 'Введите число:' ):
#     while True:
#         user_input = input(intText)
#         try:
#             number = float(user_input)
#             if number < 0:
#                 print('Квадратный корень из отрицательного числа не определен.')
#                 continue
#             else:
#                 return number ** 0.5
#         except ValueError:
#             print('Пожалуйста, введите корректное число.')
#
# result = get_number()
# print(result)


# def get_float(prom):
#     while True:
#         try:
#             return float(input(prom))
#         except ValueError:
#             print("Пожалуйста, введите корректное число.")
#
# def get_num():
#     while True:
#         num1 = get_float("Введите первое число: ")
#         num2 = get_float("Введите второе число: ")
#         try:
#             result = num1 / num2
#             print(f"Результат деления: {result}")
#             break
#         except ZeroDivisionError:
#             print("Деление на ноль невозможно. Пожалуйста, введите другое второе число.")
# get_num()

#
# def calculate():
#     while True:
#         try:
#             num1 = float(input("Введите первое число: "))
#             num2 = float(input("Введите второе число: "))
#             operation = input("Введите операцию (+, -, *, /): ")
#             if operation == '+':
#                 result = num1 + num2
#             elif operation == '-':
#                 result = num1 - num2
#             elif operation == '*':
#                 result = num1 * num2
#             elif operation == '/':
#                 if num2 == 0:
#                     raise ZeroDivisionError("Деление на ноль невозможно")
#                 result = num1 / num2
#             else:
#                 raise ValueError("Неверная операция. Используйте только +, -, *, /")
#             print("Результат:", result)
#             break
#         except ValueError as ve:
#             print("Ошибка ввода:", ve)
#         except ZeroDivisionError as zde:
#             print("Ошибка:", zde)
#         except Exception as e:
#             print("Произошла непредвиденная ошибка:", e)
# calculate()




def get_valid_number(prompt_text):
    while True:
        try:
            return float(input(f"Введите {prompt_text} число: "))
        except ValueError:
            print(f"Ошибка: {prompt_text} число введено некорректно. Повторите ввод.")

def average():
    num1 = get_valid_number('первое')
    num2 = get_valid_number('второе')
    num3 = get_valid_number('третье')

    return (num1 + num2 + num3) / 3

result = average()
print("Среднее значение:", result)
