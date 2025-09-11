# while True:
#     week = input('Введите номер дня недели (от 1 до 7): ')
#     if week.isdigit():
#         week = int(week)
#     else:
#         print(f'Введите корректное число')
#         continue
#     if  1 <= week <= 7:
#         if week in [1]:
#             print('Понедельник')
#         elif week in [2]:
#             print('Вторник')
#         elif week in [3]:
#             print('Среда')
#         elif week in [4]:
#             print('Четверг')
#         elif week in [5]:
#             print('Пятница')
#         elif week in [6]:
#             print('Суббота')
#         elif week in [7]:
#             print('Воскресенье')
#         else:
#             print('Enter correct number between 1 and 7')
#             continue
#         break
#     else:
#         print('Enter correct number')



# while True:
#     month = input('Введите номер месяца (от 1 до 12): ')
#     if month.isdigit():
#         month = int(month)
#     else:
#         print(f'Введите корректное число')
#         continue
#     if  1 <= month <= 12:
#         if month in [1]:
#             print('Январь')
#         elif month in [2]:
#             print('Февраль')
#         elif month in [3]:
#             print('Март')
#         elif month in [4]:
#             print('Апрель')
#         elif month in [5]:
#             print('Май')
#         elif month in [6]:
#             print('Июнь')
#         elif month in [7]:
#             print('Июль')
#         elif month in [8]:
#             print('Август')
#         elif month in [9]:
#             print('Сентябрь')
#         elif month in [10]:
#             print('Октябрь')
#         elif month in [11]:
#             print('Ноябрь')
#         elif month in [12]:
#             print('Декабрь')
#         else:
#             print('Enter correct number between 1 and 12')
#             continue
#         break
#     else:
#         print('Enter correct number')



# while True:
#
#     number = input("Введите число: ").strip()
#     if number.startswith("-"):
#         if number[1:].isdigit():
#             number = int(number)
#         else:
#             print("Введите корректное число")
#             continue
#     elif number.isdigit():
#         number = int(number)
#     else:
#         print("Введите корректное число")
#         continue
#     if  number > 0:
#         print('Number is positive')
#     elif number < 0:
#         print('Number is negative')
#     else:
#         print('Number is equal to zero')
#         break




# while True:
#     number_1 = input('Введите первое число: ')
#     number_2 = input('Введите второе число: ')
#     if number_1.isdigit() and number_2.isdigit():
#         number_1 = int(number_1)
#         number_2 = int(number_2)
#     else:
#         print(f'Введите корректные числа')
#         continue
#     if  number_1 == number_2:
#         print('Эти числа равны')
#     elif number_1 <= number_2:
#         print(f'{number_1}, {number_2}')
#     elif number_1 >= number_2:
#         print(f'{number_2}, {number_1}')
#         break



while True:
    number = input("Введите целое шестизначное число: ").strip()
    if not number.isdigit() or len(number) != 6:
        print("Ошибка: нужно ввести именно шестизначное число")
        continue
    a = int(number[0])
    b = int(number[1])
    c = int(number[2])
    d = int(number[3])
    e = int(number[4])
    f = int(number[5])
    if a + b + c == d + e + f:
        print("Поздравляем! Ваше число счастливое!")
    else:
        print("Увы, число не счастливое!")
    break