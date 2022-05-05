# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "]" and stack:
                el = ""
                while stack and not el.startswith("["):
                    el = stack.pop() + el
                while stack and stack[-1].isdigit():
                    el = stack.pop() + el

                num, el = el.strip("]").split("[")
                ch = el * int(num)

            stack.append(ch)
        return "".join(stack)


if __name__ == '__main__':
    assert Solution().decodeString(s="3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString(s="3[a2[c]]") == "accaccacc"
    assert Solution().decodeString(s="2[abc]3[cd]ef") == "abcabccdcdcdef"
