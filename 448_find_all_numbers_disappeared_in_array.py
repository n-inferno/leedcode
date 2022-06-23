# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        for num in nums:
            all_nums.discard(num)
        return list(all_nums)
