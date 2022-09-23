# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = []
        for i in range(1, n + 1):
            result.append(bin(i)[2:])

        return int("".join(result), base=2) % 1000000007


if __name__ == '__main__':
    assert Solution().concatenatedBinary(1) == 1
    assert Solution().concatenatedBinary(3) == 27
    assert Solution().concatenatedBinary(12) == 505379714
