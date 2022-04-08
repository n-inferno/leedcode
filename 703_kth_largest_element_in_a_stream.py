# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import enum
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums

    def insertion_sort(self, element: int):
        for i in range(len(self.nums)):
            if self.nums[i] <= element:
                self.nums.insert(i, element)
                return
        self.nums.append(element)

    def add(self, val: int) -> int:
        self.insertion_sort(val)
        return self.nums[self.k - 1]


class Action(enum.Enum):
    INIT = 'init'
    ADD = 'add'


class TestKthLargest:

    def __init__(self):
        self.instance = None

    def make_operation(self, action: Action, *data):
        if action == Action.INIT:
            instance = KthLargest(*data)
            self.instance = instance
        elif action == Action.ADD:
            if self.instance is None:
                raise Exception
            return self.instance.add(*data)


if __name__ == '__main__':
    test = TestKthLargest()
    test.make_operation(Action.INIT, 3, [4, 5, 8, 2])
    assert test.make_operation(Action.ADD, 3) == 4
    assert test.make_operation(Action.ADD, 5) == 5
    assert test.make_operation(Action.ADD, 10) == 5
    assert test.make_operation(Action.ADD, 9) == 8
    assert test.make_operation(Action.ADD, 4) == 8
