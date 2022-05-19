# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        steps = (0, 1), (1, 0), (0, -1), (-1, 0)

        def dfs(x, y):
            nonlocal positions_cache
            if (x, y) in positions_cache:
                return positions_cache[(x, y)]

            points = []
            for dx, dy in steps:
                new_x, new_y = x + dx, y + dy
                if new_x in range(len(matrix)) and new_y in range(len(matrix[0])) and matrix[x][y] < matrix[new_x][new_y]:
                    points.append((new_x, new_y))

            res = 1
            res = max([res, *[1 + dfs(*point) for point in points]])
            positions_cache[(x, y)] = res
            return res

        positions_cache = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dfs(i, j)

        return max(positions_cache.values())


if __name__ == '__main__':
    assert Solution().longestIncreasingPath(matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert Solution().longestIncreasingPath(matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert Solution().longestIncreasingPath(matrix=[[1]]) == 1
