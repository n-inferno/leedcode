# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        operands = {"+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.truediv}
        while i < len(tokens):
            if tokens[i] in operands:
                tokens[i - 2: i + 1] = [operands[tokens[i]](int(tokens[i - 2]), int(tokens[i - 1]))]
                i -= 2
            else:
                i += 1

        return int(tokens[0])


if __name__ == '__main__':
    assert Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert Solution().evalRPN(tokens=["4", "-2", "/", "2", "-3", "-", "-"]) == -7
