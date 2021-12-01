# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    # lambda sorting solution
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: x == 0)
        return nums

    # two pointers solution
    def moveZeroes(self, nums: List[int]) -> None:
        first = last = None
        i = 0
        while i < len(nums):
            if nums[i] == 0 and first is None:
                first = last = i
            elif first is not None:
                last += 1

            if nums[i] != 0 and first is not None:
                nums[i], nums[first] = nums[first], nums[i]
                first += 1
                last += 1

            i += 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.moveZeroes(nums=[0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes(nums=[0, 1, 3, 12, 0]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes(nums=[0]) == [0]
    assert solution.moveZeroes(nums=[0, 1]) == [1, 0]
    assert solution.moveZeroes(nums=[1, 0]) == [1, 0]
