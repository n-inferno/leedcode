# https://leetcode.com/problems/01-matrix/
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result_mat = [[None] * len(mat[0]) for _ in range(len(mat))]
        steps = (0, 1), (1, 0), (0, -1), (-1, 0)

        q = deque()
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    q.append((row, col))
                    result_mat[row][col] = 0

        while q:
            x, y = q.popleft()

            for dx, dy in steps:
                new_x, new_y = x + dx, y + dy
                if new_x in range(len(mat)) and new_y in range(len(mat[0])):
                    if result_mat[new_x][new_y] is not None and result_mat[new_x][new_y] > result_mat[x][y] + 1:
                        result_mat[new_x][new_y] = result_mat[x][y] + 1
                        q.append((new_x, new_y))
                    elif result_mat[new_x][new_y] is None:
                        result_mat[new_x][new_y] = result_mat[x][y] + 1
                        q.append((new_x, new_y))

        return result_mat


if __name__ == '__main__':
    assert Solution().updateMatrix(mat=[[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]) == [[0, 1, 0], [0, 1, 0],
                                                                                                    [0, 1, 0], [0, 1, 0],
                                                                                                    [0, 1, 0]]
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
