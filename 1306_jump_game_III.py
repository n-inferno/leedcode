# https://leetcode.com/problems/jump-game-iii/
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()

        def helper(start):
            nonlocal seen
            if not 0 <= start < len(arr) or start in seen:
                return False
            if arr[start] == 0:
                return True
            seen.add(start)
            return helper(start + arr[start]) or helper(start - arr[start])

        return helper(start)


if __name__ == '__main__':
    solution = Solution()
    assert solution.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5) is True
    assert solution.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0) is True
    assert solution.canReach(arr=[3, 0, 2, 1, 2], start=2) is False
