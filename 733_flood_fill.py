# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]

        def helper(x, y):
            if x not in range(len(image)) or y not in range(len(image[0])) or image[x][y] != old_color:
                return

            image[x][y] = newColor

            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                helper(x + dx, y + dy)

        if newColor == old_color:
            return image
        helper(sr, sc)
        return image


if __name__ == '__main__':
    solution = Solution()
    assert solution.floodFill(image=[[0, 0, 0], [1, 0, 0]], sr=1, sc=0, newColor=2) == [[0, 0, 0], [2, 0, 0]]
    assert solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2) == [[2, 2, 2], [2, 2, 0],
                                                                                                   [2, 0, 1]]
    assert solution.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2) == [[2, 2, 2], [2, 2, 2]]
    assert solution.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1) == [[0, 0, 0], [0, 1, 1]]
