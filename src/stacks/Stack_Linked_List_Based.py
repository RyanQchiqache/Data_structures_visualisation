class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """Add a new element to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            raise IndexError('Pop from an empty stack')
        remove_value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return remove_value

    def peek(self):
        """Return the top element of the stack without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
