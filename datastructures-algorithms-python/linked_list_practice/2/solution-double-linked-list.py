class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.next: Node | None = next
        self.prev: Node | None = prev


class LinkedList:
    def __init__(self, init_data: list | None = None) -> None:
        if init_data:
            for index, value in enumerate(init_data):
                if value:
                    if index == 0:
                        self.head = Node(value)
                    else:
                        self.insert_at_end(value)
                else:
                    self.head = None
        else:
            self.head = None

    def print(self) -> None:
        if self.head:
            current = self.head
            str = ""
            while current:
                if current.prev:
                    str += "<"
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

    def insert_at_beginning(self, data) -> None:
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node
        if self.head.next:
            self.head.next.prev = node

    def insert_at_end(self, data) -> None:
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            node.prev = current
            if current.next:
                current.next.prev = node
            current.next = node
        else:
            self.head = node

    def insert_at(self, data, index) -> None:
        if index < 0 | index > self.get_length() - 1:
            raise Exception('Invalid index')

        current = self.head
        currentIndex = 0

        while current:
            if currentIndex + 1 == index:
                node = Node(data, current, current.next)
                current.next = node
                if current.next.next:
                    current.next.next.prev = node
                break
            currentIndex += 1
            current = current.next

    def insert_after_value(self, after_value, value) -> None:
        if self.head:
            current = self.head
            while current:
                if current.data == after_value:
                    node = Node(value, current, current.next)
                    current.next = node
                    if current.next.next:
                        current.next.next.prev = node
                    break
                current = current.next
        else:
            raise Exception('List is empty')

    def remove_at_beginning(self) -> None:
        if self.head:
            if self.head.next:
                self.head = self.head.next
            if self.head.next:
                self.head.next.prev = self.head
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
            if currentIndex == index:
                if current.prev:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                        break
                else:
                    if current.next:
                        current.next.prev = None
                        self.head = current.next
                        break
                    else:
                        self.head = None
            current = current.next
            currentIndex += 1

    def remove_by_value(self, value) -> None:
        if self.head:
            current = self.head
            counter = 0
            while current:
                if current.data == value:
                    self.remove_at(counter)
                current = current.next
                counter += 1
        else:
            raise Exception('Empty List')


el1 = 'Banana'
el2 = 'Orange'
el3 = 'Apple'
el4 = 'Dragonfruit'
ll = LinkedList([el1, el2, el3])
ll.print()
