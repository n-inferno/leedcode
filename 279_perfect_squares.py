# https://leetcode.com/problems/perfect-squares/
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        minimal_elements = []
        for i in range(1, int(n ** 0.5) + 1):
            v = i ** 2
            q.append((v, 1))
            minimal_elements.append(v)

        cache = set()
        while q:
            curr_sum, level = q.popleft()
            if curr_sum == n:
                return level

            for el in minimal_elements:
                if el + curr_sum > n:
                    break
                to_add_v = (el + curr_sum, level + 1)
                if to_add_v not in cache:
                    cache.add(to_add_v)
                    q.append((el + curr_sum, level + 1))

        return 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.numSquares(n=12) == 3
    assert solution.numSquares(n=0) == 0
    assert solution.numSquares(n=1) == 1
    assert solution.numSquares(n=16) == 1
    assert solution.numSquares(n=13) == 2
    assert solution.numSquares(n=7168) == 4
