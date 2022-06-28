# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        d = []
        possible_steps = ((0, -1), (-1, 0))
        for x in range(len(grid)):
            d.append([])
            for y in range(len(grid[x])):
                min_steps = float("inf")
                for dx, dy in possible_steps:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[x]):
                        min_steps = min(min_steps, d[new_x][new_y] + grid[x][y])

                if (x, y) != (0, 0):
                    d[-1].append(min_steps)
                else:
                    d[-1].append(grid[x][y])

        return d[-1][-1]


if __name__ == '__main__':
    assert Solution().minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution().minPathSum(grid=[[1, 2, 3], [4, 5, 6]]) == 12
