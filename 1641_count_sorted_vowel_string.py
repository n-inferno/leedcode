# https://leetcode.com/problems/count-sorted-vowel-strings/
from functools import lru_cache


class Solution:

    def countVowelStrings(self, n: int) -> int:
        vowels = ("a", "e", "i", "o", "u")

        @lru_cache
        def backtracking(n, prefix, result):
            nonlocal vowels
            if n <= 0:
                return 1

            r = result
            for i in vowels:
                if not prefix or prefix <= i:
                    r += backtracking(n - 1,  i, result)
            return r

        return backtracking(n, "", 0)


if __name__ == '__main__':
    assert Solution().countVowelStrings(1) == 5
    assert Solution().countVowelStrings(2) == 15
    assert Solution().countVowelStrings(3) == 35
    assert Solution().countVowelStrings(33) == 66045
    assert Solution().countVowelStrings(50) == 316251
