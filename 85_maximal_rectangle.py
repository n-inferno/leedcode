# https://leetcode.com/problems/maximal-rectangle/
from typing import List


class Solution:
    def maxSquare(self, row):
        max_len, max_high = 0, 0
        curr_len, curr_high = 0, 0
        for item in row:
            if item == 0:
                break
            if max_high == 0:
                curr_high = max_high = item
                max_len = curr_len = 1
            else:
                minimum = min(curr_high, item)
                curr_len += 1
                curr_high = min(curr_high, item)
                if minimum * curr_len > max_len * max_high:
                    max_len = curr_len
                    max_high = minimum

        return max_len, max_high

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        hystogram = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_rect = 0
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[i]):
                if matrix[i][j] != '0':
                    prev = hystogram[i - 1][j] if i > 0 else 0
                    hystogram[i][j] = prev + 1
                j += 1

            j = 0
            max_len, max_high = 0, 0
            while j < len(matrix[i]):
                curr_len, curr_high = self.maxSquare(hystogram[i][j:])
                if max_high * max_len < curr_high * curr_len:
                    max_len, max_high = curr_len, curr_high
                j += 1
            max_rect = max(max_rect, max_len * max_high)
            i += 1

        return max_rect


if __name__ == '__main__':
    solution = Solution()
    assert solution.maximalRectangle(
        matrix=[["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]) == 6
    assert solution.maximalRectangle(matrix=[["1", "1", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"]]) == 6
    assert solution.maximalRectangle(matrix=[]) == 0
    assert solution.maximalRectangle(matrix=[["0"]]) == 0
    assert solution.maximalRectangle(matrix=[["1", "0", "0", "0", "1"],
                                             ["1", "1", "0", "1", "1"],
                                             ["1", "1", "1", "1", "1"]]) == 5
