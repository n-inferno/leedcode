# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]

        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1

        return max([dp[i][j] for i in range(len(dp)) for j in range(len(dp[i]))])


if __name__ == '__main__':
    assert Solution().findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]) == 3
    assert Solution().findLength(nums1=[0, 0, 0, 0, 0], nums2=[0, 0, 0, 0, 0]) == 5
    assert Solution().findLength(nums1=[0, 0], nums2=[1, 1, 1]) == 0
    assert Solution().findLength(nums1=[0, 0], nums2=[1, 1, 0]) == 1
