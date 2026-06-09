# Необходимо с нуля написать структуру данных
# Односвязный список реализовав два класса: Node (узел) и LinkedList (управляющий класс).

class Node:
    pass


class LinkedList:
    def __init__(self):
        pass

    def append(self, value):
        """Добавить элемент в конец списка"""
        pass

    def prepend(self, value):
        """Добавить элемент в начало списка (новый head)"""
        pass

    def delete(self, value):
        """Удалить первое вхождение узла с указанным value"""
        pass

    def find(self, value) -> bool:
        """Вернуть True, если элемент есть в списке, иначе False"""
        pass

    def display(self):
        """Вывести список в формате: 1 -> 2 -> 3 -> None"""
        pass


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