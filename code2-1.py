# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
from datetime import datetime
start_time = datetime.now()

number = 5
numbers = []
count = 1
number2 = 1
sum = 0
while count - 1 < number:
    number2 = (1 + 1/number) ** number
    numbers.append(number2)
    count += 1
    sum += number2
print(numbers)
print(sum)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))