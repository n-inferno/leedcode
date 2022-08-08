# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {len(nums) - 1: 1}
        result = 1
        for i in range(len(nums) - 2, -1, -1):
            curr_max = 1
            for j in range(i + 1, len(nums)):
                val = cache.get(j)
                if val and nums[j] > nums[i]:
                    curr_max = max(curr_max, val + 1)

            cache[i] = curr_max
            result = max(curr_max, result)
        return result


if __name__ == '__main__':
    assert Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7]) == 1
