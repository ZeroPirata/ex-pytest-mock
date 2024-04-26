import pytest

from src.custom_stack.custom_stack_class import CustomStack
from src.custom_stack.exceptions import StackEmptyException
from src.custom_stack.number_asc_order import NumberAscOrder


class TestNumberAscOrder:
    @pytest.fixture()
    def custom_stack_with_numbers(self, mocker):
        stack = CustomStack(6)
        for number in [10, 5, 20, 3, 15, 8]:
            stack.push(number)
        return stack

    @pytest.fixture()
    def empty_custom_stack(self, mocker):
        return CustomStack(6)

    def test_sort_with_numbers(self, custom_stack_with_numbers):
        sorted_numbers = NumberAscOrder.sort(custom_stack_with_numbers)
        assert sorted_numbers == [3, 5, 8, 10, 15, 20]

    def test_sort_empty_stack(self, empty_custom_stack):
        with pytest.raises(StackEmptyException):
            NumberAscOrder.sort(empty_custom_stack)
