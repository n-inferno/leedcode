# https://leetcode.com/problems/game-of-life/
from copy import deepcopy
from typing import List


class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        max_x = len(board) - 1
        max_y = len(board[0]) - 1

        def get_state(x, y):
            counter_alive = 0
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if 0 <= x + dx <= max_x and 0 <= y + dy <= max_y:
                    counter_alive += board_copy[x + dx][y + dy]

            if board_copy[x][y]:
                if counter_alive < 2:
                    return 0
                elif 2 <= counter_alive <= 3:
                    return 1
                elif counter_alive > 3:
                    return 0

            if not board_copy[x][y] and counter_alive == 3:
                return 1

            return board_copy[x][y]

        board_copy = deepcopy(board)

        for i in range(len(board_copy)):
            for j in range(len(board_copy[i])):
                board[i][j] = get_state(i, j)


if __name__ == '__main__':
    solution = Solution()

    case1 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    solution.gameOfLife(case1)
    assert case1 == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    case2 = [[1, 1], [1, 0]]
    solution.gameOfLife(case2)
    assert case2 == [[1, 1], [1, 1]]
