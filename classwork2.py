# FOR 1

# a = 'hello'
# for i in a:
#     print(i)
# # начало . кол - во . длина шага (2,10,1)
# for e in range(2,10,1):
#     print(e)
#
# for ind in range(len(a)):
#     print(ind)

# FOR 2
# in _
# for _ in range(3):
#     print('HELLO')
#
# Задача 1 Факториал
# n = int(input('Введите число : '))
# a = 1
# k = 1
# while k <= n:
#     a = a * k
#     k = k + 1
# print(a)

# Задача 2 Фибоначчи
# n = int(input('Enter number '))
# a = 0
# b = 1
# count = 1
# s = 0
# while s < n:
#     s = a + b
#     a = b
#     b = s
#     count += 1
# if s > n:
#     print(-1)
# else:
#     print('Place number Fibonacci')
#     print(count+1)

# Задача 3 Диапазон
n = int(input('Введите период '))
print('Вводите температуру по периоду')
max_count = 0
count = 0
for _ in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0
if max_count == 0 and count != 0:
    print(count)
else:
    print(max_count)

# Задача 4




