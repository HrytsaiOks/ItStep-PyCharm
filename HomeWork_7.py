# def greet_by_time(name, hour):
#     if 6 <= hour < 12:
#         greeting = "Доброе утро"
#     elif 12 <= hour < 18:
#         greeting = "Добрый день"
#     elif 18 <= hour < 22:
#         greeting = "Добрый вечер"
#     else:
#         greeting = "Доброй ночи"
#
#     print(f"{greeting}, {name}!")
#
# greet_by_time("Alice", 9)
# greet_by_time("Bob", 20)
# greet_by_time("Ivan", 23)
# greet_by_time("Lena", 5)



# def sort_list(numbers):
#     n = len(numbers)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#     return numbers
#
# result = sort_list([3, 1, 4, 1, 5, 9])
# print(result)


# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
# print(is_prime(77))
# print(is_prime(5))



def reverse_list(numbers):
    reversed_numbers = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_numbers += [numbers[i]]
    return reversed_numbers

result = reverse_list([1, 2, 3, 4, 5])
print(result)


