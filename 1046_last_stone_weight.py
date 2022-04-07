# https://leetcode.com/problems/last-stone-weight/
from typing import List


class Solution:
    def insertionSort(self, arr: List, element):
        for i in range(len(arr)):
            if arr[i] >= element:
                arr.insert(i, element)
                return
        arr.append(element)

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            first, second = stones.pop(), stones.pop()
            if first != second:
                self.insertionSort(stones, abs(first - second))

        return stones[0] if stones else 0


if __name__ == '__main__':
    solution = Solution()
    assert solution.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert solution.lastStoneWeight([1, 3]) == 2
    assert solution.lastStoneWeight([2, 2, 1]) == 1
    assert solution.lastStoneWeight([2, 2]) == 0
    assert solution.lastStoneWeight([1]) == 1
