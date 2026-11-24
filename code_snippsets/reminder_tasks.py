class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """Добавить элемент в начало списка (новый head)"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Удалить первое вхождение узла с указанным value"""
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next 

    def find(self, value) -> bool:
        """Вернуть True, если элемент есть в списке, иначе False"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def display(self):
        """Вывести список в формате: 1 -> 2 -> 3 -> None"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) + " -> None" if values else 'None')

# Задача 1. Связный список + Рекурсия
# Условие: Напиши рекурсивную функцию sum_linked_list(head), которая
# вычисляет сумму всех значений в связном списке.

    def sum_linked_list(self, head):
        if head is None:
            return 0   
        return head.value + self.sum_linked_list(head.next)

# Задача 2 Дан неотсортированный связный список 4 -> 2 -> 7 -> 1. Напиши
# функцию sort_linked_list(head), которая возвращает новый связный список с теми
# же элементами, но отсортированными по возрастанию (1 -> 2 -> 4 -> 7).

    def sort_linked_list(self, head):
        pass


if __name__ == "__main__":
    ll = LinkedList()
# 4 -> 2 -> 7 -> 1
    ll.append(4)
    ll.append(2)
    ll.append(7)
    ll.append(1)
    ll.display()
    print(ll.sum_linked_list(ll.head))
    
# Задание 1. Ручная трассировка Selection Sort
# Дан массив: [29, 10, 14, 37, 13].
#
# Запиши состояние массива после 1-й, 2-й и 3-й итераций внешнего цикла.
# [10, 29, 14, 37, 13]
# [10, 13, 14, 37, 29]
# [10, 13, 14, 37, 29]
# [10, 13, 14, 29, 37]

# Дан массив: [8, 3, 12, 5, 1, 9, 6]. Опорный элемент (pivot) - первый элемент (8).
#
# Kакие элементы попадут в список left, а какие- в right на первом
# шаге разделения.
# [3, 5, 1, 6]
# [9, 12]
# [8]

# Задание 3. Подсчёт узлов в связном списке
# Напишите функцию count_nodes(head), которая принимает голову связного списка
# head и возвращает количество элементов в нём (если список пуст, вернуть 0).

def count_nodes(head):
    total_nodes = 0
    current_node = head
    while current_node:
        total_nodes += 1
        current_node = current_node.next

    return total_nodes

# Задание 4. Построение и поиск в BST
# 1. Нарисуй бинарное дерево поиска, последовательно добавляя числа:
# 10, 5, 15, 3, 7, 12.
# 
# 2. Куда попадёт число 6, если добавить его следующим?
# 3. Напиши функцию search_bst(root, target), которая возвращает True,
# если число target есть в дереве, и False - если нет.

def search_bst(root, target):
    if root is None:
        return False
    if target == root.value:
            return True
    if target < root.value:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

# В каждом фрагменте кода ниже допущена одна логическая или техническая ошибка.
# Определи, что пойдёт не так при запуске, и исправьте код.

def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)

def quicksort_buggy(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_buggy(left) + pivot + quicksort_buggy(right)

def selection_sort_buggy(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def print_and_return_head(head):
    current_node = head
    while current_node is not None:
        print(current_node.val)
        current_node = current_node.next
    return head

def search_bst_buggy(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst_buggy(root.left, target)
    else:
        return search_bst_buggy(root.right, target)

# Задачи

# Задача 3. Бинарное дерево поиска + Рекурсия (In-order обход)
# Условие: Дано бинарное дерево поиска (root). Напиши рекурсивную функцию
# get_sorted_elements(root), которая возвращает список всех элементов дерева в
# строго возрастающем порядке.


# Задача 4. Найди максимум в связном списке (итеративно).
# Если список пуст — верни None.
# def find_max(head): ...


# Задача 5. Рекурсивно найди длину связного списка.
# (То же, что count_nodes, но обязательно через рекурсию.)
# def list_length(head): ...

