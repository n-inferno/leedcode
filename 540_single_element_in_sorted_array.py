# https://leetcode.com/problems/single-element-in-a-sorted-array/
from functools import reduce
from typing import List


class Solution:
    # O(n) time, O(1) mem
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

    # O(log n) time, O(1) mem
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                return self.singleNonDuplicate(nums[:mid - 1])
            else:
                return self.singleNonDuplicate(nums[mid + 1:])
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                return self.singleNonDuplicate(nums[mid:])
            else:
                return self.singleNonDuplicate(nums[:mid])
        else:
            return nums[mid]


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert solution.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]) == 10
    assert solution.singleNonDuplicate(nums=[1]) == 1
    assert solution.singleNonDuplicate(nums=[1, 1, 2]) == 2
    assert solution.singleNonDuplicate(nums=[1, 2, 2]) == 1
    assert solution.singleNonDuplicate(nums=[1, 1, 2, 2, 3]) == 3
    assert solution.singleNonDuplicate(nums=[1, 2, 2, 3, 3]) == 1
