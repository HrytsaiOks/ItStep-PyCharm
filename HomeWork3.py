# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# c = int(input('Enter number c: '))
#
# if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
#     if a == b == c:
#         print('треугольник равносторонний')
#     elif a == b or a == c or b == c:
#         print('равнобедренный')
#     else:
#         print('разносторонний')
# else:
#     print("Некорректные стороны")


# base_cena = 100
# age = int(input('Введите свой возраст: '))
# is_student = True
# is_veteran = False
# is_weekend = True
#
# if age < 6:
#     final_cena = 0
#     msg = 'Дети до 6 лет вход бесплатный'
# elif age > 65:
#     final_cena = base_cena * 0.5
#     msg = 'Пенсионеры 65+ имеют скидку 50%'
# elif is_veteran:
#     final_cena = base_cena * 0.6
#     msg = ('Ветераны имеют скидку 40%')
# elif is_student and 18 <= age <= 25:
#     final_cena = base_cena * 0.7
#     msg = 'Студенты имеют скидку 30%'
# else:
#     final_cena = base_cena
#     msg = 'Билет без скидки'
#
# day_type = 'выходной' if is_weekend else 'будний'
#
# if final_cena != 0 and is_weekend:
#     final_cena += 10
#
# print(f'Итог: {int(final_cena)}; причина: {msg}; день: {day_type}')



is_first_order = True
base_cena =  float(input('Введите базовую цену: '))
promo = input("Введите промо-код:")

if promo == "WELCOME" and is_first_order:
    final_cena = base_cena * 0.75
    msg = "Скидка 25% за первый заказ с промо-кодом WELCOME"
elif promo == "SALE10":
    final_cena = base_cena * 0.9
    msg = "Скидка 10% с промо-кодом SALE10"
else:
    final_cena = base_cena
    msg = "Без Cкидки"
print(f'К оплате: {final_cena:.2f} {msg}')

