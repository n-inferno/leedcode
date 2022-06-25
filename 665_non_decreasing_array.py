# https://leetcode.com/problems/non-decreasing-array/
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True

        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count >= 1:
                    return False
                count += 1
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]

        return True


if __name__ == '__main__':
    assert Solution().checkPossibility(nums=[4, 2, 3])
    assert not Solution().checkPossibility(nums=[4, 2, 1])
    assert Solution().checkPossibility(nums=[1, 10, 2])
    assert not Solution().checkPossibility(nums=[1, 10, 11, 10, 2])
    assert not Solution().checkPossibility(nums=[3, 4, 2, 3])
