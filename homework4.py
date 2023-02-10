# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random

# n = int(input('Введите длину первого числового массива: '))
# m = int(input('Введите длину второго числового массива: '))
# string_text1 = []
# string_text2 = []
# count = 1
# for i in range(n):
#     a = int(input(f'Элемент {count} первого массива'))
#     string_text1.append(a)
#     count += 1
#     if count == n+1:
#         count = 1
#         for j in range(m):
#             b = (int(input(f'Элемент {count} второго массива')))
#             string_text2.append(b)
#             count += 1
#
# poli1 = set(string_text1)
# poli2 = set(string_text2)
# result_list = []
# print(poli1, poli2)
# for k in poli1:
#     for s in poli2:
#         if k == s:
#             result_list.append(k)
# print(*f'Элементы совпадения: ',*result_list)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов.Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.В этом фермерском хозяйстве
# внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
n = int(input('Введите колличество кустов на грядке: '))
bush_counts = [random.randint(1,10) for _ in range(n)]
best_bush = []
print(f'Количество ягод на каждом кусте {bush_counts}' )
a = 0
for i in range(1, len(bush_counts) - 1):
    a += bush_counts[i] + bush_counts[i+1] + bush_counts[i-1]
    best_bush.append(a)
    a = 0
    if i > len(bush_counts)-i:
        a = 0
        a += bush_counts[-2] + bush_counts[-1] + bush_counts[0]
        best_bush.append(a)
        a = 0
        a += bush_counts[-1] + bush_counts[0] + bush_counts[1]
        best_bush.append(a)
print(f'Доступные комбинации сборки модуля {best_bush}')
a = 0
for j in range(0, len(best_bush)):
    if best_bush[j-1] >= best_bush[j]:
        a = best_bush[j]
        best_bush[j] = best_bush[j-1]
        best_bush[j-1] = a
print( f'Вывод : {best_bush[-1]} лучшая комбинация')













# print(bush_counts)
# for i in range(0, len(bush_counts)+3):
#     a = bush_counts[i] + bush_counts[i + 1] + bush_counts[i + 2]
#     b = bush_counts[i + 1] + bush_counts[i + 2] + bush_counts[i + 3]
#     c = bush_counts[i + 2] + bush_counts[i + 3] + bush_counts[i + 4]
#     if a > b and a > c:
#        best_bush.append(a)
#        print(a)
#     elif b > c and b > a:
#         best_bush.append(b)
#     else:
#         best_bush.append(c)
#         for j in range(0, len(best_bush)+2):
#             if best_bush[j] > best_bush[j + 1]:
#                 print(best_bush)
#             else:
#                 best_bush.remove(j)














