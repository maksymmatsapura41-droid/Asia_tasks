# Задание 1. Ручная трассировка Selection Sort
# Дан массив: [29, 10, 14, 37, 13].
#
# Запиши состояние массива после 1-й, 2-й и 3-й итераций внешнего цикла.
#
# Дан массив: [8, 3, 12, 5, 1, 9, 6]. Опорный элемент (pivot) - первый элемент (8).
#
# Kакие элементы попадут в список left, а какие- в right на первом
# шаге разделения.
#
#
# Задание 3. Подсчёт узлов в связном списке
# Напишите функцию count_nodes(head), которая принимает голову связного списка
# head и возвращает количество элементов в нём (если список пуст, вернуть 0).
#
#
# Задание 4. Построение и поиск в BST
# 1. Нарисуй бинарное дерево поиска, последовательно добавляя числа:
# 10, 5, 15, 3, 7, 12.
# 2. Куда попадёт число 6, если добавить его следующим?
# 3. Напиши функцию search_bst(root, target), которая возвращает True,
# если число target есть в дереве, и False - если нет.


# В каждом фрагменте кода ниже допущена одна логическая или техническая ошибка.
# Определи, что пойдёт не так при запуске, и исправьте код.

def sum_to_n(n):
    if n == 1:
        return 1
    n + sum_to_n(n - 1)


def quicksort_buggy(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_buggy(left) + quicksort_buggy(right)

def selection_sort_buggy(arr):
    for i in range(len(arr)):
        min_idx = 0
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def print_and_return_head(head):
    while head is not None:
        print(head.val)
        head = head.next
    return head


def search_bst_buggy(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst_buggy(root.right, target)
    else:
        return search_bst_buggy(root.left, target)


# Задачи
# Задача 1. Связный список + Рекурсия
# Условие: Напиши рекурсивную функцию sum_linked_list(head), которая
# вычисляет сумму всех значений в связном списке.


# Задача 2 Дан неотсортированный связный список 4 -> 2 -> 7 -> 1. Напиши
# функцию sort_linked_list(head), которая возвращает новый связный список с теми
# же элементами, но отсортированными по возрастанию (1 -> 2 -> 4 -> 7).


# Задача 3. Бинарное дерево поиска + Рекурсия (In-order обход)
# Условие: Дано бинарное дерево поиска (root). Напиши рекурсивную функцию
# get_sorted_elements(root), которая возвращает список всех элементов дерева в
# строго возрастающем порядке.
