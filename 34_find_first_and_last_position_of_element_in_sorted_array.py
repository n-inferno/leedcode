# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def search_bin(self, lst, target, first, last):
        for i in (first, last):
            if lst[i] == target:
                return i
        if last - first <= 1:
            return -1

        mid = (first + last) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            return self.search_bin(lst, target, mid, last)
        if lst[mid] > target:
            return self.search_bin(lst, target, first, mid)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = self.search_bin(nums, target, 0, len(nums) - 1) if nums else -1
        if n == -1:
            return [-1, -1]
        first, last = n, n
        track_first, track_last = False, False
        while not (track_first and track_last):
            if first > 0 and nums[first - 1] == target:
                first -= 1
            else:
                track_first = True
            if last < len(nums) - 1 and nums[last + 1] == target:
                last += 1
            else:
                track_last = True

        return [first, last]


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchRange(nums=[3, 3, 3], target=3) == [0, 2]
    assert solution.searchRange(nums=[1], target=1) == [0, 0]
    assert solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert solution.searchRange(nums=[5, 5, 7, 7, 8, 8, 10], target=5) == [0, 1]
    assert solution.searchRange(nums=[5, 5, 7, 7, 8, 8, 10], target=10) == [6, 6]
    assert solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert solution.searchRange(nums=[], target=0) == [-1, -1]
