# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dd = {}
        for ch in s:
            dd[ch] = dd.setdefault(ch, 0) + 1
        for ch in t:
            if ch in dd:
                if dd[ch] == 1:
                    del dd[ch]
                else:
                    dd[ch] -= 1
            else:
                return False

        return not dd


if __name__ == '__main__':
    assert Solution().isAnagram(s="anagram", t="nagaram")
    assert not Solution().isAnagram(s="rat", t="car")
