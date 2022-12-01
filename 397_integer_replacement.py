# https://leetcode.com/problems/integer-replacement/


class Solution:
    def integerReplacement(self, n: int, curr: int = 0) -> int:
        if n == 1:
            return curr

        if n % 2 == 0:
            return self.integerReplacement(n // 2, curr + 1)

        return min(self.integerReplacement(n + 1, curr + 1), self.integerReplacement(n - 1, curr + 1))


if __name__ == '__main__':
    assert Solution().integerReplacement(7) == 4
    assert Solution().integerReplacement(8) == 3
    assert Solution().integerReplacement(4) == 2
