# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums):
            return
        k %= len(nums)
        j = len(nums) - 1
        nums.extend([None for _ in range(k)])
        i = len(nums) - 1

        while i >= 0:
            nums[j], nums[i] = nums[i], nums[j]
            j -= 1
            i -= 1

        for i in range(k):
            nums.pop()



if __name__ == '__main__':
    solution = Solution()
    assert solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
    assert solution.rotate(nums=[-1, -100, 3, 99], k=2) == [3, 99, -1, -100]
    assert solution.rotate(nums=[1, 2, 3, 4, 5, 6], k=11) == [2, 3, 4, 5, 6, 1]
