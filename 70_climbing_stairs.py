# https://leetcode.com/problems/climbing-stairs/
from functools import lru_cache


class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    solution = Solution()
    assert solution.climbStairs(n=2) == 2
    assert solution.climbStairs(n=3) == 3
