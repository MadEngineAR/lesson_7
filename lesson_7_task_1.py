from random import randint
from timeit import timeit
"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""


# В данной задаче ввел счетчик в доработанную функция сортировки. При каждой замене элементов счетчик +=1,
# по завершении прохода счетчик сравнивается с 0. Если они равны то выход из цикла(подразумевается, что массив уже
# отсортирован. Замеры показывают не большую эффективность в плане времени на работу, нередко доработанная
# функция меделенней.
# Эффективность подхода со счетчиком будет расти со степенью упорядоченности Исходного массива(чем он больше изначально
# упорядочен - тем эффективней дораб.функция. Так как у нас заполнение рандомное, то вероятность получить более  менее
# упорядоченный массив изначально мала."""
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def i_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        replace_count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                replace_count += 1
        if replace_count == 0:
            break
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
# print(orig_list[:])
# print(bubble_sort(orig_list[:]))
# print(orig_list[:])
# print(i_bubble_sort(orig_list[:]))
# замеры 10
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "i_bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]
# print(orig_list[:])
# print(bubble_sort(orig_list[:]))
# print(orig_list[:])
# print(i_bubble_sort(orig_list[:]))
# замеры 100
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "i_bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
#  замеры 1000
orig_list = [randint(-100, 100) for _ in range(1000)]
print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit(
        "i_bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
