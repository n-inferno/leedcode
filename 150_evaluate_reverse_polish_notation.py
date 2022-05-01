# https://leetcode.com/problems/evaluate-reverse-polish-notation/
import operator
from math import ceil
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        operands = {"+": operator.add, "*": operator.mul, "-": operator.sub, "/": operator.truediv}
        nums_counter = 0
        i = len(tokens) - 1
        while nums_counter < 2 and i >= 0:
            if tokens[i] in operands:
                nums_counter = 0
            else:
                nums_counter += 1
            stack.append(tokens[i])
            i -= 1

        a, b, op = int(stack.pop()), int(stack.pop()), stack.pop()
        result = ceil(int(operands[op](a, b)))

        while stack:
            if tokens[i] not in operands:
                token = stack.pop()
                if token in operands:
                    num = int(tokens[i])
                    result = operands[token](num, result)
                    i -= 1
                elif stack:
                    operand = stack.pop()
                    result = operands[operand](result, int(token))
            else:
                operand = tokens[i]
                num = tokens[i - 1]
                i -= 2
                result = operands[operand](int(num), result)
            result = ceil(result)

        return result


if __name__ == '__main__':
    assert Solution().evalRPN(tokens=["4", "-2", "/", "2", "-3", "-", "-"]) == -7
    assert Solution().evalRPN(tokens=["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
