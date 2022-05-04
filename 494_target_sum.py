# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def helper(current_sum=0, nums_pointer=0):
            if nums_pointer >= len(nums):
                return 1 if current_sum == target else 0

            if (current_sum, nums_pointer) in cache:
                return cache[(current_sum, nums_pointer)]

            new_pointer = nums_pointer + 1
            cache[(current_sum, nums_pointer)] = \
                helper(current_sum + nums[nums_pointer], new_pointer) + helper(current_sum - nums[nums_pointer], new_pointer)
            return cache[(current_sum, nums_pointer)]

        return helper()


if __name__ == '__main__':
    assert Solution().findTargetSumWays(nums=[1, 0], target=1) == 2
    assert Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3) == 5
    assert Solution().findTargetSumWays(nums=[1], target=1) == 1
    assert Solution().findTargetSumWays(nums=[6, 44, 30, 25, 8, 26, 34, 22, 10, 18, 34, 8, 0, 32, 13, 48, 29, 41, 16, 30],
                                        target=12) == 6692
    assert Solution().findTargetSumWays(nums=[7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13],
                                        target=3) == 5756
    assert Solution().findTargetSumWays(nums=[40, 2, 49, 50, 46, 6, 5, 23, 38, 45, 45, 17, 4, 26, 40, 33, 14, 9, 37, 24],
                                        target=7) == 5682
