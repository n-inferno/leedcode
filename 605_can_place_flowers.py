# https://leetcode.com/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev_planted = False
        for pos in range(len(flowerbed)):
            if flowerbed[pos] == 1:
                prev_planted = True
            elif not prev_planted and (pos == len(flowerbed) - 1 or flowerbed[pos + 1] == 0):
                n -= 1
                prev_planted = True
            else:
                prev_planted = False

        return n <= 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=1) == True
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 1], n=2) == False
    assert solution.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2) == False
