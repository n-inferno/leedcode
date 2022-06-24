# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_summa = summa = nums[0]
        for i in range(1, len(nums)):
            summa = max(summa + nums[i], nums[i])
            max_summa = max(summa, max_summa)

        return max_summa


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
    assert solution.maxSubArray(nums=[1]) == 1
