import math
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
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
# Выбрал сортировку Шелла(в худшем случае принимает сложность О(n**2)


def median_shell_sort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return f'Медиана массива {array[m]}'


# замеры 10
m = 5
lst = [randint(-100, 100) for _ in range(2*m + 1)]
print(lst[:])
print(median_shell_sort(lst[:]))
print(
    timeit(
        "median_shell_sort(lst[:])",
        globals=globals(),
        number=1000))
# замеры 100
m = 50
lst = [randint(-100, 100) for _ in range(2*m + 1)]
print(median_shell_sort(lst[:]))
# замеры 100
print(
    timeit(
        "median_shell_sort(lst[:])",
        globals=globals(),
        number=1000))
#  замеры 1000
m = 500
lst = [randint(-100, 100) for _ in range(2*m + 1)]
print(median_shell_sort(lst[:]))
print(
    timeit(
        "median_shell_sort(lst[:])",
        globals=globals(),
        number=1000))
