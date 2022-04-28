# https://leetcode.com/problems/path-with-minimum-effort/
from typing import List


class Solution:
    # todo need -update, Time limit exceeded
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_absolute_diff = float('inf')

        def helper(x, y, max_difference, visited):
            nonlocal heights, min_absolute_diff
            if x == len(heights) - 1 and y == len(heights[0]) - 1:
                min_absolute_diff = min(max_difference, min_absolute_diff)
                return
            if (x, y) in visited:
                return
            visited.add((x, y))

            curren_height = heights[x][y]
            if max_difference < min_absolute_diff:
                if x > 0:
                    helper(x - 1, y, max(max_difference, abs(heights[x - 1][y] - curren_height)), visited.copy())
                if y > 0:
                    helper(x, y - 1, max(max_difference, abs(heights[x][y - 1] - curren_height)), visited.copy())
                if x < len(heights) - 1:
                    helper(x + 1, y, max(max_difference, abs(heights[x + 1][y] - curren_height)), visited.copy())
                if y < len(heights[0]) - 1:
                    helper(x, y + 1, max(max_difference, abs(heights[x][y + 1] - curren_height)), visited.copy())

        helper(0, 0, 0, set())
        return min_absolute_diff


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumEffortPath(heights=[[1, 10, 6, 7, 9, 10, 4, 9]]) == 9
    assert solution.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert solution.minimumEffortPath(heights=[[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert solution.minimumEffortPath(
        heights=[[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    ) == 0
    assert solution.minimumEffortPath(heights=[
        [4, 3, 4, 10, 5, 5, 9, 2],
        [10, 8, 2, 10, 9, 7, 5, 6],
        [5, 8, 10, 10, 10, 7, 4, 2],
        [5, 1, 3, 1, 1, 3, 1, 9],
        [6, 4, 10, 6, 10, 9, 4, 6],
    ]
    ) == 5
