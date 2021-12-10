# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = '0' * (32 - len(binary)) + binary
        return int(binary[::-1], base=2)


if __name__ == '__main__':
    solution = Solution()
    assert solution.reverseBits(n=43261596) == 964176192
