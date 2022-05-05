# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.stack = []
        self.enqueued = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.enqueued:
            return self.enqueued.pop()
        self._enqueue_stack()
        return self.enqueued.pop()

    def peek(self) -> int:
        if self.enqueued:
            return self.enqueued[-1]
        self._enqueue_stack()
        return self.enqueued[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.enqueued) == 0

    def _enqueue_stack(self):
        while self.stack:
            self.enqueued.append(self.stack.pop())
