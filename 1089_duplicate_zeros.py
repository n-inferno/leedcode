# https://leetcode.com/problems/duplicate-zeros/
from collections import deque
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        stack = deque()
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                stack.append(0)
            stack.append(arr[i])
            arr[i] = stack.popleft()
            i += 1


if __name__ == '__main__':
    solution = Solution()
    case1 = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(case1)
    assert case1 == [1, 0, 0, 2, 3, 0, 0, 4]

    case2 = [1, 2, 3]
    solution.duplicateZeros(case2)
    assert case2 == [1, 2, 3]
