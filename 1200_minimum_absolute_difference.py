# https://leetcode.com/problems/minimum-absolute-difference/
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = None
        for i in range(1, len(arr)):
            mod = abs(arr[i] - arr[i - 1])
            if minimum is None or mod < minimum:
                minimum = mod

        result = []
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == minimum:
                result.append([arr[i - 1], arr[i]])

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumAbsDifference(arr=[4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
    assert solution.minimumAbsDifference(arr=[1, 3, 6, 10, 15]) == [[1, 3]]
    assert solution.minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]
