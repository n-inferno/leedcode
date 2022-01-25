# https://leetcode.com/problems/valid-mountain-array/
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True if arr[1] > arr[0] else False
        if not increasing:
            return False
        for i in range(1, len(arr)):
            if increasing and arr[i] < arr[i - 1]:
                increasing = False
            elif not increasing and arr[i] > arr[i - 1]:
                return False
            elif not ((increasing and arr[i] > arr[i - 1]) or (not increasing and arr[i] < arr[i - 1])):
                return False

        return True if not increasing else False


if __name__ == '__main__':
    solution = Solution()
    assert solution.validMountainArray([1, 2]) == False
    assert solution.validMountainArray([3, 5, 5]) == False
    assert solution.validMountainArray([0, 3, 2, 1]) == True
    assert solution.validMountainArray([0, 1, 2, 1, 2]) == False
    assert solution.validMountainArray([0, 3, 2, 1]) == True
    assert solution.validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False
