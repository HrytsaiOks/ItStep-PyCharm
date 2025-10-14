# try:
#     num_1 = int(input('Enter a number_1: '))
#     num_2 = int(input('Enter a number_2: '))
#     result = num_1/num_2
# except ZeroDivisionError:
#     print('Ошибка: Деление на ноль невозможно!')
# except ValueError:
#     print('Ошибка: Введите только числа!')
# else:
#     print(f'Результат: {result}')


# file = None
# try:
#     file = open('data.txt', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print('Ошибка: Файл не найден!')
# finally:
#     if file:
#         file.close()
#     print("Программа завершена.")



# try:
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#     operation = input("Введите операцию (+, -, *, /): ")
#
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         if num2 == 0:
#             raise ZeroDivisionError
#         result = num1 / num2
#     else:
#         raise Exception("Операция не поддерживается!")
#
# except ZeroDivisionError:
#     print("Ошибка: Деление на ноль невозможно!")
# except ValueError:
#     print("Ошибка: Введите только числа!")
# except Exception as e:
#     print(f"Ошибка: {e}")
# else:
#     print("Результат:", result)



# try:
#     user_input = input("Введите число: ")
#     number = int(user_input)
#     print("Вы ввели число:", number)
# except ValueError as e:
#     print("Оши бка:", e)



# Что делает finally? Когда он выполняется?
# Блок finally в конструкции try-except выполняется всегда, независимо от того, была ошибка или нет.
# Гарантированно выполняет завершающие действия, закрывает файл, выводит сообщение: "Программа завершена" и т.д.
#
# Можно ли написать try без except ?
# Да, можно написать try без except, но только если используется finally.
#
# Чем Exception отличается от конкретных ошибок (ValueError , ZeroDivisionError )?
# Exception — это базовый (общий) класс для всех стандартных ошибок в Python.
# ValueError, ZeroDivisionError и другие — это конкретные типы исключений, которые унаследованы от Exception.
# Обработка конкретных ошибок предпочтительнее, чем общий Exception.
#
# Можно ли использовать несколько except в одном try?
# Да, в Python можно (и нужно) использовать несколько except в одном try, чтобы обрабатывать разные типы ошибок по-разному.
# Разные ошибки требуют разной реакции. ValueError — пользователь ввёл не число → показать сообщение.
# ZeroDivisionError — деление на ноль → предупредить.
# Другие ошибки — логировать или остановить программу.
#
# Что произойдет, если в except не указать тип ошибки?
# Если в except не указать тип ошибки, Python перехватит любое исключение, как будто вы написали except Exception, но это не рекомендуется: нельзя отличить ошибки друг от друга, можно случайно скрыть баги.