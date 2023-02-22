#  чтение файлов
# with open('les8.txt', 'r', encoding='utf8') as file:
#     # text = file.read().splitlines()
#     # print(text)
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())

# запись файлов
# with open('les8.txt', 'a', encoding='utf8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# 1поиск буквы и ее повторение с проверкой
import time


# with open('les8.txt', 'r', encoding='utf8') as file:
#     find_letter = input()
#     count = 0
#     start = time.time()
#     for letter in file.read():
#         if letter == find_letter:
#             count += 1
#     end = time.time()
#     print(count)
#     print(end - start)
#
# with open('les8.txt', 'r', encoding='utf8') as file:
#     find_letter = input()
#     start = time.time()
#     end = time.time()
#     print(file.read().count(find_letter))
#     print(end - start)
#
# 2 список из N элементов. заполнить числами от [-N, N].найти произведение элементов
# на указанных позициях

from random import randint
n = int(input('Введите кол элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('les8.txt', 'w', encoding='utf8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('les8.txt', 'r', encoding='utf8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)