# https://leetcode.com/problems/find-original-array-from-doubled-array/
from typing import List
from bisect import bisect_left


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        for i, num in enumerate(changed):
            if num != -1:
                double = bisect_left(changed, num * 2, i + 1)
                if double < len(changed) and num * 2 == changed[double]:
                    changed[double] = -1
                else:
                    return []
        return [i for i in changed if i != -1]


if __name__ == '__main__':
    assert Solution().findOriginalArray(changed=[1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert Solution().findOriginalArray(changed=[6, 3, 0, 1]) == []
    assert Solution().findOriginalArray(changed=[1]) == []
    assert Solution().findOriginalArray(changed=[5, 2, 4, 6, 8, 10, 1, 2, 3, 4]) == [1, 2, 3, 4, 5]
    assert Solution().findOriginalArray(changed=[3, 3, 3, 3]) == []
    assert Solution().findOriginalArray(changed=[4, 5, 2, 4, 6, 8, 10, 1, 2, 3]) == [1, 2, 3, 4, 5]
    assert Solution().findOriginalArray(changed=[4, 5, 2, 4, 6, 8, 1, 2, 3]) == []

