# https://leetcode.com/problems/longest-valid-parentheses/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                stack.pop()
                if stack:
                    result = max(i - stack[-1], result)
                else:
                    stack.append(i)

        return result


if __name__ == '__main__':
    assert Solution().longestValidParentheses(s="(()))())(") == 4
    assert Solution().longestValidParentheses(s="(()") == 2
    assert Solution().longestValidParentheses(s="(())") == 4
    assert Solution().longestValidParentheses(s=")()())") == 4
    assert Solution().longestValidParentheses(s="())()((()())") == 6
