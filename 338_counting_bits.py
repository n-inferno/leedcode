# https://leetcode.com/problems/counting-bits/
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]


if __name__ == '__main__':
    assert Solution().countBits(2) == [0, 1, 1]
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
