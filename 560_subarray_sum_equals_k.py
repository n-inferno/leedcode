# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        sums = defaultdict(int)
        sums[0] = 1
        curr_sum = 0
        for item in nums:
            curr_sum += item
            if curr_sum - k in sums:
                result += sums[curr_sum - k]
            sums[curr_sum] += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.subarraySum(nums=[1, -1, 1, 1, 1, 1], k=3) == 4
    assert solution.subarraySum(nums=[1, 1, 1], k=2) == 2
    assert solution.subarraySum(nums=[1, 2, 3], k=3) == 2
    assert solution.subarraySum(nums=[1], k=0) == 0
