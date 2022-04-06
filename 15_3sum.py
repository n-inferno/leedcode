# https://leetcode.com/problems/3sum/
from collections import Counter
from itertools import permutations


class Solution:
    def _check_equal_triplet(self, results, to_add):
        for c in permutations(to_add, 3):
            if c in results:
                return False
        return True

    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums_map = Counter(nums)

        results = set()
        for x in nums_map:
            if nums_map[x]:
                nums_map[x] -= 1
                for y in nums_map:
                    if nums_map[y]:
                        nums_map[y] -= 1
                        search = 0 - (x + y)
                        if search in nums_map and nums_map[search] and self._check_equal_triplet(results, (x, y, search)):
                            results.add((x, y, search))
                        nums_map[y] += 1
                nums_map[x] += 1

        return results


if __name__ == '__main__':
    solution = Solution()
    assert solution.threeSum(nums=[3, 0, -2, -1, 1, 2]) == {(3, -2, -1), (0, -1, 1), (0, -2, 2)}
    assert solution.threeSum(nums=[-1, 0, 1, 2, -1, -4]) == {(-1, 0, 1), (-1, -1, 2)}
    assert solution.threeSum(nums=[-1, 0, 1, 0]) == {(-1, 0, 1)}
    assert solution.threeSum(nums=[]) == []
    assert solution.threeSum(nums=[0]) == []
