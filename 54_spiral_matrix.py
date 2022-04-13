# https://leetcode.com/problems/spiral-matrix/
import math
from typing import List


class Solution:
    def finished(self, y_left_border, y_right_border, x_up_border, x_down_border):
        return y_left_border > y_right_border or x_up_border > x_down_border

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        y_left_border, y_right_border, x_up_border, x_down_border = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        result = []
        round = 0
        x, y = 0, 0
        while not self.finished(y_left_border, y_right_border, x_up_border, x_down_border):
            result.extend(matrix[x][y_left_border:y_right_border + 1])
            x_up_border += 1
            y = y_right_border

            result.extend([matrix[i][y] for i in range(x_up_border, x_down_border + 1)])
            y_right_border -= 1
            x = x_down_border

            if self.finished(y_left_border, y_right_border, x_up_border, x_down_border):
                break

            result.extend([matrix[x][i] for i in range(y_right_border, y_left_border - 1, -1)])
            x_down_border -= 1
            y = y_left_border

            result.extend([matrix[i][y] for i in range(x_down_border, x_up_border - 1, -1)])
            y_left_border += 1

            round += 1
            y = x = round

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
