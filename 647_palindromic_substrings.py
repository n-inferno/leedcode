# https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        def count_palindroms(l, r):
            nonlocal counter
            while l in range(len(s)) and r in range(len(s)):
                if not s[l] == s[r]:
                    break
                counter += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            count_palindroms(i, i)
            count_palindroms(i, i + 1)

        return counter


if __name__ == '__main__':
    assert Solution().countSubstrings(s="abc") == 3
    assert Solution().countSubstrings(s="aaa") == 6
