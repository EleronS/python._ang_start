# Дан список чисел. Определить сколько в нем встречается различных чисел.
# numbers = [130, 44, 22, 311, 52353, 314, 5]
# unique_numbers = list(set(numbers))
# print(len(unique_numbers))


# Дана последовательность из n целых чисел и число k.
# Необходимо сдвинуть всю последовательность ( сдвиг - циклический )  на k элементов вправо.
# k - положительное число.

# numbers = [130, 44, 22, 311, 52353, 314, 5]
# k = int(input())
# list_res = list()
# for i in range(k):
#     list_res.append(numbers[len(numbers) - 1 - i])
# print(i)
# for i in range(len(numbers) - k):
#     list_res.append(numbers[i])
#     print(list_res)
# print(list_res)

# Напишите программу для печати всех уникальных значений в словаре

# list = [{"v": "5001"}, {"v": "5002"}, {"vi": "5001"}, {"vi": "5005"}, {"vii": "5005"}, {" v ": "5009"}, {" viii ": "5007"}]
# print(list)
#
# set_list = set()
# for i in list:
#     print(i)
#     for j in i:
#         print(j)
#         set_list.add(i[j])
# print(set_list)

# Дан массив целых чисел, напишите программу которая подсчитает колличество элементов массива больших предидущего.
array = [0, -1, 5, 2, 3]
n = 0
for i in range(1, len(array)):
    if array[i] > array[i - 1]:
        n += 1
print(n)


