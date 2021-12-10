# https://leetcode.com/problems/number-of-1-bits/
from functools import reduce


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        counter = 0
        for i in binary:
            counter += (i == '1')

        return counter


if __name__ == '__main__':
    solution = Solution()
    assert solution.hammingWeight(n=11) == 3
    assert solution.hammingWeight(n=128) == 1
