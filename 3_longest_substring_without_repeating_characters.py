# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = current = 0
        i = 0
        seen = set()
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                current += 1
            else:
                j = i - current
                while j < i:
                    if s[j] == s[i]:
                        break
                    seen.remove(s[j])
                    j += 1
                    current -= 1
            longest = max(longest, current)
            i += 1
        return longest


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s="abcabcbb") == 3
    assert solution.lengthOfLongestSubstring(s="bbbbb") == 1
    assert solution.lengthOfLongestSubstring(s="pwwkew") == 3
    assert solution.lengthOfLongestSubstring(s="") == 0
    assert solution.lengthOfLongestSubstring(s="aababcabcdabcde") == 5
    assert solution.lengthOfLongestSubstring(s="abcdabccbcbdfa") == 5
    assert solution.lengthOfLongestSubstring(s=" ") == 1
    assert solution.lengthOfLongestSubstring(s="au") == 2
