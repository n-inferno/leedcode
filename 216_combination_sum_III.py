# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = set()

        def backtrack(combination, current_sum, taken):
            nonlocal result
            if len(combination) == k:
                if current_sum == n:
                    result.add(frozenset(combination))
                return

            for i in range(1, 10):
                if i not in taken:
                    taken.add(i)
                    backtrack({*combination, i}, current_sum + i, taken)
                    taken.discard(i)

        backtrack(set(), 0, set())
        return [list(item) for item in result]


if __name__ == '__main__':
    assert Solution().combinationSum3(k=3, n=7) == [[1, 2, 4]]
    assert Solution().combinationSum3(k=3, n=9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert Solution().combinationSum3(k=4, n=1) == []
