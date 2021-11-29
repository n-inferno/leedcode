# https://leetcode.com/problems/squares-of-a-sorted-array/
from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])

    def sortedSquares(self, nums: List[int]) -> List[int]:
        low, up = 0, len(nums) - 1
        result = deque()
        i = len(nums) - 1
        while i >= 0:
            if abs(nums[low]) >= abs(nums[up]):
                result.appendleft(nums[low] * nums[low])
                low += 1
            else:
                result.appendleft(nums[up] * nums[up])
                up -= 1
            i -= 1

        return list(result)


if __name__ == '__main__':
    solution = Solution()
    assert solution.sortedSquares(nums=[-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert solution.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert solution.sortedSquares([-5, -3, -2, -1]) == [1, 4, 9, 25]
