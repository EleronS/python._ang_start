# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела


# def read_last(lines, file):
#     with open(file, 'r', encoding='utf8') as file:
#         while lines > 0:
#             some_list = []
#             for line in file:
#                 some_list.append(line)
#             for i in range(0, len(some_list)):
#                 if i >= len(some_list) - lines:
#                     print(*some_list[i].strip().split())
#             break
#
# read_last(4, 'article.txt')

# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf8') as file:
        some_list = []
        new_list = []
        for line in file:
            some_list.append(line)
        some_str = ''.join(some_list)
        long_str = max(some_str.split(), key=len)
        for word in some_str.split():
            if len(word) == len(long_str):
                new_list.append(word)
        print('Слово(слова) с самой большой длиной из файла: ')
        print(*new_list)
        print(f'эти слова из {len(new_list[0])} символов')


longest_words('article.txt')



















