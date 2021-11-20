# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    # O(n^2) solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    #
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i = len(nums) - 1
        while nums[i] > target:
            i -= 1
        j = 0
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                i -= 1
            else:
                j += 1

        return [j, i]


if __name__ == '__main__':
    solution = Solution()
    assert set(solution.twoSum([2, 7, 11, 15], 9)) == {0, 1}
    assert set(solution.twoSum([3, 2, 4], 6)) == {1, 2}
    assert set(solution.twoSum([3, 3], 6)) == {0, 1}
