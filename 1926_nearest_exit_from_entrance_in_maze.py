from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = tuple(entrance)

        def is_exit(x, y):
            if (x, y) == entrance:
                return False
            if x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1:
                return True
            return False

        def is_in_maze(x, y):
            return 0 <= x < len(maze) and 0 <= y < len(maze[0])

        steps_dx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        q.append((entrance, 0))
        visited = set()

        while q:
            point, curr_steps = q.popleft()

            if point in visited:
                continue
            visited.add(point)

            for dx, dy in steps_dx:
                x, y = point[0] + dx, point[1] + dy

                if is_in_maze(x, y) and maze[x][y] == ".":
                    if is_exit(x, y):
                        return curr_steps + 1
                    q.append(((x, y), curr_steps + 1))

        return -1


if __name__ == "__main__":
    assert (
        Solution().nearestExit(
            [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
        )
        == 2
    )
    assert (
        Solution().nearestExit(
            [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
        )
        == 1
    )
    assert Solution().nearestExit([[".", "+"]], [0, 0]) == -1
