# Необходимо с нуля написать структуру данных
# Односвязный список реализовав два класса: Node (узел) и LinkedList (управляющий класс).

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


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.display()  # Ожидается: 10 -> 20 -> None

    ll.prepend(5)
    ll.display()  # Ожидается: 5 -> 10 -> 20 -> None

    print("Найдено 10:", ll.find(10))  # Ожидается: True
    print("Найдено 100:", ll.find(100))  # Ожидается: False

    ll.delete(10)
    ll.display()  # Ожидается: 5 -> 20 -> None

    ll.delete(5)
    ll.display()  # Ожидается: 20 -> None
