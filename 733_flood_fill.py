# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def helper(self, image, i, j, current_color, new_color):
        if not 0 <= i < len(image) or not 0 <= j < len(image[i]) or image[i][j] != current_color:
            return
        image[i][j] = new_color
        self.helper(image, i - 1, j, current_color, new_color)
        self.helper(image, i, j + 1, current_color, new_color)
        self.helper(image, i + 1, j, current_color, new_color)
        self.helper(image, i, j - 1, current_color, new_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        if color == newColor:
            return image
        self.helper(image, sr, sc, color, newColor)
        return image


if __name__ == '__main__':
    solution = Solution()
    assert solution.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2) == [[2, 2, 2], [2, 2, 0],
                                                                                                   [2, 0, 1]]
    assert solution.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, newColor=2) == [[2, 2, 2], [2, 2, 2]]
    assert solution.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1) == [[0, 0, 0], [0, 1, 1]]
