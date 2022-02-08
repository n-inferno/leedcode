# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10

        if sum > 9:
            return self.addDigits(sum)
        return sum



if __name__ == '__main__':
    solution = Solution()
    assert solution.addDigits(num=38) == 2
    assert solution.addDigits(num=0) == 0