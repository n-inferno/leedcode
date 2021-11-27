# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first, last = 0, len(nums) - 1
        while first <= last:
            mid = first + (last - first) // 2
            if nums[mid] > target:
                last = mid - 1
            if nums[mid] < target:
                first = mid + 1
            if nums[mid] == target:
                return mid

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12, 16], target=16) == 6
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12, 16], target=0) == 1
    assert solution.search(nums=[-1, 0, 3, 5, 9, 12, 16], target=-2) == -1
