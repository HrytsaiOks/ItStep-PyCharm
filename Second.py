from calendar import different_locale
from enum import unique

fruits = ['banana', 'apple', 'cherry']
banan = fruits[1]
print(banan)

# Словари
student = {"name": "Alice", "age": 25, "is_student": True}

# Доступ к значениям по ключам
name = student["name"]
age = student["age"]
is_student = student["is_student"]

unique_nambers = {1, 2, 3, 4, 5}
leters = {"a", "b", "c", "a", "b"}

unique_nambers.add(8)
print(unique_nambers)

a = 5
b = 10
c = 3
print(c)
c = a + b
print(c)

# integer = int(3.14)
integer1 = float(3)
print(integer1)

stroka = "10"
chislo = 10
n_chislo = '3.14'
print(stroka)
print(chislo)
print(n_chislo)
print("встретимся в " + stroka)

x = 10
y = 3
sum1 = x + y
difference = x - y
quotient = x / y
product = x * y
remainder = x % y
power = x ** y
integer_division = x // y
print(sum1, difference, quotient, product)
print(integer_division)
print(remainder)
print(power)

greeting = 'Hello'
substring = greeting[1:4]
print(greeting)
print(substring *3)


z = (1, 2, 3)
print(sum(z))

x = 10
y = 3
# sum((x,y))
print(sum((x,y)))

otvet = input('Как тебя зовут? :')
q = '5'
w = '10'
res = q + w

print(otvet)
print(f'меня зовут {otvet}')
#
a = int(input('Enter number A:'))
b = int(input('Enter number B:'))
sum = a + b
print(sum)

rounded = round(3.14159, 2)
print(rounded)

maximum = max(1,2,3,4,5)
minimum = min(1, 2, 3, 4, 5)

print(f'MAX:  {maximum}')
print(f'MIN:  {minimum}')


