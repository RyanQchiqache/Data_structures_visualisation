"""
Simple Array Stack implementation (LIFO): Last in First Out
"""


class StackArray:

    def __init__(self):
        self.stack = []

    def push(self, value):
        """add value to the stack"""
        self.stack.append(value)

    def pop(self):
        """remove value from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """return the value at the top of the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
