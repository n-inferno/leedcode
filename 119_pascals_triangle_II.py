# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def helper(index, current_row):
            if index == 0:
                return current_row

            result = []
            first, second = 0, 1
            while second < len(current_row):
                result.append(current_row[first] + current_row[second])
                first, second = second, second + 1
            return helper(index - 1, [1, *result, 1])

        return helper(rowIndex, [1])


if __name__ == '__main__':
    solution = Solution()
    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(2) == [1, 2, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(4) == [1, 4, 6, 4, 1]
    assert solution.getRow(5) == [1, 5, 10, 10, 5, 1]
