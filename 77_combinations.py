# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def helper(start, combination):
            if len(combination) >= k:
                result.append(combination.copy())
                return
            for i in range(start, n + 1):
                combination.append(i)
                helper(i + 1, combination)
                combination.pop()
        helper(1, [])
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.combine(n=4, k=2) == [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]
    assert solution.combine(n=1, k=1) == [[1]]
