# https://leetcode.com/problems/k-diff-pairs-in-an-array/
from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        counter = Counter(nums)
        for item in counter:
            mod_look_for = item - k
            if mod_look_for in counter:
                if not (item == mod_look_for and counter[mod_look_for] < 2):
                    pairs.add(frozenset((item, mod_look_for)))
        return len(pairs)


if __name__ == '__main__':
    solution = Solution()
    assert solution.findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2
    assert solution.findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4
    assert solution.findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1
    assert solution.findPairs(nums=[1, 1, 1, 1, 1], k=0) == 1
