# https://leetcode.com/problems/range-sum-query-immutable/
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = []
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            self.sums.append(current)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (self.sums[left - 1] if left != 0 else 0)
