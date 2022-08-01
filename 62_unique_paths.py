# https://leetcode.com/problems/unique-paths/
from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def is_out_of_range(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return True
            return False

        @lru_cache
        def rec(x, y):
            if is_out_of_range(x, y):
                return 0
            if (x, y) == (0, 0):
                return 1
            return rec(x - 1, y) + rec(x, y - 1)

        return rec(m - 1, n - 1)


if __name__ == '__main__':
    assert Solution().uniquePaths(m = 3, n = 7) == 28
    assert Solution().uniquePaths(m = 3, n = 2) == 3