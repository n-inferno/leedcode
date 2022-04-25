# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        is_island = False

        def helper(x, y):
            nonlocal visited, is_island
            if (x, y) in visited or x not in range(len(grid)) or y not in range(len(grid[0])):
                return
            visited.add((x, y))
            if grid[x][y] == "0":
                return
            is_island = True
            for m, n in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                helper(m, n)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                helper(i, j)
                if is_island:
                    islands += 1
                is_island = False

        return islands


if __name__ == '__main__':
    solution = Solution()
    assert solution.numIslands(grid=[
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    ) == 1
    assert solution.numIslands(grid=[
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ) == 3
