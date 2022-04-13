# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List


class Solution:

    def get_next_step(self, curr=None):
        steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
        curr_ind = steps.index(curr) if curr else None
        next_ind = 0 if not curr or (curr_ind + 1 >= len(steps)) else curr_ind + 1
        return steps[next_ind]

    def check_borders(self, x, y, n):
        r = range(0, n)
        return x not in r or y not in r

    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]

        step = self.get_next_step()
        x, y = 0, 0
        for number in range(1, n ** 2 + 1):
            result[x][y] = number
            x += step[0]
            y += step[1]

            if self.check_borders(x, y, n) or result[x][y]:
                x -= step[0]
                y -= step[1]
                step = self.get_next_step(step)
                x += step[0]
                y += step[1]

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.generateMatrix(5) == [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8],
                                          [13, 12, 11, 10, 9]]
    assert solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert solution.generateMatrix(2) == [[1, 2], [4, 3]]
    assert solution.generateMatrix(1) == [[1]]
