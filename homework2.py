# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2
# noinspection PyInterpreter
# n = int(input('Введите количество монеток: '))
# print(f'Вводите положение монеты {n} раз')
# print('1 - решка / 0 - герб')
# count1 = 0
# count2 = 0
# for _ in range(n):
#     m = int(input())
#     if m == 0:
#         count1 += 1
#     elif m == 1:
#         count2 += 1
#     else:
#         print('Данные некоректны!')
# if count1 < count2:
#     print(f'переверните {count1} монетки гербом')
# else:
#     print(f'переверните {count2} монетки решкой')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
#
# 4 4 -> 2 2
# 5 6 -> 2 3
# print('Введите два числа: ')
# s = int(input())
# p = int(input())
# x = 0
# while x <= 1000:
#     for i in range(1000):
#         x += 1
#         y = s - x
#         if x == p / y:
#             print(x)
#             print(y)

# x = 0
# print('Эти числа были загаданы: ')
# while x < s:
#     for i in range(1000):
#         x += 1
#         y = s - x
#         if x < s:
#             if x == p / y:
#                 print(x)
#                 if x == y:
#                     print(y)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
#
# 10 -> 1 2 4 8
#
# пользователь будет вводить каждое число на новой строке для задач 10, 12.

while True:
    a = 1
    k = 2
    n = int(input())
    while a <= n:
        print(a)
        a = a * k











