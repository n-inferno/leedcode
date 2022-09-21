# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum(i for i in nums if i % 2 == 0)
        results = []
        for val, index in queries:
            new_val = nums[index] + val
            if nums[index] % 2 == 0:
                sum_even -= nums[index]
            if new_val % 2 == 0:
                sum_even += new_val

            nums[index] = new_val
            results.append(sum_even)

        return results


if __name__ == '__main__':
    assert Solution().sumEvenAfterQueries(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]]) == [8, 6, 2, 4]
    assert Solution().sumEvenAfterQueries(nums=[1], queries=[[4, 0]]) == [0]
