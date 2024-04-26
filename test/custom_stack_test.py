import pytest


from src.custom_stack.custom_stack_class import (
    CustomStack,
    StackEmptyException,
    StackFullException,
)


class TestCustomStack:
    @pytest.fixture()
    def mock_custom_stack(self, mocker):
        mocker.patch("src.custom_stack.custom_stack_class.CustomStack", autospec=True)
        result = CustomStack(5)
        return result

    def test_push(self, mock_custom_stack):
        mock_custom_stack.push(1)
        mock_custom_stack.push(2)
        mock_custom_stack.push(3)
        assert mock_custom_stack.size() == 3
        with pytest.raises(StackFullException):
            for i in range(3):
                mock_custom_stack.push(i)

    def test_pop(self, mock_custom_stack):
        mock_custom_stack.push(1)
        mock_custom_stack.push(2)
        assert mock_custom_stack.pop() == 2
        assert mock_custom_stack.pop() == 1
        assert mock_custom_stack.size() == 0
        with pytest.raises(StackEmptyException):
            mock_custom_stack.pop()

    def test_top(self, mock_custom_stack):
        mock_custom_stack.push(1)
        mock_custom_stack.push(2)
        assert mock_custom_stack.top() == 2
        assert mock_custom_stack.size() == 2
        mock_custom_stack.pop()
        mock_custom_stack.pop()
        with pytest.raises(StackEmptyException):
            mock_custom_stack.top()
