from src.custom_stack.exceptions import StackEmptyException, StackFullException


class CustomStack:
    def __init__(self, pLimit):
        self.limit = pLimit
        self.elements = []

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.limit:
            raise StackFullException

        self.elements.append(element)

    def pop(self):
        if self.isEmpty():
            raise StackEmptyException
        return self.elements.pop()

    def top(self):
        if self.isEmpty():
            raise StackEmptyException
        return self.elements[-1]
