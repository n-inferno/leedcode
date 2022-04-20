# https://leetcode.com/problems/design-circular-queue/
from typing import List, Optional


class MyCircularQueue:

    def __init__(self, k: int):
        self.queue: List[Optional[int]] = [None for _ in range(k)]
        self.k = k
        self.counter = 0
        self.head = self.tail = None

    def __repr__(self):
        return str(self.queue)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.head is None:
            self.head = 0

        if self.tail is None or self.tail == self.k - 1:
            self.tail = 0
        elif self.tail < self.k - 1:
            self.tail += 1

        self.queue[self.tail] = value
        self.counter += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = None
        if self.head < self.k - 1:
            self.head += 1
        else:
            self.head = 0
        self.counter -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter == self.k
