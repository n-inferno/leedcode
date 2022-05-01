# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(permutation, used):
            nonlocal nums
            if len(permutation) == len(nums):
                result.append(permutation)
                return
            for i in nums:
                if i not in used:
                    permutation.append(i)
                    used.add(i)
                    helper(permutation.copy(), used.copy())
                    used.discard(i)
                    permutation.pop()

        helper([], set())
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.permute(nums=[1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert solution.permute(nums=[0, 1]) == [[0, 1], [1, 0]]
    assert solution.permute(nums=[1]) == [[1]]
