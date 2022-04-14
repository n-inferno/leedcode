# https://leetcode.com/problems/check-if-n-and-its-double-exist/
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for item in arr:
            if item * 2 in seen or item / 2 in seen:
                return True
            seen.add(item)

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.checkIfExist(arr=[10, 2, 5, 3]) is True
    assert solution.checkIfExist(arr=[7, 1, 14, 11]) is True
    assert solution.checkIfExist(arr=[3, 1, 7, 11]) is False
