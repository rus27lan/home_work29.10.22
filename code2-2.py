# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
from datetime import datetime
start_time = datetime.now()

number = 5
nums = [(1 + 1/number) ** number for n in range(number)]
print(nums)
print(sum(nums))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))