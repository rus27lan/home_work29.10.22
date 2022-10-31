# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from datetime import datetime
start_time = datetime.now()

number = int(input("Сколько чисел будет в списке: "))
print("Введите по очереди числа что бы добавить их в список: ")
list = []
i = 0
while int(i) < number:
    numbers = input()
    list.append(numbers)
    i += 1
print(list)

count = 1
sum = 0
while count < number:
    sum = sum + int(list[count])
    count += 2
print(f"ответ: {sum}")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))