# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)


if __name__ == '__main__':
    solution = Solution()
    assert solution.minCostToMoveChips([1, 2, 3]) == 1
    assert solution.minCostToMoveChips([2, 2, 2, 3, 3]) == 2
    assert solution.minCostToMoveChips([1, 1000000000]) == 1
