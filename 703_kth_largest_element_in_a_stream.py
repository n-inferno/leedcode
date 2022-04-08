# https://leetcode.com/problems/kth-largest-element-in-a-stream/
import enum
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums[:k]

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort(reverse=True)
        elif val > self.nums[-1]:
            self.nums.pop()
            self.nums.append(val)
            self.nums.sort(reverse=True)
        return self.nums[-1]


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


def case1():
    test = TestKthLargest()
    test.make_operation(Action.INIT, 3, [4, 5, 8, 2])
    assert test.make_operation(Action.ADD, 3) == 4
    assert test.make_operation(Action.ADD, 5) == 5
    assert test.make_operation(Action.ADD, 10) == 5
    assert test.make_operation(Action.ADD, 9) == 8
    assert test.make_operation(Action.ADD, 4) == 8


def case2():
    test = TestKthLargest()
    test.make_operation(Action.INIT, 1, [])
    assert test.make_operation(Action.ADD, -3) == -3
    assert test.make_operation(Action.ADD, -2) == -2
    assert test.make_operation(Action.ADD, -4) == -2
    assert test.make_operation(Action.ADD, 0) == 0
    assert test.make_operation(Action.ADD, 4) == 4


def case3():
    test = TestKthLargest()
    test.make_operation(Action.INIT, 2, [0])
    assert test.make_operation(Action.ADD, -1) == -1
    assert test.make_operation(Action.ADD, 1) == 0
    assert test.make_operation(Action.ADD, -2) == 0
    assert test.make_operation(Action.ADD, -4) == 0
    assert test.make_operation(Action.ADD, 3) == 1


if __name__ == '__main__':
    case1()
    case2()
    case3()
