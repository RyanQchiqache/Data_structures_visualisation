import pytest
from stacks.StackArray import StackArray
from src.stacks.Stack_Linked_List_Based import StackLinkedList


def test_stack_Array():
    stack = StackArray()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size() == 3
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.size() == 2
    assert not stack.is_empty()

    with pytest.raises(IndexError):
        stacks = StackArray()
        stacks.pop()


def test_stack_Linked_List():
    stacks = StackLinkedList()
    stacks.push(1)
    stacks.push(2)
    stacks.push(3)
    assert stacks.get_size() == 3
    assert stacks.peek() == 3
    assert stacks.pop() == 3
    assert stacks.get_size() == 2
    assert not stacks.is_empty()

    with pytest.raises(IndexError):
        stacks = StackLinkedList()
        stacks.pop()
