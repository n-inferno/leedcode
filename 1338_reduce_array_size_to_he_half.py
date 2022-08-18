# https://leetcode.com/problems/reduce-array-size-to-the-half/
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        sorted_elements = sorted(Counter(arr), key=lambda x: -c[x])

        size = len(arr)
        removed = 0

        for el in sorted_elements:
            if size <= len(arr) // 2:
                break
            size -= c[el]
            removed += 1

        return removed
