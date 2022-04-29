# https://leetcode.com/problems/daily-temperatures/
from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = deque()
        for t in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[t]:
                stack.pop()
            if stack:
                result.appendleft(stack[-1][1] - t)
            else:
                result.appendleft(0)
            stack.append((temperatures[t], t))

        return list(result)


if __name__ == '__main__':
    solution = Solution()
    assert solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures(temperatures=[30, 40, 50, 60]) == [1, 1, 1, 0]
    assert solution.dailyTemperatures(temperatures=[30, 60, 90]) == [1, 1, 0]
