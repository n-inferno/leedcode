# https://leetcode.com/problems/powx-n/


class Solution:

    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if n == 0 or x == 1:
                return 1

            if n % 2 == 0:
                return helper(x * x, n // 2)
            return helper(x, n - 1) * x

        result = helper(x, abs(n))

        return 1 / result if n < 0 else result


if __name__ == '__main__':
    solution = Solution()
    assert 1024.00000 - solution.myPow(2.00000, 10) < 0.00001
    assert 9.26100 - solution.myPow(2.10000, 3) < 0.00001
    assert 0.25000 - solution.myPow(2.00000, -2) < 0.00001
    assert 1.00000 - solution.myPow(0.44528, 0) < 0.00001
