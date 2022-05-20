# https://leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        visited = {}

        def dp(x, y, curr):
            if (x, y) == (0, 0):
                return curr + 1 if obstacleGrid[0][0] != 1 else curr
            if x not in range(len(obstacleGrid)) or y not in range(len(obstacleGrid[0])) or obstacleGrid[x][y] == 1:
                return 0

            if (x, y) not in visited:
                visited[(x, y)] = dp(x - 1, y, curr) + dp(x, y - 1, curr)

            return visited[(x, y)]

        return dp(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, 0)


if __name__ == '__main__':
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]) == 1
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0]]) == 1
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[1]]) == 0
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[1, 0]]) == 0
    assert Solution().uniquePathsWithObstacles(obstacleGrid=[[0, 1]]) == 0
