# Напишите программу которая принимает на вход строку и отслеживает скрлько раз символ уже встречался.
# Количество повторов добавляется к символу с помощью постфикса формата _n.

# string = 'd g h t r g r h t j h b v f d s d f'
# print(string)
# list_1 = string.split()
# print(list_1)
# dict_1 = {}
# new_list = []
# for letter in list_1:
#     dict_1[letter] = dict_1.get(letter, 0) + 1
#     if dict_1.get(letter) > 1:
#         new_list.append(letter + '_' + str(dict_1.get(letter)))
#     else:
#         new_list.append(letter)
# print(' '.join(new_list))

# Пользователь вводит текст(строка) Словом будет считаться последовательность непробельных
# символов идущих подряд. Слова разделены одним или большим числом пробелов.
# Определить, сколько различных слов содержится в этом тексте.

# 1
# string = 'sdsd sdsd    sdref fdrtg jjh ldk ffgghhgg sdsd'
# list_1 = string.split()
# print(*list_1)
# set_1 = set(list_1)
# print(*set_1)
# print(len(set_1))

# 2
# string = set(input('Введите текст: ').split())
# print(f'В тексте {len(string)} уникальных слов')

# 3
# string = input('Введите текст: ')
# string = string.split()
# new_list = []
# for word in string:
#     if not word in new_list:
#         new_list.append(word)
# print(f'В тексте {len(new_list)} уникальных слова')

# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => 2, 10

# 1
# list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
# list_2 = []
# dict_1 = {}
# for i in list_1:
#     dict_1[i] = dict_1.get(i, 0) + 1
# for j in dict_1:
#     if dict_1.get(j) == 1:
#         list_2.append(j)
# print(list_2)

# 2
# list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
# list_2 = []
# for i in list_1:
#     if list_1.count(i) == 1:
#         list_2.append(i)
# print(f'Уникальные элементы {list_2}')

# 3
list_1 = [1, 2, 3, 5, 1, 5, 3, 10]
print([i for i in list_1 if list_1.count(i) == 1])








