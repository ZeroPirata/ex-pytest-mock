class StackEmptyException(Exception):
    def __init__(self, message="Stack is empty"):
        self.message = message
        super().__init__(self.message)


class StackFullException(Exception):
    def __init__(self, message="Stack is full"):
        self.message = message
        super().__init__(self.message)
