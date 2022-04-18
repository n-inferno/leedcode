# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        i = len(arr) - 1
        while i >= 0:
            arr[i], greatest = greatest, max(arr[i], greatest)
            i -= 1

        return arr


if __name__ == '__main__':
    solution = Solution()
    assert solution.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
    assert solution.replaceElements([400]) == [-1]
