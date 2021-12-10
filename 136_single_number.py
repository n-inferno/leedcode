# https://leetcode.com/problems/single-number/
from functools import reduce
from typing import List


class Solution:
    # seen method
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)

        return seen.pop()

    # bits manipulation
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


if __name__ == '__main__':
    solution = Solution()
    assert solution.singleNumber(nums=[2, 2, 1]) == 1
