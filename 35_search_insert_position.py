# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while last > first + 1:
            mid = first + (last - first) // 2
            if nums[mid] > target:
                last = mid
            elif nums[mid] < target:
                first = mid
            else:
                return mid
        if nums[last] < target:
            return last + 1
        elif nums[first] < target:
            return last
        else:
            return first


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
    assert solution.searchInsert(nums=[1, 3, 4, 5, 6], target=5) == 3
    assert solution.searchInsert(nums=[1, 3, 4, 5, 6], target=1) == 0
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    assert solution.searchInsert(nums=[1, 3, 5, 6], target=0) == 0
    assert solution.searchInsert(nums=[1], target=0) == 0
