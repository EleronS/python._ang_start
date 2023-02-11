# Fibonacci 0 1 1 2 3
import random

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
#
# n = int(input())
# for i in range(n):
#     print(fibonacci(i))

# Поменять максимальные значения списка на минимальные
# n = int(input('Введите количество оценок: '))
# list_1 = [random.randint(2, 5) for _ in range(n)]
# min = 5
# max = 2
# for i in list_1:
#     if i < min:
#         min = i
#     if i > max:
#         max = i
# print(min, max)
# print(list_1)
#
# for i in range(len(list_1)):
#     if list_1[i] == max:
#         list_1[i] = min
# print(list_1)

# напишите функцию которая принимает одно число и проверяет является ли оно простым
# def checkNum (n):
#     if not n % 2 == 0:
#         print(f'Число { n } является простым')
#     else:
#         print(f'Число { n }  НЕ является простым')
#     return n
#
# checkNum(13)

# list comprehension
magazine = [int(input('Введите оценку: ')) for _ in range(int(input('Введите кол-во оценок: ')))]










