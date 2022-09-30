# https://leetcode.com/problems/find-k-closest-elements/
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pos = bisect_left(arr, x)

        if pos == 0:
            return arr[:k]
        elif pos == len(arr):
            return arr[-k:]

        if x - arr[pos] <= arr[pos - 1] - x:
            i, j = pos - 1, pos
        else:
            i, j = pos, pos + 1

        while j - i < k and (i > 0 or j <= len(arr)):
            if i == 0:
                j += 1
            elif j == len(arr):
                i -= 1

            elif abs(x - arr[i - 1]) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1

        return arr[i:j]


if __name__ == '__main__':
    assert Solution().findClosestElements([1, 3], 1, 2) == [1]
    assert Solution().findClosestElements([1], 1, 1) == [1]
    assert Solution().findClosestElements([1], 1, 5) == [1]
    assert Solution().findClosestElements([1], 1, 0) == [1]

    assert Solution().findClosestElements([1, 2], 1, 1) == [1]
    assert Solution().findClosestElements([1, 2], 1, 3) == [2]
    assert Solution().findClosestElements([1, 2], 2, 3) == [1, 2]
    assert Solution().findClosestElements([1, 2], 2, 0) == [1, 2]
    assert Solution().findClosestElements([1, 2, 4, 5, 7], 5, 6) == [1, 2, 4, 5, 7]

    assert Solution().findClosestElements([1, 2, 3, 4, 5, 6], 3, 4) == [3, 4, 5]

    assert Solution().findClosestElements([1, 2, 3, 3, 5, 6], 3, 4) == [3, 3, 5]
    assert Solution().findClosestElements([1, 2, 3, 5, 5, 6], 3, 3) == [1, 2, 3]

    assert Solution().findClosestElements([1, 1, 1, 10, 10, 10], 1, 9) == [10]

    assert Solution().findClosestElements([1, 1, 1, 10, 10, 10], 1, 6) == [10]
    assert Solution().findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5) == [3, 3, 4]

    assert Solution().findClosestElements([0, 2, 2, 3, 4, 6, 7, 8, 9, 9], 4, 5) == [3, 4, 6, 7]
