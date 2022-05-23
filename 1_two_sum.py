# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i


if __name__ == '__main__':
    solution = Solution()
    assert set(solution.twoSum([2, 7, 11, 15], 9)) == {0, 1}
    assert set(solution.twoSum([3, 2, 4], 6)) == {1, 2}
    assert set(solution.twoSum([3, 3], 6)) == {0, 1}
