# some_list = [1, 2, 3, 4, 5, 'a', 'b']
import math

# //1
# for ind in range(0, len(some_list)):
#     some_list[ind] = str(some_list[ind])
# print(some_list)
#
#
# new_list = list(map(str, some_list))
# print(new_list)

# //2 map
#  # def square(x):
# #     return  x ** 2
#
# new_list1 = list(map(square, some_list))
# print(new_list1)

# // filter 1
# def even(x):
#     return x % 2 == 0
#
#
# new_list = list(filter(even, some_list))
# print(new_list)

# // filter 2

# def notint(x):
#     return type(x) == int
#
#
# new_list = list(filter(notint, some_list))
# print(new_list)


# lambda

# new_list = list(filter(lambda x: type(x) == int, some_list))
# print(new_list)

# enumirate
# some_list = [10, 20, 30, 40]
# print(list(enumerate(some_list)))
# for ind, value in enumerate(some_list):
#     print(ind, value)

# //zip
# first_list = ['apple', 'orange', 'grape']
# second_list = ['яблоко', 'апельсин', 'виноград']
# for eng, ru in zip(first_list, second_list):
#     print(eng, ru)

# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values

# transfomation = lambda x: x
#
# values = [2, 3, 5, 7, 11, 13, 17]
#
# print(list(map(transfomation, values)))

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна



# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# new = list(filter(lambda x: x[0] != x[1], orbits))
# print(*new)
# new2 = max(map(lambda x: x[0] * x[1] * math.pi, new))
# print(list(filter(lambda x: x[0] * x[1] * math.pi == new2, new)))


# summa = 102
# list1 = [90, 19, 48, 24, 12, 5]
# some_set = set(list1)
# for el in list1:
#     if summa - el in list1:
#         print('yes')
#         break
# else:
#     print('no')

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    for i in range(len(objects)):
        if characteristic(objects[i]) != characteristic(objects[0]):
            return False
    return True
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')







