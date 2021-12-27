# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        bits = len(bin(num)) - 2
        result = (1 << bits) - 1 - num
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.findComplement(num=1) == 0
    assert solution.findComplement(num=2) == 1
    assert solution.findComplement(num=3) == 0
    assert solution.findComplement(num=4) == 3
    assert solution.findComplement(num=5) == 2
