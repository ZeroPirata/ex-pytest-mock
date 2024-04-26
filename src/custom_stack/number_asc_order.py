from typing import List
from src.custom_stack.custom_stack_class import CustomStack
from src.custom_stack.exceptions import StackEmptyException


class NumberAscOrder:
    @staticmethod
    def sort(stack: CustomStack) -> List[int]:
        if stack.isEmpty():
            raise StackEmptyException("A pilha está vazia")
        numbers = []
        while not stack.isEmpty():
            numbers.append(stack.pop())
        numbers.sort()
        return numbers
