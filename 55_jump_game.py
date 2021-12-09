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

    # greedy recursive
    def canJump(self, nums: List[int]) -> bool:
        sys.setrecursionlimit(11000)

        def helper(goal):
            if goal == 0:
                return True
            for i in range(goal - 1, -1, -1):
                if nums[i] + i >= goal:
                    return helper(i)
            else:
                return False

        return helper(len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    assert solution.canJump(nums=[2, 3, 1, 1, 4]) is True
    assert solution.canJump(nums=[3, 2, 1, 0, 4]) is False
    assert solution.canJump(nums=[1]) is True
