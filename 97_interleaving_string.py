# https://leetcode.com/problems/interleaving-string/
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache
        def helper(pointer_s1, pointer_s2, pointer_s3):
            if pointer_s3 >= len(s3):
                return True if pointer_s1 == len(s1) and pointer_s2 == len(s2) else False

            result1, result2 = False, False
            if pointer_s1 < len(s1) and s1[pointer_s1] == s3[pointer_s3]:
                result1 = helper(pointer_s1 + 1, pointer_s2, pointer_s3 + 1)
            if pointer_s2 < len(s2) and s2[pointer_s2] == s3[pointer_s3]:
                result2 = helper(pointer_s1, pointer_s2 + 1, pointer_s3 + 1)

            return result1 or result2

        return helper(0, 0, 0)


if __name__ == '__main__':
    assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    assert not Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    assert Solution().isInterleave(s1="", s2="", s3="")
