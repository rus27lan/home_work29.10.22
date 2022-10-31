# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from datetime import datetime
start_time = datetime.now()

number = int(input("Сколько чисел будет в списке: "))
lst = [n for n in range(number)]
print(lst)
new_lst = list(filter(lambda x: x % 2 , lst))
print(f'{new_lst}\nответ: {sum(new_lst)}')

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))