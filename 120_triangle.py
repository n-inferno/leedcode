# https://leetcode.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][-1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

        return min(triangle[-1])


if __name__ == '__main__':
    assert Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert Solution().minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [10, 11, 12, 13, 14]]) == 22
    assert Solution().minimumTotal(triangle=[[-10]]) == -10
