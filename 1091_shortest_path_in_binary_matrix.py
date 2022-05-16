# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        directions = (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)
        q = deque([(0, 0, 1)])

        visited = {(0, 0)}
        while q:
            x, y, steps = q.popleft()
            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return steps

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if new_x in range(len(grid)) and new_y in range(len(grid[0])) and \
                        not grid[new_x][new_y] and not (new_x, new_y) in visited:
                    q.append((new_x, new_y, steps + 1))
                    visited.add((new_x, new_y))

        return -1


if __name__ == '__main__':
    assert Solution().shortestPathBinaryMatrix(grid=[[0, 1, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert Solution().shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert Solution().shortestPathBinaryMatrix(grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert Solution().shortestPathBinaryMatrix(grid=[[0, 1], [1, 0]]) == 2
