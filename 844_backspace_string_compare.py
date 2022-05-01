# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        results = []
        for st in (s, t):
            i = 0
            result = []
            while i < len(st):
                if st[i] == "#":
                    result.pop() if result else None
                else:
                    result.append(st[i])
                i += 1
            results.append(result)

        return results[0] == results[1]


if __name__ == '__main__':
    assert Solution().backspaceCompare(s="ab#c", t="ad#c")
    assert Solution().backspaceCompare(s="ab##", t="c#d#")
    assert not Solution().backspaceCompare(s="a#c", t="b")
