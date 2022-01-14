from random import randint
from timeit import timeit

"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


def no_sort(lst_obj):
    for i in range(len(lst_obj) // 2):
        lst_obj.remove(min(lst_obj))
    return f'Медиана массива no_sort {min(lst_obj)}'


# замеры 10
m = 5
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(no_sort(lst[:]))
print(
    timeit(
        "no_sort(lst[:])",
        globals=globals(),
        number=1000))
# замеры 100
m = 50
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(no_sort(lst[:]))
print(
    timeit(
        "no_sort(lst[:])",
        globals=globals(),
        number=1000))
#  замеры 1000
m = 500
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(no_sort(lst[:]))
print(
    timeit(
        "no_sort(lst[:])",
        globals=globals(),
        number=1000))
