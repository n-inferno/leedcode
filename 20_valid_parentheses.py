# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch not in parentheses:
                stack.append(ch)
            elif stack:
                opening = stack.pop()
                if opening != parentheses[ch]:
                    return False
            else:
                return False

        return True if not stack else False


if __name__ == '__main__':
    solution = Solution()
    assert solution.isValid(s="()")
    assert solution.isValid(s="()[]{}")
    assert not solution.isValid(s="(]")
    assert not solution.isValid(s="(")
    assert not solution.isValid(s=")")
