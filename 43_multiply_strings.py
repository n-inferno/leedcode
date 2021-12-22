# https://leetcode.com/problems/multiply-strings/
from functools import reduce
from itertools import zip_longest
from operator import mul, add
from random import randint


class Solution:
    @staticmethod
    def operate_one(first, second, carry, method=mul, no_carry=False):
        result = method(int(first), int(second)) + carry

        if no_carry:
            str_digit = str(result % 10)
            carry = result // 10
        else:
            return str(result), 0

        return str_digit, carry

    @staticmethod
    def add_string(first, second) -> str:
        result = ''
        prev_carry = 0
        counter = max(len(first), len(second)) - 1
        for f, s in zip_longest(first[::-1], second[::-1], fillvalue='0'):
            no_carry = True if counter != 0 else False
            r, c = Solution.operate_one(f, s, prev_carry, method=add, no_carry=no_carry)
            result = r + result
            prev_carry = c
            counter -= 1
        return result

    def multiply(self, num1: str, num2: str) -> str:
        results = []
        k = 0
        for i in range(len(num1) - 1, -1, -1):
            prev_carry = 0
            result = '0' * k
            for j in range(len(num2) - 1, -1, -1):
                no_carry = True if j != 0 else False
                r, c = Solution.operate_one(num1[i], num2[j], prev_carry, no_carry=no_carry)
                result = r + result
                prev_carry = c
            results.append(result)
            k += 1

        reduced_result = reduce(Solution.add_string, results)
        i = 0
        met_not_zero = False
        while i < len(reduced_result) - 1:
            if reduced_result[i] == '0' and not met_not_zero:
                reduced_result = reduced_result[i + 1:]
            else:
                break

        return reduced_result


if __name__ == '__main__':
    solution = Solution()
    assert solution.multiply(num1="2", num2="3") == "6"
    assert solution.multiply(num1="123", num2="456") == "56088"
    assert solution.multiply(num1="0", num2="9133") == "0"

    for _ in range(1000):
        a, b = randint(1, 10000), randint(1, 10000)
        assert str(a * b) == solution.multiply(str(a), str(b))
