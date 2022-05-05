# https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        elements = deque()
        while self.queue:
            elements.append(self.queue.popleft())
        self.queue.append(x)
        while elements:
            self.queue.append(elements.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
