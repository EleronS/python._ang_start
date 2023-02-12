# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def integerPower(a, b):
#     if b == 1:
#         return a
#     c = 0
#     d = integerPower(a, b - 1)
#     for i in range(a):
#         c += d
#     return c
#
#
# a = int(input('Число: '))
# b = int(input('Степень: '))
# integerPower(a, b)
# print(f'Результат:{integerPower(a, b)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def sum(a, b, d):

    if a != 0:
        a -= 1
        d += 1
        return sum(a, b, d)
    elif b != 0:
        b -= 1
        d += 1
        return sum(a, b, d)
    else:
        return d

d = 0
a = int(input('Число1: '))
b = int(input('Число2: '))
sum(a, b, d)
print(f'Результат сложения : {sum(a, b, d)}')