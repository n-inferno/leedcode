# https://leetcode.com/problems/find-pivot-index/
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summa = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == summa - nums[i]:
                return i

            left += nums[i]
            summa -= nums[i]

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.pivotIndex(nums=[1, 7, 3, 6, 5, 6]) == 3
    assert solution.pivotIndex(nums=[1, 2, 3]) == -1
    assert solution.pivotIndex(nums=[2, 1, -1]) == 0
