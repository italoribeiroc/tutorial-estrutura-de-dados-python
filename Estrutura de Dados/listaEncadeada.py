class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return '%s -> %s' % (self.data, self.next)

class ListaEncadeada:
    def __init__(self, head = None):
        self.head = head

    def __repr__(self) -> str:
        return '[' + str(self.head) + ']'

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self. head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def deleteWithValue(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next