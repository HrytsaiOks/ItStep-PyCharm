# def compare_length(a,b):
#     if len(a) > len(b):
#         return ("Первая длиннее")
#     elif len(a) < len(b):
#         return ("Вторая длиннее")
#     else:
#         return ("Одинаковой длины")
#
# print(compare_length("кот", "собака"))
# print(compare_length("кот", "пес"))


# def greetings_table(names, greeting):
#     for name in names:
#         print(f"{greeting}, {name}!")
#
# greetings_table(["Анна", "Иван", "Алиса"], "Добрый день")


# def sum_and_diff(a,b):
#     s = a + b
#     d = a - b
#     return s, d

# s, d = sum_and_diff(10, 5)
# print("Сумма =", s)
# print("Разность =", d)


# def check_age(name,age):
#     if age < 18:
#         print(f'{name}, вам нет 18 лет')
#     else:
#         print(f'{name}, доступ разрешён')
#
# check_age("Анна", 16)
# check_age("Иван", 20)


def max_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(22, 55, 9))






