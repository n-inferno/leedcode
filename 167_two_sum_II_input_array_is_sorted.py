# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, up = 0, len(numbers) - 1

        while low < up:
            summa = numbers[low] + numbers[up]
            if summa == target:
                return [low + 1, up + 1]
            if summa > target:
                up -= 1
            else:
                low += 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert solution.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert solution.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
    assert solution.twoSum(numbers=[0, 0, 3, 4], target=0) == [1, 2]
