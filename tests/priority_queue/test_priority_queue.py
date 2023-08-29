import pytest
from ting_file_management.priority_queue import PriorityQueue
from tests.priority_queue.mocks2 import file1, file2


def test_basic_priority_queueing():
    priority_example = PriorityQueue()
    priority_example.enqueue(file1)
    priority_example.enqueue(file2)

    assert priority_example.is_priority(file1) is True
    assert priority_example.is_priority(file2) is False

    assert priority_example.__len__() == 2
    assert priority_example.search(0) == file1
    assert priority_example.search(1) == file2

    with pytest.raises(IndexError):
        priority_example.search(999)

    assert priority_example.dequeue() == file1
    assert priority_example.dequeue() == file2
    assert priority_example.dequeue() is None
