class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print(self) -> None:
        if self.head:
            current = self.head
            str = ""
            while current:
                str += current.data + "-->"
                current = current.next

            print(str)
        else:
            raise Exception('Empty linked list')

    def get_length(self) -> int:
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def insert_at_beginning(self, node) -> None:
        if self.head:
            node.next = self.head
        self.head = node

    def insert_at_end(self, node) -> None:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def insert_at(self, node, index) -> None:
        if index < 0 | index > self.get_length() - 1:
            raise Exception('Invalid index')

        current = self.head
        currentIndex = 0

        while current:
            if currentIndex + 1 == index:
                node.next = current.next
                current.next = node
                break
            currentIndex += 1
            current = current.next

    def remove_at_beginning(self) -> None:
        if self.head:
            self.head = self.head.next
        else:
            raise Exception('Empty linked list')

    def remove_at_end(self) -> None:
        if self.head:
            current = self.head
            while current.next:
                if current.next.next is None:
                    current.next = None
        else:
            raise Exception('Empty linked list')

    def remove_at(self, index) -> None:
        if index < 0 | index > self.get_length() - 1:
            raise Exception('Invalid index')

        current = self.head
        currentIndex = 0

        while current:
            if currentIndex + 1 == index:
                current.next = current.next.next
                break
            currentIndex += 1
            current = current.next


el1 = Node("Apple")
el2 = Node("Banana")
el3 = Node("Orange")

linkedList = LinkedList()
linkedList.insert_at_beginning(el1)
linkedList.insert_at_end(el2)
linkedList.print()
linkedList.insert_at(el3, 1)
linkedList.print()
linkedList.remove_at(1)
linkedList.print()
