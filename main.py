# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# print(f'Сумма данных чисел {a + b + c}')

# a = float(input())
# b = float(input())
# print({a * b})

# a = float(input())
# b = float(input())
# print({})

# name = 'Alex'
# age = 24
# # print('Вас зовут ' + name +' ' + str(age))
# # print('Вас зовут ', name, age)
# print(f'Вас зовут {name} {age}')

# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# elif a==b:
#     print('Числа равные')
# else:
#     print(b)

# a = int(input())
# if 1000 <= a <= 9999 or -9999 <= a <= -1000:
#     print('Yes')
# else:
#     print('No')

# a = input()
# if'-' in a:
#     if len(a) == 5:
#         print('Yes')
#     else:
#         print('No')
# else:
#     if len(a) == 4:
#         print('Yes')
#     else:
#         print('No')

# пользователь вводит строки пока не введет пустую, все строки гарантированно числовые. Найти сумму введенных чисел кратных 4.
# summa = 0
# while True:
#     a = input()
#     if a == '':
#         break
#     if int(a) % 4 == 0:
#         summa += int(a)
# print(summa)

# За день машина проезжает n километров. Сколько дней нужно что бы проехать m километров. При решении этой задачи
# нельзя пользоваться условной конструкцией if и циклами.

# n = int(input())
# m = int(input())
# print((n + m - 1)//n)




# В некоторой школе за каждой партой может сидеть только два учащихся.Известно количество учащихся трех классах.
# Выведите наименьщее число парт которое нужно приобрести для них.

# a = int(input())
# b = int(input())
# c = int(input())
#
# summa = a + b + c
# if summa % 2 == 0:
#     print(int(summa/2))
# else:
#     print(int(summa/2+1))

# Дано натуральное число. Требуется определить является ли год с данным числом високосным. Да - вывести Yes, нет - no.
# Григорианским високосным годом является год номер которого кратен 4 но не кратен 100, а также кратен 400.

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')