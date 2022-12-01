# https://leetcode.com/problems/word-search/description/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(x, y, pos, cache):
            if pos == len(word) - 1 and word[pos] == board[x][y]:
                return True
            elif word[pos] != board[x][y]:
                return False

            result = False
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                    if (new_x, new_y) not in cache:
                        cache.add((new_x, new_y))
                        result = result or backtrack(new_x, new_y, pos + 1, cache)
                        if result:
                            return result
                        cache.discard((new_x, new_y))

            return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0, {(i, j)}):
                        return True

        return False


if __name__ == '__main__':
    assert Solution().exist([["A"]], "A")
    assert Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    assert Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    assert not Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")
    assert Solution().exist([["A", "B", "C", "E"], ["B", "F", "D", "S"], ["A", "D", "E", "E"]], "ABFBC")
