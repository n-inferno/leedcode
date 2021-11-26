# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, current = nums[0], 0
        for i in range(len(nums)):
            current += nums[i]
            result = max(current, result)
            current = max(current, 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert solution.maxSubArray(nums=[5, 4, -1, 7, 8]) == 23
    assert solution.maxSubArray(nums=[1]) == 1
