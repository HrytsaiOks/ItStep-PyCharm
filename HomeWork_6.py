# room = input("Enter the room number: ").strip()
# if len(room) !=5:
#     print('Ошибка: неверная длина')
# elif room[1] !='-' :
#     print('Ошибка: отсутствует дефиз на позиции 2')
# else:
#     abc = room[0]
#     num = room[2:]
#     if abc not in ("A", "B", "C", "D"):
#         print("Ошибка формата")
#     elif not num.isdigit() or len(num) != 3:
#         print("Ошибка формата")
#     else:
#         print("Формат принят")



# qty_str = input("Введите число от 1 до 100: ").strip()
# if not qty_str.isdigit():
#     print("Ошибка: не число")
# else:
#     qty = int(qty_str)
#     if qty < 1 or qty > 100:
#         print("Ошибка: вне диапазона")
#     else:
#         print(f"Количество принято: {qty}")



start_time = input('Введите значение часов в формате HH:MM: ').strip()
end_time = input('Введите значение часов в формате HH:MM: ').strip()
if len(start_time) !=5 or len(end_time) !=5:
    print('Ошибка: неверная длина')
elif start_time[2] != ':' or end_time[2] != ':' :
    print('Ошибка: отсутствует двоеточие на позиции 3')
else:
    hh_1 = start_time[:2]
    mm_1 = start_time[3:]
    hh_2 = end_time[:2]
    mm_2 = end_time[3:]
    if not (hh_1.isdigit() and hh_2.isdigit() and mm_1.isdigit() and mm_2.isdigit()):
        print('Ошибка: часы и минуты должны быть цифрами')
    else:
        hh_1 = int(hh_1)
        mm_1 = int(mm_1)
        hh_2 = int(hh_2)
        mm_2 = int(mm_2)
        if not (0 <= hh_1 <= 23 and 0 <= mm_1 <= 59 and 0 <= hh_2 <= 23 and 0 <= mm_2 <= 59):
            print('Ошибка: недопустимые значения часов и минут')
        else:
            total_start = hh_1 * 60 + mm_1
            total_end = hh_2 * 60 + mm_2
            if total_end > total_start:
                print('Интервал корректен')
            else:
                print('Ошибка: время окончания раньше или равно времени начала')


