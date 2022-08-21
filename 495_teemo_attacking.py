# https://leetcode.com/problems/assign-cookies/
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        when_last_ends = 0
        for poisoning in timeSeries:
            total += duration - (when_last_ends - poisoning if when_last_ends > poisoning else 0)
            when_last_ends = poisoning + duration

        return total


if __name__ == '__main__':
    assert Solution().findPoisonedDuration(timeSeries=[1, 4], duration=2) == 4
    assert Solution().findPoisonedDuration(timeSeries=[1, 2], duration=2) == 3
