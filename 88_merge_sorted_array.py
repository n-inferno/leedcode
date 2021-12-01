# https://leetcode.com/problems/merge-sorted-array/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m
        for item in nums2:
            nums1[i] = item
            pointer = i
            while pointer > 0 and nums1[pointer] <= nums1[pointer - 1]:
                nums1[pointer], nums1[pointer - 1] = nums1[pointer - 1], nums1[pointer]
                pointer -= 1
            i += 1

        return nums1


if __name__ == '__main__':
    solution = Solution()
    assert solution.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [1, 2, 2, 3, 5, 6]
    assert solution.merge(nums1=[1], m=1, nums2=[], n=0) == [1]
    assert solution.merge(nums1=[0], m=0, nums2=[1], n=1) == [1]
    assert solution.merge(nums1=[2, 0], m=1, nums2=[1], n=1) == [1, 2]
    assert solution.merge(nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0], m=6, nums2=[1, 2, 2], n=3) == [-1, 0, 0, 1, 2, 2, 3, 3, 3]
