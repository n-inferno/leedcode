# https://leetcode.com/problems/combination-sum/
from collections import Counter
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        combinations = []

        def backtrack(combination, current_sum):
            nonlocal combinations, result
            if current_sum > target:
                return
            elif current_sum == target:
                count = Counter(combination)
                if count not in combinations:
                    combinations.append(count)
                    result.append(combination)

            for candidate in candidates:
                backtrack([*combination, candidate], current_sum + candidate)

        backtrack([], 0)
        return result


if __name__ == '__main__':
    assert Solution().combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum(candidates=[2, 3, 5], target=8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum(candidates=[2], target=1) == []
