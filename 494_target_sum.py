# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counter = 0

        def helper(current_sum=0, nums_pointer=0):
            nonlocal counter, nums
            if nums_pointer >= len(nums):
                if current_sum == target:
                    counter += 1
                return

            new_pointer = nums_pointer + 1
            helper(current_sum + nums[nums_pointer], new_pointer)
            helper(current_sum - nums[nums_pointer], new_pointer)

        helper()
        print(counter)
        return counter


if __name__ == '__main__':
    assert Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3) == 5
    assert Solution().findTargetSumWays(nums=[1], target=1) == 1
    assert Solution().findTargetSumWays(nums=[6, 44, 30, 25, 8, 26, 34, 22, 10, 18, 34, 8, 0, 32, 13, 48, 29, 41, 16, 30],
                                        target=12) == 6692
    assert Solution().findTargetSumWays(nums=[7, 46, 36, 49, 5, 34, 25, 39, 41, 38, 49, 47, 17, 11, 1, 41, 7, 16, 23, 13],
                                        target=3) == 5756
