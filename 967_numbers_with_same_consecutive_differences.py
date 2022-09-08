# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = set()

        def dfs(length, curr, last):
            if length <= 0:
                result.add(curr)
                return

            valid_steps = []
            if 0 <= last + k < 10:
                valid_steps.append(last + k)
            if 0 <= last - k < 10:
                valid_steps.append(last - k)

            for step in valid_steps:
                dfs(length - 1, curr + str(step), step)

        for i in range(1, 10):
            dfs(n - 1, str(i), i)

        return [int(i) for i in result]


if __name__ == '__main__':
    assert set(Solution().numsSameConsecDiff(n=3, k=7)) == {181, 292, 707, 818, 929}
    assert set(Solution().numsSameConsecDiff(n=2, k=1)) == {10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98}
