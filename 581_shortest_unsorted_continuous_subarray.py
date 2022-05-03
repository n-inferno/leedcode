# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        cp = nums.copy()
        cp.sort()
        p1, p2 = 0, len(cp) - 1
        start, end = None, None
        while p1 < len(nums) and p2 >= 0:
            if cp[p1] != nums[p1] and start is None:
                start = p1
            if cp[p2] != nums[p2] and end is None:
                end = p2
            if start is not None and end is not None:
                return end - start + 1
            p1 += 1
            p2 -= 1

        return 0


if __name__ == '__main__':
    assert Solution().findUnsortedSubarray(nums=[1, 2, 3, 5, 4]) == 2
    assert Solution().findUnsortedSubarray(nums=[1, 3, 5, 4, 2]) == 4
    assert Solution().findUnsortedSubarray(nums=[2, 3, 3, 2, 4]) == 3
    assert Solution().findUnsortedSubarray(nums=[1, 3, 2, 3, 3]) == 2
    assert Solution().findUnsortedSubarray(nums=[1, 2, 2, 2, 3]) == 0
    assert Solution().findUnsortedSubarray(nums=[1, 3, 2, 2, 2]) == 4
    assert Solution().findUnsortedSubarray(nums=[2, 6, 4, 8, 10, 9, 15]) == 5
    assert Solution().findUnsortedSubarray(nums=[2, 6, 1, 8, 10, 9, 15]) == 6
    assert Solution().findUnsortedSubarray(nums=[1, 2, 3, 4]) == 0
    assert Solution().findUnsortedSubarray(nums=[1]) == 0
