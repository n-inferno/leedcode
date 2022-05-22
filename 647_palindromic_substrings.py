# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            l = r = i
            while l in range(len(s)) and r in range(len(s)):
                if not s[l] == s[r]:
                    break
                counter += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            l = i
            r = i + 1
            while l in range(len(s)) and r in range(len(s)):
                if not s[l] == s[r]:
                    break
                counter += 1
                l -= 1
                r += 1

        return counter


if __name__ == '__main__':
    assert Solution().countSubstrings(s="abc") == 3
    assert Solution().countSubstrings(s="aaa") == 6
