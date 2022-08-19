# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
from collections import deque
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequences = deque()
        for num in nums:
            for i in range(len(sequences)):
                if sequences[i][-1] + 1 == num:
                    sequences[i].append(num)
                    while i > 0 and len(sequences[i]) < len(sequences[i - 1]):
                        sequences[i], sequences[i - 1] = sequences[i - 1], sequences[i]
                    break
            else:
                sequences.appendleft([num])

        return all(len(sq) >= 3 for sq in sequences)


if __name__ == '__main__':
    assert Solution().isPossible(nums=[1, 2, 3, 3, 4, 5])
    assert Solution().isPossible(nums=[1, 2, 3, 3, 4, 4, 5, 5])
    assert not Solution().isPossible(nums=[1, 2, 3, 4, 4, 5])
