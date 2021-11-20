# https://leetcode.com/problems/single-element-in-a-sorted-array/
from functools import reduce
from typing import List


class Solution:
    # O(n) time, O(1) mem
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert solution.singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]) == 10
