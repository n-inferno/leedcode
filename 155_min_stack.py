# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_element = float("inf")

    def find_min(self):
        if not self.stack:
            self.min_element = float("inf")
            return
        self.min_element = self.stack[0]
        for i in range(1, len(self.stack)):
            self.min_element = min(self.min_element, self.stack[i])

    def push(self, val: int) -> None:
        self.min_element = min(self.min_element, val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_element == popped:
            self.find_min()
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_element
