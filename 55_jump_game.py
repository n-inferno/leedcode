# https://leetcode.com/problems/jump-game/
import sys
from typing import List


class Solution:
    # brute force (time limit exceeded)
    def canJump(self, nums: List[int]) -> bool:
        seen = set()

        def helper(start=0):
            nonlocal seen
            if not 0 <= start < len(nums) or start in seen:
                return False
            if start == len(nums) - 1:
                return True
            seen.add(start)
            return any([helper(start + i) for i in range(nums[start], 0, -1)])

        return helper()

    # greedy - O(n)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return True if goal == 0 else False


if __name__ == '__main__':
    solution = Solution()
    assert solution.canJump(nums=[2, 3, 1, 1, 4]) is True
    assert solution.canJump(nums=[3, 2, 1, 0, 4]) is False
    assert solution.canJump(nums=[1]) is True
    assert solution.canJump(
        nums=[8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5,
              1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0,
              1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]) is True
