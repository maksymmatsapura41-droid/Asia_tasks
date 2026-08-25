"""
Цель: Написать собственную реализацию структуры данных «Бинарное дерево поиска».

Что нужно сделать:
Класс Node (Узел дерева):

Хранит значение val.
Хранит ссылки на левого (left) и правого (right) потомка (по умолчанию None).

Класс BinarySearchTree (Дерево):
В конструкторе __init__ инициализирует пустое дерево (self.root = None).
Метод insert(val): Вставляет новое значение в дерево, 
сохраняя главное правило BST (все элементы слева меньше узла, все элементы справа — больше).
Метод search(val): Ищет значение в дереве. Возвращает True, если элемент найден, и False, если его нет.
Метод print tree :) 
"""

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else: 
            self.insert_recursive(self.root, val)

    def insert_recursive(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else: 
                self.insert_recursive(node.left, value)
        
        else: # value >= node.val
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive(node.right, value)

    def search(self, value):
        return self.search_recursive(self.root, value)

    def search_recursive(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        
        if val < node.val:
            return self.search_recursive(node.left, val)
        # if val > node.val:
        return self.search_recursive(node.right, val)

    # 653 Two Sum IV - Input is a BST
    def findTarget(self, k: int) -> bool:
        # k - val , set() 
        candidates = set()
        def find_pair(current_node):
            if not current_node:
                return False
            if k - current_node.val in candidates:
                return True
            candidates.add(current_node.val)
            return find_pair(current_node.left) or find_pair(current_node.right)
        
        return find_pair(self.root)    
        
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(2)
bst.insert(4)
bst.insert(0)
bst.insert(7)

print(bst.findTarget(28))



            
        

        
        
