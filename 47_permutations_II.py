# https://leetcode.com/problems/permutations-ii/
from typing import List, Tuple


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[Tuple[int]]:
        results = set()
        permutation_length = len(nums)

        def backtrack(index_taken, prefix):
            nonlocal nums, results, permutation_length
            if len(prefix) == permutation_length:
                results.add(prefix)
                return

            for i in range(len(nums)):
                if i not in index_taken:
                    index_taken.add(i)
                    backtrack(index_taken, (*prefix, nums[i]))
                    index_taken.discard(i)

        backtrack(set(), [])
        return list(results)


if __name__ == '__main__':
    assert Solution().permuteUnique(nums=[1, 1, 2]) == [(1, 2, 1), (2, 1, 1), (1, 1, 2)]
    assert Solution().permuteUnique(nums=[1, 2, 3]) == [(1, 3, 2), (1, 2, 3), (2, 1, 3), (3, 2, 1), (3, 1, 2), (2, 3, 1)]
