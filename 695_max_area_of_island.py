# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def area(i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[i]) or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            return 1 + area(i - 1, j) + area(i + 1, j) + area(i, j + 1) + area(i, j - 1)

        return max(area(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxAreaOfIsland(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]) == 6
    assert solution.maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
